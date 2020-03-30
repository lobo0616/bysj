#  学号:1827405169
#  姓名:焦阳子璇
#  IP:192.168.157.131
#  上传时间:2018/11/12 15:03:45

Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:01:18) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
def func1(a,b):
    x=1
    count=0
    for i in range(a,b+1):
        x=x*i
    if x%10!=0:
        return None
    while x%10==0:
        x=x/10
        count+=1
    return count
def func2(a,b):
    count=0
    for i in range(a,b+1):
        res=0
        num=i
        while i>0:
            res=res*10+i%10
            i=i//10
        if res==num:
            count+=1
    return count
            
def func3(lst):
    alist=[]
    for i in range(len(lst)):
        x=lst[i]
        if x>=0 and x%3!=0:
            alist.append(x)

    sorted(alist,reverse=True)
    return alist

if __name__=="__main__":
	pass
