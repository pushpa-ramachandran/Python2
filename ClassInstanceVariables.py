
# Class variables are shared among all instances of a class
# Instance variables are unique to the instance where class variables are not unique
# for each instance and the value is same across all the instances

class Employee:

    num_of_Employees = 0 # Class variable which need not be customized at instance level
    raise_amount =1.04 # variable which can be customized at instance level

    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay
        self.email = fname + '.' + lname + '@company.com'

        Employee.num_of_Employees += 1 # increment by one every time the Employee instance is created

    def fullname(self):
        return '{} {}'.format(self.fname,self.lname)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
        # self.pay = int(self.pay * Employee.raise_amount) #Employee.raise_amount can also be specified here


emp1 = Employee('fname1' , 'lname1' , 150000)
emp2 = Employee('fname2' , 'lname2' , 160000)

Employee.apply_raise(emp1)

print(emp1.fullname() +' - ' + str(emp1.pay)) #fname1 lname1 - 156000

# {'__dict__': <attribute '__dict__' of 'Employee' objects>,
# '__init__': <function Employee.__init__ at 0x0000000000EB6D90>,
# 'fullname': <function Employee.fullname at 0x0000000000EB6E18>,
# '__module__': '__main__', '__doc__': None, 'raise_amount': 1.04,
# 'apply_raise': <function Employee.apply_raise at 0x0000000000EB6EA0>, '__weakref__':
# <attribute '__weakref__' of 'Employee' objects>}
print(Employee.__dict__)
# Does not have raise_amount.
#{'pay': 156000, 'fname': 'fname1', 'lname': 'lname1', 'email': 'fname1.lname1@company.com'}
print(emp1.__dict__)

####################
# Irrespective of whether self.raise_amount or Employee.raise_amount is used,
# the value is uniform across all the instances until the value is modified in one instance

print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)

# 1.04
# 1.04
# 1.04

# If the value is modified for an instance, it does not change the value for the class level
emp1.raise_amount = 1.05
print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)

# value is changed only emp1 instance
# 1.04
# 1.05
# 1.04

# Now the emp1 instance would have the raise_amount in its namespace
print(emp1.__dict__)
# {'pay': 156000, 'raise_amount': 1.05, 'fname': 'fname1', 'email': 'fname1.lname1@company.com', 'lname': 'lname1'}

# Before and after customization for emp1 with 1.05
print('emp1 Normal Raise 1.04' ,emp1.pay)
emp1.apply_raise()
print('emp1 specific Raise 1.05 ' ,emp1.pay)

# num_of_Employees should be equal to the number of instances created
print('num_of_Employees ' ,Employee.num_of_Employees) #2











