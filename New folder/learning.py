'''# Variables and their shit
x = 5
a, b, c = 24, "Poopy", 6.5  # Multiple declaration
A = float(3.4)  # Case Sensitive and typecasting
A = "rooo"      # Python don't care bout no typecast. it will change datatype according to the value assigned
print(x, a, b, c, A)

# More difficult variables
# Lists and tuples are ordered and kinda work like arrays

# List elements can be changed and/or manipulated
list1 = ["apple", "banana", 1]
print(list1)
list1[0] = "bah"
print(list1)


# Ways to fuck arounf with lists
list1[0] = "Meow"
list1[1:3] = ["ew", 2]
list1.append("trte")
print(list1)


# accessing elements of a list or a tuple and also a string works the same

# Tuple cannot be fucked with it no change
tuple1 = ("this is", "a", 6.8)

print(tuple1[0])
print(tuple1)

# boolean means true or false value thingy

# set is a unordered list with no repeating elements
set1 = {"Meow", 1, 3, 1, 1, 1}  # 1 no repeat
print(set1)
'''

s=2
n=12
current=0
previous=0
dict={}
for x in range(s,n):
    bin1=bin(x)
    print(bin1)
    for y in range(2,len(bin1)-1):
        current=bin1[y]
        previous=bin1[y+1]
        if current=="1" and previous=="1":
            dict[x]=True
        else:
            dict[x]=False
print(dict)
