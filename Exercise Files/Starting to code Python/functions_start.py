#
# Example file for working with functions
#

# define a basic function
def func():
  print("I am a function")

# function that takes arguments
def some_func(c1, c2):
  print(c1, " ", c2)

# function that returns a value
def square(x):
  return x*x

# function with default value for an argument
def exp(num, x=1):
  result =1
  for i in range(x):
    result = result * num
  return result

#function with variable number of arguments
def multi_add(*args):
  result = 0
  for x in args:
    result = result + x
  return result



# func()
# print(func())
# print(func)
# some_func(10, 20)
# print(some_func(10, 20))
# print(some_func)
# square(9)
# print(square(9))
# print(square)
# print(exp(2))
# print(exp(2, 4))
# print(exp(x=3, num=2))
# print(multi_add(10, 4, 5, 8))
