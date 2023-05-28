import re


def handleCellInfo(content):
    pStructuralName = re.compile(r'_chemical_formula_structural\s+(\'?.*)\'?')
    pSpaceGroupName = re.compile(r'_symmetry_space_group_name_H-M\s+\'(.*?)\'')
    pTablesNumber = re.compile(r'_symmetry_Int_Tables_number\s+(.*)')
    for name in pStructuralName.findall(content):
        structName = name
    for nameSpace in pSpaceGroupName.findall(content):
        spaceGroupName = nameSpace
    for num in pTablesNumber.findall(content):
        spaceGroupNum = num

    arr = spaceGroupName.split(' ')

    patternLength = r'_cell_length_[abc]\s+(\d*\.?\d+)\.?\(?\d*\)?'
    matchLength = re.findall(patternLength, content.strip("\n"), re.I)
    lengthA = matchLength[0]
    lengthB = matchLength[1]
    lengthC = matchLength[2]

    patternAngle = r'_cell_angle_[alpha|beta|gamma]+\s+(\d*\.?\d+)\.?\(?\d*\)?'
    matchAngle = re.findall(patternAngle, content, re.I)
    angleAlpha = matchAngle[0]
    angleBeta = matchAngle[1]
    angleGamma = matchAngle[2]

    patternVolume = r'_cell_volume\s+(\d*\.?\d+)\.?\(?\d*\)?'
    matchVolume = re.findall(patternVolume, content, re.I)
    volume = matchVolume[0]

    crystalInfoFile = open('temp\\crystalInfo.txt', 'w+')
    crystalInfoFile.write(lengthA + "\n")
    crystalInfoFile.write(lengthB + "\n")
    crystalInfoFile.write(lengthC + "\n")
    crystalInfoFile.write(angleAlpha + "\n")
    crystalInfoFile.write(angleBeta + "\n")
    crystalInfoFile.write(angleGamma + "\n")
    crystalInfoFile.write(volume + "\n")
    crystalInfoFile.write(arr[0] + "\n")
    crystalInfoFile.write(spaceGroupNum + "\n")
    crystalInfoFile.write(spaceGroupName + "\n")
    crystalInfoFile.write(structName + "\n")
    crystalInfoFile.close()

    return arr[0], spaceGroupNum, spaceGroupName