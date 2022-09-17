list1 = []
n = int(input("Enter the number of elements"))
for i in range(0, n):
    element = int(input())
    list1.append(element)
for y in range(0, n):
    for x in range(0, n-1):
        if list1[x] < list1[x+1]:
            temp = list1[x]
            list1[x] = list1[x+1]
            list1[x+1] = temp
print(list1)
