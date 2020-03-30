#  学号:1827405081
#  姓名:曾子越
#  IP:192.168.157.146
#  上传时间:2018/11/12 14:50:30

import math


def func1(a, b):
    product = 1
    acount = 0
    bcount =0

    for i in range(a, b+1):
        product *= i
    aproduct = product
    bproduct = product

    while aproduct % 2 == 0:
        aproduct /= 2
        acount += 1

    while bproduct % 2 == 0:
        bproduct /= 2
        bcount += 1

    return min(acount, bcount)

def func2(a,b):
    count = 0
    for i in range(a, b+1):
        xstr = str(i)
        digits = list(xstr)
        length = len(digits)
        ystr = ''

        for i in range(0, length):
            ystr += list.pop(digits)
        if ystr == xstr:
            count += 1

    return count
            
def func3(lst):
    length = len(lst)
    for i in range(1, length+1):
        x = lst[length-i]
        if x < 0:
            del lst[length-i]

    length = len(lst)
    for i in range(1, length+1):
        x = lst[length-i]
        if x % 3 == 0:
            del lst[length-i]

    lst = sorted(lst)
    return lst

if __name__=="__main__":
    func3([-1, -2, -3, 0, 9, 7, 6, 8, 2, 5, 4, 3, 1])

    pass
