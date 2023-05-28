#!/usr/bin/python
# -*- coding: UTF-8 -*-
import re

import PySide2
import abtem

import func.HandleCalculateDefocus
import func.HandleDraw3D
import func.HandleDraw3DSimulation
import func.HandleDrawStrusture
import func.HandleHAADF
import func.HandleHRTEM2
import func.SelectFile
import func.HandleMyDataBase
import func.SelectFile
import ase.io
import mylib.share


class frame_Simulation(PySide2.QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.ui = PySide2.QtUiTools.QUiLoader().load('gui/frame_Simulation.ui')
        self.ui.setWindowTitle("Real space-STEM")
        self.ui.setWindowIcon(PySide2.QtGui.QIcon('img/HR.png'))

        self.ui.btn_openFile.clicked.connect(self.selectMyFileDialog)

        self.ui.pushButton_updateView.clicked.connect(self.clickedUpdateViewButton)

        self.ui.pushButton_3D.clicked.connect(self.show3DImageFunc)

        self.ui.btn_clearFile.clicked.connect(self.clearFilePathFunc)

        self.ui.pushButton_loadConfig.clicked.connect(self.loadConfigFun)

        self.ui.pushButton_savaConfig.clicked.connect(self.saveConfigFun)

        self.ui.pushButton_startSimulation.clicked.connect(self.handleSimultate)

        self.ui.pushButton_setThickness.clicked.connect(self.calThicknessFunc)

        self.ui.pushButton_scherzer.clicked.connect(self.calScherzerFunc)

        self.ui.radio_HRTEM.clicked.connect(lambda: self.changeCheckBoxFunc(self.ui.radio_HAADF.isChecked()))
        self.ui.radio_HAADF.clicked.connect(lambda: self.changeCheckBoxFunc(self.ui.radio_HAADF.isChecked()))

        self.ui.pushButton_clearParams.clicked.connect(self.clearParasFunc)

    def selectMyFileDialog(self):
        filePath = func.SelectFile.selectFileDialog(self)
        self.ui.value_filePath.setText(filePath)

    def clickedUpdateViewButton(self):
        filename = self.ui.value_filePath.text()

        self.ui.value_filePath.setText(filename)

        if filename == "":
            PySide2.QtWidgets.QMessageBox().information(self, "Tip", "Please select a cif file Or input the cif file path")

        nx = int(self.ui.value_Nx.text())
        ny = int(self.ui.value_Ny.text())
        nz = int(self.ui.value_Nz.text())
        u = int(self.ui.value_viewDirectorU.text())
        v = int(self.ui.value_viewDirectorV.text())
        w = int(self.ui.value_viewDirectorW.text())

        orthogonal_crystal_xyz = func.HandleDrawStrusture.handleDraw(filename, nx, ny, nz, u, v, w)

        show_pic = abtem.show_atoms(orthogonal_crystal_xyz, title='crystal[%d%d%d]' % (u, v, w), ax=None, legend=True)
        show_pic.savefig('temp/hSaveStructureImage.tif')

        imgName = 'temp/hSaveStructureImage.tif'
        jpg = PySide2.QtGui.QPixmap(imgName).scaled(self.ui.showImage.width(), self.ui.showImage.height())
        self.ui.showImage.setPixmap(jpg)

    def show3DImageFunc(self):
        filename = self.ui.value_filePath.text()

        # filename = 'crystal/136/MgF2.cif'
        self.ui.value_filePath.setText(filename)

        if filename == "":
            PySide2.QtWidgets.QMessageBox().information(self, "Tip", "Please select a cif file Or input the cif file path")

        nx = int(self.ui.value_Nx.text())
        ny = int(self.ui.value_Ny.text())
        nz = int(self.ui.value_Nz.text())

        allCoordinationSet = func.HandleDraw3DSimulation.handleDraw3DSimultation(filename, nx, ny, nz)

        func.HandleMyDataBase.elemEnterDatabase(mylib.share.SI.dbconn, mylib.share.SI.cursor, allCoordinationSet)

        func.HandleDraw3D.showMy3DImage1(mylib.share.SI.dbconn)

    def clearFilePathFunc(self):
        self.ui.value_filePath.setText('')

    def clearParasFunc(self):
        self.ui.value_Nx.setText('')
        self.ui.value_Ny.setText('')
        self.ui.value_Nz.setText('')
        self.ui.value_viewDirectorU.setText('')
        self.ui.value_viewDirectorV.setText('')
        self.ui.value_viewDirectorW.setText('')

        self.ui.radio_CPU.setChecked(1)
        self.ui.radio_HAADF.setChecked(1)

        self.ui.value_gpts_x.setText('')
        self.ui.value_gpts_y.setText('')
        self.ui.value_thincknessMul.setText('')
        self.ui.value_sampling.setText('')
        self.ui.value_samplingThickness.setText('')

        self.ui.value_highVoltage.setText('')
        self.ui.value_sphericalAberrC5.setText('')
        self.ui.value_defocus.setText('')
        self.ui.value_apertureRadiusAlpha.setText('')  # Aperture radius aplha
        self.ui.value_focal_spread.setText('')  # Focus spread Delta(1/e half with)
        self.ui.value_gaussian_spread.setText('')

        self.ui.value_innerAngle.setText('')
        self.ui.value_outerAngle.setText('')
        self.ui.value_temperature.setText('')
        self.ui.value_TDS.setText('')

    '''点击 最佳欠焦量 scherzer 按钮'''

    def calScherzerFunc(self):
        cs = float(self.ui.value_sphericalAberrC5.text())
        energy = float(self.ui.value_highVoltage.text())
        defocus = func.HandleCalculateDefocus.calculateDefocus(cs, energy)
        self.ui.value_defocus.setText(str(defocus))

    def calThicknessFunc(self):
        filename = self.ui.value_filePath.text()
        atoms = ase.io.read(filename)
        arr = atoms.cell.array
        z_thickness = arr[2][2]
        value_thincknessMul = int(self.ui.value_thincknessMul.text())
        self.ui.value_sampling.setText(str(round(z_thickness * value_thincknessMul * 0.1, 6)))

    def handleSimultate(self):
        filename = self.ui.value_filePath.text()
        # filename = 'crystal//136//MgF2.cif'
        value_Nx = int(self.ui.value_Nx.text())
        value_Ny = int(self.ui.value_Ny.text())
        value_Nz = int(self.ui.value_Nz.text())
        value_u = int(self.ui.value_viewDirectorU.text())
        value_v = int(self.ui.value_viewDirectorV.text())
        value_w = int(self.ui.value_viewDirectorW.text())
        radio_CPU = self.ui.radio_CPU.isChecked()
        '''Potential'''
        value_gpts_x = int(self.ui.value_gpts_x.text())
        value_gpts_y = int(self.ui.value_gpts_y.text())
        value_thincknessMul = int(self.ui.value_thincknessMul.text())
        value_sampling = float(self.ui.value_sampling.text())
        value_samplingThickness = float(self.ui.value_samplingThickness.text())
        '''CTF'''
        value_highVoltage = float(self.ui.value_highVoltage.text()) * 1e3
        value_sphericalAberrC5 = float(self.ui.value_sphericalAberrC5.text())
        value_defocus = float(self.ui.value_defocus.text())
        value_apertureRadiusAlpha = float(self.ui.value_apertureRadiusAlpha.text())
        value_focal_spread = float(self.ui.value_focal_spread.text())
        value_gaussian_spread = float(self.ui.value_gaussian_spread.text())
        '''Probe'''
        # value_expansion_cutoff = float(self.ui.value_expansion_cutoff.text())
        # value_interpolation = int(self.ui.value_interpolation.text())
        # value_num_partitions = int(self.ui.value_num_partitions.text())
        # value_beamTiltX = float(self.ui.value_beamTiltX.text())
        # value_beamTiltY = float(self.ui.value_beamTiltY.text())
        '''Detectors'''
        radio_fullScan = self.ui.radio_fullScan.isChecked()
        value_innerAngle = float(self.ui.value_innerAngle.text())
        value_outerAngle = float(self.ui.value_outerAngle.text())
        value_temperature = float(self.ui.value_temperature.text())
        value_TDS = float(self.ui.value_TDS.text())

        if self.ui.radio_HRTEM.isChecked():
            func.HandleHRTEM2.handleHRTEM(filename, value_Nx, value_Ny, value_Nz, value_u, value_v, value_w, radio_CPU, radio_fullScan,
                        value_gpts_x, value_gpts_y, value_thincknessMul, value_sampling, value_highVoltage,
                        value_sphericalAberrC5, value_defocus, value_apertureRadiusAlpha, value_focal_spread,
                        value_gaussian_spread, value_innerAngle, value_outerAngle, value_samplingThickness)

        if self.ui.radio_HAADF.isChecked():
            func.HandleHAADF.handleHAADF(filename, value_Nx, value_Ny, value_Nz, value_u, value_v, value_w, radio_CPU, radio_fullScan,
                        value_gpts_x, value_gpts_y, value_thincknessMul, value_sampling, value_highVoltage,
                        value_sphericalAberrC5, value_defocus, value_apertureRadiusAlpha, value_focal_spread,
                        value_gaussian_spread, value_innerAngle, value_outerAngle, value_temperature,
                        value_TDS, value_samplingThickness)

    def changeCheckBoxFunc(self, Flag_HAADF):
        self.ui.value_TDS.setEnabled(Flag_HAADF)
        self.ui.checkBox_TDS.setEnabled(Flag_HAADF)

    def changeProjectionFunc(self, Flag_finite):
        self.ui.value_cutoffTolerance.setEnabled(Flag_finite)
        if not Flag_finite:
            self.ui.radio_parametrization_kirkland.setChecked(1)
            # self.ui.radio_parametrization_lobato.setCheckable(False)

        if Flag_finite:
            self.ui.radio_parametrization_lobato.setChecked(1)
            # self.ui.radio_parametrization_lobato.setCheckable(True)

    def changeLobatoAndKirlandFun(self, Flag_Lobato):
        if Flag_Lobato and self.ui.radio_projection_infinite.isChecked():
            self.ui.radio_parametrization_kirkland.setChecked(1)
            PySide2.QtWidgets.QMessageBox().information(self, "Tip",
                                      "Infinite projections are only implemented for the Kirkland parametrization")

    def saveConfigFun(self):
        datas = "filePath:" + str(self.ui.value_filePath.text()) + "\n" \
                + "value_Nx:" + str(self.ui.value_Nx.text()) + "\n" \
                + "value_Ny:" + str(self.ui.value_Ny.text()) + "\n" \
                + "value_Nz:" + str(self.ui.value_Nz.text()) + "\n" \
                + "value_u:" + str(self.ui.value_viewDirectorU.text()) + "\n" \
                + "value_v:" + str(self.ui.value_viewDirectorV.text()) + "\n" \
                + "value_w:" + str(self.ui.value_viewDirectorW.text()) + "\n" \
                + "radio_CPU:" + str(self.ui.radio_CPU.isChecked()) + "\n" \
                + "radio_HRTEM:" + str(self.ui.radio_HRTEM.isChecked()) + "\n" \
                + "value_gpts_x:" + str(self.ui.value_gpts_x.text()) + "\n" \
                + "value_gpts_y:" + str(self.ui.value_gpts_y.text()) + "\n" \
                + "value_thincknessMul:" + str(self.ui.value_thincknessMul.text()) + "\n" \
                + "value_sampling:" + str(self.ui.value_sampling.text()) + "\n" \
                + "value_highVoltage:" + str(self.ui.value_highVoltage.text()) + "\n" \
                + "value_sphericalAberrC5:" + str(self.ui.value_sphericalAberrC5.text()) + "\n" \
                + "value_defocus:" + str(self.ui.value_defocus.text()) + "\n" \
                + "value_apertureRadiusAlpha:" + str(self.ui.value_apertureRadiusAlpha.text()) + "\n" \
                + "value_focal_spread:" + str(self.ui.value_focal_spread.text()) + "\n" \
                + "value_gaussian_spread:" + str(self.ui.value_gaussian_spread.text()) + "\n" \
                + "value_innerAngle:" + str(self.ui.value_innerAngle.text()) + "\n" \
                + "value_outerAngle:" + str(self.ui.value_outerAngle.text()) + "\n" \
                + "value_temperature:" + str(self.ui.value_temperature.text()) + "\n" \
                + "value_TDS:" + str(self.ui.value_TDS.text()) + "\n" \
                + "checkBox_TDS_true:" + str(self.ui.checkBox_TDS.isChecked()) + "\n" \
                + "radio_fullScan:" + str(self.ui.radio_fullScan.isChecked()) + "\n" \
                + "value_samplingThickness:" + str(self.ui.value_samplingThickness.text())
        func.SelectFile.saveFileDialog(self, datas)

    def loadConfigFun(self):
        configFilePath = func.SelectFile.selectConfigFileDialog(self)
        configInfoFile = open(configFilePath, 'r')
        # print(configInfoFile)
        configInfoLines = configInfoFile.read().splitlines()
        # print(str(configInfoLines))
        pattern = re.compile(r':(\S+)\',?')
        datas = pattern.findall(str(configInfoLines))

        self.ui.value_filePath.setText(datas[0])
        self.ui.value_Nx.setText(datas[1])
        self.ui.value_Ny.setText(datas[2])
        self.ui.value_Nz.setText(datas[3])
        self.ui.value_viewDirectorU.setText(datas[4])
        self.ui.value_viewDirectorV.setText(datas[5])
        self.ui.value_viewDirectorW.setText(datas[6])
        if datas[7] == 'True':
            self.ui.radio_CPU.setChecked(1)
        else:
            self.ui.radio_GPU.setChecked(1)
        if datas[8] == 'True':
            self.ui.radio_HRTEM.setChecked(1)
        else:
            self.ui.radio_HAADF.setChecked(1)
            self.changeCheckBoxFunc(True)
        self.ui.value_gpts_x.setText(datas[9])
        self.ui.value_gpts_y.setText(datas[10])
        self.ui.value_thincknessMul.setText(datas[11])
        self.ui.value_sampling.setText(datas[12])
        self.ui.value_highVoltage.setText(datas[13])
        self.ui.value_sphericalAberrC5.setText(datas[14])
        self.ui.value_defocus.setText(datas[15])
        self.ui.value_apertureRadiusAlpha.setText(datas[16])
        # self.ui.value_rolloff.setText(datas[22])
        self.ui.value_focal_spread.setText(datas[17])
        # self.ui.value_angular_spread.setText(datas[24])
        self.ui.value_gaussian_spread.setText(datas[18])
        self.ui.value_innerAngle.setText(datas[19])
        self.ui.value_outerAngle.setText(datas[20])
        self.ui.value_temperature.setText(datas[21])
        self.ui.value_TDS.setText(datas[22])
        if datas[23] == 'True':
            self.ui.checkBox_TDS.setChecked(1)
        if datas[24] == 'True':
            self.ui.radio_fullScan.setChecked(1)
        else:
            self.ui.radio_centerScan.setChecked(1)
        self.ui.value_samplingThickness.setText(datas[25])

    def closeEvent(self, event):
        print("close the windows")
