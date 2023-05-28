#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time

from abtem import Potential, Probe, PlaneWave, FresnelPropagator, CTF, FrozenPhonons
from abtem.structures import orthogonalize_cell
from abtem.transfer import scherzer_defocus, point_resolution
from abtem.utils import energy2wavelength
from ase.io import read, write
from ase.visualize import view
from abtem.visualize import show_atoms
from ase.build import surface
import matplotlib.pyplot as plt


def handleHRTEM(filename, value_Nx, value_Ny, value_Nz, value_u, value_v, value_w, radio_CPU, radio_fullScan, value_gpts_x,
                value_gpts_y, value_thincknessMul, value_sampling, value_highVoltage, value_sphericalAberrC5,
                value_defocus, value_apertureRadiusAlpha, value_focal_spread, value_gaussian_spread, value_innerAngle,
                value_outerAngle, value_samplingThickness):
    print("HRTEM,",
          "方向[%d%d%d]," % (value_u, value_v, value_w),
          "晶胞大小%d×%d×%dÅ," % (value_Nx, value_Ny, value_Nz),
          "片层厚度%fÅ," % value_sampling,
          "像素%d×%dpixels," % (value_gpts_x, value_gpts_y),
          "加速电压%fKv," % (value_highVoltage / 1000),
          "会聚半角%fmrad" % value_apertureRadiusAlpha,
          "焦散%fÅ," % value_focal_spread,
          "欠焦量%fnm," % value_defocus,
          "球差系数%fmm," % value_sphericalAberrC5,
          "CPU:", radio_CPU)

    # 程序开始时间
    start_time = time.time()

    # 设置cpu 或 gpu
    device = 'cpu' if radio_CPU else 'gpu'
    # parametrization = 'lobato' if radio_parametrization_lobato else 'kirkland'
    # projection = 'finite' if radio_projection_finite else 'infinite'

    # 导入文件
    crystal = read(filename)
    # print(crystal.positions)

    # 扩大视图，获得更大的晶体
    crystal *= (value_Nx, value_Ny, value_Nz)

    # 该函数自动执行我们上面对3D任意单元格采取的步骤。
    crystal_uvw = surface(crystal, indices=(value_u, value_v, value_w), layers=4, periodic=True)
    # 使 ASE 原子对象的单元格正交。这是通过重复单元格直到晶格向量来实现的接近三个主要的笛卡尔方向。
    # 如果结构在 结构重复给定最大值，剩余差值将通过施加应变来弥补。
    orthogonal_crystal_uvw = orthogonalize_cell(crystal_uvw, max_repetitions=5)
    frozen_phonons = FrozenPhonons(orthogonal_crystal_uvw, num_configs=1, sigmas=0.01, seed=1)
    atoms_conf = next(iter(frozen_phonons))
    # 展示视图
    # show_atoms(crystal_uvw, title='crystal', ax=None, legend=True)
    # show_pic = show_atoms(orthogonal_crystal_uvw, title='crystal[%d%d%d]' % (value_u, value_v, value_w), ax=None,
    #                       legend=True, )
    # show_pic.set_xlabel('')
    # show_pic.set_ylabel('')

    # 晶体势能模拟， 使用独立原子模型（IAM），它忽略了任何键合效应，并将样品视为原子势阵列。
    # 设置一个合理的截止值cutoff_tolerance, 因为单个原子的电位是非常局部的，但原则上是无限的。
    # with tds
    # 使用无限投影方案来加快计算速度。
    # potential = Potential(orthogonal_crystal_uvw,
    #                       cutoff_tolerance=1e-3,
    #                       sampling=value_sampling,
    #                       parametrization=parametrization,
    #                       gpts=value_gpts_x,
    #                       device=device)
    potential = Potential(atoms_conf,
                          # Number of grid points describing each slice of the potential.
                          gpts=(value_gpts_x, value_gpts_y),  # 每个电位切片的网络点数： 16 × 16
                          # Lateral sampling of the potential [1 / Å].
                          sampling=value_sampling,  # 电位采样，可选
                          parametrization='kirkland',
                          # parametrization=parametrization,
                          # # If 'finite' the 3d potential is numerically integrated between the slice boundaries.
                          # # If 'infinite' the infinite potential projection of each atom will be assigned to a single slice.
                          # projection=projection,
                          # # The error tolerance used for deciding the radial cutoff distance of the potential [eV / e].
                          # # The cutoff is only  relevant for potentials using the 'finite' projection scheme.
                          cutoff_tolerance=1e-3,
                          # The device used for calculating the potential. The default is 'cpu'.  Other is 'gpu'.
                          device=device)
    # potential.project().show()

    # 仿真 需要多次传播  pbar 自动预先计算电位
    # precalculated_potential 计算出的电位可以以HDF5文件格式存储并读回
    precalculated_potential = potential.build(pbar=True)
    # precalculated_potential[4].project().show()

    # 多片算法
    # 设置平面波
    wave = PlaneWave(energy=value_highVoltage)
    # 使用波函数网格的方法确保波函数与电位匹配
    wave.grid.match(precalculated_potential)
    wave = wave.build()

    # 然后通过传播函数来完成多切片算法
    propagator = FresnelPropagator()
    for potential_slice in precalculated_potential:
        potential_slice.transmit(wave)
        propagator.propagate(wave, potential_slice.thickness)

    # wave.show(title="HRTEM")

    # 出射波
    pw_exit_wave = wave.multislice(orthogonal_crystal_uvw)
    # 展示 出射波
    pw_exit_wave.show(cmap='gray', title="exit_wave")

    # 加入对比度传递函数（CTF）,加入热漫散射TDF
    ctf = CTF(Cs=value_sphericalAberrC5 * 1e-3,
              energy=value_highVoltage,
              semiangle_cutoff=value_apertureRadiusAlpha,
              focal_spread=value_focal_spread,
              gaussian_spread=value_gaussian_spread)
    # 最佳欠焦量
    # ctf.defocus = scherzer_defocus(value_Cs, ctf.energy)
    ctf.defocus = value_defocus * 10e-4
    image_wave = pw_exit_wave.apply_ctf(ctf)
    # image_wave.intensity().tile((value_Nx, value_Ny)).show(title="HRTEM_intensity")
    image_wave.intensity().show(title="HRTEM_intensity")
    # image_wave.write("temp/hrtem.tif")
    image_wave.intensity().write("temp/hrtem")
    # plt.savefig(image_wave)
    # plt.title("HRTEM_intensity")
    # plt.show()
    # image_wave.intensity().array
    # print(image_wave.intensity().array)

    ent_time = time.time()
    print("The HRTEM simulate use %f sec" % (ent_time - start_time))

