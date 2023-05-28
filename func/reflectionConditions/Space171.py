import func.reflectionConditions.BaseFunction as bf


# 171
def spaceHandle(spaceGroupName, hklRes):
    print("enter space171 Function")

    hklList = []
    hklDeglare = []

    for linedatas in hklRes:
        h = linedatas[0]
        k = linedatas[1]
        l = linedatas[2]

        if bf.is00l(h, k, l):
            if bf.is_l_three(l):
                hklList.append((0, linedatas))
            else:
                hklDeglare.append((1, linedatas))
        else:
            hklList.append((0, linedatas))

    print("exit space171 Function")

    return hklList
