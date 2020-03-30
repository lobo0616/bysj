#  学号:1727402027
#  姓名:田芳琳
#  IP:192.168.157.178
#  上传时间:2018/11/12 15:00:24

import math

def func1(a,b):
    i=1;
    count = 0
    for j in range(b-a):
        a=a*(a+1)            #计算最后结果
    #print(a)
    s=str(a)                 #转换为字符串
    while s[-i]=="0":       #从末尾进行搜索为0的字符
        count=count+1        #如果是0，加1
        i=i+1                #继续往前搜索
    return ("结尾连续0的个数：%d"%count)

def func2(a,b):
    num=0
    for i in range(b-a+1):
        if a>10:        #如果是两位数
          a2=a//10
          a3=a%10
          if a3*10+a2==a:
            num=num+1
        if a>100:       #如果是三位数
            a1=a//100
            a2=a//10%10
            a3=a%10
            if a3*100+a2*10+a1==a:
                num = num + 1
        a=a+1
    return ("正整数a和b之间回文数的个数:%d"%num)
            
def func3(lst):
    lst2=[]                 #新建一个列表，用于装符合条件的元素
    for i in range(len(lst)):
        if lst[i]>0 and lst[i]%3!=0:    #除去负数和3的倍数
            lst2.append(lst[i])
    lst2.sort(reverse=True)      #降序排列
    return lst2


if __name__=="__main__":
    pass

    print(func1(10,14))
    print()
    print(func2(101,121))
    print()
    lst=[12,-3,14,9,16,-9,-1,17,31,29]
    print(func3(lst))

