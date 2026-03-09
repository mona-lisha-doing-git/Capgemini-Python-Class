# Date: 09-03-2026 (Monday) 10:00 am to 4:30 pm

'Creating a college class with init contructor'
class College:
    c_name = 'JECRC'
    loc = 'Jaipur'

    def __init__(self, name, id, age):
        self.name = name
        self.id = id
        self.age = age
    


s1 = College("abc", "22bcon", 12)
# s2 = College()
# print(s1.c_name)
# print(s1.name)

'Creating variables manually'
# s1.name = 'abc'
# print(s2.c_name)

'What are classes and objects?'
# print(College) # <class '__main__.College'>
# print(s1) # <__main__.College object at 0x102c3f140>

# =======================================================================================================================================================================================================================

'Creating an Animal class with init constructor and manually and see the difference'
class Animal:
    sound = "zzz"
    home = "Shelter"
    loc = "Jaipur"

    # Creating constructor
    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species
    
    # Object method
    def display(self):
        print(self.name)
        print(self.age)
        print(self.species)
        print()

    # Creating class method
    @classmethod
    def c_disp(cls):
        print(cls.sound)
        print(cls.home)
        print(cls.loc)
        print()

a1 = Animal("max", 3, "horse")
a2 = Animal("tom", 2, "dog")
a3 = Animal("alle", 1, "cat")
a4 = Animal("titu", 2, "parrot")
a5 = Animal("semual", 1, "sparrow")

'Printing using class method'
# a1.c_disp()
# Animal.c_disp()

'Printing by calling object method-> display()'
# a1.display()
# a2.display()
# a3.display()
# a4.display()
# a5.display()

# a1.name = "max"
# a1.age = 3
# a1.species = "horse"

# a2.name = "tom"
# a2.age = 2
# a2.species = "dog"

# a3.name = "Alle"
# a3.age = 1
# a3.species = "cat"

# print("First Object: ")
# print(a1.name)
# print(a1.age)
# print(a1.species)

# print("\nSecond Object: ")
# print(a2.name)
# print(a2.age)
# print(a2.species)

# print("\nThird Object: ")
# print(a3.name)
# print(a3.age)
# print(a3.species)

'Static Method, decorator->@staticmethod'
class Student:
    s_name = "ABC"
    loc = "India"
    def __init__(self, name, roll, sec):
        self.name = name
        self.roll = roll
        self.sec = sec

    def display(self):
        print(self.name)
        print(self.roll)
        print(self.sec)
        print()

    @classmethod # object method will only change for the particular object but not for the class
    def ch_school(cls, new):
        cls.c_name = new

    @classmethod
    def ch_loc(cls, new):
        cls.loc = new

    @staticmethod
    def prod():
        a = int(input("a: "))
        b = int(input("b: "))
        return a*b


st1 = Student("abc", 540, 'A')
# print(st1.prod())
# st1.display()

# Student.c_name = "BCD"
# print(st1.c_name)

class Shapes:
    loc = "paper"
    tool = "pen"

    @staticmethod
    def add():
        a = int(input('a: '))
        b = int(input('b: '))
        return a+b

# print(Shapes.add())
# s1 = Shapes
# print(s1.add())

'OOPS: 4 pillars'

# Abstraction, Encuptulation, Inheritance, Polymorphism
class Car:
    def __init__(self):
        self.acc = True
        self.clutch = True
        self.brk = False