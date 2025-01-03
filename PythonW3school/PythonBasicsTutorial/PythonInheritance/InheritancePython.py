'''
Python Inheritance
Inheritance allows us to define a class that inherits all the methods and properties from another class.

Parent class is the class being inherited from, also called base class.

Child class is the class that inherits from another class, also called derived class.
'''
# Create a class named Person, with firstname and lastname properties, and a printname method:


class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def printname(self):
        print(self.fname, self.lname)


x = Person("Rabin", "Mishra")
x.printname()

# creating a class named student to inherit from Person class


class Student(Person):
    pass


# using the same Student class to create an onject and then execute the printname method
y = Student("Sabin", "Mishra")
y.printname()


class Student1(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)


z = Student("Mike", "Olsen")
z.printname()
