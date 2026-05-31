#calculator
num1=int(input())
num2=int(input())
print("choose operation:")
print("1.Addition(+)")
print("2.subtraction(-)")
print("3.multication(*)")
print("4.division(/)")


choice=input("Enter your choice(1/2/3/4)")
if choice=='1':
    print("Result=",num1+num2)
elif choice=='2':
    print("Result=",num1-num2)
elif choice=='3':
    print("Result=",num1*num2)
elif choice=='4':
     if num2!=0:
         print("Result=",num1/num2)
     else:
          print("division by zero is not divisible")
else:
    print("invalid number")
