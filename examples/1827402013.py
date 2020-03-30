#  学号:1827402013
#  姓名:司诺男
#  IP:192.168.157.154
#  上传时间:2018/11/12 15:02:21

import math
def func1(a,b):
    if a>b:
        return None
    else:
        ji=1
        for i in range (a,b+1):
            ji=ji*i

        count = 0
        while ji%10 == 0:
            count+=1
            ji=ji/10
        return count

def func2(a,b):
    if a>b:
        return None
    else:
        datas=[]
        temp = 1
        for i in range (a,b+1):
            hui=0
            while x>0:
                hui = hui*10+x%10
                temp = temp//10
            if hui == i:
                datas.append(i)
            count= len(datas)
    return count
            
def func3(lst):
    for i in range (1,len(lst)+1):
        if lst[i]<0:
            del lst[i]
    for j in range (1,len(lst)+1):
        if lst[j]%3==0:
            del lst[j]
    lst1 = sorted(lst,reverse=True)
	return lst1

if __name__=="__main__":
	pass
