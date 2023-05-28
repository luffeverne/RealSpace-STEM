import func.reflectionConditions.BaseFunction


def spaceHandle(spaceGroupName, hklRes):
    print("enter space004 Function")

    hklList = []
    hklDeglare = []

    if spaceGroupName == "P1211":
        for lineDatas in hklRes:
            h = lineDatas[0]
            k = lineDatas[1]
            l = lineDatas[2]
            if func.reflectionConditions.BaseFunction.is0k0(h, k, l):
                if func.reflectionConditions.BaseFunction.is_k_even(k):
                    hklList.append((0, lineDatas))
                else:
                    hklDeglare.append((1, lineDatas))
            else:
                hklList.append((0, lineDatas))

    elif spaceGroupName == "P1121":
        for lineDatas in hklRes:
            h = lineDatas[0]
            k = lineDatas[1]
            l = lineDatas[2]
            if func.reflectionConditions.BaseFunction.is00l(h, k, l):
                if func.reflectionConditions.BaseFunction.is_l_even(l):
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

    print("exit space004 Function")

    return hklList
