import func.reflectionConditions.BaseFunction as bf


# 228
def spaceHandle(spaceGroupName, hklRes):
    print("enter space228 Function")

    hklList = []
    hklDeglare = []

    for lineDatas in hklRes:
        h = lineDatas[0]
        k = lineDatas[1]
        l = lineDatas[2]

        if bf.ishkl(h, k, l):
            if bf.is_h_k_even(h, k) and bf.is_h_l_even(h, l) and bf.is_k_l_even(k, l):
                hklList.append((0, lineDatas))
            else:
                hklDeglare.append((1, lineDatas))
        elif bf.is0kl(h, k, l):
            if bf.is_k_l_four(k, l) and bf.is_k_even(k) and bf.is_l_even(l):
                hklList.append((0, lineDatas))
            else:
                hklDeglare.append((1, lineDatas))
        elif bf.ish0l(h, k, l):
            if bf.is_h_l_four(h, l) and bf.is_h_even(h) and bf.is_l_even(l):
                hklList.append((0, lineDatas))
            else:
                hklDeglare.append((1, lineDatas))
        elif bf.ishk0(h, k, l):
            if bf.is_h_k_four(h, k) and bf.is_h_even(h) and bf.is_k_even(k):
                hklList.append((0, lineDatas))
            else:
                hklDeglare.append((1, lineDatas))
        elif bf.ishhl(h, k, l):
            if bf.is_h_even(h) and bf.is_l_even(l):
                hklList.append((0, lineDatas))
            else:
                hklDeglare.append((1, lineDatas))
        elif bf.ishkk(h, k, l):
            if bf.is_h_even(h) and bf.is_k_even(k):
                hklList.append((0, lineDatas))
            else:
                hklDeglare.append((1, lineDatas))
        elif bf.islkl(h, k, l):
            if bf.is_k_even(k) and bf.is_l_even(l):
                hklList.append((0, lineDatas))
            else:
                hklDeglare.append((1, lineDatas))
        elif bf.ish00(h, k, l):
            if bf.is_h_four(h):
                hklList.append((0, lineDatas))
            else:
                hklDeglare.append((1, lineDatas))
        elif bf.is0k0(h, k, l):
            if bf.is_k_four(k):
                hklList.append((0, lineDatas))
            else:
                hklDeglare.append((1, lineDatas))
        elif bf.is00l(h, k, l):
            if bf.is_l_four(l):
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

    print("exit space228 Function")

    return hklList
