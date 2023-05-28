import func.reflectionConditions.BaseFunction as bf


# 146, 148, 155,
def spaceHandle(spaceGroupName, hklRes):
    print("enter space146 Function")

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
            if bf.is_h_l_three(h, l):
                hklList.append((0, linedatas))
            else:
                hklDeglare.append((1, linedatas))
        elif bf.is00l(h, k, l):
            if bf.is_l_three(l):
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

    print("exit space146 Function")

    return hklList
