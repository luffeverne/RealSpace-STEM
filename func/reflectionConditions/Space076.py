# -*-coding:utf-8-*-
import func.reflectionConditions.BaseFunction as bf


# 76, 78, 91, 95
def spaceHandle(spaceGroupName, hklRes):
    print("enter space076 Function")

    hklList = []
    hklDeglare = []

    for linedatas in hklRes:
        h = linedatas[0]
        k = linedatas[1]
        l = linedatas[2]

        if bf.is00l(h, k, l):
            if bf.is_l_four(l):
                hklList.append((0, linedatas))
            else:
                hklDeglare.append((1, linedatas))
        else:
            hklList.append((0, linedatas))

    # 拼接
    for data in hklDeglare:
        hklList.append(data)

    print("hklList")
    for data in hklList:
        print(data)

    print("exit space076 Function")

    return hklList
