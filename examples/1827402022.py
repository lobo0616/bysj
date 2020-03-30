#  学号:1827402022
#  姓名:强蕾
#  IP:192.168.157.149
#  上传时间:2018/11/12 15:14:24

import math
def func1(a,b):
    sums=1
    count=0
    if a>b:
        a,b=b,a
    for i in range(b-a+1):
        sums=sums*(a+i)
    print(sums)
    if sums==0:
        count=1
        return count
    while sums%10==0:
        count=count+1
        sums=sums/10
        print(sums)
    else:
        return count

def func2(a,b):
    count=0
    for i in range(a,b+1):
        sums=0
        nums=i
        while nums>0:
            single=nums%10
            sums=sums*10+single
            nums=nums//10
        if sums==i:
            count=count+1
    return count
            
def func3(lst):
    list1=[]
    for i in range(len(lst)):
        if lst[i]%3==0:
            lst[i]=-1
        if lst[i]>=0:
            list1.append(lst[i])
    list1.sort(reverse=True)
    return list1

if __name__=="__main__":
    a=1
    b=20
    print(func1(a,b))
    # a=100
    # b=365
    # print(func2(a,b))
    #lst=[1,2,3,6,-12,340,23,9,27,29,-9]
    #print(func3(lst))
	#pass
