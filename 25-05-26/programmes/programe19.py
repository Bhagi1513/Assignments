#Armstrong number
num=int(input("enter a value:"))
str_len=str(num)
l=len(str_len)
sum=0
rem=0
temp=num
while num>0:
    rem=num%10
    sum=sum+rem**l
    num=num//10
if temp==sum:
     print(f"the {sum} is Armstrong number")
else:
    print(f"the {sum} is not Armstrong number")
