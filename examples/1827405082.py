#  学号:1827405082
#  姓名:张悟童
#  IP:192.168.157.219
#  上传时间:2018/11/12 15:19:18

import math
def func1(a,b):
    a=int(input('a='))
    b=int(input('b='))
    if a>=b:
        a,b=b,a
    list=range(a,b+1,1)
    two=0
    five=0
    for i in list:
        while i%2==0:
            two+=1
            i=i//2
        while i%5==0:
            five+=1
            i=i//5
    print(min(two,five))
    return

def func2(a,b):
    a=int(input('a='))
    b=int(input('b='))
    list=range(a,b+1,1)
    count=0
    for i in list:
        if i==int(str(i)[::-1]):
            count+=1
    print(count)
    return
            
def func3(lst):
    num=int(input('请输入一些数字'))
    list=[]
    list.append(num)
    if num % 3 ==0 or num<0:
        list.remove(num)
    list.sort(num)
    print(list)
    return

if __name__=="__main__":
    pass


