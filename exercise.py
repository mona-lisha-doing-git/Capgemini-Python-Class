# 27/02/2026 (Friday)

# Ex 1. Output this: 
# 10@20@40@, 5@10, #%#%, 1$2$3^
'''
print(10,20,30, sep="@", end="@")
print("\n")
print(5,10, sep="@")
print("#","#", sep="%", end="%")
print("\n")
print(1,2,3, sep="$", end="^")
'''
'''
n = eval(input("Enter: "))
print(n)
'''

# 11
'''
n = int(input("Enter Value: "))
count = 0
while(int(n)):
    count+=1
    print(n)
    n /= 10
if(count != 3):
    print("no")
else:
    print("yes")
'''

# 12
'''
s = input("Enter string: ")
if(len(s) > 5):
    print("Greater than 5")
else:
    print("Not greater than 5")
'''

# 13
'''
n = 0
if(n == 0):
    print("zero")
else:
    print("not zero")
'''

# 14
'''
age = int(input("Enter age: "))
id = input("Enter id: ")
if(age > 18 and id == 'zyx'):
    print("Eligible")
else:
    print("Not eligible")
'''

# 15
'''
n = int(input("Enter value: "))
if(n >= 10 and n <= 50):
    print("In Range")
else:
    print("Not in Range")
'''

# 16
'''
a = int(input("Enter first value: "))
b = int(input("Enter second value: "))
op = input("Operation: (+/-) ")
if(op == "+"):
    print("Sum: ", a+b)
else:
    print("Difference: ", abs(a-b))
'''

# 17
'''
username = input("Enter username: ")
password = input("Enter password: ")

if(username == "monalisha" and password == "123"):
    print("Login Successful")
else:
    print("Invaid credentials")
'''

# 18
'''
temp = int(input("Enter temperature: "))
if(temp > 30):
    print("Hot")
else:
    print("Cold")
'''

#19
'''
s = input("Enter value: ")
i, j = 0, len(s)-1
flag = True
while(i < j):
    if(s[i] != s[j]):
        flag = False
        break
    i += 1
    j -= 1

if(flag):
    print("Palindrome")
else:
    print("Not palindrome")
'''

# 20
"""
n = int(input("Enter Number: "))
if(n > 100):
    print("Greater than 100")
else:
    print("Not Greater than 100")
"""

# Check wheather a person is eligible to vote or not
'''
age = int(input("Enter age: "))
if(age >= 18):
    print("Eligible to vote")
else:
    print("Not eligible")
'''

# Bank Loan Eligibility System
'''
age = int(input("Enter Age: "))
income = float(input("Enter Salary: "))
credits = int(input("Enter Credit Score: "))
if(age >= 21):
    if(income >= 25000):
        if(credits >= 700):
            print("Loan Approved")
        else:
            print("Low Credit")
    else:
        print("Low Income")
else:
    print("Age not eligible")
'''

# Online Exam Result with Distinction
'''
maths = int(input("Enter Maths marks: "))
science = int(input("Enter Science marks: "))
english = int(input("Enter English marks: "))

average = (maths + science + english)/3

if(maths >= 40 and science >= 40 and english >= 40):
    if(average >= 75):
        print("Distinction")
    else:
        print("Pass")
else:
    print("Fail")
'''

# Income Tax Calculator
'''
income = int(input("Enter income: "))

if(income > 500000):
    if(income <= 1000000):
        print("20%")
    else:
        print("30%")
elif(income > 250000):
    print("5%")
else:
    print("No Tax")
'''
# Print 50 to 40
'''
i = 50
while(i >= 40):
    print(i)
    i-=1
'''

# Print 
'''
i = 0
while(i <= 20):
    print(i)
    i+=2'''

# num = int(input("Enter a number: "))
# ans = 0
# while(num):
#     ans = ans*10 + (num%10)
#     num//=10
# print(ans)

# s = input("Enter value: ")
# j = len(s) - 1
# ans = ""
# while(j >= 0):
#     ans+=s[j]
#     j-=1
# print(ans)

# i = 0
# ans = 0
# n = int(input("Enter a number: "))
# while(i < n):
#     ans += i
#     i += 2
# print(ans)

# n = int(input("Enter value: "))
# i = 1
# while(i <= 10):
#     print(f"{n} x {i} = {n*i}")
#     i+=1

# st = {1,2,3}
# for i in st:
#     print(i)

# for i in range(1,10):
#     print(i)

# for i in range(10,0,-1):
#     print(i)

# write a program to replace a space with underscores
# s =input("Enter name: ")
# t = ""
# for i in s:
#     if(i == ' '):
#         t += '_'
#     else:
#         t += i
# print(t)