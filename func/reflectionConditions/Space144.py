# -*-coding:utf-8-*-
import func.reflectionConditions.BaseFunction as bf


# 144, 145, 151, 152, 153, 154
def spaceHandle(spaceGroupName, hklRes):
    print("enter space144 Function")

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

    # 拼接
    for data in hklDeglare:
        hklList.append(data)

    print("hklList")
    for data in hklList:
        print(data)

    print("exit space144 Function")

    return hklList
