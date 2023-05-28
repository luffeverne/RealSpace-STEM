import math
import random

import numpy as np
import matplotlib.pyplot as plt


def numStr(num):
    if num >= 0:
        return str(num)
    return r'$\overline{' + str(abs(num)) + '}$'


def draw2d(showAllRadio):
    print("handleDraw2DPolar begin")
    hklFile = open('temp\\hklInfoFile.txt', 'r')
    hklLines = hklFile.read().splitlines()
    length = len(hklLines)

    crystalInfoFile = open('temp\\crystalInfo.txt', 'r')
    crystalInfoLines = crystalInfoFile.read().splitlines()

    alphabet = 'abcdefghijklmnopqrstuvwxyz@#$%&*'
    characters = ''.join(random.sample(alphabet, 5))
    plt.figure(num="Crystal Diffraction--" + crystalInfoLines[10] + "--" + characters, facecolor="black",
               figsize=(7, 6))

    f = np.zeros(length)
    h = np.zeros(length)
    k = np.zeros(length)
    l = np.zeros(length)
    it = np.zeros(length)
    ur = np.zeros(length, dtype=complex)
    r = np.zeros(length, dtype=float)
    cos_theta = np.zeros(length)
    radians_theta = np.zeros(length)

    hklRes = []

    i = 0
    recordedCos = set()
    for dataLines in hklLines:
        data = dataLines.split(',')

        f[i] = data[0]
        h[i] = data[1]
        k[i] = data[2]
        l[i] = data[3]
        it[i] = data[4]
        ur[i] = data[5]

        # print(f[i], h[i], k[i], l[i], it[i], ur[i])
        r[i] = round(math.sqrt(h[i] ** 2 + k[i] ** 2 + l[i] ** 2), 2)

        hklRes.append((f[i], h[i], k[i], l[i], it[i], ur[i], r[i]))
        i += 1

    hklRes.sort(key=lambda hklRes: (hklRes[0], hklRes[6]))

    hklResPlus = []
    i = 0
    thetaIndex = 0
    recordedCos = set()
    for data in hklRes:
        f[i] = data[0]
        h[i] = data[1]
        k[i] = data[2]
        l[i] = data[3]
        it[i] = data[4]
        ur[i] = data[5]
        r[i] = data[6]

        if i == 0:
            hklResPlus.append((f[i], h[i], k[i], l[i], it[i], ur[i], r[i], 0, i))
        elif i == 1:
            cos_theta[i] = 0
            baseH = h[i]
            baseK = k[i]
            baseL = l[i]
            baseSqrt = math.sqrt(baseH ** 2 + baseK ** 2 + baseL ** 2)
            hklResPlus.append((f[i], h[i], k[i], l[i], it[i], ur[i], r[i], cos_theta[i], i))
        else:
            cos_theta[i] = round(
                ((baseH * h[i] + baseK * k[i] + baseL * l[i]) / (math.sqrt(h[i] ** 2 + k[i] ** 2 + l[i] ** 2)
                                                                 * baseSqrt)), 2)
            if cos_theta[i] in recordedCos:
                if cos_theta[i] == 1 or cos_theta[i] == -1:
                    radians_theta[i] = round((math.acos(cos_theta[i])), 2)
                else:
                    radians_theta[i] = round((math.acos(cos_theta[i]) + math.pi), 2)
                recordedCos.remove(cos_theta[i])
            else:
                radians_theta[i] = round((math.acos(cos_theta[i])), 2)
                recordedCos.add(cos_theta[i])

            hklResPlus.append((f[i], h[i], k[i], l[i], it[i], ur[i], r[i], radians_theta[i], i))

        i += 1

    reflection_length = 0
    for line in hklResPlus:
        if line[0] == 0:
            reflection_length += 1

    reflection_theta = np.zeros(reflection_length)
    reflection_r = np.zeros(reflection_length)
    reflection_it = np.zeros(reflection_length)
    reflection_index = 0

    deglare_length = length - reflection_length
    deglare_theta = np.zeros(deglare_length)
    deglare_r = np.zeros(deglare_length)
    deglare_it = np.zeros(deglare_length)
    deglare_index = 0

    for line in hklResPlus:
        # print(line)
        if line[0] == 0:
            reflection_theta[reflection_index] = line[7]
            reflection_r[reflection_index] = line[6]
            reflection_it[reflection_index] = line[4]
            reflection_index += 1

        if showAllRadio == True and line[0] == 1:
            deglare_theta[deglare_index] = line[7]
            deglare_r[deglare_index] = line[6]
            deglare_it[deglare_index] = line[4]
            deglare_index += 1


    ax = plt.subplot(111, projection='polar')
    ax.scatter(reflection_theta, reflection_r, s=reflection_it * 5, c='white', alpha=0.75)

    if showAllRadio == True:
        ax.scatter(deglare_theta, deglare_r, s=deglare_it * 8, c='gray', alpha=0.75, marker='x')


    print(deglare_length)
    print(reflection_length)
    for i in range(reflection_length):
        coorShow = numStr(int(h[i])) + numStr(int(k[i])) + numStr(int(l[i]))
        plt.text(reflection_theta[i], reflection_r[i], coorShow, fontsize=10, color="white")

    if showAllRadio == True and deglare_length != 0:
        for i in range(deglare_length):
            coorShow = numStr(int(h[i])) + numStr(int(k[i])) + numStr(int(l[i]))
            plt.text(deglare_theta[i], deglare_r[i], coorShow, fontsize=10, color="gray")

    plt.grid()
    plt.axis("off")
    ax.set_theta_zero_location('E')
    plt.show()
    print("handleDraw2DPolar end")

    hklFile.close()
    crystalInfoFile.close()

