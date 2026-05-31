import math
num=int(input())
if num<0:
    print("enter a positive integer")
else:
    result=math.log(num)
    print(f"the natural logarithm of {num}is:{result}")
