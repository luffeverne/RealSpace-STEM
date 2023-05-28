# -*-coding:utf-8-*-
import func.reflectionConditions.BaseFunction as bf


# 212
def spaceHandle(spaceGroupName, hklRes):
    print("enter space212 Function")

    hklList = []
    hklDeglare = []

    for linedatas in hklRes:
        h = linedatas[0]
        k = linedatas[1]
        l = linedatas[2]

        if bf.ish00(h, k, l):
            if bf.is_h_four(h):
                hklList.append((0, linedatas))
            else:
                hklDeglare.append((1, linedatas))
        elif bf.is0k0(h, k, l):
            if bf.is_k_four(k):
                hklList.append((0, linedatas))
            else:
                hklDeglare.append((1, linedatas))
        elif bf.is00l(h, k, l):
            if bf.is_l_four(l):
                hklList.append((0, linedatas))
            else:
                hklDeglare.append((1, linedatas))
        else:
            if h == 0 and k == 0 and l == 0:
                hklList.append((0, linedatas))
            else:
                hklList.append((1, linedatas))

    # 拼接
    for data in hklDeglare:
        hklList.append(data)

    print("hklList")
    for data in hklList:
        print(data)

    print("exit space212 Function")

    return hklList
