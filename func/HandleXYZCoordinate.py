import re
import numpy

import func.HandleFormateNum
import func.HandleTranslatePlot
import func.HandleSpaceGroup

x = []
y = []
z = []


def calculator(lineArr, x, y, z):
    return eval(lineArr)


def handle(formulationFile, coordinationFile, crystalType):
    print("handleXYZCoordination begin")
    fFile = open(formulationFile, 'r')
    fLines = fFile.readlines()
    cFile = open(coordinationFile, 'r')
    cLines = cFile.readlines()
    fFile.close()
    cFile.close()

    allCoordinationSet = set()
    atomKindFile = open('temp\\atomsKind.txt', 'w+')
    atomKindSet = set()

    num = 0

    for cLine in cLines:
        num += 1
        data = cLine.split(' ')

        coordinationSet = set()
        for fLine in fLines:
            fLine = fLine.strip()
            xyzPosition = calculator(fLine, func.HandleFormateNum.formateNum(data[4]), func.HandleFormateNum.formateNum(data[5]), func.HandleFormateNum.formateNum(data[6]))

            coordinationSet.add(xyzPosition)

        patterAtom = r'[a-zA-Z]+'
        currentAtom = re.findall(patterAtom, data[0])

        atomKindSet.add(currentAtom[0])

        for cooTuple in coordinationSet:
            resmatrix = func.HandleSpaceGroup.handleSpaceGroup(crystalType, cooTuple[0], cooTuple[1], cooTuple[2])
            for ma in resmatrix:
                res = func.HandleTranslatePlot.translatePlot(ma[0], ma[1], ma[2])
                for i in range(len(res)):
                    allCoordinationSet.add((currentAtom[0], numpy.round(res[i][0], 4),
                                            numpy.round(res[i][1], 4), numpy.round(res[i][2], 4)))

        x.clear()
        y.clear()
        z.clear()
        coordinationSet.clear()

    for atom in atomKindSet:
        atomKindFile.write(atom + "\n")
    atomKindFile.close()
    print("handleXYZCoordination end")
    return allCoordinationSet
