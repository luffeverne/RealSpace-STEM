# -*-coding:utf-8-*-
import func.reflectionConditions.BaseFunction as bf


# 29
def spaceHandle(spaceGroupName, hklRes):
    print("enter space029 Function")

    hklList = []
    hklDeglare = []

    for linedatas in hklRes:
        h = linedatas[0]
        k = linedatas[1]
        l = linedatas[2]

        if bf.is0kl(h, k, l):
            if bf.is_l_even(l):
                hklList.append(linedatas)
            else:
                continue
        elif bf.ish0l(h, k, l):
            if bf.is_h_even(h):
                hklList.append(linedatas)
            else:
                continue
        elif bf.ish00(h, k, l):
            if bf.is_h_even(h):
                hklList.append(linedatas)
            else:
                continue
        elif bf.is00l(h, k, l):
            if bf.is_l_even(l):
                hklList.append(linedatas)
            else:
                continue
        else:
            hklList.append((0, linedatas))

    # 拼接
    for data in hklDeglare:
        hklList.append(data)

    print("hklList")
    for data in hklList:
        print(data)

    print("exit space029 Function")

    return hklList
