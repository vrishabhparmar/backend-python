"""
Exception Handling allows a program to handle unexpected errors during execution in a controlled way, 
instead of crashing abruptly. 
It enables programs to detect errors, manage them properly and continue execution wherever possib
"""

# Basic Exmple

try:
    n = 0
    res = 10/n
except (ZeroDivisionError, ValueError) as e:
    print("Error: ", e)

else:
    print("Result :", res)
 
finally:
    print("Execution Complete")


# Raise an Error 
    
def set(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    print(f"Age set to {age}")

try:
    set(-5)
except ValueError as e:
    print(e)


"""
User defined Exceptions
"""

# Step 1: Define a custom exception class
class InvalidAgeError(Exception):
    def __init__(self, age, msg="Age must be between 0 and 120"):
        self.age = age
        self.msg = msg
        super().__init__(self.msg)

    def __str__(self):
        return f'{self.age} -> {self.msg}'

# Step 2: Use the custom exception in your code
def set_age(age):
    if age < 0 or age > 120:
        raise InvalidAgeError(age)
    else:
        print(f"Age set to: {age}")

# Step 3: Handling the custom exception
try:
    set_age(150)  # This will raise the custom exception
except InvalidAgeError as e:
    print(e)