#  学号:1827405148
#  姓名:杨岸睿
#  IP:192.168.157.132
#  上传时间:2018/11/12 14:54:22

import math
def func1(a,b):
    ji = 1
    while a <= b:
        ji = a * ji
        a = a + 1
    ji = str(ji)
    return(ji.count("0"))

def func2(a,b):
    num = 0
    for i in range(a,b+1):
        res = 0
        temp = i
        while i > 0:
            res = res*10 + i % 10
            i = i//10
        if res == temp:
            num = num + 1
    return(num)
            
def func3(lst):
    temp = lst[:]
    for i in lst:
        if i < 0 or i % 3 == 0:
            temp.remove(i)
    return(temp)

if __name__=="__main__":
	pass
