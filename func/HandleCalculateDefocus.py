#!/usr/bin/python
# -*- coding: UTF-8 -*-
import abtem.transfer


def calculateDefocus(cs, energy):
    Cs = cs * 1e5
    energy = energy * 1e3
    defocus = abtem.transfer.scherzer_defocus(Cs, energy)
    # print(defocus)
    return round(defocus, 2)



