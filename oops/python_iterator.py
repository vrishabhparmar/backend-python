"""
Iterator

An iterator in Python is an object used to traverse through all the elements of a collection 
(like lists, tuples or dictionaries) one element at a time. It follows the iterator protocol, 
which involves two key methods

__iter__(): Returns the iterator object itself.
__next__(): Returns the next value from the sequence. Raises StopIteration when the sequence ends.

Need For Iterators

1. Lazy Evaluation: Processes items only when needed, saving memory.
2. Generator Integration: Pairs well with generators and functional tools.
3. Stateful Traversal: Keeps track of where it left off.
4. Composable Logic: Easily build complex pipelines using tools like itertools.
5. Uniform Looping: Same for loop works for lists, strings and more.


"""

# Built-in iterator

name = "Vrishabh"
it = iter(name)

print(it.__next__())
print(it.__next__())
print(it.__next__())

# Creating a Custom Iterartor

"""
Creating a custom iterator in Python involves defining a class that implements the __iter__() and __next__() 
methods according to the Python iterator protocol.

Steps to follow:

1. Define the Class: Start by defining a class that will act as the iterator.
2. Initialize Attributes: In the __init__() method of the class, initialize any required attributes 
    that will be used throughout the iteration process.
3. Implement __iter__(): This method should return the iterator object itself. 
    This is usually as simple as returning self.
4. Implement __next__(): This method should provide the next item in the sequence each time it's called.
"""



class Computer:
    def __init__(self, limit):
        self.limit = limit
        self.n = 2

    def __iter__(self):
        return self
    
    def __next__(self):
        if(self.n > self.limit):
            raise StopIteration
        x = self.n
        self.n += 2
        return x

even = Computer(10)

for i in even:
    print(i)




