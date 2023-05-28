import numpy as np
import math
import cmath
import func.HandleMyDataBase
import func.HandleAtomDeglare


def calculateStructureFactor(h, k, l, ff, tpi, ii, three, itype, number):
    fr = complex(0, 0)
    for j1 in range(number):
        pp = h * three[j1, 0] + k * three[j1, 1] + l * three[j1, 2]
        fr = fr + ff[int(itype[j1] - 1)] * (cmath.exp(tpi * pp * ii))
        fr = complex(round(fr.real, 2), round(fr.imag, 2))
        return fr


def calculate2DArgs(conn, voltage, hRange, kRange, lRange, u, v, w, crystalType, spaceGroupName, selectedDeglare):
    print("HandleCalculate2D-begin")
    hConst = 6.62607015 * pow(10, -34)
    m0Const = 9.11 * pow(10, -31)
    eConst = 1.6 * pow(10, -19)
    cConst = 2.998 * pow(10, 8)
    uValue = voltage * 1e3
    lambdaArg = hConst / math.sqrt(
        2 * m0Const * eConst * uValue * (1 + (eConst * uValue) / (2 * m0Const * cConst * cConst)))  # λ
    print("%.2f" % (lambdaArg * pow(10, 12)), 'pm')

    gama = 1 + (eConst * uValue) / (m0Const * cConst * cConst)  # γ
    sigma = (2 * math.pi * gama * m0Const * eConst * lambdaArg) / (hConst * hConst)  # σ

    crystalInfoFile = open('temp\\crystalInfo.txt', 'r')
    crystalInfoLines = crystalInfoFile.read().splitlines()
    crystalInfoFile.close()

    omiga = float(crystalInfoLines[6]) * pow(10, -27)  # Ω
    coe = lambdaArg / (sigma * omiga)

    def calD(V, h, k, l):
        d = V * math.pow(((h ** 2) * (b ** 2) * (c ** 2) * (sinAlpha ** 2)
                          + (k ** 2) * (a ** 2) * (c ** 2) * (sinBeta ** 2)
                          + (l ** 2) * (a ** 2) * (b ** 2) * (sinGamma ** 2)
                          + 2 * h * k * a * (b ** 2) * c * (cosAlpha * cosGamma - cosBeta)), -1 / 2)
        return d

    crystalInfoFile = open('temp\\crystalInfo.txt', 'r')
    crystalInfoLines = crystalInfoFile.read().splitlines()
    a = float(crystalInfoLines[0])
    b = float(crystalInfoLines[1])
    c = float(crystalInfoLines[2])
    alphaAngle = float(crystalInfoLines[3])
    betaAngle = float(crystalInfoLines[4])
    gammaAngle = float(crystalInfoLines[5])
    crystalInfoFile.close()

    atomKindFile = open('temp\\atomsKind.txt', 'r')
    atomKindLines = atomKindFile.read().splitlines()
    atomKindFile.close()

    kind = len(atomKindLines)
    print("handleCalDeron-kind: ", kind)
    datas = func.HandleMyDataBase.allElem(conn)
    number = len(datas)
    print("handleCalDeron-number: ", number)

    lamda = .0251
    pi = 3.141592653589793
    tpi = 2.0 * pi
    ii = 0.0 + 1.0j
    tpic = tpi * ii

    alpha = alphaAngle * pi / 180
    beta = betaAngle * pi / 180
    gamma = gammaAngle * pi / 180

    cosAlpha = math.cos(alpha)
    cosBeta = math.cos(beta)
    cosGamma = math.cos(gamma)
    sinAlpha = math.sin(alpha)
    sinBeta = math.sin(beta)
    sinGamma = math.sin(gamma)

    cosAlpha_ = (cosBeta * cosGamma - cosAlpha) / (sinBeta * sinGamma)
    cosBeta_ = (cosGamma * cosAlpha - cosBeta) / (sinGamma * sinAlpha)
    cosGamma_ = (cosAlpha * cosBeta - cosGamma) / (sinAlpha * sinBeta)

    V = a * b * c * math.pow((1 - cosAlpha ** 2 - cosBeta ** 2 - cosGamma ** 2 + 2 * cosAlpha * cosBeta * cosGamma),
                             -1 / 2)
    a_ = 1 / calD(V, 1, 0, 0)
    b_ = 1 / calD(V, 0, 1, 0)
    c_ = 1 / calD(V, 0, 0, 1)

    crystalInfoFile = open('temp\\crystalInfo.txt', 'a')
    crystalInfoFile.write(str(round(a_, 2)) + "\n")
    crystalInfoFile.write(str(round(b_, 2)) + "\n")
    crystalInfoFile.write(str(round(c_, 2)) + "\n")
    crystalInfoFile.write(str(round(math.acos(cosAlpha_) * 180 / pi)) + "\n")
    crystalInfoFile.write(str(round(math.acos(cosBeta_) * 180 / pi)) + "\n")
    crystalInfoFile.write(str(round(math.acos(cosGamma_) * 180 / pi)) + "\n")
    crystalInfoFile.close()

    ff = np.zeros(kind)
    ax = np.zeros((kind, 5))
    bx = np.zeros((kind, 5))
    itype = np.zeros(number)
    three = np.zeros((number, 3))
    i = 0
    for currentAtom in atomKindLines:
        mydatas = func.HandleMyDataBase.elemaxbx(currentAtom, conn)
        for rowdata in mydatas:
            ax[i, 0] = rowdata[2]
            ax[i, 1] = rowdata[3]
            ax[i, 2] = rowdata[4]
            ax[i, 3] = rowdata[5]
            ax[i, 4] = rowdata[6]
            bx[i, 0] = rowdata[7]
            bx[i, 1] = rowdata[8]
            bx[i, 2] = rowdata[9]
            bx[i, 3] = rowdata[10]
            bx[i, 4] = rowdata[11]
            i += 1

    i = 0
    step = 1
    for currentAtom in atomKindLines:
        mydatas = func.HandleMyDataBase.elemCoor(currentAtom, conn)
        for rowdata in mydatas:
            itype[i] = step
            three[i, 0] = rowdata[1]
            three[i, 1] = rowdata[2]
            three[i, 2] = rowdata[3]
            i += 1
        step += 1

    res = []
    print("hRange", hRange)
    print("kRange", kRange)
    print("lRange", lRange)
    h = -1 * hRange
    while h <= hRange:
        k = -1 * kRange
        while k <= kRange:
            l = -1 * lRange
            while l <= lRange:
                g21 = (h ** 2) * (a_ ** 2) + (k ** 2) * (b_ ** 2) + (l ** 2) * (c_ ** 2) \
                      + 2 * h * k * (a_ * b_ * cosGamma_) \
                      + 2 * h * l * (a_ * c_ * cosBeta_) \
                      + 2 * k * l * (b_ * c_ * cosAlpha_)

                s = 0.5 * lamda * g21 + 0.000001
                i = 0
                while i < kind:
                    ff[i] = 0.0
                    j = 0
                    while j < 5:
                        ff[i] = ff[i] + ax[i, j] * math.exp(-bx[i, j] * g21 / 4.0)
                        j += 1
                    i += 1

                ur = complex(0, 0)
                for j1 in range(number):
                    fr = calculateStructureFactor(h, k, l, ff, tpi, ii, three, itype, number)
                    fr = complex(round(fr.real, 2), round(fr.imag, 2))
                    pp = h * three[j1, 0] + k * three[j1, 1] + l * three[j1, 2]
                    ur = ur + coe * fr * (cmath.exp(-1 * tpi * pp * ii))
                    ur = complex(round(ur.real, 2), round(ur.imag, 2))

                it = abs(fr) ** 2

                # print("it, ur, fr, it, u, v, w, h, k, l", it, ur, fr, u, v, w, h, k, l)
                if it > 0.01 and h * u + k * v + l * w == 0:
                    # print(h, k, l, it, ur)
                    res.append((h, k, l, it, ur))
                l += 1
            k += 1
        h += 1

    hklRes = func.HandleAtomDeglare.handle(crystalType, spaceGroupName, res)

    hklInfoFile = open("temp\\hklInfoFile.txt", 'w+')
    for lineDatas in hklRes:
        lineStr = str(lineDatas[0]) + "," + str(lineDatas[1][0]) + "," + str(lineDatas[1][1]) + "," \
                  + str(lineDatas[1][2]) + "," + str(lineDatas[1][3]) + "," + str(lineDatas[1][4])
        hklInfoFile.writelines(lineStr + "\n")
    hklInfoFile.close()

    print("HandleCalculate2D-end")
    return hklRes
