#!/usr/bin/python
# -*- coding: UTF-8 -*-
import re
import func.HandlePreHandle
import func.HandleXYZCoordinate
import func.HandleMyDataBase


def calculate(filename, conn, cursor):
    filename = re.sub(r'\\', r'\\\\', filename)
    file = open(filename, 'r')
    content = file.read()
    type_Num_Name = func.HandlePreHandle.preHandle(content)

    allCoordinationSet = func.HandleXYZCoordinate.handle('temp\\xyzFormulation.txt', 'temp\\xyzCoordination.txt', type_Num_Name[0])
    func.HandleMyDataBase.elemEnterDatabase(conn, cursor, allCoordinationSet)
    return type_Num_Name
