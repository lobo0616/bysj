#  学号:1827405072
#  姓名:孙王吉
#  IP:192.168.157.158
#  上传时间:2018/11/12 15:18:55

import math
def func1(a,b):
    if a<=0 or b<=0 or a>=b:
        return None
    else:
        chengji=1
        weishu=0
        for i in range(a,b+1):
            chengji=chengji*i
        while chengji%10==0:
            weishu+=1
            chengji=chengji/10
    return weishu

def func2(a,b):
    sum=0
    for i in range(a,b+1):
        count=1
        num=0
        num1=i
        while count<=len(str(num1)):
            k=i%10
            num+=k*(10**(len(str(i))-1))
            count+=1
            i=int(i/10)
        if num==num1:
            sum+=1
    return sum

def func3(lst):
    for i in lst[::-1]:
        if i<0 or i%3==0:
            lst.remove(i)
    lst.sort(reverse=True)
    return lst

if __name__=="__main__":
    pass