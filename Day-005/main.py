# 100 Days of Python - Day 005 For Loops, Range and Code Blocks

# Ex01: For Loops
# Loops repeats actions without having to write repeated code.
# Syntax
#     for <variable name of each item> in <a List>:
#         <do something>
#         <do something else> 

fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
  print(fruit)
  print(fruit + " Pie")

# Indentation is very important in Python programming.
# This code will behave very differently:
fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
    print("Hello")

# from this code:
fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
print("Hello")