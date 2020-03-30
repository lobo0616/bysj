#  学号:1827402010
#  姓名:李欣雨
#  IP:192.168.157.170
#  上传时间:2018/11/12 15:16:27

import math
def func1(a,b):
    m=a
    while a<=b:
        m=m*(a+1)
        a+=1
    j=0
    while m%10==0:
        j+=1
        m=m/10
    return j

def func2(a,b):
    i=0
    for j in range(a,b+1):
        j=str(j)
        if j==j[::-1]:
            i+=1
    return i
            
def func3(lst):
    res1=[]
    res2=[]
    for i in lst:
        if i <0 or i%3==0 or i/3==1:
            res1.append(i)
        else:
            res2.append(i)
            lst1=sorted(res2,reverse=True)
    return lst1

if __name__=="__main__":
 print(func1(5,10))