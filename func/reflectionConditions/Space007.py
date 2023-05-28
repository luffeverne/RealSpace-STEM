import func.reflectionConditions.BaseFunction


# 7
def spaceHandle(spaceGroupName, hklRes):
    print("enter space007 Function")

    hklList = []
    hklDeglare = []

    if spaceGroupName == "Pc11" \
            or spaceGroupName == "P1c1":
        for lineDatas in hklRes:
            h = lineDatas[0]
            k = lineDatas[1]
            l = lineDatas[2]
            if func.reflectionConditions.BaseFunction.ish0l(h, k, l):
                if func.reflectionConditions.BaseFunction.is_l_even(l):
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
    elif spaceGroupName == "P1n1":
        for lineDatas in hklRes:
            h = lineDatas[0]
            k = lineDatas[1]
            l = lineDatas[2]
            if func.reflectionConditions.BaseFunction.ish0l(h, k, l):
                if func.reflectionConditions.BaseFunction.is_h_l_even(h, l):
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
    elif spaceGroupName == "P1a1":
        for lineDatas in hklRes:
            h = lineDatas[0]
            k = lineDatas[1]
            l = lineDatas[2]
            if func.reflectionConditions.BaseFunction.ish0l(h, k, l):
                if func.reflectionConditions.BaseFunction.is_h_even(h):
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
    elif spaceGroupName == "P11a":
        for lineDatas in hklRes:
            h = lineDatas[0]
            k = lineDatas[1]
            l = lineDatas[2]
            if func.reflectionConditions.BaseFunction.ishk0(h, k, l):
                if func.reflectionConditions.BaseFunction.is_h_even(h):
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
    elif spaceGroupName == "P11n":
        for lineDatas in hklRes:
            h = lineDatas[0]
            k = lineDatas[1]
            l = lineDatas[2]
            if func.reflectionConditions.BaseFunction.ishk0(h, k, l):
                if func.reflectionConditions.BaseFunction.is_h_k_even(h, k):
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
    elif spaceGroupName == "P11b":
        for lineDatas in hklRes:
            h = lineDatas[0]
            k = lineDatas[1]
            l = lineDatas[2]
            if func.reflectionConditions.BaseFunction.ishk0(h, k, l):
                if func.reflectionConditions.BaseFunction.is_k_even(k):
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

    print("hklList")
    for data in hklList:
        print(data)

    print("exit space007 Function")

    return hklList
