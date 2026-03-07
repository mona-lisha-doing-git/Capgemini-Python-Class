# 05-03-2026 (Saturday)

import sys
sys.setrecursionlimit(2000)

def fac(n):
    if(n <= 1):
        return 1
    return n * fac(n-1)

# n = int(input("Enter number: "))
# print(fac(n))

'''
In Memory Space: func(4)
Value Space-> (0x1)func(4) (0x2)func(3) (0x3)func(2) (0x4)func(1)
'''

# Write a program to create a function which adds min two and max five numbers
def add(a, b, c=0, d=0, e=0):
    return a + b + c + d + e
# print(add(1,2))
# print(add(1,2,3,2,1))

# Write a program to find out individual digits given in a number
def func(n):
    ans = 0
    while(n > 0):
        ans += n%10
        n//=10
    return ans

def func1(n):
    if(n <= 1):
        return n
    return n%10 + func1(n//10)

# print(func(123))

'''
Class and Object
'''
class abc:
    name = "hello"

english = abc()
print(english.name)