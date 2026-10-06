from abc import ABC, abstractmethod

# Class in Python
class Dog:
    species = "Canine" # Class attribute

    def __init__(self, name, age):
        self.name = name # Instance attribute
        self.age = age # Instance attribute

"""
Explanation:

class Dog: creates a class name Dog, which acts as a blueprint for dog object

'species' is a class attribute, meaning it is shared by all instances of the class

__init_(): is a constructor method which runs automatically when a new object is created. It is used to
            initialize object data

'self' refers to the current object, allowing each object to store and access its owns data. 

self.name and self.age are instance attributes, unique to each Dog object created from the class.

"""

# Creating Object

dog1 = Dog("Buddy", 3)
print(dog1.name)
print(dog1.age)


class Greet(ABC):
    @abstractmethod
    def say_hello(self):
        pass # Abstract Method

