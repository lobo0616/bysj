#  学号:1827402007
#  姓名:徐李琨
#  IP:192.168.157.140
#  上传时间:2018/11/12 15:07:46

import math
def func1(a,b):
    if a>b:
        return None
    t = 1
    for i in range(a,b+1):
        t=i*t
    s=0
    while t%10==0:
        t=t//10
        s=s+1
    return s
def func2(a,b):
    r=0
    for i in range(a,b+1):

        if i%10==0:
            continue
        if a>b:
            return None
        y = 0
        while (i > y):
            y = i % 10 + y * 10
            i //= 10
        if i == y or i == y // 10:
            r+=1
    return r
            
def func3(lst):
    i=0
    while i<len(lst):
        if lst[i]<0  or lst[i]%3==0 :
            lst.pop(i)
        else:
            i+=1
    lst.sort(reverse=True)
    return lst
if __name__=="__main__":
   print(func3([-1,5,3,549847,21654,54]))
