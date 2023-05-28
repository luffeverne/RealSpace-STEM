#!/usr/bin/python
# -*- coding: UTF-8 -*-
import threading
import PySide2.QtGui
import PySide2.QtWidgets
import PySide2.QtUiTools

import gui.frame_3DModel
import gui.frame_SAED
import gui.frame_Simulation
import gui.frame_UserGuide
import gui.frame_Contact

import mylib.share

class MyMainWidget(PySide2.QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = PySide2.QtUiTools.QUiLoader().load('gui/mainWindow.ui')
        self.ui.setWindowTitle("Hello Crystal [V1.0]")
        self.ui.setWindowIcon(PySide2.QtGui.QIcon('img/logo.png'))

        self.ui.btn_3DModel.setStyleSheet("QPushButton:hover{background-color: #cce6ff}")
        self.ui.btn_SAED.setStyleSheet("QPushButton:hover{background-color: #cce6ff}")
        self.ui.btn_HighResolution.setStyleSheet("QPushButton:hover{background-color: #cce6ff}")
        self.ui.btn_UserGuide.setStyleSheet("QPushButton:hover{background-color: #cce6ff}")
        self.ui.btn_Contact.setStyleSheet("QPushButton:hover{background-color: #cce6ff}")

        self.ui.btn_3DModel.clicked.connect(lambda: self.frame_show(gui.frame_3DModel.frame_Model3D))
        self.ui.btn_SAED.clicked.connect(lambda: self.frame_show(gui.frame_SAED.frame_SAED))
        self.ui.btn_HighResolution.clicked.connect(lambda: self.frame_show(gui.frame_Simulation.frame_Simulation))
        self.ui.btn_UserGuide.clicked.connect(lambda: self.frame_show(gui.frame_UserGuide.frame_UserGuide))
        self.ui.btn_Contact.clicked.connect(lambda: self.frame_show(gui.frame_Contact.frame_Contact))

    def __frame_show(self, frameName):
        # print(frameName.__name__, "show")
        # print(SI.name)
        # print(SI.cursor)
        mylib.share.SI.frameName = frameName()
        mylib.share.SI.frameName.ui.show()

    def frame_show(self, frameName):
        T = threading.Thread(target=self.__frame_show(frameName))
        # T = threading.Thread(target=self.__frame_show, args=(frameName,))
        T.start()

    def closeEvent(self, event):
        print("close the windows")