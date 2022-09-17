# quadratic soln
"""def quad(a, b, c):
    ans = ((-b+((b**2)-4*a*c)**1/2)/2*a, (-b-((b**2)-4*a*c)**1/2)/2*a)
    return ans


a = int(input("Enter a"))
b = int(input("Enter b"))
c = int(input("Enter c"))
roots = (quad(a, b, c))
x = 0
for x in range(len(roots)):
    print(roots[x])"""

# instance inside string
'''str = "Mary had a little lamb little lamb little lamb"
a = str.split()
n = 0
for x in a:
    if x == "lamb":
        n += 1
        text = "Instance {} appeared"
        print(text.format(n))
        

print(n)
'''
# PAttern
'''for x in range(1, 6):
    for y in range(x):
        print(x, end=" ")#end is a keyword torpint shit on the same line 
    print("\n")
'''

# palindrome
'''a = 133331
b = 0
num = a
while num != 0:
    b = int(b)*10+int((num % 10))
    num = int(num/10)
if a == b:
    print("It palindrome")
else:
    print("It aint")
print(a, b)
'''

'''a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

c = {x for x in a for y in b if x == y}
d = list(c)
print(d)
'''


def rps(a, b):
    play1 = 0
    play2 = 0
    list1 = ["rock", "paper", "scissors", "rock"]
    for x in range(len(list1)):
        if a == list1[x]:
            play1 = x
    for y in range(len(list1)):
        if a == list1[y]:
            play2 = y
    if x > y:
        return "user1"
    if y > x:
        return "user2"


win = 0

while win == 0:
    user1 = input("Player 1 pick rock paper scissors")
    user2 = input("Player 2 pick rock paper scissors")
    if user1.lower() == user2.lower():
        print("It is a tie try again")
    winner = rps(user1.lower(), user2.lower())
    print(winner)
    win = 1
