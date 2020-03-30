#  学号:1827402030
#  姓名:刘佳豪
#  IP:192.168.157.161
#  上传时间:2018/11/12 14:52:18

import math
def func1(a,b):
    if isinstance(a,int) and isinstance(b,int):
        number = 1
        answer = 0
        for i in range(a,b+1):
            number *= ｉ
        number_str = str(number)
        for i in number_str[::-1]:
            if i == "0":
                answer += 1
            else:break
    else:return None



def func2(a,b):
    try:
        answer_list = [i for i in range(a,b+1) str(i)[::-1] == str(i)]
        return len(answer_list)
    except:return None

def func3(lst):
    lst_first = sorted(lst)
    lst_second = [i for i in lst_first if i%3 != 0 and i >= 0]
    return lst_second


if __name__=="__main__":
    print(func1([1,2,3]))
