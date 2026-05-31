num=int(input())

n1=0
n2=1
for i in range(num):
    print("the fabinocci series are:",n1)

    n=n1+n2
    n1=n2
    n2=n
    #print("the fabinocci series are:",n1)

