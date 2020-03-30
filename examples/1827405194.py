#  学号:1827405194
#  姓名:吴青洹
#  IP:192.168.157.134
#  上传时间:2018/11/12 15:24:04

import math
def func1(a,b):
	if b>= a > 0:
		num1=a
		all=num1
		while num1< b:           
			num1+=1
			all=all*num1
		else:
			count=0
			while all %10 == 0:
				count+=1
				all=all//10
			return count
	return None

	


def func2(a,b):
  x=str(int(a))
  y=str(int(b))
  for i in range(len(x)//2):
    for j in range(len(y)//2):
        if x[i]==x[-1-i] and y[j]==y[-1-i]:
            return 2
        elif x[i]!=x[-1-i] and y[j]!=y[-1-j]:
            return 0
        else:
            return 1

	

            
def func3(list):
    def func3(list):
        for i in range(len(list)):
            if i < 0 or i % 3 == 0:
                list.pop(i)
                list.sort(reverse=True)
                return list
def main():
    print(func3([1,2,3,4,5,6,76]))
main()


if __name__=="__main__":
	print(func1(2,8))
	
