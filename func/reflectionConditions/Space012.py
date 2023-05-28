# -*-coding:utf-8-*-
import func.reflectionConditions.BaseFunction


# 12
def spaceHandle(spaceGroupName, hklRes):
    print("enter space012 Function")

    hklList = []
    hklDeglare = []

    if spaceGroupName == "C12/m1":
        for linedatas in hklRes:
            h = linedatas[0]
            k = linedatas[1]
            l = linedatas[2]
            if func.reflectionConditions.BaseFunction.ishkl(h, k, l):
                if func.reflectionConditions.BaseFunction.is_h_k_even(h, k):
                    hklList.append((0, linedatas))
                else:
                    hklDeglare.append((1, linedatas))
            elif func.reflectionConditions.BaseFunction.ish0l(h, k, l):
                if func.reflectionConditions.BaseFunction.is_h_even(h):
                    hklList.append((0, linedatas))
                else:
                    hklDeglare.append((1, linedatas))
            elif func.reflectionConditions.BaseFunction.is0kl(h, k, l):
                if func.reflectionConditions.BaseFunction.is_k_even(k):
                    hklList.append((0, linedatas))
                else:
                    hklDeglare.append((1, linedatas))
            elif func.reflectionConditions.BaseFunction.ishk0(h, k, l):
                if func.reflectionConditions.BaseFunction.is_h_k_even(h, k):
                    hklList.append((0, linedatas))
                else:
                    hklDeglare.append((1, linedatas))
            elif func.reflectionConditions.BaseFunction.is0k0(h, k, l):
                if func.reflectionConditions.BaseFunction.is_k_even(k):
                    hklList.append((0, linedatas))
                else:
                    hklDeglare.append((1, linedatas))
            elif func.reflectionConditions.BaseFunction.ish00(h, k, l):
                if func.reflectionConditions.BaseFunction.is_h_even(h):
                    hklList.append((0, linedatas))
                else:
                    hklDeglare.append((1, linedatas))
            else:
                hklList.append((0, linedatas))
    elif spaceGroupName == "A12/m1":
        for linedatas in hklRes:
            h = linedatas[0]
            k = linedatas[1]
            l = linedatas[2]
            if func.reflectionConditions.BaseFunction.ishkl(h, k, l):
                if func.reflectionConditions.BaseFunction.is_k_l_even(h, l):
                    hklList.append((0, linedatas))
                else:
                    hklDeglare.append((1, linedatas))
            elif func.reflectionConditions.BaseFunction.ish0l(h, k, l):
                if func.reflectionConditions.BaseFunction.is_l_even(l):
                    hklList.append((0, linedatas))
                else:
                    hklDeglare.append((1, linedatas))
            elif func.reflectionConditions.BaseFunction.is0kl(h, k, l):
                if func.reflectionConditions.BaseFunction.is_k_l_even(k, l):
                    hklList.append((0, linedatas))
                else:
                    hklDeglare.append((1, linedatas))
            elif func.reflectionConditions.BaseFunction.ishk0(h, k, l):
                if func.reflectionConditions.BaseFunction.is_k_even(k):
                    hklList.append((0, linedatas))
                else:
                    hklDeglare.append((1, linedatas))
            elif func.reflectionConditions.BaseFunction.is0k0(h, k, l):
                if func.reflectionConditions.BaseFunction.is_k_even(k):
                    hklList.append((0, linedatas))
                else:
                    hklDeglare.append((1, linedatas))
            elif func.reflectionConditions.BaseFunction.is00l(h, k, l):
                if func.reflectionConditions.BaseFunction.is_l_even(l):
                    hklList.append((0, linedatas))
                else:
                    hklDeglare.append((1, linedatas))
            else:
                hklList.append((0, linedatas))
    elif spaceGroupName == "I12/m1":
        for linedatas in hklRes:
            h = linedatas[0]
            k = linedatas[1]
            l = linedatas[2]
            if func.reflectionConditions.BaseFunction.ishkl(h, k, l):
                if func.reflectionConditions.BaseFunction.is_h_k_l_even(h, k, l):
                    hklList.append((0, linedatas))
                else:
                    hklDeglare.append((1, linedatas))
            elif func.reflectionConditions.BaseFunction.ish0l(h, k, l):
                if func.reflectionConditions.BaseFunction.is_h_l_even(h, l):
                    hklList.append((0, linedatas))
                else:
                    hklDeglare.append((1, linedatas))
            elif func.reflectionConditions.BaseFunction.is0kl(h, k, l):
                if func.reflectionConditions.BaseFunction.is_k_l_even(k, l):
                    hklList.append((0, linedatas))
                else:
                    hklDeglare.append((1, linedatas))
            elif func.reflectionConditions.BaseFunction.ishk0(h, k, l):
                if func.reflectionConditions.BaseFunction.is_h_k_even(h, k):
                    hklList.append((0, linedatas))
                else:
                    hklDeglare.append((1, linedatas))
            elif func.reflectionConditions.BaseFunction.is0k0(h, k, l):
                if func.reflectionConditions.BaseFunction.is_k_even(k):
                    hklList.append((0, linedatas))
                else:
                    hklDeglare.append((1, linedatas))
            elif func.reflectionConditions.BaseFunction.ish00(h, k, l):
                if func.reflectionConditions.BaseFunction.is_h_even(h):
                    hklList.append((0, linedatas))
                else:
                    hklDeglare.append((1, linedatas))
            elif func.reflectionConditions.BaseFunction.is00l(h, k, l):
                if func.reflectionConditions.BaseFunction.is_l_even(l):
                    hklList.append((0, linedatas))
                else:
                    hklDeglare.append((1, linedatas))
            else:
                hklList.append((0, linedatas))
    elif spaceGroupName == "A112/m":
        for linedatas in hklRes:
            h = linedatas[0]
            k = linedatas[1]
            l = linedatas[2]
            if func.reflectionConditions.BaseFunction.ishkl(h, k, l):
                if func.reflectionConditions.BaseFunction.is_k_l_even(k, l):
                    hklList.append((0, linedatas))
                else:
                    hklDeglare.append((1, linedatas))
            elif func.reflectionConditions.BaseFunction.ishk0(h, k, l):
                if func.reflectionConditions.BaseFunction.is_k_even(k):
                    hklList.append((0, linedatas))
                else:
                    hklDeglare.append((1, linedatas))
            elif func.reflectionConditions.BaseFunction.is0kl(h, k, l):
                if func.reflectionConditions.BaseFunction.is_k_l_even(k, l):
                    hklList.append((0, linedatas))
                else:
                    hklDeglare.append((1, linedatas))
            elif func.reflectionConditions.BaseFunction.ish0l(h, k, l):
                if func.reflectionConditions.BaseFunction.is_l_even(l):
                    hklList.append((0, linedatas))
                else:
                    hklDeglare.append((1, linedatas))
            elif func.reflectionConditions.BaseFunction.is00l(h, k, l):
                if func.reflectionConditions.BaseFunction.is_l_even(l):
                    hklList.append((0, linedatas))
                else:
                    hklDeglare.append((1, linedatas))
            elif func.reflectionConditions.BaseFunction.is0k0(h, k, l):
                if func.reflectionConditions.BaseFunction.is_k_even(k):
                    hklList.append((0, linedatas))
                else:
                    hklDeglare.append((1, linedatas))
            else:
                hklList.append((0, linedatas))
    elif spaceGroupName == "B112/m":
        for linedatas in hklRes:
            h = linedatas[0]
            k = linedatas[1]
            l = linedatas[2]
            if func.reflectionConditions.BaseFunction.ishkl(h, k, l):
                if func.reflectionConditions.BaseFunction.is_h_l_even(h, l):
                    hklList.append((0, linedatas))
                else:
                    hklDeglare.append((1, linedatas))
            elif func.reflectionConditions.BaseFunction.ishk0(h, k, l):
                if func.reflectionConditions.BaseFunction.is_h_even(h):
                    hklList.append((0, linedatas))
                else:
                    hklDeglare.append((1, linedatas))
            elif func.reflectionConditions.BaseFunction.is0kl(h, k, l):
                if func.reflectionConditions.BaseFunction.is_l_even(l):
                    hklList.append((0, linedatas))
                else:
                    hklDeglare.append((1, linedatas))
            elif func.reflectionConditions.BaseFunction.ish0l(h, k, l):
                if func.reflectionConditions.BaseFunction.is_h_l_even(h, l):
                    hklList.append((0, linedatas))
                else:
                    hklDeglare.append((1, linedatas))
            elif func.reflectionConditions.BaseFunction.is00l(h, k, l):
                if func.reflectionConditions.BaseFunction.is_l_even(l):
                    hklList.append((0, linedatas))
                else:
                    hklDeglare.append((1, linedatas))
            elif func.reflectionConditions.BaseFunction.ish00(h, k, l):
                if func.reflectionConditions.BaseFunction.is_h_even(h):
                    hklList.append((0, linedatas))
                else:
                    hklDeglare.append((1, linedatas))
            else:
                hklList.append((0, linedatas))
    elif spaceGroupName == "I112/m":
        for linedatas in hklRes:
            h = linedatas[0]
            k = linedatas[1]
            l = linedatas[2]
            if func.reflectionConditions.BaseFunction.ishkl(h, k, l):
                if func.reflectionConditions.BaseFunction.is_h_k_l_even(h, k, l):
                    hklList.append((0, linedatas))
                else:
                    hklDeglare.append((1, linedatas))
            elif func.reflectionConditions.BaseFunction.ishk0(h, k, l):
                if func.reflectionConditions.BaseFunction.is_h_k_even(h, k):
                    hklList.append((0, linedatas))
                else:
                    hklDeglare.append((1, linedatas))
            elif func.reflectionConditions.BaseFunction.is0kl(h, k, l):
                if func.reflectionConditions.BaseFunction.is_k_l_even(k, l):
                    hklList.append((0, linedatas))
                else:
                    hklDeglare.append((1, linedatas))
            elif func.reflectionConditions.BaseFunction.ish0l(h, k, l):
                if func.reflectionConditions.BaseFunction.is_h_l_even(h, l):
                    hklList.append((0, linedatas))
                else:
                    hklDeglare.append((1, linedatas))
            elif func.reflectionConditions.BaseFunction.is00l(h, k, l):
                if func.reflectionConditions.BaseFunction.is_l_even(l):
                    hklList.append((0, linedatas))
                else:
                    hklDeglare.append((1, linedatas))
            elif func.reflectionConditions.BaseFunction.ish00(h, k, l):
                if func.reflectionConditions.BaseFunction.is_h_even(h):
                    hklList.append((0, linedatas))
                else:
                    hklDeglare.append((1, linedatas))
            elif func.reflectionConditions.BaseFunction.is0k0(h, k, l):
                if func.reflectionConditions.BaseFunction.is_k_even(k):
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