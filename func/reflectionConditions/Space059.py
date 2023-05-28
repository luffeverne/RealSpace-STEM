# -*-coding:utf-8-*-
import func.reflectionConditions.BaseFunction as bf


# 59
def spaceHandle(spaceGroupName, hklRes):
    print("enter space059 Function")

    hklList = []
    hklDeglare = []

    for linedatas in hklRes:
        h = linedatas[0]
        k = linedatas[1]
        l = linedatas[2]

        if bf.is0kl(h, k, l):
            if bf.is_k_l_even(k, l):
                hklList.append((0, linedatas))
            else:
                hklDeglare.append((1, linedatas))
        elif bf.ish0l(h, k, l):
            if bf.is_h_l_even(h, l):
                hklList.append((0, linedatas))
            else:
                hklDeglare.append((1, linedatas))
        elif bf.ish00(h, k, l):
            if bf.is_h_even(h):
                hklList.append((0, linedatas))
            else:
                hklDeglare.append((1, linedatas))
        elif bf.is0k0(h, k, l):
            if bf.is_k_even(k):
                hklList.append((0, linedatas))
            else:
                hklDeglare.append((1, linedatas))
        elif bf.is00l(h, k, l):
            if bf.is_l_even(l):
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

    print("exit space059 Function")

    return hklList
