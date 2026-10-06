import keyword
from functools import reduce
import math

# Simple print 
print("Hello! From Python")

# Single Input
#name = input("Enter you name")

#print("Hello, ", name, "! Welcome. ")

#Multiple Inputs
#x, y = input('Enter twp numbers:').split()

#print( x + y)

# Variable Naming convention 
# Can contain lettes, digits, and underscore

age = 21
_colour = "lilac"
total_score = 90

# Counting Character 

print('Color len ',len(_colour))


# ternary operator

a, b = 10, 12

min = a if a < b else b

print(keyword.kwlist)

# lambda: anonymous functions

x = 'Vrishabh'
upper = lambda x: x.upper()
print(upper(x))

# List comprehesion 

# List comprehension is a concise way to create new lists by applying an 
# expression to each item in an existing iterable like a list, tuple or range. It helps to write clean, 
# readable and efficient code compared to traditional loops.

a = [1,2,3,4,5]

print([val * 2 for val in a])

# List comprehension can be combined with lambda

func = [lambda arg=x: arg*10 for x in range(1,5)]

for i in func:
    print(i())

even = filter(lambda x: x % 2 == 0, a)
print(list(even))    

double = map(lambda x: x * 2, a)
print(list(double))

mul = reduce(lambda x, y: x * y, a)
print(mul)

# print factorial from 1 to 10

factorial = [lambda x=x: math.factorial(x) for x in range(1,11)]

for i in factorial:
    print(i())

# with (Automatic closing)
with open("sample.txt") as file:
    data = file.read()
    print(data)

with open("sample.txt", "w") as file:
    file.write("Sample Data was read")

with open("sample.txt") as file:
    data = file.read()
    print(data)


# list is ordered and store duplicate  
    
a = [1,3,"Vrishabh", '1', 1]
print(a)

#tuple

t = (1,2)
print(t)

# set is unordered and used tp store unique element - cannot access using index

s1 = {"1", 2, 2}
print(s1)

for i in s1:
    print(i)

# Dict
    
d = {1:"Vrishabh", 2:"Parmar"} 
print(d[1])
print(d.get(1))

# recursion in function 

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(10))

# *args and **kwargs 

def func(*args):
    return sum(args)

print(func(1,2,3))

def func1(**kwargs):
    for k, val in kwargs.items():
        print(k,val)


func1(a=1, b=2)


# Decorators are flexible way to modify or extend behavior of functions or methods,
# without changing their actual code
# 1.A decorator is essentially a function that takes another function as an argument and returns a 
# new function with enhanced functionality.

# 2. They are often used in scenarios such as logging, authentication and memoization, allowing us to add additional functionality 
# to existing functions or methods in a clean, reusable way.

def decorator_name(func):
    def wrapper(*args, **kwargs):
        print("Before execution")
        result = func(*args, **kwargs)
        print("After execution")
        return result
    return wrapper

@decorator_name
def add(a, b):
    return a + b

print(add(5, 3))