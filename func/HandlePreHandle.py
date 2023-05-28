import re
import func.HandleCellInfo


def preHandle(content):
    flag_output = False
    flag_atom_site = True
    result = list()

    for data in content.split('\n'):
        if not len(data):
            break

        if "_atom_site_" in data:
            flag_atom_site = True
            flag_output = True
        else:
            flag_atom_site = False

        if flag_output and not flag_atom_site:
            result.append(data)

    xyzCoordinationFile = open('temp\\xyzCoordination.txt', 'w')
    xyzCoordinationFile.write('\n'.join(result))
    xyzCoordinationFile.close()

    xyz = re.compile(r'^\s+\d+\s\'(.*?),\s(.*?),\s(.*)\'', re.MULTILINE)
    xyzFormulate = list()
    for lineArr in xyz.findall(content):
        resStr = lineArr[0] + "," + lineArr[1] + "," + lineArr[2]
        xyzFormulate.append(resStr)

    xyzFormulateFile = open('temp\\xyzFormulation.txt', 'w')
    xyzFormulateFile.write('\n'.join(xyzFormulate))
    xyzFormulateFile.close()

    type_Num_Name = func.HandleCellInfo.handleCellInfo(content)

    return type_Num_Name
