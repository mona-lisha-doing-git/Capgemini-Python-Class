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
n = int(input("Enter Number: "))
if(n > 100):
    print("Greater than 100")
else:
    print("Not Greater than 100")