#!/usr/bin/python
# -*- coding: UTF-8 -*-
import math
import time
import matplotlib.pyplot
import abtem
import abtem.structures
import ase.io
import ase.build


def handleHRTEM(filename, value_Nx, value_Ny, value_Nz, value_u, value_v, value_w, radio_CPU, radio_fullScan, value_gpts_x,
                value_gpts_y, value_thincknessMul, value_sampling, value_highVoltage, value_sphericalAberrC5,
                value_defocus, value_apertureRadiusAlpha, value_focal_spread, value_gaussian_spread, value_innerAngle,
                value_outerAngle, value_samplingThickness):
    print("HRTEM，",
          "方向[%d%d%d]，" % (value_u, value_v, value_w),
          "晶胞大小%d×%d×%dÅ，" % (value_Nx, value_Ny, value_Nz),
          "片层厚度%fnm，" % value_sampling,
          "像素%d×%dpixels，" % (value_gpts_x, value_gpts_y),
          "加速电压%fKv，" % (value_highVoltage / 1000),
          "会聚半角%fmrad，" % value_apertureRadiusAlpha,
          "焦散%fÅ，" % value_focal_spread,
          "欠焦量%fnm，" % value_defocus,
          "球差系数%fmm，" % value_sphericalAberrC5,
          "CPU:", radio_CPU)

    start_time = time.time()

    device = 'cpu' if radio_CPU else 'gpu'

    crystal = ase.io.read(filename)

    # 扩大视图，获得更大的晶体
    repetitions = (value_Nx, value_Ny, value_Nz)
    crystal *= repetitions

    # 该函数自动执行我们上面对3D任意单元格采取的步骤。
    # expand_z_z = nz if nz != 1 else 2
    crystal_uvw = ase.build.surface(crystal, indices=(value_u, value_v, value_w), layers=2, periodic=True)
    orthogonal_crystal_uvw = abtem.structures.orthogonalize_cell(crystal_uvw, max_repetitions=5)
    '''
    FrozenPhonon 类使用具有给定种子的随机数生成器从高斯分布（相当于声子的状态密度的爱因斯坦模型）生成偏移量。
    为每个元素提供高斯分布的标准偏差作为字典。'''
    frozen_phonons = abtem.FrozenPhonons(orthogonal_crystal_uvw, num_configs=1, sigmas=1.0, seed=1)
    potential = abtem.Potential(orthogonal_crystal_uvw,
                          # Number of grid points describing each slice of the potential.
                          # gpts=(value_gpts_x, value_gpts_y),  # 每个电位切片的网络点数： 16 × 16
                          # Lateral sampling of the potential [1 / Å].
                          sampling=value_samplingThickness,  # 电位采样，可选
                          cutoff_tolerance=1e-3,
                          # The device used for calculating the potential. The default is 'cpu'.  Other is 'gpu'.
                          device=device)

    # 仿真 需要多次传播  pbar 自动预先计算电位
    # precalculated_potential 计算出的电位可以以HDF5文件格式存储并读回, pbar = True 显示进度条
    precalculated_potential = potential.build(pbar=True)
    # precalculated_potential = potential.build(pbar=False)

    # precalculated_potential[4].project().show()

    # 多片算法
    # 设置平面波
    wave = abtem.PlaneWave(energy=value_highVoltage)
    # 使用波函数网格的方法确保波函数与电位匹配
    wave.grid.match(precalculated_potential)
    wave = wave.build()

    # 然后通过传播函数来完成多切片算法
    propagator = abtem.FresnelPropagator()
    for potential_slice in precalculated_potential:
        potential_slice.transmit(wave)
        propagator.propagate(wave, potential_slice.thickness)

    # wave.show(title="HAADF")

    # 出射波
    pw_exit_wave = wave.multislice(orthogonal_crystal_uvw)
    # 展示 出射波
    pw_exit_wave.show(cmap='gray', title="exit_wave")

    # 探测器
    detector = abtem.AnnularDetector(inner=value_innerAngle,
                               outer=value_outerAngle,
                               save_file='temp/gridscan.hdf5')
    # 探测网格
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


    # # 探测网格
    # endParam = (potential.extent[0] / repetitions[0],
    #             potential.extent[1] / repetitions[1])
    #
    # # gridscan = GridScan(start=[endParam[0] / 4.0 * value_Nx, endParam[1] / 4.0 * value_Ny],
    # #                     end=[(endParam[0] / 2.0 + endParam[0] / 4.0) * value_Nx,
    # #                          (endParam[1] / 2.0 + endParam[1] / 4.0) * value_Ny],
    # #                     gpts=(value_gpts_x, value_gpts_y))
    #
    # gridscan = GridScan(start=[0, 0],
    #                     end=endParam,
    #                     gpts=(value_gpts_x, value_gpts_y))
    #
    # # ax, im = potential.project().show()
    # # ax, im = pw_exit_wave.show(cmap='gray', title="exit_wave")
    # # gridscan.add_to_mpl_plot(ax)

    # 加入对比度传递函数（CTF）,加入热漫散射TDF
    # ctf = CTF(Cs=value_sphericalAberrC5 * 1e-3,
    #           energy=value_highVoltage,
    #           semiangle_cutoff=value_apertureRadiusAlpha * 2,
    #           focal_spread=value_focal_spread,
    #           gaussian_spread=value_gaussian_spread)
    ctf = abtem.CTF(Cs=value_sphericalAberrC5 * 1e-3 * 1e10,
              energy=value_highVoltage,
              semiangle_cutoff=value_apertureRadiusAlpha/2,
              focal_spread=value_focal_spread,
              gaussian_spread=value_gaussian_spread)
    # 最佳欠焦量
    # ctf.defocus = scherzer_defocus(value_Cs, ctf.energy)
    # ctf.defocus = value_defocus * 10e-4
    ctf.defocus = value_defocus * 1e-9 * 1e10
    # image_wave = pw_exit_wave.apply_ctf(ctf)
    # image_wave.intensity().tile((1, 1)).show(title="HRTEM_intensity0")

    # noCTF
    # pw_exit_wave.intensity().tile((1, 1)).show(title="HRTEM_intensity0")

    # 对出射波堆栈应用对比度转移，然后取强度的平均值以获得更逼真的图像。
    # image_wave.intensity().show(cmap='gray', title="HRTEM_intensity")
    # print(image_wave)
    # # 2. 创建探针
    probe = abtem.Probe(energy=value_highVoltage,
                  ctf=ctf,
                  semiangle_cutoff=5,
                  device=device)
    probe.scan(gridscan, [detector], potential)
    measurement = abtem.Measurement.read('temp/gridscan.hdf5')
    measurement.save_as_image('temp/hrtem.tif')
    measurement.show()
    # image_wave.intensity().show("test2")

    matplotlib.pyplot.title("HRTEM_intensity")
    # matplotlib.pyplot.xticks([])
    # matplotlib.pyplot.yticks([])
    matplotlib.pyplot.axis('off')
    matplotlib.pyplot.show()

    # image_wave.multislice(potential, detector, pbar=True).show(cmap='gray', title="HRTEM_intensity_noProbe")

    end_time = time.time()
    print("The HRTEM simulate use %f sec" % (int(end_time - start_time) * 1))
