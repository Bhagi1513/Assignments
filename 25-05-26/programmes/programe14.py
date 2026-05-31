num=int(input("enter a value"))
if num>1:
    for i in range(2,num):
        if num%i==0:
            print(f"the {num} is not prime")
            break
    else:
          print(f"the {num} is prime")
else:
    print("the num is not prime")
