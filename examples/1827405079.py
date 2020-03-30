#  学号:1827405079
#  姓名:陈佑
#  IP:192.168.157.218
#  上传时间:2018/11/12 15:20:48

import math


def func1(a, b):
    a = int(input('a='))
    b = int(input('b='))
    if a >= b:
        a, b = b, a
    list = range(a, b + 1, 1)
    x = 0
    y = 0
    for i in list:
        while i % 2 == 0:
            x += 1
            i = i // 2
        while i % 5 == 0:
            y += 1
            i = i // 5
    print(min(x, y))
    return


def func2(a, b):
    a = int(input('a='))
    b = int(input('b='))
    list = range(a, b + 1, 1)
    for i in list:
        if i == int(str(i)[::-1]):
    print()
    return


def func3(lst):
    a_list = []
    x = int(input('随机数'))
    list.append(x)
    if x % 3 == 0:
        del a_list[x]
    if x < 0:
        del a_list[x]
    a_list.sort()
    return


if __name__ == "__main__":
    pass
