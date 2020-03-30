#  学号:1827402026
#  姓名:谢仪伟
#  IP:192.168.157.177
#  上传时间:2018/11/12 15:22:50

import math
def func1(a,b):
    if a>b:
       n=a
       a=b
       b=n

    if a<b:
       a=a*(a+1)
       m=a%10
       n=0
       while m==0:
          n=n+1
       return



def func2(a, b):
    if a<=0 or b<=0:
       return
    if a>b:
       c=a
       a=b
       b=c
    m=0
    for i in range(a,b+1):
        n=i
    hui=int(math.huiwen(i))+1
    o=0
    for j in range(0,hui):
        o=o*10+n%10
        n=n//10
    if hui==i:
        m=m+1
    return m






def func3(lst):
    for i in range(len[lst]-1,-1)
   if lst[i]
    return


if __name__ == "__main__":
    pass
