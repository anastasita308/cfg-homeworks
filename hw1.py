"""

TASK 1

Write a class to represent a Cash Register.
You class should keep the state of price total and purchased items

Below is a starter code:
------------------------
1. you can add new variables and function if you want to
2. you will NEED to add accepted method parameters where required.
For example, method add_item probably accepts some kind of an item?..
3. You will need to write some examples of how your code works.

"""


class CashRegister:

    def __init__(self, discount):
        self.total_items = dict()
        self.total_price = 0
        self._discount = discount

    def add_item(self, item, price):
        self.total_items[item] = price
        self.total_price += price
        print("Item added")
        return self.total_price, self.total_items

    def remove_item(self, item, price):
        if item in self.total_items:
            self.total_items.pop(item)
            self.total_price -= price #unsafe, but methods to get data from dict such as get() or square brackets did not work :(
            print("Item removed")
        else:
            print(f"Such item is not on the system")
        return self.total_price, self.total_items

    def apply_discount(self):
        return self.total_price - self.total_price * (self._discount/100) #assume discount is written as a percentage

    def get_total(self):
        print(f"Your total price to pay is: {self.apply_discount()}")

    def show_items(self):
        return [item for item in self.total_items]

    def reset_register(self):
        self.total_items.clear()
        self.total_price = 0

# EXAMPLE code run:
my_items = CashRegister(20)
my_items.add_item("Chocolate", 1.50)
my_items.add_item("Milk", 1.00)
my_items.add_item("Doughnuts", 2.50)
my_items.apply_discount()
my_items.get_total()
print(my_items.show_items())

my_items.remove_item("Chocolate", 1.50) #so potentially if you write a wrong price, no error will be raised
my_items.get_total()
print(my_items.show_items())

my_items.reset_register()
my_items.get_total()
print(my_items.show_items())

# ADD


"""

TASK 2

Write a base class to represent a student. Below is a starter code. 
Feel free to add any more new features to your class. 
As a minimum a student has a name and age and a unique ID.

Create a new subclass from student to represent a concrete student doing a specialization, for example:
Software Student and Data Science student. 

"""


class Student:

    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id
        self.subjects = dict()

# class CFGStudent(<should inherit from Student>)
#     create new methods that manage student's subects (add/remove new subject and its graade to the dict)
#     create a method to view all subjects taken by a student
#     create a method  (and a new variable) to get student's overall mark (use average)

class CFGStudent(Student):
    def __init__(self, name, age, id):
        super().__init__(name, age, id)
        self.total_grade = 0
        self.average_grade = 0

    def add_subject(self, subject, grade):
        self.subjects[subject] = grade
        print("Subject added")
        self.total_grade += grade
        self.average_grade = self.total_grade / len(self.subjects)
        return self.total_grade, self.average_grade, self.subjects

    def remove_subject(self, subject, grade):
        if subject in self.subjects:
            self.subjects.pop(subject)
            print("Subject removed")
            self.total_grade -= grade #same in this task as above
            self.average_grade = self.total_grade / len(self.subjects)
        else:
            print(f"Such subject is not on the system")
        return self.total_grade, self.average_grade, self.subjects

    def view_subjects(self):
        return [subject for subject in self.subjects]

    def get_average_grade(self):

        print(f"Your average grade is: {self.average_grade}")

anastasiia = CFGStudent("Anastasiia", 19, 1)

anastasiia.add_subject("OOP", 80)
anastasiia.add_subject("Dev concepts", 95)
anastasiia.add_subject("Iteration", 90)
anastasiia.add_subject("Python methods", 100)
print(anastasiia.view_subjects())
anastasiia.get_average_grade()

anastasiia.remove_subject("OOP", 80)
print(anastasiia.view_subjects())
anastasiia.get_average_grade()

