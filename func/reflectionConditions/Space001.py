# 1, 2, 3, 6, 10, 16, 25, 47, 75, 81, 83, 89, 99, 110, 115, 123, 143, 147, 149, 156, 157, 162, 168, 174
# 175, 177, 183, 187, 189, 191, 195, 200, 207, 215, 221
def spaceHandle(spaceGroupName, hklRes):
    print("enter space001 Function")

    hklList = []

    for lineDatas in hklRes:
        hklList.append((0, lineDatas))

    print("exit space001 Function")

    return hklList
