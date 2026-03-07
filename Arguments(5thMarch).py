# 05-03-2026 (Saturday)

# Default arguments must be always after positional arguments
def form(name, mail, ph=None, age=20):
    print("Name is:", name)
    print("Email is:", mail)
    print("Phone no. is:", ph)
    print("Age is:", age)

# form("abc","abc@gmail.com")

# Variable length arguments
# 1
def func(*a):
    print(len(a))
    print("a:", a)

func("hello", "world", 123, False)

# 2
def func1(**k):
    print(len(k))
    print("k:", k)

func1(a=1, b=2, c=3)