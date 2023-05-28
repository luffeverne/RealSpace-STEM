import func.reflectionConditions.BaseFunction as bf


# 198, 208
def spaceHandle(spaceGroupName, hklRes):
    print("enter space198 Function")

    hklList = []
    hklDeglare = []

    for lineDatas in hklRes:
        h = lineDatas[0]
        k = lineDatas[1]
        l = lineDatas[2]

        if bf.ish00(h, k, l):
            if bf.is_h_even(h):
                hklList.append((0, lineDatas))
            else:
                hklDeglare.append((1, lineDatas))
        elif bf.is0k0(h, k, l):
            if bf.is_k_even(k):
                hklList.append((0, lineDatas))
            else:
                hklDeglare.append((1, lineDatas))
        elif bf.is00l(h, k, l):
            if bf.is_l_even(l):
                hklList.append((0, lineDatas))
            else:
                hklDeglare.append((1, lineDatas))
        else:
            if h == 0 and k == 0 and l == 0:
                hklList.append((0, lineDatas))
            else:
                hklList.append((1, lineDatas))

    for data in hklDeglare:
        hklList.append(data)

    print("exit space198 Function")

    return hklList
