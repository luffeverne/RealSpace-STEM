import re


def formateNum(content):
    pNum = r'^(-?\d*\.\d+)'
    arr = re.findall(pNum, content)  # str
    if len(arr) == 0:
        return 0
    return round(float(arr[0]), 4)
