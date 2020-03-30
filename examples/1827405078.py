#  学号:1827405078
#  姓名:周童
#  IP:192.168.157.228
#  上传时间:2018/11/12 15:20:49

import math
def func1(a,b):
    if int(a)!=a or int(b)!=b or a>=b or a<=0 or b<=0:
        return None
    else:
        Tn=1
        d=0
        for i in range(a,b+1):
            Tn=Tn*i
            c=list(str(Tn))
            while c[-1]!="0":
                del c[-1]
                continue
            else:
                d+=1
        return d
def func2(a,b):
    if int(a)!=a or int(b)!=b or a<=0 or b<=0 or a==b:
        return None
    elif a<b:
        for i in range(a,b+1):
            c=list(str(i))
            d=0
            while list(reversed(c))==c:
                d+=1
                continue
        return d
    elif a>b:
        for j in range(b,a+1):
            c=list(str(j))
            d=0
            while list(reversed(c))==c:
                d+=1
                continue
        return d
def func3(lst):
    for i in lst:
        if int(str(i))!=str(i) or str(i)<0 or str(i)%3==0:
            lst.remove(i)
        else:
            lst=sorted(lst,reverse=True)
    return lst

if __name__=="__main__":
	print(func3([1]))
