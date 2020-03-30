#  学号:1827402025
#  姓名:杨婕
#  IP:192.168.157.216
#  上传时间:2018/11/12 15:18:09

import math
def func1(a,b):
    if a<=0 or b<=0:
        return
    if a>b:
        a,b=b,a
        p=1
        for i in range(a,b+1):
            p=p*i
            s=0
            while p%10==0:
                s=s+1
                p=p//10
            return s
        print(func1(1,10))


def func2(a,b):
    s=0
    for i in range(a,b+1):
        n=i
        x=int(math.log10(i))+1
        h=0
        for j in range(x):
            h=h*10+n%10
            n=n//10
        if h==i:
            s=s+1
    return s

def func3(lst):
    for i in range(len(lst)):
        if lst[i]<0 or lst[i]%3==0:
            lst.remove(lst[i])
    lst.sort(reverse=True)
    return lst

if __name__=="__main__":
    print()