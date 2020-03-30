#  学号:1827402003
#  姓名:陆熠晨
#  IP:10.40.37.104
#  上传时间:2018/11/12 14:34:04

import math
def func1(a,b):
    if a<=0 or a!= int(a) or b <=0 or b!=int(b) or a>b:
        return None
    res = 1
    while a <=b:
        res *=(a)
        a+=1
    count0 = 0
    res = str(res)
    for i in range(len(res)):
        if res[-i-1]=='0':
            count0+=1
        else:
            break
    return count0

def func2(a,b):
    if a<=0 or a!= int(a) or b <=0 or b!=int(b) or a>b:
        return None
    s = 0
    for i in range(a, b+1):
        tmp = 0
        k = i
        n = 0 #n用于计算i的位数
        m = i #因为i在后面的会改变 所以要取一个m=i用于判断tmp是否是回文数
        while k>=1:#计算i的位数
            k=k//10
            n+=1
        while n>=1:
            tmp += (i%10)*(10**(n-1))
            i=i//10
            n -= 1
        if tmp == m:
            s += 1
    return s
            
def func3(lst):
    i=0
    while i<=len(lst)-1:
        if lst[i]<0 or lst[i]%3==0:
            lst.pop(i) #因为去掉了这个数 所以下一次还要判断这个位置的数
        else:
            i+=1 #该数没被去掉 所以要判断下个位置的数
    lst.sort(reverse=True)
    return lst

if __name__=="__main__":
	pass

