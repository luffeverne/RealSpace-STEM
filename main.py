#!/usr/bin/python
# -*- coding: UTF-8 -*-
import PySide2.QtWidgets
import PySide2.QtGui
import sys
import mylib.share
import gui.mainWindow

if __name__ == "__main__":
    app = PySide2.QtWidgets.QApplication.instance()
    if app is None:
        app = PySide2.QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(PySide2.QtGui.QIcon('gui/img/logo.png'))
    mylib.share.SI.MainWidget = gui.mainWindow.MyMainWidget()
    mylib.share.SI.MainWidget.ui.show()
    sys.exit(app.exec_())

    input('Press <Enter>')
