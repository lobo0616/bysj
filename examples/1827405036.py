#  学号:1827405036
#  姓名:徐辰洋
#  IP:192.168.157.180
#  上传时间:2018/11/12 15:20:20

import math


def func1(a, b):
    num = 0
    rfs = 1
    for i in range(a, b + 1):
        rfs = rfs * i
    while rfs % 10 == 0:
        num += 1
        rfs = rfs / 10
    return num

    return


def func2(a, b):
    num = 0

    for i in range(a, b + 1):
        x = i
        res = 0
        while i > 0:
            res = res * 10 + i % 10
            i = i // 10
        if res == x:
            num += 1
    return num
    return


def func3(lst):
    for i in range(0, len(lst)):
        if lst[i] < 0 or lst[i] % 3 == 0:
            del lst[i]
    lst.sort(reverse=True)
    return lst
    return


if __name__ == "__main__":
    print(func3([4, 9]))
