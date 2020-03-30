#  学号:1827405095
#  姓名:周广华
#  IP:192.168.157.225
#  上传时间:2018/11/12 15:20:50

import math
def func1(a,b):
    if isinstance(a,int) and isinstance(b,int):
        res=1
        for i in range(a,b+1):
            res=res*i
        x=res
        lista=list(str(x))
        listb=lista[::-1]
        j=0
        count=0
        while j<len(listb):
            if listb[j]=='0':
                j+=1
                count+=1
            else:break
        return count
    else:return None

def func2(a,b):
    if isinstance(a, int) and isinstance(b, int):
        res=[]
        for i in range(a, b + 1):
            lista = list(str(i))
            listb = lista[::-1]
            while lista==listb and listb[0]!='0':
                res.append(i)
            return len(res)
    else:
        return None
def func3(lst):
    lista=lst[::]
    for i in lista:
        if i<0 or i//3==0:
            listb=lista.remove(i)
        return listb


if __name__=="__main__":
    print(func3([3,6,7,8]))
#	pass

