#find largest element in the array
def largest_num(array):
    if not array:
        return it is not array
    largest_element=array[0]
    for  i in array:
        if i>largest_element:
            largest_element=i
    return largest_element        
my_array=[10,20,30,40,50]
result=largest_num(my_array)
print("largest num in array is:",result)
