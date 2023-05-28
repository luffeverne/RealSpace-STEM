# -*-coding:utf-8-*-
import func.reflectionConditions.BaseFunction as bf


# 108, 119, 121
def spaceHandle(spaceGroupName, hklRes):
    print("enter space108 Function")

    hklList = []
    hklDeglare = []

    for linedatas in hklRes:
        h = linedatas[0]
        k = linedatas[1]
        l = linedatas[2]

        if bf.ishkl(h, k, l):
            if bf.is_h_k_l_even(h, k, l):
                hklList.append((0, linedatas))
            else:
                hklDeglare.append((1, linedatas))
        elif bf.ishk0(h, k, l):
            if bf.is_h_k_even(h, k):
                hklList.append((0, linedatas))
            else:
                hklDeglare.append((1, linedatas))
        elif bf.is0kl(h, k, l):
            if bf.is_k_even(k) and bf.is_l_even(l):
                hklList.append((0, linedatas))
            else:
                hklDeglare.append((1, linedatas))
        elif bf.ishhl(h, k, l):
            if bf.is_l_even(l):
                hklList.append((0, linedatas))
            else:
                hklDeglare.append((1, linedatas))
        elif bf.is00l(h, k, l):
            if bf.is_l_even(l):
                hklList.append((0, linedatas))
            else:
                hklDeglare.append((1, linedatas))
        elif bf.ish00(h, k, l):
            if bf.is_h_even(h):
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

    print("exit space108 Function")

    return hklList
