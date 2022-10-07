number_list = []
n = int(input("Insert # of elements: "))
print("\n")
for i in range(0,n):
    print("Insert element for: ", i, " ")
    item = int(input())
    number_list.append(item)
print("The list is", number_list)
for i in range(n):
    for j in range(0, n-i-1):
        if number_list[j] > number_list[j+1]:
            number_list[j], number_list[j+1] = number_list[j+1], number_list[j]
print("Sorted list is:", number_list)
