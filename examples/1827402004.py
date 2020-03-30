#  学号:1827402004
#  姓名:施畅
#  IP:192.168.157.182
#  上传时间:2018/11/12 14:37:14

import math
def func1(a,b):
    if a<=b:
        ji=1
        while a<=b:
            ji=ji*a
            a+=1
        lingshu=0
        while ji%10==0:
            lingshu+=1
            ji=ji//10
        return lingshu
    else:
        return None


def func2(a,b):
    if a<=b:
        geshu=0
        for i in range(a,b+1):
            i1=[]
            for j in str(i):
                i1.append(j)
            i2=i1[::-1]
            if i1==i2:
                geshu+=1
        return geshu
    else:
        return None
            
def func3(lst):
    lst1=[]
    for i in lst:
        if i>0 and i%3!=0:
            lst1.append(i)
    lst1=sorted(lst1)
    return lst1

if __name__=="__main__":
	pass

