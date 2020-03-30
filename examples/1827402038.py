#  学号:1827402038
#  姓名:赵旭佳
#  IP:192.168.157.164
#  上传时间:2018/11/12 15:24:48

import math
def func1(a,b):
    if int(a)==a and int(b)==b:
        result=a
        while a<b:
            result*=(a+1)
            a+=1
        result=result*b
        ge=0
        while result%10==0:
            result=result//10
            ge+=1
        return ge
    else:
        return


def func2(a,b):
    if int(a) == a and int(b) == b:
        ge=0
        for i in range(a,b+1):
            if i[::-1]==i:
                ge+=1
                continue
                return ge
            else:
                return 0
    else:
        return None
            
def func3(lst):
    for i in lst:
        if i>=0 or i%3==0:
            lst.remove(i)
            continue
        lst.sort()
        lst.reverse()
        return lst

if __name__=="__main__":
	print(func1(31,38))