#  学号:1827405162
#  姓名:霍宣甫
#  IP:192.168.157.174
#  上传时间:2018/11/12 15:17:56

import math


def func1(a, b):
    if a < 0 or b < 0 or a > b:
        return False
    else:
        if a == b:
            num1 = a * a
        else:
            num1 = 1
            for i in range(a, b + 1):
                num1 = num1 * i
        num = 0
        while num1 // 10 != 0 and num1 % 10 == 0:
            num += 1
            num1 = num1 / 10
        else:
            return num


def func2(a, b):
    if a < 0 or b < 0:
        return False
    else:
        num = 0
        if a <= b:
            for i in range(a, b + 1):
                x = str(i)
                y = x[::-1]
                if x == y:
                    num += 1

        else:
            for i in range(b, a + 1):
                x = str(i)
                y = x[::-1]
                if x == y:
                    num += 1
    return num


def func3(lst):
    n = []
    for i in range(0, len(lst)):
        m = lst[i]
        if m > 0 and m % 3 != 0:
            n.append(lst[i])
    sorted(n, reverse=True)
    return n




