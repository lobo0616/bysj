#  学号:1827402001
#  姓名:徐天顺
#  IP:192.168.157.143
#  上传时间:2018/11/12 14:38:44

import math
def func1(a,b):
    import itertools
    if a<b:
        s=1
        for i in range(a,b+1):
            s=s*i
        b=[int(i) for i in str(s)]
        c=(max([len(list(v)) for k,v in itertools.groupby(b)]))
        return c
    else:
        return None

def func2(a,b):
    if a<b:
        count=0
        for i in range(a,b+1):
            k=i
            y=0
            while i!=0:
                y=y*10+i%10
                i=i//10
            if y==k:
                count+=1

        return count
    else:
        return None

            
def func3(lst):
    for i in lst[::1]:
        if i<0 or i%3==0:
            lst.remove(i)
    lst.sort(reverse=True)
    return(lst)

if __name__=="__main__":
    print(func1(2,6))
    print(func2(100,500))
    print(func3([3,6,-1,1,2]))
	#pass
#main()
