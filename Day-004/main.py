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
