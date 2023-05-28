#!/usr/bin/python
# -*- coding: UTF-8 -*-

import PySide2.QtGui
import PySide2.QtWidgets
import PySide2.QtUiTools


class frame_UserGuide(PySide2.QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.ui = PySide2.QtUiTools.QUiLoader().load('gui/frame_UserGuide.ui')
        self.ui.setWindowTitle("frame_UserGuide-Display")
        self.ui.setWindowIcon(PySide2.QtGui.QIcon('img/UserGuide.png'))
