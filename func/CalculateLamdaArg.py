#!/usr/bin/python
# -*- coding: UTF-8 -*-
import math


def calcuteLamdaArgFunc(voltage):
    hConst = 6.62607015 * pow(10, -34)
    m0Const = 9.11 * pow(10, -31)
    eConst = 1.6 * pow(10, -19)
    cConst = 2.998 * pow(10, 8)
    uValue = voltage * pow(10, 3)
    lambdaArg = hConst / math.sqrt(
        2 * m0Const * eConst * uValue * (1 + (eConst * uValue) / (2 * m0Const * cConst * cConst))) * pow(10, 10) # λ
    return lambdaArg