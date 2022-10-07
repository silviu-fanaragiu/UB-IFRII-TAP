from array import array
from itertools import count

def count_sort(array):
    elements = len(array)
    output = [0] * elements
    count = [0] * 10
    for i in range (0,elements):
        count[array[i]] += 1
    
    for i in range (1,10):
        count[i]=count[i]+count[i-1]
    
    i=elements - 1
    while i>= 0:
        output[count[array[i]]-1]=array[i]
        count[array[i]]=count[array[i]]-1
        i-=1
    
    for i in range(0,elements):
        array[i]=output[i]

number_list = []
n = int(input("Insert # of elements: "))
print("\n")
for i in range(0,n):
    print("Insert element for: ", i, " ")
    item = int(input())
    number_list.append(item)
print("The list is", number_list)

count_sort(number_list)
print("The count sorted list is:")
print(number_list)