#  学号:1827402028
#  姓名:宋怡霖
#  IP:192.168.157.184
#  上传时间:2018/11/12 15:19:11

import math
def func1(a,b):
    if a<=0 or b<=0:
        return
    if a>b:
        a,b=b,a
    p=1
    for i in range(a,b+1):
        p=p*i
    n=0
    while p%10==0:
        n+=1
        p=p//10
    return n


def func2(a,b):
    if a<=0 or b<=0:
        return
    if a>b:
        a,b=b,a
    s=0
    res=0
    for i in range(a,b+1):
        while res<i:
            res=res*10+i%10
            i=i//10
        if i==res or i==res//10:
            s+=1
        res=0
    return s


            
def func3(lst):
    for i in range (len(lst)-1,-1,-1):
        if lst[i]<0 or lst[i]%3==0:
            lst.remove(lst[i])
        lst.sort(reverse=True)
    return lst

if __name__=="__main__":
    print(func3([1,8,3,3,3,36]))

