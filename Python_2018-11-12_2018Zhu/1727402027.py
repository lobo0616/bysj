#  ѧ��:1727402027
#  ����:�﷼��
#  IP:192.168.157.178
#  �ϴ�ʱ��:2018/11/12 15:00:24

import math

def func1(a,b):
    i=1;
    count = 0
    for j in range(b-a):
        a=a*(a+1)            #���������
    #print(a)
    s=str(a)                 #ת��Ϊ�ַ���
    while s[-i]=="0":       #��ĩβ��������Ϊ0���ַ�
        count=count+1        #�����0����1
        i=i+1                #������ǰ����
    return ("��β����0�ĸ�����%d"%count)

def func2(a,b):
    num=0
    for i in range(b-a+1):
        if a>10:        #�������λ��
          a2=a//10
          a3=a%10
          if a3*10+a2==a:
            num=num+1
        if a>100:       #�������λ��
            a1=a//100
            a2=a//10%10
            a3=a%10
            if a3*100+a2*10+a1==a:
                num = num + 1
        a=a+1
    return ("������a��b֮��������ĸ���:%d"%num)
            
def func3(lst):
    lst2=[]                 #�½�һ���б�����װ����������Ԫ��
    for i in range(len(lst)):
        if lst[i]>0 and lst[i]%3!=0:    #��ȥ������3�ı���
            lst2.append(lst[i])
    lst2.sort(reverse=True)      #��������
    return lst2


if __name__=="__main__":
    pass

    print(func1(10,14))
    print()
    print(func2(101,121))
    print()
    lst=[12,-3,14,9,16,-9,-1,17,31,29]
    print(func3(lst))

