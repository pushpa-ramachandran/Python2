############################ Lambda #######################
# A simple one line function. No def or return keywords, they are implicit
# Anonymous Functions
# def keyword is used to define the normal functions and the lambda keyword is used to create anonymous functions
# syntax - lambda arguments: expression
# This function can have any number of arguments but only one expression, which is evaluated and returned.

# Lamda function to find the square
a = lambda x : x ** 2
print(a (5 ) )

# Lambda functions can be used along with built-in functions like filter(), map() and reduce().
#### filter ##########
# Filters out all the elements in the sequence which satisfies the condition
list1 = [1,2,3,4,5,6,7,8,9]

onlyOddNumbers = list(filter(lambda x : (x % 2 != 0) ,list1  ))
print(onlyOddNumbers)

############# List comprehension ##################
# List comprehension also works in place of filter()

print( [  x for x in list1 if ( x % 2 != 0 )])

##### map ############
# The function is called with a lambda function and a list and
# a new list is returned which contains all the lambda modified items
# returned by that function for each item.

mapSquare = list(map((lambda x : x ** 2 ), list1 ))
print(mapSquare)

############# List comprehension ##################
# List comprehension also works in place of map()

print( [x **2 for x in list1 ] )

################## reduce () ###############
# Takes in a function and a list as argument.

from functools import reduce

reduceSum = reduce( (lambda x,y : x+y ), list1)
print(reduceSum)


################### lambda ###################

largerOfTwo = lambda x ,y : x if x > y else y

print('Larger of two - largerOfTwo(10, 15) --->', largerOfTwo(10, 15) )