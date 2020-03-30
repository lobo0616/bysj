#  学号:1827405187
#  姓名:李克剑
#  IP:192.168.157.186
#  上传时间:2018/11/12 15:13:31

import math
def func1(a,b):
    count = 0
    result = 1
    if b>=a>0:
        for i in range(a, b+1):
            result = result *i
        while result%10 ==0:
            count+=1
            result = result/10
        return count
    else:
        return

def func2(a,b):
    count = 0
    if b >a >0:
        for i in range(a, b+1):
            if str(i)[::-1] == str(i):
                count += 1
        return  count
    else:
        return
            
def func3(lst):
    for i in lst[::]:
        if i<0 or i%3==0:
            lst.remove(i)
    lst.sort
    return lst

if __name__=="__main__":
    pass
