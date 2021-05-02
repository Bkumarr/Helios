# 
# Example file for variables
#

# Declare a variable and initialize it
# f = 0
# print(f)


# re-declaring the variable works
# f = "abc"
# print(f)

# ERROR: variables of different types cannot be combined

# print("this is a string" + 123)
print("this is a string" + str(123))

# Global vs. local variables in functions

def my_Function():
  global f
  f ="def"
  print(f)

del f
my_Function()
print(f)