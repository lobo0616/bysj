#  学号:1827402012
#  姓名:余畅
#  IP:192.168.157.237
#  上传时间:2018/11/12 15:20:32

import math
def func1(a,b):
    a=int(a)
    b=int(b)
    if a>=b:
        a,b=b,a
    c=1
    while a<=b:
        c=c*a
        a+=1
    count=0
    if c%10!=0:
        return None
    else:
        while c%10==0:
            count+=1
            c=c/10
    return(count)
    return

def func2(a,b):
    count=0
    if a>b:
        return None
    for x in range(a,b+1):
        c=str(x)
        if list(reversed(c))==list(c):
            count+=1
    return(count)
    return
            
def func3(lst):
    list1=[]
    for x in lst:
        if x<0 or x%3==0:
            continue
        else:
            list1.append(x)
    sorted(list1,reverse=True)
    return(list1)
    return

if __name__=="__main__":
	print(func2(23,45))
