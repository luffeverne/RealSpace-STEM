import func.reflectionConditions.BaseFunction 


# 9
def spaceHandle(spaceGroupName, hklRes):
    print("enter space009 Function")

    hklList = []
    hklDeglare = []

    if spaceGroupName == "C1c1":
        for linedatas in hklRes:
            h = linedatas[0]
            k = (0, linedatas)[1]
            l = (0, linedatas)[2]
            if func.reflectionConditions.BaseFunction.ishkl(h, k, l):
                if func.reflectionConditions.BaseFunction.is_h_k_even(h, k):
                    hklList.append((0, linedatas))
                else:
                    hklDeglare.append((1, linedatas))
            elif func.reflectionConditions.BaseFunction.ish0l(h, k, l):
                if func.reflectionConditions.BaseFunction.is_h_even(h) and func.reflectionConditions.BaseFunction.is_l_even(l):
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
            elif func.reflectionConditions.BaseFunction.is00l(h, k, l):
                if func.reflectionConditions.BaseFunction.is_l_even(l):
                    hklList.append((0, linedatas))
            else:
                hklList.append((0, linedatas))

    elif spaceGroupName == "A1n1":
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
                if func.reflectionConditions.BaseFunction.is_h_even(h) and func.reflectionConditions.BaseFunction.is_l_even(l):
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
            elif func.reflectionConditions.BaseFunction.ish00(h, k, l):
                if func.reflectionConditions.BaseFunction.is_h_even(h):
                    hklList.append((0, linedatas))
                else:
                    hklDeglare.append((1, linedatas))
            elif func.reflectionConditions.BaseFunction.is00l(h, k, l):
                if func.reflectionConditions.BaseFunction.is_l_even(l):
                    hklList.append((0, linedatas))
            else:
                hklList.append((0, linedatas))

    elif spaceGroupName == "I1a1":
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
                if func.reflectionConditions.BaseFunction.is_h_even(h) and func.reflectionConditions.BaseFunction.is_l_even(l):
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
                hklList.append((0, linedatas))

    elif spaceGroupName == "A11a":
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
                if func.reflectionConditions.BaseFunction.is_h_even(h) and func.reflectionConditions.BaseFunction.is_k_even(k):
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
            elif func.reflectionConditions.BaseFunction.ish00(h, k, l):
                if func.reflectionConditions.BaseFunction.is_h_even(h):
                    hklList.append((0, linedatas))
                else:
                    hklDeglare.append((1, linedatas))
            elif func.reflectionConditions.BaseFunction.is0k0(h, k, l):
                if func.reflectionConditions.BaseFunction.is_k_even(k):
                    hklList.append((0, linedatas))
            else:
                hklList.append((0, linedatas))

    elif spaceGroupName == "B11n":
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
                if func.reflectionConditions.BaseFunction.is_h_even(h) and func.reflectionConditions.BaseFunction.is_k_even(k):
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
            elif func.reflectionConditions.BaseFunction.is0k0(h, k, l):
                if func.reflectionConditions.BaseFunction.is_k_even(k):
                    hklList.append((0, linedatas))
            else:
                hklList.append((0, linedatas))

    elif spaceGroupName == "I11b":
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
                if func.reflectionConditions.BaseFunction.is_h_even(h) and func.reflectionConditions.BaseFunction.is_k_even(k):
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
