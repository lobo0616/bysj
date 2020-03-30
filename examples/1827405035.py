#  学号:1827405035
#  姓名:朱弘毅
#  IP:192.168.157.179
#  上传时间:2018/11/12 14:35:14

import math
def func1(a,b):
    if a>0 and b>0 and a<b:
        ans=1
        for i in range(a,b+1):
            ans*=i
        count=0
        while ans%10==0:
            count+=1
            ans/=10
        return count
    if a>=b or a<0 or b<0:
        return none


def func2(a,b):
    if a<0 or b<0:
        return none
    else:
        count=0
        for i in range(a,b+1):
            res=0
            temp=i
            while temp>0:
                res=res*10+temp%10
                temp=temp//10
            if res==i:
                count+=1
        return count
            
def func3(lst):
    res=[]
    for i in range(len(lst)):
        if lst[i]>0 and lst[i]%3!=0:
            res.append(lst[i])
    res.sort(reverse=True)
    return res

if __name__=="__main__":
	print(func3([1,3,2,-1]))
