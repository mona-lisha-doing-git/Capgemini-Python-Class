# 10-03-2026 (Tuesday)

# withdraw, deposit, print balance, create account-> edit constructor
class Bank:
    b_name = "abc bank"
    loc = 'Jaipur'
    

class Account(Bank):
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        print(f"Account created for {self.name} with balance {self.balance}.")

    def deposit(self, amount):
        if amount >= 0:
            self.balance += amount
            print(f"Successfully deposited amount: {amount}. Current Balance: {self.balance}.")
        else:
            print("Invalid amount entered.")

    def withdraw(self, amount):
        if amount < 0:
            print("Invalid amount entered.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"Withdrawn: {amount}. Current balance: {self.balance}")

    def balance(self):
        print(f"Current Balance: {self.balance}.")

# a1 = Account("Naina Naval", 2000)
# a2 = Account("Abc Def", 2000)
# a3 = Account("Tara Tara", 2000)
# print(a1.b_name)

# a1.withdraw(3000)
# a2.withdraw(1588)
# a3.withdraw(-9)

'''
Manager - Employee
name sal
name sal dept
'''
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary  = salary

    def details(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")

class Manager(Employee):
    def __init__(self, name, salary, dept):
        super().__init__(name, salary)
        self.dept = dept

    def dept(self):
        print(f"Department: {self.dept}")

    @property
    def greetings(self):
        print("You are all set!!")

# m1 = Manager("abc", "50k", "hr")
# m1.details()
# m1.greetings

class CreditCard:
    def pay(self, amt):
        print(f"Rs.{amt} paid by Credit Card.")


# circle -> radius, obj create-> area and parameters
class Circle:
    def __init__(self):
        self.radius = int(input("Enter radius: "))

    @property
    def area(self):
        ans = 3.14 * (self.radius ** 2)
        print(f"Area: {ans}")

    @property
    def parameter(self):
        print(f"Parameter: {2*3.14*self.radius}")

c1 = Circle()
c1.area
c1.parameter

# lambda, map, filter