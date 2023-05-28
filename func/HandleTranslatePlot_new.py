import numpy


def translatePlot(x, y, z):
    if x < 0:
        x = 1 + x
    if y < 0:
        y = 1 + y
    if z < 0:
        z = 1 + z
    if x > 1:
        x = 1 - x
    if y > 1:
        y = 1 - y
    if z > 1:
        z = 1 - z

    matrix = numpy.array([[x, y, z, 1]])
    movetoPositiveX = numpy.array([[1, 0, 0, 0],
                                [0, 1, 0, 0],
                                [0, 0, 1, 0],
                                [1, 0, 0, 1]])
    movetoNegativeX = numpy.array([[1, 0, 0, 0],
                                [0, 1, 0, 0],
                                [0, 0, 1, 0],
                                [-1, 0, 0, 1]])
    movetoPositiveY = numpy.array([[1, 0, 0, 0],
                                [0, 1, 0, 0],
                                [0, 0, 1, 0],
                                [0, 1, 0, 1]])
    movetoNegativeY = numpy.array([[1, 0, 0, 0],
                                [0, 1, 0, 0],
                                [0, 0, 1, 0],
                                [0, -1, 0, 1]])
    movetoPositiveZ = numpy.array([[1, 0, 0, 0],
                                [0, 1, 0, 0],
                                [0, 0, 1, 0],
                                [0, 0, 1, 1]])
    movetoNegativeZ = numpy.array([[1, 0, 0, 0],
                                [0, 1, 0, 0],
                                [0, 0, 1, 0],
                                [0, 0, -1, 1]])
    movetoPositiveD1 = numpy.array([[1, 0, 0, 0],
                                [0, 1, 0, 0],
                                [0, 0, 1, 0],
                                [1, 1, 0, 1]])
    movetoNegativeD1 = numpy.array([[1, 0, 0, 0],
                                 [0, 1, 0, 0],
                                 [0, 0, 1, 0],
                                 [-1, -1, 0, 1]])
    movetoPositiveD2 = numpy.array([[1, 0, 0, 0],
                                [0, 1, 0, 0],
                                [0, 0, 1, 0],
                                [1, 0, 1, 1]])
    movetoNegativeD2 = numpy.array([[1, 0, 0, 0],
                                 [0, 1, 0, 0],
                                 [0, 0, 1, 0],
                                 [-1, 0, -1, 1]])
    movetoPositiveD3 = numpy.array([[1, 0, 0, 0],
                                [0, 1, 0, 0],
                                [0, 0, 1, 0],
                                [0, 1, 1, 1]])
    movetoNegativeD3 = numpy.array([[1, 0, 0, 0],
                                 [0, 1, 0, 0],
                                 [0, 0, 1, 0],
                                 [0, -1, -1, 1]])
    movetoPositiveD4 = numpy.array([[1, 0, 0, 0],
                                 [0, 1, 0, 0],
                                 [0, 0, 1, 0],
                                 [1, 1, 1, 1]])
    movetoNegativeD4 = numpy.array([[1, 0, 0, 0],
                                 [0, 1, 0, 0],
                                 [0, 0, 1, 0],
                                 [-1, -1, -1, 1]])

    nx = numpy.dot(matrix, movetoPositiveX)
    px = numpy.dot(matrix, movetoNegativeX)
    ny = numpy.dot(matrix, movetoPositiveY)
    py = numpy.dot(matrix, movetoNegativeY)
    nz = numpy.dot(matrix, movetoPositiveZ)
    pz = numpy.dot(matrix, movetoNegativeZ)
    pd1 = numpy.dot(matrix, movetoPositiveD1)
    pd2 = numpy.dot(matrix, movetoPositiveD2)
    pd3 = numpy.dot(matrix, movetoPositiveD3)
    pd4 = numpy.dot(matrix, movetoPositiveD4)
    pd5 = numpy.dot(matrix, movetoNegativeD1)
    pd6 = numpy.dot(matrix, movetoNegativeD2)
    pd7 = numpy.dot(matrix, movetoNegativeD3)
    pd8 = numpy.dot(matrix, movetoNegativeD4)

    # print(nx, px, ny, py, nz, pz)
    #
    matrix = numpy.r_[matrix, nx]
    matrix = numpy.r_[matrix, px]
    matrix = numpy.r_[matrix, ny]
    matrix = numpy.r_[matrix, py]
    matrix = numpy.r_[matrix, nz]
    matrix = numpy.r_[matrix, pz]
    matrix = numpy.r_[matrix, pd1]
    matrix = numpy.r_[matrix, pd2]
    matrix = numpy.r_[matrix, pd3]
    matrix = numpy.r_[matrix, pd4]
    matrix = numpy.r_[matrix, pd5]
    matrix = numpy.r_[matrix, pd6]
    matrix = numpy.r_[matrix, pd7]
    matrix = numpy.r_[matrix, pd8]

    # print("matrix before\n", matrix)

    index = []
    for i in range(len(matrix)):
        if (matrix[i][0] > 1 or matrix[i][0] < 0) or (matrix[i][1] > 1 or matrix[i][1] < 0) or (matrix[i][2] > 1 or matrix[i][2] < 0):
            index.append(i)

    matrix = numpy.delete(matrix, index, axis=0)

    return matrix
