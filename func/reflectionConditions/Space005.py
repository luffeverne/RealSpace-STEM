import func.reflectionConditions.BaseFunction


# 5, 8
def spaceHandle(spaceGroupName, hklRes):
    print("enter space005 Function")

    hklList = []
    hklDeglare = []

    if spaceGroupName == "C121" or spaceGroupName == "C1m1":
        for lineDatas in hklRes:
            h = lineDatas[0]
            k = lineDatas[1]
            l = lineDatas[2]
            if func.reflectionConditions.BaseFunction.ishkl(h, k, l):
                if func.reflectionConditions.BaseFunction.is_h_k_even(h, k):
                    hklList.append((0, lineDatas))
                else:
                    hklDeglare.append((1, lineDatas))
            elif func.reflectionConditions.BaseFunction.ish0l(h, k, l):
                if func.reflectionConditions.BaseFunction.is_h_even(h):
                    hklList.append((0, lineDatas))
                else:
                    hklDeglare.append((1, lineDatas))
            elif func.reflectionConditions.BaseFunction.is0kl(h, k, l):
                if func.reflectionConditions.BaseFunction.is_k_even(k):
                    hklList.append((0, lineDatas))
                else:
                    hklDeglare.append((1, lineDatas))
            elif func.reflectionConditions.BaseFunction.ishk0(h, k, l):
                if func.reflectionConditions.BaseFunction.is_h_k_even(h, k):
                    hklList.append((0, lineDatas))
                else:
                    hklDeglare.append((1, lineDatas))
            elif func.reflectionConditions.BaseFunction.is0k0(h, k, l):
                if func.reflectionConditions.BaseFunction.is_k_even(k):
                    hklList.append((0, lineDatas))
                else:
                    hklDeglare.append((1, lineDatas))
            elif func.reflectionConditions.BaseFunction.ish00(h, k, l):
                if func.reflectionConditions.BaseFunction.is_h_even(h):
                    hklList.append((0, lineDatas))
                else:
                    hklDeglare.append((1, lineDatas))
            else:
                hklList.append((0, lineDatas))

    elif spaceGroupName == "A121" or spaceGroupName == "A1m1":
        for lineDatas in hklRes:
            h = lineDatas[0]
            k = lineDatas[1]
            l = lineDatas[2]
            if func.reflectionConditions.BaseFunction.ishkl(h, k, l):
                if func.reflectionConditions.BaseFunction.is_k_l_even(k, l):
                    hklList.append((0, lineDatas))
                else:
                    hklDeglare.append((1, lineDatas))
            elif func.reflectionConditions.BaseFunction.ish0l(h, k, l):
                if func.reflectionConditions.BaseFunction.is_l_even(l):
                    hklList.append((0, lineDatas))
                else:
                    hklDeglare.append((1, lineDatas))
            elif func.reflectionConditions.BaseFunction.is0kl(h, k, l):
                if func.reflectionConditions.BaseFunction.is_k_l_even(k, l):
                    hklList.append((0, lineDatas))
                else:
                    hklDeglare.append((1, lineDatas))
            elif func.reflectionConditions.BaseFunction.ishk0(h, k, l):
                if func.reflectionConditions.BaseFunction.is_k_even(k):
                    hklList.append((0, lineDatas))
                else:
                    hklDeglare.append((1, lineDatas))
            elif func.reflectionConditions.BaseFunction.is0k0(h, k, l):
                if func.reflectionConditions.BaseFunction.is_k_even(k):
                    hklList.append((0, lineDatas))
                else:
                    hklDeglare.append((1, lineDatas))
            elif func.reflectionConditions.BaseFunction.is00l(h, k, l):
                if func.reflectionConditions.BaseFunction.is_l_even(l):
                    hklList.append((0, lineDatas))
                else:
                    hklDeglare.append((1, lineDatas))
            else:
                hklList.append((0, lineDatas))

    elif spaceGroupName == "I121" or spaceGroupName == "I1m1":
        for lineDatas in hklRes:
            h = lineDatas[0]
            k = lineDatas[1]
            l = lineDatas[2]
            if func.reflectionConditions.BaseFunction.ishkl(h, k, l):
                if func.reflectionConditions.BaseFunction.is_h_k_l_even(h, k, l):
                    hklList.append((0, lineDatas))
                else:
                    hklDeglare.append((1, lineDatas))
            elif func.reflectionConditions.BaseFunction.ish0l(h, k, l):
                if func.reflectionConditions.BaseFunction.is_h_l_even(h, l):
                    hklList.append((0, lineDatas))
                else:
                    hklDeglare.append((1, lineDatas))
            elif func.reflectionConditions.BaseFunction.is0kl(h, k, l):
                if func.reflectionConditions.BaseFunction.is_k_l_even(k, l):
                    hklList.append((0, lineDatas))
                else:
                    hklDeglare.append((1, lineDatas))
            elif func.reflectionConditions.BaseFunction.ishk0(h, k, l):
                if func.reflectionConditions.BaseFunction.is_h_k_even(h, k):
                    hklList.append((0, lineDatas))
                else:
                    hklDeglare.append((1, lineDatas))
            elif func.reflectionConditions.BaseFunction.is0k0(h, k, l):
                if func.reflectionConditions.BaseFunction.is_k_even(k):
                    hklList.append((0, lineDatas))
                else:
                    hklDeglare.append((1, lineDatas))
            elif func.reflectionConditions.BaseFunction.ish00(h, k, l):
                if func.reflectionConditions.BaseFunction.is_h_even(h):
                    hklList.append((0, lineDatas))
                else:
                    hklDeglare.append((1, lineDatas))
            elif func.reflectionConditions.BaseFunction.is00l(h, k, l):
                if func.reflectionConditions.BaseFunction.is_l_even(l):
                    hklList.append((0, lineDatas))
                else:
                    hklDeglare.append((1, lineDatas))
            else:
                hklList.append((0, lineDatas))

    elif spaceGroupName == "A112" or spaceGroupName == "A11m":
        for lineDatas in hklRes:
            h = lineDatas[0]
            k = lineDatas[1]
            l = lineDatas[2]
            if func.reflectionConditions.BaseFunction.ishkl(h, k, l):
                if func.reflectionConditions.BaseFunction.is_k_l_even(k, l):
                    hklList.append((0, lineDatas))
                else:
                    hklDeglare.append((1, lineDatas))
            elif func.reflectionConditions.BaseFunction.ishk0(h, k, l):
                if func.reflectionConditions.BaseFunction.is_k_even(k):
                    hklList.append((0, lineDatas))
                else:
                    hklDeglare.append((1, lineDatas))
            elif func.reflectionConditions.BaseFunction.is0kl(h, k, l):
                if func.reflectionConditions.BaseFunction.is_k_l_even(k, l):
                    hklList.append((0, lineDatas))
                else:
                    hklDeglare.append((1, lineDatas))
            elif func.reflectionConditions.BaseFunction.ish0l(h, k, l):
                if func.reflectionConditions.BaseFunction.is_l_even(l):
                    hklList.append((0, lineDatas))
                else:
                    hklDeglare.append((1, lineDatas))
            elif func.reflectionConditions.BaseFunction.is00l(h, k, l):
                if func.reflectionConditions.BaseFunction.is_l_even(l):
                    hklList.append((0, lineDatas))
                else:
                    hklDeglare.append((1, lineDatas))
            elif func.reflectionConditions.BaseFunction.is0k0(h, k, l):
                if func.reflectionConditions.BaseFunction.is_k_even(k):
                    hklList.append((0, lineDatas))
                else:
                    hklDeglare.append((1, lineDatas))
            else:
                hklList.append((0, lineDatas))

    elif spaceGroupName == "B112" or spaceGroupName == "B11m":
        for lineDatas in hklRes:
            h = lineDatas[0]
            k = lineDatas[1]
            l = lineDatas[2]
            if func.reflectionConditions.BaseFunction.ishkl(h, k, l):
                if func.reflectionConditions.BaseFunction.is_h_l_even(h, l):
                    hklList.append((0, lineDatas))
                else:
                    hklDeglare.append((1, lineDatas))
            elif func.reflectionConditions.BaseFunction.ishk0(h, k, l):
                if func.reflectionConditions.BaseFunction.is_h_even(h):
                    hklList.append((0, lineDatas))
                else:
                    hklDeglare.append((1, lineDatas))
            elif func.reflectionConditions.BaseFunction.is0kl(h, k, l):
                if func.reflectionConditions.BaseFunction.is_l_even(l):
                    hklList.append((0, lineDatas))
                else:
                    hklDeglare.append((1, lineDatas))
            elif func.reflectionConditions.BaseFunction.ish0l(h, k, l):
                if func.reflectionConditions.BaseFunction.is_h_l_even(h, l):
                    hklList.append((0, lineDatas))
                else:
                    hklDeglare.append((1, lineDatas))
            elif func.reflectionConditions.BaseFunction.is00l(h, k, l):
                if func.reflectionConditions.BaseFunction.is_l_even(l):
                    hklList.append((0, lineDatas))
                else:
                    hklDeglare.append((1, lineDatas))
            elif func.reflectionConditions.BaseFunction.ish00(h, k, l):
                if func.reflectionConditions.BaseFunction.is_h_even(h):
                    hklList.append((0, lineDatas))
                else:
                    hklDeglare.append((1, lineDatas))
            else:
                hklList.append((0, lineDatas))

    elif spaceGroupName == "I112" or spaceGroupName == "I11m":
        for lineDatas in hklRes:
            h = lineDatas[0]
            k = lineDatas[1]
            l = lineDatas[2]
            if func.reflectionConditions.BaseFunction.ishkl(h, k, l):
                if func.reflectionConditions.BaseFunction.is_h_k_l_even(h, k, l):
                    hklList.append((0, lineDatas))
                else:
                    hklDeglare.append((1, lineDatas))
            elif func.reflectionConditions.BaseFunction.ishk0(h, k, l):
                if func.reflectionConditions.BaseFunction.is_h_k_even(h, k):
                    hklList.append((0, lineDatas))
                else:
                    hklDeglare.append((1, lineDatas))
            elif func.reflectionConditions.BaseFunction.is0kl(h, k, l):
                if func.reflectionConditions.BaseFunction.is_k_l_even(k, l):
                    hklList.append((0, lineDatas))
                else:
                    hklDeglare.append((1, lineDatas))
            elif func.reflectionConditions.BaseFunction.ish0l(h, k, l):
                if func.reflectionConditions.BaseFunction.is_h_l_even(h, l):
                    hklList.append((0, lineDatas))
                else:
                    hklDeglare.append((1, lineDatas))
            elif func.reflectionConditions.BaseFunction.is00l(h, k, l):
                if func.reflectionConditions.BaseFunction.is_l_even(l):
                    hklList.append((0, lineDatas))
                else:
                    hklDeglare.append((1, lineDatas))
            elif func.reflectionConditions.BaseFunction.ish00(h, k, l):
                if func.reflectionConditions.BaseFunction.is_h_even(h):
                    hklList.append((0, lineDatas))
                else:
                    hklDeglare.append((1, lineDatas))
            elif func.reflectionConditions.BaseFunction.is0k0(h, k, l):
                if func.reflectionConditions.BaseFunction.is_k_even(k):
                    hklList.append((0, lineDatas))
                else:
                    hklDeglare.append((1, lineDatas))
            else:
                hklList.append((0, lineDatas))
    else:
        for lineDatas in hklRes:
            hklList.append((0, lineDatas))


    # 拼接
    for data in hklDeglare:
        hklList.append(data)

    for data in hklList:
        print(data)

    print("exit space005 Function")

    return hklList
