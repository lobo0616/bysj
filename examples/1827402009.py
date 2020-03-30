#  学号:1827402009
#  姓名:肖鹏
#  IP:192.168.157.232
#  上传时间:2018/11/12 15:22:55

import math
def func1(a,b): if a>=b or int(a)!=a or int(b)!=b :
        return None
    else:
        d=1
        for i in range(a,b):
            d=d*i
        c=len(str(d))
        x=1
        for j in range(1,x+1):
            if c%10**j==0:
                x=x+1
            else:
                break
        return(x)

def func2(a,b): if int(a)!=a or int(b)!=b:
        return None
    else:
        n=0
        for i in range(a,b+1):
            m=str(i)
            h=list(m)
            if list(reversed(m))==h:
                n+=1
            else:
                break
            return(n)

            
def func3(lst): for i in lst[:]:
        if int(i)!=i:
            return None
        elif i<0 or i%3==0:
            lst.remove(i)
    lst.sort(reverse=True)
    return (lst)


if __name__=="__main__":
	pass
