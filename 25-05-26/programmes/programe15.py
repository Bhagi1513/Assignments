#To check a python programe all prime numbers br=etwen 1 to 19
upper_case=10
lower_case=1
print("prime numbers between ",lower_case ,"and",upper_case, "are:")
for num in range(lower_case,upper_case+1):
    if num>1:
      for i in range(2,num):
         if num%i==0:
             break
      else:
          print(num)
      
      
