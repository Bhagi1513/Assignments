lower=int(input())
upper=int(input())
for i in range(lower,upper+1):
    order=len(str(i))
    temp_i=i
    sum=0
    while temp_i>0:
        digit=temp_i%10
        sum+=digit**order
        temp_i//=10
    if i==sum:
        print(sum)
