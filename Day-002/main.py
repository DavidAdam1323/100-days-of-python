# 100 Days of Python - Day 002

# Ex01: Python primitive data types.
# Strings
# Sequence of characters enclosed in either single quotes ('') or double quotes (“”).
print(type("123 456"))

# Integers
# Whole number, positive or negative, without decimals.
print(type(123_456))

# Floats
# Fractional numbers, with decimals.
print(type(123.456))

# Booleans
# Represent one of two values: True or False.
print(type(True))


# Ex02: Type Error, Checking and Conversion
# These errors occur when using the wrong data type. 
#       e.g. len(12345)

# Only give the len() function "Strings", it will give a TypeError if give it a number (Integer).
# Fix the len() function so it has no more warnings or errors: 
# print("Number of letters in your name: " + len(input("Enter your name")))
name = input("Enter your name:\n")
length = len(name)
print(f"Your name contains {length} letters!")
print("Number of letters in your name: " + str(length))
print(str(len(input("Enter your name: "))))

# Type Conversion
# Convert data into different data types using special functions. 
#   e.g.
#       float()
#       int()
#       str()


# Ex02: Mathematical operators
# PEMDAS - Parentheses, Exponents, Multiplication/Division, Addition/Subtraction (+, -, *, /, // and **).
# What is the output of this code? 3 * 3 + 3 / 3 - 3
print(3 * 3 + 3 / 3 - 3)

# Change the code so it outputs 3?
print(3 * (3 + 3) / 3 - 3)