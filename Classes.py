############ Class ##################

# Class is a blueprint to create any instances
# Almost everything in Python is an object, with its properties and methods
# Methods are functions which act on objects

##################### The __init__ method #############
# It is similar to constructors in C++ and Java.
# It is run as soon as an object of a class is instantiated.
# The method is useful to do any initialization you want to do with your object.
# They get the instance as the first argument automatically - self

# Class variables - variables with a value assigned in class declaration
# Instance variables - Variables inside methods and constructors. Have unique values for each instance

# How to create an empty class
class EmployeeEmpty:
    pass

class Employee :
    def __init__(self, fname, lname, pay):
        self.fname =  fname
        self.lname = lname
        self.pay = pay
        self.email = fname + '.' + lname + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.fname, self.lname)

# create instances of class employee
emp1 = Employee('first1' , 'last1', 150000)
emp2 = Employee('first2' , 'last2', 160000)

print ( '{} {}'.format(emp1.fname, emp1.lname))
print ( '{} {}'.format(emp2.fname, emp2.lname))

print('emp1.fullname()  -- >',emp1.fullname())
print('emp2.fullname()  -- >',emp2.fullname())

###### Run at the class level and pass the instance in the argument
print('Run at the class level and pass the instance in the argument --> ', Employee.fullname(emp1))
print('Run at the class level and pass the instance in the argument --> ', Employee.fullname(emp2))

#### Access the instance variable without a method
print(emp1.email)
print(emp2.email)

