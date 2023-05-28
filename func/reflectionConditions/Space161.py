import func.reflectionConditions.BaseFunction as bf


# 161
def spaceHandle(spaceGroupName, hklRes):
    print("enter space161 Function")

    hklList = []
    hklDeglare = []

    for linedatas in hklRes:
        h = linedatas[0]
        k = linedatas[1]
        l = linedatas[2]

        if bf.ishkl(h, k, l):
            if bf.is__h_k_l_three(h, k, l):
                hklList.append((0, linedatas))
            else:
                hklDeglare.append((1, linedatas))
        elif bf.ishk0(h, k, l):
            if bf.is__h_k_three(h, k):
                hklList.append((0, linedatas))
            else:
                hklDeglare.append((1, linedatas))
        elif bf.ishhl(h, k, l):
            if bf.is_l_three(l):
                hklList.append((0, linedatas))
            else:
                hklDeglare.append((1, linedatas))
        elif bf.ish_hl(h, k, l):
            if bf.is_h_l_three(h, l) and bf.is_l_even(l):
                hklList.append((0, linedatas))
            else:
                hklDeglare.append((1, linedatas))
        elif bf.is00l(h, k, l):
            if bf.is_l_six(l):
                hklList.append((0, linedatas))
            else:
                hklDeglare.append((1, linedatas))
        elif bf.ish_h0(h, k, l):
            if bf.is_h_three(h):
                hklList.append((0, linedatas))
            else:
                hklDeglare.append((1, linedatas))
        else:
            hklList.append((0, linedatas))

    print("exit space161 Function")

    return hklList
