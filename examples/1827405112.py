#  学号:1827405112
#  姓名:陈翔
#  IP:192.168.157.183
#  上传时间:2018/11/12 15:07:36

import math
def func1(a,b):
    sum=1
    num=0
    if a>b :
        return None
    else :
        while a<=b :
            sum=sum*a
            a=a+1
        while sum%10==0 :
            sum=sum//10
            num=num+1
    return  num

def func2(a,b):
    geshu=0
    if a>b :
        return None
    else :
        for i in range(a,b+1):
            i=str(i)
            res=list(i)
            if res[::-1]==res :
                geshu=geshu+1
    return geshu
            
def func3(lst):
    res=[i for i in lst if i>0 and i%3!=0]
    res=sorted(res,reverse=False)
    return res

if __name__=="__main__":
	pass


