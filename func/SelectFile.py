#!/usr/bin/python
# -*- coding: UTF-8 -*-
import PySide2.QtWidgets

def selectFileDialog(self):
    filename = PySide2.QtWidgets.QFileDialog().getOpenFileName(self, "select the file", "crystal", "iamge file (*.cif)")
    return filename[0]

def selectConfigFileDialog(self):
    filename = PySide2.QtWidgets.QFileDialog().getOpenFileName(self, "select the file", "temp",
                                                               "txt files (*.txt);;all files(*.*)")
    return filename[0]


def saveFileDialog(self, datas):
    file_path, _ = PySide2.QtWidgets.QFileDialog.getSaveFileName(self, "save file", "temp",
                                               "txt files (*.txt);;all files(*.*)")
    try:
        with open(file_path, mode='w', encoding='utf-8') as saveDatas:
            saveDatas.write(datas)
        PySide2.QtWidgets.QMessageBox.information(self, "Tip", "Succeed!")
    except:
        pass