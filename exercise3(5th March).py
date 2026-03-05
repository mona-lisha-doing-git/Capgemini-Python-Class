# 05/03/2026 (Thursday)

'Revision'
# dic = {"name":"bhavik"}
# print(dic["name"][5:2:-1])

# PATTERNS

# Rectangle
'''
l = int(input("Enter length: "))
b = int(input("Enter width: "))
for i in range (b):
    for j in range (l):
        print("#", end=" ")
    print()
'''


# Right Angle Triangle
'''
for i in range(1, 5):
    for j in range(i):
        print("*", end="")
    print()
'''

# Diagonal Line
'''
for i in range(5):
    for j in range(5):
        if i == j:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
'''

# Diagonal Line with Different symbols for upper triangle, lower triangle and diagonal
# Primary diagonal(left)
'''
for i in range(5):
    for j in range(5):
        if i == j:
            print("*", end=" ")
        elif i > j:
            print("#", end=" ")
        else:
            print("@", end=" ")

    print()
'''

# Secondary diagonal(right)
'''
row = int(input("Enter no. of rows: "))
col = int(input("Enter no. of cols: "))
for i in range(1, row+1):
    for j in range(1, col+1):
        if i+j == row+1:
            print("#", end=" ")
        elif i+j < row+1:
            print("*", end=" ")
        else:
            print("@", end=" ")
    print()
'''

# Both Diagonal 
'''
row = int(input("Enter no. of rows: "))
col = int(input("Enter no. of cols: "))
for i in range(1, row+1):
    for j in range(1, col+1):
        if i+j == row+1:
            print("#", end=" ")
        elif i == j and i+j < row+1:
            print("*", end=" ")
        elif i == j and i+j >= row+1:
            print("@", end=" ")
        else:
            print("", end=" ")
    print()
'''