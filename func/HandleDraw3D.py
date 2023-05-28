#!/usr/bin/python
# -*- coding: UTF-8 -*-
import random
import numpy as np
import mayavi.mlab
# from mayavi import mlab

import func.HandleMyDataBase
import func.CalculateCifInfo


def draw3d(myMlab, atomName, num, x, y, z):
    mycolor = (random.randint(0, 8) * 0.1, random.randint(1, 8) * 0.1, random.randint(2, 9) * 0.1)
    myMlab.points3d(x, y, z, scale_factor=random.randint(5, 11) * 0.01, resolution=30, mode="sphere", color=mycolor)
    myMlab.text(0.88, abs(0.98 - num * 0.15), atomName, width=0.05, color=mycolor)

    return len(x)


def showMy3DImage(self, filename, conn, cursor):
    num = 0
    print(filename)
    if filename != '':
        func.CalculateCifInfo.calculate(filename, conn, cursor)
        crystalInfoFile = open('temp\\crystalInfo.txt', 'r')
        crystalInfoLines = crystalInfoFile.read().splitlines()
        alphabet = 'abcdefghijklmnopqrstuvwxyz@#$%&*'
        characters = ''.join(random.sample(alphabet, 5))
        mayavi.mlab.figure(size=(700, 500), figure="Crystal Maker--" + crystalInfoLines[10] + "--" + characters,
                    bgcolor=(0.85, 0.85, 0.85))

        atomKindFile = open('temp\\atomsKind.txt', 'r')
        atomKindLines = atomKindFile.read().splitlines()
        atomKindFile.close()
        for currentAtom in atomKindLines:
            x = []
            y = []
            z = []
            num += 1
            print(currentAtom)
            mydatas = func.HandleMyDataBase.elemCoor(currentAtom, conn)
            for data in mydatas:
                x.append(np.round(data[1], 4))
                y.append(np.round(data[2], 4))
                z.append(np.round(data[3], 4))

            draw3d(mayavi.mlab, currentAtom, 6.5, x, y, z)

        mayavi.mlab.orientation_axes()
        mayavi.mlab.outline()
        mayavi.mlab.show()

def showMy3DImage1(conn):
    alphabet = 'abcdefghijklmnopqrstuvwxyz@#$%&*'
    characters = ''.join(random.sample(alphabet, 5))

    mayavi.mlab.figure(size=(700, 500), figure="Crystal Maker--" + "--" + characters,
                bgcolor=(0.85, 0.85, 0.85))

    atomKindFile = open('temp\\atomsKind.txt', 'r')
    atomKindLines = atomKindFile.read().splitlines()
    atomKindFile.close()

    num = 0
    for currentAtom in atomKindLines:
        x = []
        y = []
        z = []
        num += 1
        print(currentAtom)
        mydatas = func.HandleMyDataBase.elemCoor(currentAtom, conn)
        for data in mydatas:
            x.append(np.round(data[1], 4))
            y.append(np.round(data[2], 4))
            z.append(np.round(data[3], 4))

        draw3d(mayavi.mlab, currentAtom, num, x, y, z)

    mayavi.mlab.orientation_axes()
    points = np.array([[0, 0, 0],
                       [1, 0, 0],
                       [0, 1, 0],
                       [0, 0, 1],
                       [1, 1, 1]])
    x, y, z = points[:, 0], points[:, 1], points[:, 2]
    mayavi.mlab.points3d(x, y, z, scale_factor=0.01, resolution=30, mode="sphere", color=(1, 1, 1))
    mayavi.mlab.outline()
    mayavi.mlab.show()

