# 05-03-2026 (Thursday)

# FUNCTIONS
# In Built Functions
'''
-> Utility in-built function
-> String functions: upper, lower, isupper, islower, swapcase, replace, capitalize, title, split, join, index, count, isdigit, strip, rstrip, lstrip
-> List functions: sort, append, insert, pop, remove, reverse, count, index
-> Tuple functions: index, count
-> Set functions: update, remove, pop, add, union, intersaction, difference, clear
-> Dictionary functions: values, items, pop, update, clear
'''

# User Defined Functions
'''
-> def func_name:
-> return keyword
-> Types:
    - 1. Functions without return value and without arguments
    - 2. Functions without return value and with arguments
    - 3. Functions with return value and without arguments
    - 4. Functions with return value and with arguments
'''

# In memory space
'''
Variable Space: frame[0x90]
Value Space: 0x90[- - - - -  return value]-> method area, method block, function block
'''

# Create a function that take two user inputs and returns the product
# 1.
def product():
    a = int(input("Enter first value: "))
    b = int(input("Enter second value: "))
    print("Product:", a*b)

# product()

# 2.
def product(a, b):
    print("Product:", a*b)

# product(2,3)
# print(product(2,3)) this will print the value and too, for the print statement outside the function because it doesn't return any value

# 3.
def product1():
    a = int(input("Enter first value: "))
    b = int(input("Enter second value: "))
    return a*b

# print(product1())

# 4.
def product1(a, b): # formal arguments or parameters
    return a*b

# print(product1(3,6)) # actual arguments

def func1(l):
    a = []
    for i in l:
        if i<0:
            a.append(i)
    return a

l = [1,2,3,-5,-3, -7]
# print(func1(l))

# Global and Local Variable 
# Global variable changing
i = 0
def func2():
    global i
    i = 20
func2()
# print(i)

# Nested Function, nonlocal keyword
def func3():
    name = "hi"
    def dummy():
        nonlocal name
        name = "hello"
    dummy()
    print(name)
    
# func3()