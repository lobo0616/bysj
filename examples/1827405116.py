#  学号:1827405116
#  姓名:齐文逸
#  IP:192.168.157.137
#  上传时间:2018/11/12 15:21:42

import math
def func1(a,b):
    n=1
    for i in range(a,b+1):
        n=n*i
    for j in range(1,len(str(n))):
        if n%pow(10,j)!=0:
            break
        else:
            j=j
    return j-1


def func2(a,b):
    for j in range(a,b):
        x=0
        i=1
        while i<=len(str(j))/2:
            if j%pow(10,len(str(j))-i)==j%pow(10,i):
                i=i+1
                continue
            else:
                break
        else:
            x=x+1
        continue
    return x


def func3(lst):
    i=0
    while i<len(lst):
        if lst[i]<0 or (lst[i])%3==0:
            lst.pop(i)
            i=i
            continue
        else:
            i=i+1
            continue

    lst.sort(reverse=True)
    print(lst)

if __name__=="__main__":
    print(func2(1,100))


