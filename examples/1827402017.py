#  学号:1827402017
#  姓名:邢勇涛
#  IP:192.168.157.151
#  上传时间:2018/11/12 15:07:01

import math
def func1(a,b):
    a = int(input("a="))
    b = int(input("b="))
    s=1
    if a<b:
        for a in range(a,b+1):
            s=s*a
        str1=str(s)
        str2=str(int(str1[::-1]))
        num=len(str1)-len(str2)
        return(num)
    else:
        return(None)
    return

def func2(a,b):
    a = int(input("a="))
    b = int(input("b="))
    num = 0
    if a < b:
        for i in range(a, b + 1):
            x = str(i)
            y = x[::-1]
            if x == y:
                num = num + 1
            else:
                continue
        return(num)
    else:
        for i in range(b, a + 1):
            x = str(i)
            y = x[::-1]
            if x == y:
                num = num + 1
            else:
                continue
        return(num)
    return
            
def func3(lst):
    list_1 = sorted(list)
    list_2 = [i for i in list_1 if i >= 0 and i % 3 != 0]
    return(list_2)

if __name__=="__main__":
	pass
