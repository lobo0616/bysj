#  学号:1827405047
#  姓名:刘源
#  IP:192.168.157.157
#  上传时间:2018/11/12 15:17:35

import math


def func1(a, b):
    if a<=0 or b<=0 or a>=b:
        return None
    sum=1
    count=1
    while a<b:
        sum=sum*a
        a+=1
    while sum%(10**count)==0:
        count+=1

    return count-1


def func2(a, b):
    return


def func3(lst):
    list = [i for i in lst if i > 0 and i % 3 != 0]
    list.sort(reverse=True)
    return list
if __name__ == "__main__":
    pass
