import func.reflectionConditions.BaseFunction as bf


# 169
def spaceHandle(spaceGroupName, hklRes):
    print("enter space169 Function")

    hklList = []
    hklDeglare = []

    for linedatas in hklRes:
        h = linedatas[0]
        k = linedatas[1]
        l = linedatas[2]

        if bf.is00l(h, k, l):
            if bf.is_l_six(l):
                hklList.append((0, linedatas))
            else:
                hklDeglare.append((1, linedatas))
        else:
            hklList.append((0, linedatas))

    print("exit space169 Function")

    return hklList
