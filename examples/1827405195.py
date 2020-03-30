#  学号:1827405195
#  姓名:刘浩
#  IP:192.168.157.145
#  上传时间:2018/11/12 15:11:16

import math
def func1(a,b):
    res=1
    if a<=0 or b<=0 or a>b:
        return None
    for i in range(b-a+1):
        res=res*(a+i)
    t=str(res)
    count=0
    for j in t[::-1]:
        if j=='0':
            count+=1
        else:
            res=int(res)
            break
    return count

def func2(a,b):
    A=[]
    if a<=0 or b<=0:
        return None
    for i in range(a,b+1):
        temp=i
        res=''
        while i>0:
            res=res+'{:0}'.format(i%10)
            i=i//10
        res=int(res)
        if res==temp:
            A.append(res)
    return len(A)

def func3(lst):
    for i in lst[::]:
        if i<0 or i%3==0:
            lst.remove(i)
    lst.reverse()
    return lst

if __name__=="__main__":
    pass