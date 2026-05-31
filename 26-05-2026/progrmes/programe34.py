def Rotated_Array(arr,k):
    if k<0 and k>n:
        return "invalid Rotion array"
    n=len(arr)
    rotated_array=[0]*n
    for i in range(n):
        rotated_array[i]=arr[(i+k)%n]
    return rotated_array
arr=[10,20,30,40,50]
k=2
result=Rotated_Array(arr,k)
print(f"the original array is : {arr}")
print(f"the rotated array is :{result}")
