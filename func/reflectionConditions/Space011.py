# -*-coding:utf-8-*-
import func.reflectionConditions.BaseFunction


# 11
def spaceHandle(spaceGroupName, hklRes):
    print("enter space009 Function")

    hklList = []
    hklDeglare = []

    if spaceGroupName == "P121/m1":
        for linedatas in hklRes:
            h = linedatas[0]
            k = linedatas[1]
            l = linedatas[2]
            if func.reflectionConditions.BaseFunction.is0k0(h, k, l):
                if func.reflectionConditions.BaseFunction.is_k_even(k):
                    hklList.append((0, linedatas))
                else:
                    hklDeglare.append((1, linedatas))
            else:
                hklList.append((0, linedatas))

    elif spaceGroupName == "P1121/m":
        for linedatas in hklRes:
            h = linedatas[0]
            k = linedatas[1]
            l = linedatas[2]
            if func.reflectionConditions.BaseFunction.is00l(h, k, l):
                if func.reflectionConditions.BaseFunction.is_l_even(l):
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

    print("exit space009 Function")

    return hklList
