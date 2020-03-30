#  学号:1827402018
#  姓名:王浩南
#  IP:192.168.157.238
#  上传时间:2018/11/12 15:19:26

import math
def func1(a,b):
    #请输入两个整数a和b
 if a>=b:
       a,b=b,a
 #引入一个量c
 c=1
 while a<=b:
       c=c*a
       a+=1
 count=0
 if c%10!=0:
       return None
 else:
       while c%10==0:
           count+=1
           c=c/10
 return(count)
 return

def func2(a,b):
    count=0
    if a>=b:
       a,b=b,a
    while a<=b:
          for x in range(a,b+1):
             c=str(x)
             if list(c)==list(reversed(c)):
               count+=1
    return(count)
    return
            
def func3(lst):
  list_first=sorted(lst)
  list_second=[i for i in list_first if i%3!=0 and i>=0]
  return list_second
if __name__=="__main__":
	print(func1(1,10))
