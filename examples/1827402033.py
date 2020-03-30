#  学号:1827402033
#  姓名:邓国斌
#  IP:192.168.157.159
#  上传时间:2018/11/12 14:49:10

import math
def func1(a,b):
    if a>=b or a<0 or b<0:
        return None
    n,n2=1,0
    for i in range(a,b+1):
        i=int(i)
        n*=i
    n=str(n)
    n=n[::-1]
    for j in list(n):
        if j=="0":
            n2+=1
        elif j!="0":
            break
    return n2

def func2(a,b):
    if a>=b or a<0 or b<0:
        return None
    n=0
    for i in range(a, b + 1):
        i=list(str(i))
        j=i[::-1]
        print(i, j)
        if j==i:
            n+=1
    return n


def func3(lst):
    list1=sorted(lst)
    for i in lst:
        i=int(i)
        if i<0 or i%3==0:
            list1.remove(i)
    return list1


if __name__=="__main__":
    pass


