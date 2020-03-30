#  学号:1827402008
#  姓名:李星儒
#  IP:192.168.157.142
#  上传时间:2018/11/12 15:01:24

import math


def func1(a, b):
    if a <= b:
        multipy = 1
        for i in range(a, b + 1):
            multipy = multipy * i
        k = 0
        while multipy % 10 == 0:
            k = k + 1
            multipy = multipy / 10
        return k
    else:
        return None


def func2(a, b):
    num = 0
    if a > b:
        return None
    else:
        for i in range(a, b + 1):
            alist = []
            while i / 10 >=1:
                k = i % 10
                alist.append(k)
                i = i // 10
            else:
                alist.append(i)
            if alist == alist[::-1]:
                num = num + 1
        return num


def func3(lst):
    for i in lst[::1]:
        if i < 0:
            lst.remove(i)
        elif i % 3 == 0:
            lst.remove(i)
    lst.sort(reverse=True)
    return lst


if __name__ == "__main__":
    pass