# -*-coding:utf-8-*-
import func.reflectionConditions.BaseFunction as bf


# 230
def spaceHandle(spaceGroupName, hklRes):
    print("enter space230 Function")

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
        elif bf.is0kl(h, k, l):
            if bf.is_k_even(k) and bf.is_l_even(l):
                hklList.append((0, linedatas))
            else:
                hklDeglare.append((1, linedatas))
        elif bf.ish0l(h, k, l):
            if bf.is_h_even(h) and bf.is_l_even(l):
                hklList.append((0, linedatas))
            else:
                hklDeglare.append((1, linedatas))
        elif bf.ishk0(h, k, l):
            if bf.is_h_even(h) and bf.is_k_even(k):
                hklList.append((0, linedatas))
            else:
                hklDeglare.append((1, linedatas))
        elif bf.ishhl(h, k, l):
            if bf.is_2h_l_four(h, l):
                hklList.append((0, linedatas))
            else:
                hklDeglare.append((1, linedatas))
        elif bf.ishkk(h, k, l):
            if bf.is_2k_l_four(k, l):
                hklList.append((0, linedatas))
            else:
                hklDeglare.append((1, linedatas))
        elif bf.islkl(h, k, l):
            if bf.is_k_2l_four(k, l):
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

    print("exit space230 Function")

    return hklList
