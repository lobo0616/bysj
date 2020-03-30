#  学号:1827405157
#  姓名:唐钰旻
#  IP:192.168.157.173
#  上传时间:2018/11/12 15:15:15

import math


def func1(a, b):
    return
    result = 1
    count = 0
    if a <= b:
        for i in range(a, b + 1):
            result = result * i
            while (result % 10 == 0):
                count += 1
                return count
            if (result % 10 != 0):
                return None
    else:
        return None


def func2(a, b):
    return
    if a > b:
        return None
    else:
        count = 0
        for i in range(a, b + 1):
            a = str(i)
            b = a[::-1]
            if a == b:
                count += 1
            else:
                count = count
        if count != 0:
            return count
        else:
            return None


def func3(lst):
    return
    for i in lst:
        if i < 0 or (i % 3 == 0):
            list.remove(i)
        lst.sort(reverse=True)
    return lst


if __name__ == "__main__":
    pass
