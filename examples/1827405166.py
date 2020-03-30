#  学号:1827405166
#  姓名:王泽洲
#  IP:192.168.157.166
#  上传时间:2018/11/12 15:17:52

import math
def func1(a,b):
    if b > a:
        for i in range(a + 1, b + 1):
            a = a * i
        j = 0
        count = 0
        while j >= 0:
            if str(a)[-1 - j] == '0':
                count += 1
            else:
                res = count
                break
            j += 1
        return res
    else:
        return None
def func2(a,b):
    if b > a:
        count = 0
        for i in range(a, b + 1):
            p = i
            k = 0
            while p != 0:
                k = k * 10 + p % 10
                p = p // 10
                if k == i:
                    count += 1
        return count
    else:
        return None
def func3(lst):
    res = [i for i in lst if i > 0 and i % 3 != 0]
    return sorted(res, reverse = True)


    if __name__=="__main__":
	pass
