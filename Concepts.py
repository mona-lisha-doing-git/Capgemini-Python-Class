# Library Functions
# Keywords: Reserved words
# Operators
# Buitin Functions

import keyword

#print(keyword.kwlist)

# Special keywords: True, False, None

# Variable space and value space

# id() : the actual value of the space where the variable is stored

# id is also used to convert hexadecimal into integers

'''
n = 90
id(n)
4357331240

id(90)
4357331240

variable value above 256 changes the id
y = 500
id(y)
4344060432

id(500)
4344060400

In case of string space changes the id values
'''

# 6 identifiers rules:
'''
1. It must not be a keyword.
2. Must not start with a number
3. It should not contain any special chrs except _
4. No space
5. Case-sensitive
6. Should be less than 79 chrs according to ISR.
'''

# 24/02/2026
# Data types
'''
1. Complex Data Type(a = 2+2j)
2. Boolean data type: True(1), False(0)
3. Integer and Float
'''

# z, y, x, w, v, u, t, s = 1000000000000000008, 2, .23, 3., 6 + 16j, 1.5j, True, False

# InBuit Functions
'''
1. abs
2. round -> round(2.345, 2) = 2.34
3. max -> max(23, 45, 56...)
4. min -> min(23, 45, 56...)
5. sum -> uses list: sum([1,2,3,4])=10
'''

a = '''
hellow
this
is my
world
'''
# print(a)

# String
'''
String builtin functions
-> Immutable
1. s.index('var',<begin>)
2. s.count('var')
uppercase, lowercase, isupper, islower, swap case, isdigit, isalpha, 
'''

# dir()

# List
'''
Mutable
1. append(value)
2. insert(idx, value)
3. pop() or pop(idx)
4. remove(value) ... 11 methods
'''

# Tuple
'''
Immutable
1. Only index and count.
'''

# Set
'''
Set-> Mutable, its elements-> Immutable
1. add(value) method
2. pop() and remove()
3. update(val, val)
'''
# Dictionary
'''
Immutable->keys, and Mutable->values
-> Hidden layer in a dictionary
How it is stored in the memory?
Why type casting dict to list results in only a list of keys?
'''

# Slicing
'''
var_name[start:end(-1):<step>]
[::]
[::1]
[2:]
[:4]
[::-1]
[3::-1]
'''

# Type casting
'''
For to Dict
1. All values of list must bbe Multi valued data type
2. Lenght of values must be 2
'''

# Copy operation
'''
1. Shallow copy (in list adv and disAdv) dest_var = src_var.copy()
2. Deep copy (import copy) dest_var = copy.deepcopy(src_var)
3. Normal copy
nexted list (in list, shallow copy doesn't work)
'''

# Precedence
'''
1. Complex
2. Float
3. Int
4. Bool
'''

# To prevent data loss, + and - operators are not applicable for map and set

# Operators - ALARM-BI
'''
* For complex, only true divisioin is applicable -> not // or %
ord('A') -> 65
to check ascii value
'''

# Contional Statements
'''
if condition:
    TSB(True Statement Block)
else:
    FSB
'''

# OUTPUT STATEMENT
# print(10,20,30, sep="#", end='@')
'''
print(val1, val2, ..., valn, sep=" ", end = '\n')
# by default separator is space
# by default end argument is \n
'''

# Flow Diagram
'''
Oval -> start/end
Rhombus -> Input/ Output
Rectangle -> Processing
Diamod -> Condition
Arrow -> Flow
'''

# while loop

# Formatting string: f"{}"

# for looping statements: self iterating loop

# Split function: var.split(" ")
'''
s = "this is the world i live in"
s.split(" ")
['this', 'is', 'the', 'world', 'i', 'live', 'in']
'''

# Nested for loop

# Intermediate Termination Condition
'''
-> continue
-> break
-> pass

In functions: return
'''
# Functions
'''
- Types of functions
- Formal arguments ()
- Actual arguments
- Functions in memory space
- Global and Local Variable
'''

# Packing and Unpacking
'''
- Tuple and Dictionary (The interpreter does it in this format)
- 
'''

'''
Arguments
- Types: Positional Arguments, Keyword Arguments, Default Arguments, Variable Length Arguments(*args, **kwargs)
'''

# Classes and Objects
'''
- Class -> Blueprint of a variable
- Object -> Instance of a class
- Class have attributes and properties
- In memory space: 
    Variable Space-> class_name...  
    Value Space-> 0x55(key layer: a1: attribute1, a2: attribute2... 
                       value layer: a1: 0x11, a2: 0x9)
    Memory Layer-> attribute1: a1, attribute2: a2, name: 0x3

- Init constructor
- Object method (self)
- Class method (decorator-> @classmethod)
- Static method (decorator-> @staticmethod)

- Four pillars of OOPS
- Inheritance
- Encaptulation
- Abstraction
- Polymorphism
'''

# File Handling
'''
File -> File is a type of container in which we contain or store some data
- By using extension name, we can identity what type of data is there inside of it. Eg: .py, .mp4, .html, .mp3
- Before handling any file, taking permission is very much important
open(): 
    open('filename.ext'/'absolute_path', mode)

    Here, total 3 different modea are present,
    1. write(w),
    2. read(r),
    3. append(a)

    write mode
    1. only write(w)
'''

# Package Architecture
'''
- Library: Collection of multiple packages.
- Package: Folder/Directory(Multiple files)
- Module: A file
'''