#fabinocci series
nterms=int(input("enter a value"))
n1,n2=0,1
count=0
if nterms<=0:
    print("please enter a positive")
elif nterms==1:
    print("the fabinocci series  sequence upto", nterms,":")
else:
    print("the fabinocci series:")
    while count<nterms:
        print(n1)
        nth=n1+n2
        n1=n2
        n2=nth
        count+=1
