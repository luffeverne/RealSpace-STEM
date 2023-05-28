import numpy


def mul(matrix1, matrix2):
    resMatrix = numpy.dot(matrix1, matrix2)
    matrix = numpy.r_[matrix1, resMatrix]
    for i in range(len(matrix)):
        if matrix[i][0] > 1:
            matrix[i][0] -= 1
        if matrix[i][1] > 1:
            matrix[i][1] -= 1
        if matrix[i][2] > 1:
            matrix[i][2] -= 1
    return matrix


def handleSpaceGroup(crystalType, x, y, z):
    # num = int(spaceGroupNum)
    matrix = numpy.array([[x, y, z, 1]])

    if crystalType == 'C':
        move1 = numpy.array([[1, 0, 0, 0],
                          [0, 1, 0, 0],
                          [0, 0, 1, 0],
                          [0.5, 0.5, 0, 1]])
        matrix = mul(matrix, move1)

    if crystalType == 'A':
        move1 = numpy.array([[1, 0, 0, 0],
                          [0, 1, 0, 0],
                          [0, 0, 1, 0],
                          [0, 0.5, 0.5, 1]])
        matrix = mul(matrix, move1)

    if crystalType == 'I':
        move1 = numpy.array([[1, 0, 0, 0],
                          [0, 1, 0, 0],
                          [0, 0, 1, 0],
                          [0.5, 0.5, 0.5, 1]])
        matrix = mul(matrix, move1)

    if crystalType == 'R':
        move1 = numpy.array([[1, 0, 0, 0],
                          [0, 1, 0, 0],
                          [0, 0, 1, 0],
                          [2/3, 1/3, 1/3, 1]])
        move2 = numpy.array([[1, 0, 0, 0],
                          [0, 1, 0, 0],
                          [0, 0, 1, 0],
                          [1/3, 2/3, 2/3, 1]])
        matrix = mul(matrix, move1)
        matrix = mul(matrix, move2)

    if crystalType == 'F':
        move1 = numpy.array([[1, 0, 0, 0],
                          [0, 1, 0, 0],
                          [0, 0, 1, 0],
                          [0, 0.5, 0.5, 1]])
        move2 = numpy.array([[1, 0, 0, 0],
                          [0, 1, 0, 0],
                          [0, 0, 1, 0],
                          [0.5, 0, 0.5, 1]])
        move3 = numpy.array([[1, 0, 0, 0],
                          [0, 1, 0, 0],
                          [0, 0, 1, 0],
                          [0.5, 0.5, 0, 1]])

        matrix = mul(matrix, move1)
        matrix = mul(matrix, move2)
        matrix = mul(matrix, move3)

    else:
        pass

    return matrix
