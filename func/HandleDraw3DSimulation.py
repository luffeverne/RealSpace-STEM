#!/usr/bin/python
# -*- coding: UTF-8 -*-
import numpy as np
from ase.io import read, write
import func.HandleTranslatePlot_new


def handleDraw3DSimultation(filename, nx, ny, nz):
    crystal = read(filename)
    crystal *= (nx, ny, nz)

    filename = 'temp//crystal_xyz.cif'
    write(filename, crystal)

    crystalInfoFile = open(filename, 'r')
    crystalInfoLines = crystalInfoFile.read().splitlines()

    atomKindFile = open('temp//atomsKind.txt', 'w+')
    allCoordinationSet = set()
    atomKindSet = set()

    flag_output = False
    xyzLine = list()

    for data in crystalInfoLines:
        if '_atom_site_occupancy' in data:
            flag_output = True
            continue

        if flag_output:
            # num += 1
            arr = data.split()
            xyzLine.append(arr)
            atomKindSet.add(arr[0])

    for line in xyzLine:
        res = func.HandleTranslatePlot_new.translatePlot(float(line[3]), float(line[4]), float(line[5]))

        for i in range(len(res)):
            allCoordinationSet.add((line[0], np.round(res[i][0], 4), np.round(res[i][1], 4), np.round(res[i][2], 4)))

    for atom in atomKindSet:
        atomKindFile.write(atom + "\n")
    atomKindFile.close()

    return allCoordinationSet