# 100 Days of Python - Day 003
# Conditional Statements, Logical Operators, Code Blocks and Scope

# Ex01: "If" / "Else" - Conditional Check
# Conditionals in Python tells the computer what to do in each case. e.g.

# Condition Check:
# if <this condition is true>:
#     <then execute this line of code>

# What if the condition is false?
# The "else" keyword defines a block of code that will execute, 
# if the condition checked in the "if" statement is false.

# if pigs can fly:
#     <Some code that will never execute>
# else:
#     print("This is real life")

print("Welcome to the Rollercoaster!")
height = input("What is your height in cm?\n")
if height >= "120":
  print("Yes! You can ride.")
else:
  print("No. You can't ride.")

# Ps: Indentation is important in Python because it 
# helps make code more readable and maintainable, and
# it indicates the start and end of code blocks.

# Comparator Operators:
#   > Greater than
#   < Less than
#   >= Greater than or equal to
#   <= Less than or equal to
#   == Equal to
#   != Not equal to

# Ex02: Modulo
# The modulo operator gives you the remainder of a division.
print(10 % 3)

# 6 % 2 #will be 0
# 6 % 5 #will be 1
# 6 % 4 #will be 2

# Check Odd or Even:
print("Hello, let's find out if it's an Odd or Even number!")
num = int(input("Please enter a number:\n"))
if num % 2 == 0:
  print(f"The number {num} is an Even number.")
else:
  print(f"The number {num} is an Odd number.")
