#  学号:1827405172
#  姓名:叶苏青
#  IP:192.168.157.139
#  上传时间:2018/11/12 15:02:34

import math
def func1(a,b):
    if type(a)!=int or type(b)!=int or a>b or a<0 or b<0:
        return None
    i = 0
    Num_1 = 0
    Sum = 1
    while (a+i) != b:
        Sum = Sum * (a + i)
        i+=1
    else:
        while Sum % 10 == 0:
            Sum /= 10
            Num_1 += 1
        else:
            if Sum<10:
                return 0
            else:
                return Num_1

def func2(a,b):
    Num_2=0
    for i in range(a,b):
        i=str(i)
        if i[::-1]==i:
            Num_2+=1
        else:
            continue
    return Num_2
            
def func3(lst):
    for i in lst[::-1]:
        if i < 0 or i % 3 == 0:
            lst.remove(i)
        else:
            continue
    return sorted(lst,reverse=True)

if __name__=="__main__":
    pass
