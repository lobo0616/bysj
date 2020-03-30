#  学号:1827405089
#  姓名:陆嘉炜
#  IP:192.168.157.144
#  上传时间:2018/11/12 14:34:34

import math
def func1(a,b):
    if b>a:
        x=1
        count=0
        for i in range (a,b+1):
            x=x*i
        while True:
            if x%10==0:
                count=count+1
                x=x//10
            else:
                break
        return count
    else:
        return None
def func2(a,b):
    if b>a:
        c=0
        k=0
        count=0
        x=list(range(a,b+1))
        for i in x:
            k=i
            c=0
            while i!=0:
                c=c*10
                c=c+i%10
                i=i//10
            if k==c:
                count=count+1
        return count
    else:
        return None
            
def func3(lst):
    for i in lst[::]:
        if i<0 or i%3==0:
            lst.remove(i)
    lst.sort(reverse=True)
    return lst

if __name__=="__main__":
    print(func3([1,2,3,4,5,1,1,1,1,2,2,3,4,6,3,-1,-2]))

