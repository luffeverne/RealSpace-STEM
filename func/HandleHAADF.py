#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time
import numpy as np
import matplotlib.pyplot
import abtem
import abtem.structures
import abtem.transfer
import ase.build
import ase.io
import ase.md.velocitydistribution


def handleHAADF(filename, value_Nx, value_Ny, value_Nz, value_u, value_v, value_w, radio_CPU, radio_fullScan,
                        value_gpts_x, value_gpts_y, value_thincknessMul, value_sampling, value_highVoltage, value_sphericalAberrC5,
                        value_defocus, value_apertureRadiusAlpha, value_focal_spread,
                        value_gaussian_spread, value_innerAngle, value_outerAngle, value_temperature,
                        value_TDS, value_samplingThickness):

    start_time = time.time()

    device = 'cpu' if radio_CPU else 'gpu'
    # parametrization = 'lobato' if radio_parametrization_lobato else 'kirkland'
    # projection = 'finite' if radio_projection_finite else 'infinite'

    crystal = ase.io.read(filename)

    # value_Nz = 5 if value_thincknessMul > 5 else value_thincknessMul   # exepriment

    repetitions = (value_Nx, value_Ny, value_Nz)
    crystal *= repetitions

    crystal_uvw = ase.build.surface(crystal, indices=(value_u, value_v, value_w), layers=2, periodic=True)
    orthogonal_crystal_uvw = abtem.structures.orthogonalize_cell(crystal_uvw, max_repetitions=5)

    ase.md.velocitydistribution.MaxwellBoltzmannDistribution(orthogonal_crystal_uvw, temperature_K=value_temperature)

    frozen_phonons = abtem.FrozenPhonons(orthogonal_crystal_uvw, num_configs=1, sigmas=0.001, seed=1)
    atoms_conf = next(iter(frozen_phonons))
    potential = abtem.Potential(atoms_conf,
                          sampling=value_samplingThickness,
                          cutoff_tolerance=1e-3,
                          projection='infinite',
                          parametrization='kirkland',
                          device=device)

    precalculated_potential = potential.build(pbar=True)
    wave = abtem.PlaneWave(energy=value_highVoltage)
    wave.grid.match(precalculated_potential)
    wave = wave.build()

    propagator = abtem.FresnelPropagator()
    for potential_slice in precalculated_potential:
        potential_slice.transmit(wave)
        propagator.propagate(wave, potential_slice.thickness)

    pw_exit_wave = wave.multislice(orthogonal_crystal_uvw)
    # Measurement.read(pw_exit_wave).save_as_image('temp/hExitWave.tif')

    pw_exit_wave.show(cmap='gray', title="exit_wave")

    ctf = abtem.CTF(Cs=value_sphericalAberrC5 * 1e-3 * 1e10,
              energy=value_highVoltage,
              semiangle_cutoff=value_apertureRadiusAlpha/2.0,
              focal_spread=value_focal_spread,
              gaussian_spread=value_gaussian_spread)

    ctf.defocus = value_defocus * 1e-9 * 1e10

    probe = abtem.SMatrix(energy=value_highVoltage,
                    semiangle_cutoff=value_apertureRadiusAlpha/2,
                    ctf=ctf,
                    device=device)

    abtem.transfer.point_resolution(ctf.defocus.imag, ctf.defocus.real)
    probe.grid.match(precalculated_potential)

    haadf = abtem.AnnularDetector(inner=value_innerAngle,
                            outer=value_outerAngle,
                            save_file='temp/gridscan.hdf5')

    endParam = (potential.extent[0] / repetitions[0],
                potential.extent[1] / repetitions[1])

    if radio_fullScan:
        gridscan = abtem.GridScan(start=[0, 0],
                            end=[(endParam[0] * value_Nx), (endParam[1] * value_Ny)],
                            gpts=(value_gpts_x, value_gpts_y))
    else:
        gridscan = abtem.GridScan(start=[endParam[0] / 4.0 * value_Nx, endParam[1] / 4.0 * value_Ny],
                            end=[(endParam[0] / 2.0 + endParam[0] / 4.0) * value_Nx,
                                 (endParam[1] / 2.0 + endParam[1] / 4.0) * value_Ny],
                            gpts=(value_gpts_x, value_gpts_y))

    ax, im = potential.project().show()
    # ax, im = pw_exit_wave.show(cmap='gray', title="exit_wave")
    gridscan.add_to_mpl_plot(ax)

    wave = abtem.PlaneWave(energy=value_highVoltage)

    wave.grid.match(precalculated_potential)

    probe.scan(gridscan, [haadf], potential)
    measurement = abtem.Measurement.read('temp/gridscan.hdf5')
    measurement.save_as_image('temp/haadf.tif')
    # measurement.show(cmap="gray_r")
    measurement.show()

    matplotlib.pyplot.title("HAADF_intensity")
    # matplotlib.pyplot.xticks([])
    # matplotlib.pyplot.yticks([])
    matplotlib.pyplot.axis('off')
    matplotlib.pyplot.show()

    end_time = time.time()
    print("The HAADF simulate use %f sec" % (int(end_time - start_time) * 1))

