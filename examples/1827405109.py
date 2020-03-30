#  学号:1827405109
#  姓名:郑悦薇
#  IP:192.168.157.135
#  上传时间:2018/11/12 14:11:08

import math
def func1(a,b):
    if a <= 0 or b < a:
        return
    f1_int_res = 1
    f1_int_sum = 0
    for i in range(a, b+1):
        f1_int_res *= i
    while f1_int_res % 10 == 0:
        f1_int_sum += 1
        f1_int_res //= 10
    return f1_int_sum

def func2(a,b):
    f2_int_sum = 0
    if a <= 0 or b <= 0:
        return
    if a<=b:
        for i in range(a, b+1):
            if phw(i) == True:
                f2_int_sum += 1
    else:
        for i in range(b, a+1):
            if phw(i) == True:
                f2_int_sum += 1
    return  f2_int_sum

def phw(x):
    phw_int_res = 0
    x=int(x)
    phw_int_zhz = x
    while x:
        phw_int_res = phw_int_res * 10 + x % 10
        x //= 10
    return phw_int_res == phw_int_zhz

def func3(lst):
    f3_list_res=[]
    for i in lst:
        if i % 3 and i >= 0:
            f3_list_res.append(i)
    f3_list_res.sort()
    return f3_list_res

if __name__=="__main__":
    pass