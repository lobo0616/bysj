#  学号:1827402027
#  姓名:史云龙
#  IP:192.168.157.160
#  上传时间:2018/11/12 14:52:53

import math
def func1(a,b):
    if b>a:
        n=0
        num=1
        for i in range(a,b+1):
            num*=i
        c=list(str(num))
        for j in range(1,len(c)+1):
            if c[-j]=="0":
                n+=1
            else:
                return n
        return n
    else:
        return "None"

def func2(a,b):
    if b>a:
        n=0
        for i in range(a,b+1):
            j=i
            num=0
            while i>0:
                num=i%10+num*10
                i//=10
            if num==j:
                n+=1
        return n
    else:
        return "None"
            
def func3(lst):
    for i in lst[:]:
        if i<0:
            lst.remove(i)
        elif i%3==0:
            lst.remove(i)
        print(lst)
    return sorted(lst)[::-1]

if __name__=="__main__":
    pass
