#  学号:1827402021
#  姓名:朱晨清
#  IP:192.168.157.153
#  上传时间:2018/11/12 14:55:40

import math
def func1(a,b):
    if a > b:
        return(None)
    else:
        if a<b:
            a_1 = a
            x = 1
            while a_1 <= b:
                x = x*a_1
                a_1 += 1
        else:
            x = a*b
        n = 0
        while x %10 == 0:
            n = n+1
            x = int(x/10)
        return(n)

def func2(a,b):
    if a > b:
        return(None)
    else:
        nums= []
        for i in range(a,b+1):
            x = i
            return_number = 0
            while x>0:
                return_number = return_number*10 + x%10
                x = x//10
            if return_number == i:
                nums.append(i)
        return(len(nums))

def func3(lst):
    returnlist = []
    while len(lst)>0:
        if lst[0] < 0 or lst[0]%3 == 0:
            del lst[0]
        else:
            returnlist.append(lst[0])
            del lst[0]
    returnlist.sort(reverse=True)
    return(returnlist)

if __name__ == '__main__':
    pass