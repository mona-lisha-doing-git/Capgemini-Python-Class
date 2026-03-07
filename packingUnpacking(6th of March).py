# 06/03/2026 (Friday)

# Function practice
a = 10
def fname():
    a = 50
    print(a)
# fname()
# print(a)

def productOfList(l):
    sum = 1
    for i in l:
        sum *= int(i)
    return sum

# l = eval(input("Enter list: "))
# print(productOfList(l))

' write a program to print the initial index of a character present in a given string '
c = 'd'
s = "world"

def findChar(s, c):
    for i in range(0, len(s)):
        if c == s[i]:
            return i
    return -1

# print(findChar(s, c))

# Packing and Unpacking

'Single Packing or Tuple Packing'
def in_index(v,*t):
    for i in range(len(t)):
        if t[i] == v:
            return i
    return -1
        
# print(in_index(100, 20,30,60,100,200))
# print(in_index('a', 'b','d','a','k'))

'Double Packing or Dictionary Packing'
def in_dict(**d):
    return d
# print(in_dict(a=10, b=20, c=60, d=80, e=100, f=120))

# Unpacking
def fname(s, a, b, c, d):
    return s

# print(fname(*"aeiou"))

def fname1(name, home, access):
    return name

d = {"name":"momo", "home":"plate", "access":"money"}
print(fname1(**d))

