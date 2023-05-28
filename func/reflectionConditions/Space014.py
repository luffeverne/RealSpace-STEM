# -*-coding:utf-8-*-
import func.reflectionConditions.BaseFunction as bf


# 14
def spaceHandle(spaceGroupName, hklRes):
    print("enter space014 Function")

    hklList = []
    hklDeglare = []

    if spaceGroupName == "P121/c1":
        for linedatas in hklRes:
            h = linedatas[0]
            k = linedatas[1]
            l = linedatas[2]
            if bf.ish0l(h, k, l):
                if bf.is_l_even(l):
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
    elif spaceGroupName == "P121/n1":
        for linedatas in hklRes:
            h = linedatas[0]
            k = linedatas[1]
            l = linedatas[2]
            if bf.ish0l(h, k, l):
                if bf.is_h_l_even(h, l):
                    hklList.append((0, linedatas))
                else:
                    hklDeglare.append((1, linedatas))
            elif bf.is0k0(h, k, l):
                if bf.is_k_even(k):
                    hklList.append((0, linedatas))
                else:
                    hklDeglare.append((1, linedatas))
            elif bf.ish00(h, k, l):
                if bf.is_h_even(h):
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
    elif spaceGroupName == "P121/a1":
        for linedatas in hklRes:
            h = linedatas[0]
            k = linedatas[1]
            l = linedatas[2]
            if bf.ish0l(h, k, l):
                if bf.is_h_even(h):
                    hklList.append((0, linedatas))
                else:
                    hklDeglare.append((1, linedatas))
            elif bf.is0k0(h, k, l):
                if bf.is_k_even(k):
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
    elif spaceGroupName == "P1121/a":
        for linedatas in hklRes:
            h = linedatas[0]
            k = linedatas[1]
            l = linedatas[2]
            if bf.ishk0(h, k, l):
                if bf.is_h_even(h):
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
    elif spaceGroupName == "P1121/n":
        for linedatas in hklRes:
            h = linedatas[0]
            k = linedatas[1]
            l = linedatas[2]
            if bf.ishk0(h, k, l):
                if bf.is_h_k_even(h, k):
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
            elif bf.is0k0(h, k, l):
                if bf.is_k_even(k):
                    hklList.append((0, linedatas))
                else:
                    hklDeglare.append((1, linedatas))
            else:
                hklList.append((0, linedatas))
    elif spaceGroupName == "P1121/b":
        for linedatas in hklRes:
            h = linedatas[0]
            k = linedatas[1]
            l = linedatas[2]
            if bf.ishk0(h, k, l):
                if bf.is_k_even(k):
                    hklList.append((0, linedatas))
                else:
                    hklDeglare.append((1, linedatas))
            elif bf.is00l(h, k, l):
                if bf.is_l_even(l):
                    hklList.append((0, linedatas))
                else:
                    hklDeglare.append((1, linedatas))
            elif bf.is0k0(h, k, l):
                if bf.is_k_even(k):
                    hklList.append((0, linedatas))
                else:
                    hklDeglare.append((1, linedatas))
            else:
                hklList.append((0, linedatas))
    else:
        for linedatas in hklRes:
            hklList.append((0, linedatas))

    # 拼接
    for data in hklDeglare:
        hklList.append(data)

    print("hklList")
    for data in hklList:
        print(data)

    print("exit space014 Function")

    return hklList
