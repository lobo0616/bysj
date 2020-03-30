#  学号:1827405037
#  姓名:瞿靖鸿
#  IP:192.168.157.130
#  上传时间:2018/11/12 14:57:05

import math
def func1(a,b):
    if a>=b:
        return None
    num=0
    result = 1
    for i in range(b-a):
        result=result*(a+i)
    result*=b
    while result>=10:
        if result%10==0:
            num+=1
            result/=10
        else :
            break
    return num

def func2(a,b):
    if a>=b:
        return None
    nums1=[]
    for i in range(a,b+1):
        res=0
        x=i
        while x>0:
            res=res*10+x%10
            x=x//10
        if res==i:
            nums1.append(i)


    return len(nums1)
            
def func3(lst):
    for i in lst[::1]:
        if i<0 or i%3==0:
            lst.remove(i)
    lst.sort(reverse=True)
    return lst

if __name__=="__main__":
	print(func1(9,10))
