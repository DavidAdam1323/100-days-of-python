# 100 Days of Python - Day 004 Randomisation and Python Lists

# Ex01: Random Module
# To use it you need to first import it: "import random"
import random

# Random Whole Numbers Within a Rang: This will produce a random whole number between 1 and 10 (inclusive).
rand_num = random.randint(1, 10)

# Modules in Python
# Python allows us to put code into different files and import that code if needed. 
# This means that we can better organise and modularise our code.
# You can create a new module simply by creating a new .py file 
# and then you can import variables or functions from that file just by using the import keyword.

# Random Floats
# You can generate a random number between 0 (not inclusive) and 1 (inclusive) using the following code from the random module:
rand_num_0_to_1 = random.random()

# You can expand the range of random numbers generated by this method using multiplication.
# e.g. random.random() * 5
# Will generate a random number between 0 and 5.

# Another way to generate random floating point numbers is to use the uniform() function.
#This will generate a random floating point number between 1 and 10. 
random_float = random.uniform(1, 10)

# Heads or Tails: Create a coin flip program using what you have learnt about randomisation in Python. 
# It should randomly print "Heads" or "Tails" everytime it is run.
def coin_flip():
  coin = random.randint(1, 2)
  if coin == 1:
    return "Heads"
  else:
    return "Tails"

print(coin_flip())

# Ex02: Lists
# Create a simple collection of ordered items using a Python list. 
fruits = ["Cherry", "Apple", "Pear"]

# Accessing Items in Lists: provide the name of the list then a square bracket and then the item index that you want. 
print(fruits[0])

# Access items in the list counting from the end of the list by using negative whole numbers.
print(fruits[-1])

# Use the same syntax to get hold of items in a List to modify it. 
# fruits will now become ["Orange", "Apple", "Pear"]
print(fruits[0]) = "Orange"

# Add items to the end of a List using the append() function. e.g.
# fruits will now become ["Cherry", "Apple", "Pear", "Orange"]
fruits.append("Orange")