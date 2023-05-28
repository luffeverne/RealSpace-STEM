#!/usr/bin/python
# -*- coding: UTF-8 -*-

import PySide2
# import PySide2.QtGui
# import PySide2.QtWidgets
# import PySide2.QtUiTools

import math
import re

# import PySide2.QtWidgets
import func.SelectFile
import func.HandleCalculate2D as hc2D
import func.HandleDraw2DPolar as hd2Dp
import func.CalculateCifInfo as cci

from gui.frame_3DModel import *

#
# # 连接数据库
# conn = hdb.connectDatabase()
# # 获取一个游标对象
# cursor = conn.cursor()

# 全局变量
from mylib.share import SI


class frame_SAED(PySide2.QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.ui = PySide2.QtUiTools.QUiLoader().load('gui/frame_SAED.ui')
        self.ui.setWindowTitle("SAED-Display")
        self.ui.setWindowIcon(PySide2.QtGui.QIcon('img/SAED.png'))

        self.ui.btn_openNew.clicked.connect(self.selectMyFileDialog)
        self.ui.btn_clearFile.clicked.connect(self.clearFilePath)
        self.ui.btn_show2D.clicked.connect(lambda: self.show2DImage(self.ui.radio_allAbsences.isChecked()))
        self.ui.btn_clear.clicked.connect(self.clearAllParameters)
        self.ui.btn_saveInfo.clicked.connect(self.saveInfoFunc)
        self.ui.btn_saveDatas.clicked.connect(self.saveDatasFunc)

    def selectMyFileDialog(self):
        fileName = func.SelectFile.selectFileDialog(self)
        self.ui.value_filePath.setText(fileName)

    def clearFilePath(self):
        self.ui.value_filePath.setText('')

    def show2DImage(self, showAllRadio):
        filename = self.ui.value_filePath.text()
        if filename == "":
            PySide2.QtWidgets.QMessageBox().information(self, "Tip", "Please select a cif file Or input the cif file path")
        if filename != '':
            hRangeText = str(self.ui.value_h.text())
            kRangeText = str(self.ui.value_k.text())
            lRangeText = str(self.ui.value_l.text())
            uStr = str(self.ui.value_u.text())
            vStr = str(self.ui.value_v.text())
            wStr = str(self.ui.value_w.text())
            voltageStr = str(self.ui.value_voltage.text())

            if hRangeText == '' or kRangeText == '' or lRangeText == '' \
                    or uStr == '' or vStr == '' or wStr == '' or voltageStr == '':
                PySide2.QtWidgets.QMessageBox.information(self, "Error", "The parameters is not null!")
            if re.match(r'^-', hRangeText) is not None \
                    or re.match(r'^-', kRangeText) is not None \
                    or re.match(r'^-', lRangeText) is not None:
                PySide2.QtWidgets.QMessageBox.information(self, "Error", "The left parameters must be a position number!\n"
                                                       "Please input again.")
            else:
                # type_Num_Name = self.calculateCifInfo(filename)
                type_Num_Name = cci.calculate(filename, SI.dbconn, SI.cursor)
                hRange = math.floor(float(hRangeText))
                kRange = math.floor(float(kRangeText))
                lRange = math.floor(float(lRangeText))
                u = math.floor(float(uStr))
                v = math.floor(float(vStr))
                w = math.floor(float(wStr))
                voltage = math.floor(float(voltageStr))

                selectedDeglare = True
                res = hc2D.calculate2DArgs(SI.dbconn, voltage, hRange, kRange, lRange, u, v, w, type_Num_Name[1],
                                                        type_Num_Name[2], selectedDeglare)
                # handleDraw2D.draw2d(res)
                hd2Dp.draw2d(showAllRadio)

                crystalInfoFile = open('temp/crystalInfo.txt', 'r')
                crystalInfoLines = crystalInfoFile.read().splitlines()
                self.ui.value_showParameters.setText("a:" + crystalInfoLines[0] + "Å\n"
                                                     + "b: " + crystalInfoLines[1] + "Å\n"
                                                     + "c: " + crystalInfoLines[2] + "Å\n"
                                                     + "α:" + crystalInfoLines[3] + "°\n"
                                                     + "β: " + crystalInfoLines[4] + "°\n"
                                                     + "γ: " + crystalInfoLines[5] + "°\n"
                                                     + "a*:" + crystalInfoLines[11] + "Å\n"
                                                     + "b*: " + crystalInfoLines[12] + "Å\n"
                                                     + "c*: " + crystalInfoLines[13] + "Å\n"
                                                     + "α*:" + crystalInfoLines[14] + "°\n"
                                                     + "β*: " + crystalInfoLines[15] + "°\n"
                                                     + "γ*: " + crystalInfoLines[16] + "°\n")
                crystalInfoFile.close()

                hklFile = open('temp/hklInfoFile.txt', 'r')
                hklLines = hklFile.read().splitlines()
                dataStr = ''
                for dataLines in hklLines:
                    data = dataLines.split(',')
                    dataStr += '%4s%4s%4s%10s' % (data[1], data[2], data[3], round(float(data[4]), 4)) + "\n"

                self.ui.value_showDatas.setText(dataStr)

    def clearAllParameters(self):
        self.ui.value_h.setText("")
        self.ui.value_k.setText("")
        self.ui.value_l.setText("")
        self.ui.value_u.setText("")
        self.ui.value_v.setText("")
        self.ui.value_w.setText("")
        self.ui.value_showParameters.setText("")
        self.ui.value_showDatas.setText("")

    def saveInfoFunc(self):
        # print("save Info")
        datas = self.ui.value_showParameters.toPlainText()
        func.SelectFile.saveFileDialog(self, datas)

    def saveDatasFunc(self):
        datas = self.ui.value_showDatas.toPlainText()
        func.SelectFile.saveFileDialog(self, datas)
