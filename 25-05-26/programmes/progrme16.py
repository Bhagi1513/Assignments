#factorial
num=int(input("enter a num"))
factorial =1
if num<0:
    print("the factorial doesnot exist")
elif num==0:
    print("the factorials of 0 is 1")
elif num>0:
    for i in range(1,num+1):
        factorial=factorial*i
    print(f"tha factorial of {num} is {factorial}")
