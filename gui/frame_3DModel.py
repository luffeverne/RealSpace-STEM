#!/usr/bin/python
# -*- coding: UTF-8 -*-

import PySide2.QtGui
import PySide2.QtWidgets
import PySide2.QtUiTools

import func.HandleMyDataBase
import func.HandleDraw3D
import func.HandleDraw3DSimulation
import func.SelectFile
import mylib.share


class frame_Model3D(PySide2.QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.ui = PySide2.QtUiTools.QUiLoader().load('gui/frame_3DModel.ui')
        self.ui.setWindowTitle("3D-Model-Display")
        self.ui.setWindowIcon(PySide2.QtGui.QIcon('img/3DModel.png'))

        desktop = PySide2.QtWidgets.QApplication.desktop()
        self.ui.setGeometry(desktop.width() * 0.045, desktop.height()*0.25, 400, 237)

        self.ui.btn_selectFile.clicked.connect(self.selectMyFileDialog)
        self.ui.btn_clear.clicked.connect(self.clearFilePath)
        self.ui.btn_show3D.clicked.connect(self.show3DImage)

    def selectMyFileDialog(self):
        print("you clicked the select")
        filePath = func.SelectFile.selectFileDialog(self)
        self.ui.value_filePath.setText(filePath)

    def clearFilePath(self):
        self.ui.value_filePath.setText('')

    def show3DImage(self):
        filePath = self.ui.value_filePath.text()
        if filePath == "":
            PySide2.QtWidgets.QMessageBox().information(self, "Tip", "Please select a cif file Or input the cif file path")
        nx = int(self.ui.value_Nx.text())
        ny = int(self.ui.value_Ny.text())
        nz = int(self.ui.value_Nz.text())

        allCoordinationSet = func.HandleDraw3DSimulation.handleDraw3DSimultation(filePath, nx, ny, nz)

        func.HandleMyDataBase.elemEnterDatabase(mylib.share.SI.dbconn, mylib.share.SI.cursor, allCoordinationSet)

        # func.HandleDraw3D.showMy3DImage(mylib.share.SI.dbconn)
        func.HandleDraw3D.showMy3DImage1(mylib.share.SI.dbconn)









