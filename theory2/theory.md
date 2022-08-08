# Theory assessment 2

####1. How does Object Oriented Programming differ from Process Oriented Programming?

OOP uses classes and objects, POP uses functions

POP:
- Program is divided into small parts called function
- Follows top-down approach
- No access specifier (such as private, public etc.), no data hiding, hence less secure than OOP
- Adding new data and functions is not as easy
- Overloading is not possible (creating multiple functions of the same name with different purposes)
- The function is more important than the data
- Based on the unreal world
- Used for designing medium-sized programs
- Based on the concept of procedural abstraction
- Absent code reusability

OOP:
- Program is divided into small parts called classes and objects
- Follows bottom-up approach
- There is access specifier, data hiding, hence more secure than POP
- Easy and fast to add new data, execute functions
- Overloading is possible (but not in Python)
- The data is more important than the function
- Based on the real world
- Used for designing large, complex programs; provides clear structure
- Based on the concept of data abstraction
- Code reusability is possible, which makes it easier to create larger applications with less code and shorter development time: OOP helps to keep the code DRY "Don't Repeat Yourself", and makes the code easier to maintain, modify and debug


####2. What's polymorphism in OOP?
Polymorphism is the ability of any data to be processed in more than one form. It is the ability of an object to take many forms in different instances. It implements the concept of function overloading, function overriding and virtual functions.

Operators is an example of polymorphic functions as you can add, subtract and multiply different data types.

Example 1 (operators):
```buildoutcfg
num1 = 1
num2 = 2 
print(num1 + num2)
# Output 3

str1 = "ab" 
str2 = "cd" 
print(str1 + str2) 
# Output abcd
```
The operator `+` has been used to carry out different operator operations for different data types


Example 2 (method overriding):
```buildoutcfg
# Defining parent class
class Parent():
	
	# Constructor
	def __init__(self):
		self.value = "Inside Parent"
		
	# Parent's show method
	def show(self):
		print(self.value)
		
# Defining child class
class Child(Parent):
	
	# Constructor
	def __init__(self):
		self.value = "Inside Child"
		
	# Child's show method
	def show(self):
		print(self.value)
		
		
# Driver's code
obj1 = Parent()
obj2 = Child()

obj1.show()
obj2.show()
```
Method `show()` is overridden in `Child()` class.

Example 3 (function overloading):

```buildoutcfg
Class Cat:

    def __init__(self, name, age, colour): # __init__ means initialise
        self.name = name
        self._age = age # single underscore means subclass through encapsulation
        self._colour = colour
        self._hunger_level = 0

    def __str__(self): # __str__ means string representation of a class
        return f"{self.name}, a {self._colour} cat, {self._age} years old"
    # the sentence is string only if it is returned within the function
    # return is for programmers to access data and use it somewhere else as well
    

# Makes an actual specific cat
jake = Cat("Jake", 5, "brown")
```
Overloading `print` function with `__str__()`

####3. What's inheritance in OOP?
Inheritance allows us to define a class that inherits all the methods and properties from another class.

Parent class is the class being inherited from, also called base class.

Child class is the class that inherits from another class, also called derived class or subclass.

In OOP there are five forms of inheritance: single inheritance, multiple inheritance, multi-level inheritance, hierarchical inheritance, and hybrid inheritance. 

Example:
```buildoutcfg
class Camera:

    def __init__(self, resolution):
        self.resolution = resolution

    def take_picture(self):
        print("Picture taken.")


class Radio:

    def __init__(self, modes):
        self.modes = modes

    def tune(self, frequency):
        print(f"Listening to station on frequency {frequency}.")


class MobilePhone(Camera, Radio):

    def __init__(self, make, camera_resolution, radio_modes):
        self.make = make
        Camera.__init__(self, camera_resolution)
        Radio.__init__(self, radio_modes)

    def call(self, contact):
        print(f"Calling {contact}...")
```
Class `MobilePhone(Camera, Radio)` inherits the properties of base classes `Camera()` and `Radio()`, in the first line where it uses `__init__()` method.

####4. If you had to make a program that could vote for the top three funniest people in the office, how would you do that? How would you make it possible to vote on those people?
I would use counter collection to print out most common names mentioned.
Workers can choose who to vote for from the list and then vote within user input. If the name is not on the list, the program will raise ValueError.

Example code (very simplified version):

```buildoutcfg
from collections import counter

office_workers = [
    'EMMA',
    'EMILY',
    'OLIVIA',
    'JACK',
    'WILLIAM',
    'ALEX',
]

print(office_workers)
votes = []

for worker in office_workers:
    worker = input("Who is the funniest in the office: ").upper() # to make input case insensitive
    if worker in office_workers:
        True
        votes.append(worker)
    else:
        False
        print("This person does not work here. Try again")
        raise ValueError

# Count the votes for persons and stores in the dictionary
vote_count = Counter(votes)

# Print three most common names
print(vote_count.most_common(3))
```


####5. What's the software development life cycle?

Software development lifecycle consists of 7 stages: planning, defining, designing, building, testing, deployment, operations and maintenance.

1. Planning

Project leaders evaluate the terms of the project. They calculate production costs, create a schedule with target goals, form teams and leadership structure. Planning can also include feedback from stakeholders, potential customers, developers, sales representatives, experts. Planning is the crucial part that defines the scope and purpose of the project for efficient teamwork.

2. Defining

Defining requirements is considered part of planning to determine what the application is supposed to do and its requirements. For example, a social media application would require the ability to connect with a friend.

Requirements also include defining the resources needed to build the project.

3. Designing

The Design phase models the way a software application will work. Some aspects of the design include: architecture, UI, platforms, programming, communications, security, prototyping.

Prototyping is important to receive feedback on this early basic version in order to improve the application as it is more efficient on the first steps.

4. Building (development)

In this phase the actual code is written. It also includes troubleshooting and compiling the code. Developers work in teams and sometimes require explanations from the source code for which documentation for troubleshooting or etc. is very useful.

5. Testing

It’s critical to test an application before making it available to users. Much of the testing can be automated, like security testing. Other testing can only be done in a specific environment – consider creating a simulated production environment for complex deployments. 

Testing should ensure that each function works correctly. Different parts of the application should also be tested to work seamlessly together—performance test, to reduce any hangs or lags in processing. The testing phase helps reduce the number of bugs and glitches that users encounter. This leads to a higher user satisfaction and a better usage rate.

6. Deployment

In the deployment phase, the application is made available to users. Many companies prefer to automate the deployment phase. This can be as simple as a payment portal and download link on the company website. It could also be downloading an application on a smartphone.

7. Operations and maintenance

At this point, the development cycle is almost finished. The application is done and being used in the field. The Operation and Maintenance phase is still important, though. In this phase, users discover bugs that weren’t found during testing. These errors need to be resolved, which can spawn new development cycles.

In addition to bug fixes, models like Iterative development plan additional features in future releases. For each new release, a new Development Cycle can be launched.


####6. What's the difference between agile and waterfall?

Waterfall Model methodology which is also known as Liner Sequential Life Cycle Model. Waterfall Model followed in the sequential order, and so project development team only moves to next phase of development or testing if the previous step completed successfully.

Agile methodology is a practice that helps continuous iteration of development and testing in the software development process. In this model, development and testing activities are concurrent, unlike the Waterfall model. This process allows more communication between customers, developers, managers, and testers.

- In Agile vs Waterfall difference, the Agile methodology is known for its flexibility whereas Waterfall is a structured software development methodology.
- Comparing the Waterfall methodology vs Agile which follows an incremental approach whereas the Waterfall is a sequential design process.
- Agile performs testing concurrently with software development whereas in Waterfall methodology testing comes after the “Build” phase.
- Agile allows changes in project development requirement whereas Waterfall has no scope of changing the requirements once the project development starts.

####7. What is the reduced function used for?
The `reduce(fun,seq)` function is used to apply a particular function passed in its argument to all of the list elements mentioned in the sequence passed along.This function is defined in “functools” module.

Example:
```buildoutcfg
# python code to demonstrate working of reduce()

# importing functools for reduce()
import functools

# initializing list
lis = [1, 3, 5, 6, 2, ]

# using reduce to compute sum of list
print("The sum of the list elements is : ", end="")
print(functools.reduce(lambda a, b: a+b, lis))
# Output
# The sum of the list elements is : 17

# using reduce to compute maximum element from list
print("The maximum element of the list is : ", end="")
print(functools.reduce(lambda a, b: a if a > b else b, lis))
# Output
# The maximum element of the list is : 6

```

####8. How does merge sort work?
Merge sort is one of the most efficient sorting algorithms. It is based on the divide-and-conquer strategy. Merge sort continuously cuts down a list into multiple sublists until each has only one item, then merges those sublists into a sorted list. It can be used to sort the values in any traversable data structure such as a list.

Usually, it follows a top-down approach: it starts at the top and works its way down, splitting the array in half, making a recursive call, and merging the results until it reaches the bottom of the array tree.

In other words, firstly, it obeys to ‘divide’ principle: continuously divides the unsorted list until you have N sublists, where each sublist has 1 element that is “unsorted” and N is the number of elements in the original array.

Finally, it merges the sublists according to conquer principle: repeatedly merges i.e conquers the sublists together 2 at a time to produce new sorted sublists until all elements have been fully merged into a single sorted array.


Pros of the merge sort:
- It is quicker for larger lists because unlike insertion it doesn't go through the whole list several times.
- Stable sorting algorithm

Cons:
- Slower compared to the other sort algorithms for smaller data sets
- Goes through the whole process even if the list is sorted
- It uses more memory space to store the sub elements of the initial split list


####9. Generators - generator functions allow you to declare a function that behaves like an iterator, i.e. it can be used in a for loop. What is the use case?

Python generators are a simple way of creating iterators. 
In other words, a generator is a function that returns an object (iterator) which we can iterate over (one value at a time). Every generator is an iterator, but it is implemented in a different way.

Generator properties:
- Implemented using a function	
- Uses the `yield` keyword (yield is like the `return` keyword for regular functions)
- Usage results in a concise code
- All local variables before the yield statement are stored

Example:
```buildoutcfg
# A simple generator function
def my_gen():
    n = 1
    print('This is printed first')
    # Generator function contains yield statements
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n


# Using for loop
for item in my_gen():
    print(item)
```

```buildoutcfg
# Output
This is printed first
1
This is printed second
2
This is printed at last
3
```

####10. Decorators - a page for useful (or potentially abusive?) decorator ideas. What is the return type of the decorator?

A decorator is a function which takes another function as an argument and returns a modified version of it, enhancing its functionality in some way. Decorators wrap a function, modifying its behaviour.
Certain decorators can be useful to time the function execution time or speed up the execution. Decorators are useful in making the code more readable and easy to read, contributing to the DRY principle.

Decorator return type should be `callable`, as it behaves like a function or method (in the class). Decorator ‘swallows’ the function written as its argument and returns a `callable`.

Example 1 - decorator not callable, incorrect use:
```buildoutcfg
def my_decorator(f):
    return 5
    
@my_decorator
def hello():
    print('hello')
```
This decorator returns `int` instead of `callable`, so it cannot be called a function.

Example 2 - callable decorator, correct use:
```buildoutcfg
import time

def timed(func):
    def timed_func(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        time_elapsed = end_time - start_time
        print(f"Time elapsed: {time_elapsed:.6f}s")
        return result

    return timed_func


@timed
def sum_range(lower_limit, upper_limit):
    return sum(range(lower_limit, upper_limit))


print(sum_range(1, 1234567))
```
Function `timed(func)` was used to time the execution of another external function `sum_range()`.