def isAttend(h, k, l, str):
    return eval(str)


def ishhl(h, k, l):
    if k == h and h != 0 and l != 0:
        return True
    return False


def ishhl(h, k, l):
    if k == h and h != 0 and l != 0:
        return True
    return False


def ishkk(h, k, l):
    if k == l and k != 0 and h != 0:
        return True
    return False


def islkl(h, k, l):
    if h == l and k != 0 and l != 0:
        return True
    return False


def ish_hl(h, k, l):
    if k == -h and h != 0 and l != 0:
        return True
    return False


def ishkl(h, k, l):
    if h != 0 and k != 0 and l != 0:
        return True
    return False


def is0kl(h, k, l):
    if h == 0 and k != 0 and l != 0:
        return True
    return False


def ish0l(h, k, l):
    if h != 0 and k == 0 and l != 0:
        return True
    return False


def ishk0(h, k, l):
    if h != 0 and k != 0 and l == 0:
        return True
    return False


def is00l(h, k, l):
    if h == 0 and k == 0 and l != 0:
        return True
    return False


def ish00(h, k, l):
    if h != 0 and k == 0 and l == 0:
        return True
    return False


def is0k0(h, k, l):
    if h == 0 and k != 0 and l == 0:
        return True
    return False


def ish_h0(h, k, l):
    if h != 0 and k == -h and l == 0:
        return True
    return False


def is_h_k_l_even(h, k, l):
    if (h + k + l) % 2 == 0:
        return True
    return False


def is_k_l_even(k, l):
    if (k + l) % 2 == 0:
        return True
    return False


def is_h_l_even(h, l):
    if (h + l) % 2 == 0:
        return True
    return False


def is_h_k_even(h, k):
    if (h + k) % 2 == 0:
        return True
    return False


def is_h_even(h):
    if h % 2 == 0:
        return True
    return False


def is_k_even(k):
    if k % 2 == 0:
        return True
    return False


def is_l_even(l):
    if l % 2 == 0:
        return True
    return False


def is_k_l_four(k, l):
    if (k + l) % 4 == 0:
        return True
    return False


def is_h_l_four(h, l):
    if (h + l) % 4 == 0:
        return True
    return False


def is_h_k_four(h, k):
    if (h + k) % 4 == 0:
        return True
    return False


def is_h_four(h):
    if h % 4 == 0:
        return True
    return False


def is_k_four(k):
    if k % 4 == 0:
        return True
    return False


def is_l_four(l):
    if l % 4 == 0:
        return True
    return False


def is_2h_l_four(h, l):
    if (2 * h + l) % 4 == 0:
        return True
    return False


def is_2k_l_four(k, l):
    if (2 * k + l) % 4 == 0:
        return True
    return False


def is_k_2l_four(k, l):
    if (2 * l + k) % 4 == 0:
        return True
    return False


def is_l_2k_four(k, l):
    if (2 * k + l) % 4 == 0:
        return True
    return False


def is_h_2k_four(h, k):
    if (2 * k + h) % 4 == 0:
        return True
    return False



def is_h_three(h):
    if h % 3 == 0:
        return True
    return False


def is_l_three(l):
    if l % 3 == 0:
        return True
    return False


def is_k_three(k):
    if k % 3 == 0:
        return True
    return False


def is__h_k_l_three(h, k, l):
    if (-1 * h + k + l) % 3 == 0:
        return True
    return False


def is__h_k_three(h, k):
    if (-1 * h + k) % 3 == 0:
        return True
    return False


def is_h_l_three(h, l):
    if (h + l) % 3 == 0:
        return True
    return False


def is_h_six(h):
    if h % 6 == 0:
        return True
    return False


def is_k_six(k):
    if k % 6 == 0:
        return True
    return False


def is_l_six(l):
    if l % 6 == 0:
        return True
    return False

