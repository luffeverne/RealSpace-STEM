#!/usr/bin/python
# -*- coding: UTF-8 -*-
import math
import re

import matplotlib.pyplot
import numpy as np


def drawHighResolutionImage():
    infoFile = open('temp\\imageDatas.txt', 'r')
    # infoFile = open('../test/testHighResolutionImage/121pixel.dat', 'r')
    infoLines = infoFile.read().splitlines()

    pattern = re.compile(r'[0-9]\.[0-9]*')
    datas = pattern.findall(str(infoLines))
    # print(datas)

    length = len(datas)

    intensity = np.zeros(length)
    reIntensity = np.zeros(length)

    i = 0
    j = 0

    for data in datas:
        # print(data)
        intensity[i] = data
        i += 1

    minS = min(intensity)
    # print(minS)

    for i in range(length):
        reIntensity[i] = (intensity[i] - minS)
        # print(reintensity[i])

    len1 = int(math.sqrt(length))
    reIntensity = reIntensity.reshape(len1, len1)

    matplotlib.pyplot.imshow(reIntensity, cmap='gray', aspect='equal', origin='lower')

    matplotlib.pyplot.colorbar(shrink=0.5)
    matplotlib.pyplot.xticks([])
    matplotlib.pyplot.yticks([])
    matplotlib.pyplot.show()

    infoFile.close()
