#  学号:1827405077
#  姓名:刘阳
#  IP:192.168.157.229
#  上传时间:2018/11/12 15:18:26

import math
def func1(a,b):
    if a>=b:
        return None
    else:
        n = 1
        for i in range(a,b+1):
            n*=i
        s1 = list(str(n))
        num = len(s1)
        t = 0
        f=-1
        for m in range(num):
            if s1[f] =='0':
                t+=1
                f-=1
    return  t

def func2(a,b):
    h = 0
    if a%1!=0 or b%1!=0:
        return None
    elif a==b:
        return None
    else:
        if a>b:
            a,b=b,a
    for i in range(a,b+1):
        if i <0:
            continue
        elif i ==0 or (i>1 and i<10):
            h+=1
            continue
        else:
            n = 1
            while i>=10**n:
                n+=1
            res=[]
            for j in range(n):
                a = i%10
                i = (i-a)/10
                res.append(a)
            num = len(res)
            c=0
            for n in range(num):
                if res[c] == res[num-1-c]:
                    c+=1
                if c==num:
                    h+=1
    return h
def func3(lst):
    for i in lst:
        if i%1!=0:
            lst.remove(i)
        if i<0 or i%3==0:
            lst.remove(i)
    ls11 = sorted(lst,reverse=True)
    return ls11

if __name__=="__main__":
	print(func2(1.1,200))