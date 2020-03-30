import math

def func1(a,b):
    if a<=0 or b<=0:
        return
    if a>b:
        t=a
        a=b
        b=t
    p=1
    for i in range(a,b+1):
        p = p * i
    s=0
    while p%10==0:
        s = s + 1
        p = p // 10    
    return s


def func2(a,b):
    if a<=0 or b<=0:
        return
    if a>b:
        t=a
        a=b
        b=t
    s = 0
    for i in range(a,b+1):
        n = i
        x = int(math.log10(i))+1
        h = 0
        for j in range(x):
            h = h * 10 + n%10
            n = n // 10
        if h == i:
            s = s + 1
    return s
            

def func3(lst):
    for i in range(len(lst)-1, -1, -1):
        if lst[i]<0 or lst[i]%3==0:
            lst.remove(lst[i])
    lst.sort(reverse=True)
    return lst


if __name__=="__main__":
    func2(121,121)
    func2(12221,12221)
    func2(0,10)
    func2(1,10)
    func2(2,100)
    #func1(1, 100)
    #func1(100, 1)
    #func1(100, 100)
    #func1(0, 100)
    #func1(0, -0)
    #func3([7,123,1,2,3,-1,66])
    #func3([])
    #func3([0])
