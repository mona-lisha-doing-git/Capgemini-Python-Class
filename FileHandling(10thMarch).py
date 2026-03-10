# 10-03-2026 (Tuesday)
'''
FILE HANDLING
'''

file = open("temp1.txt", 'r')

'Writing single line to the file'
# file.write("Hello world")

'Writing multiple lines to the file'
# file.writelines([
#     'first line\n'
#     'second line\n'
#     'third line\n'
#     'fourth line\n'
#     'fifth line\n'
#     'sixth line\n'
#     'hello world'
# ])


file.seek(0) # go back to the initial position that is the first position
# (we are doing this for w+, as after writing it goes starts from the 
# current position and does not read what was executed earlier)

# file.write("hi")

'Reading the file'
# print(file.read())

# print(file.readline())
# print(file.readline())
# print(file.readline())

# print(file.readlines())

file.close()

'a mode for append'
file1 = open('temp2.txt','a+')

# file1.write("hello world, ")

# file1.write("12344555\n")

# file1.writelines([
#     'first line\n'
#     'second line\n'
#     'third line\n'
# ])

file1.close()

'''
Working with csv file
'''
import csv 
from datetime import date

file2 = open('expense.csv','a+')
w = csv.writer(file2)
# w.writerow(['DATE', 'CATEGORY', 'AMOUNT']) # columns

# w.writerows(
#     [
#     [date.today(), 'Travel', 200],
#     [date.today(), 'Food', 200],
#     [date.today(), 'Entertainment', 200]
#     ]
# )

file2.close()

'''
Working with json
'''
import json
file3 = open("temp3.txt", 'a+')
data = {
    'filename' : "xyz",
    'userid' : '1234',
    'password' : '******'
}

# print(f"original data: {data}")
# print(f"Type of encrypted data: {type(data)}")
# print()

# enc_data = json.dumps(data)
# print(f"Encrypted data: {enc_data}")
# print(f"Type of encrypted data: {type(enc_data)}")
# print()

# file3.write(enc_data)

# file3.seek(0)

# dec_data = json.loads(enc_data)
# print(f"Encrypted data: {dec_data}")
# print(f"Type of encrypted data: {type(dec_data)}")
# print()

file3.close()

'''
Working with pickle
'''
