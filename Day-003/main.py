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

# Ex03: Nesting and "elif"
# Put "if/else" statements inside other if/else statements. 
# This is known as nesting. 

# E.g.; In this case only when a student has over 90 on maths 
# and english, do they get "You are good at everything".

# if maths_score >= 90:
#     if english_score >= 90:
#         print("You're good at everything")
#     else:
#         print("You're good at maths")
# if english_score >= 90:
#     print("You're good at english)


# Note: You can also have if statements that don't have a paired else statement.


# Ex04: Multiple "ifs"
# write as many if statements as you need to check for different conditions that are unrelated to each other. Compare the code blocks below:

# If/elif/else
# if <condition 1 is true>
#     <do A>
# elif <condition 2 is true>
#     <do B>
# else
#     <do C>

# Nested if statements
# if <condition 1 is true>
#     <do A>
#     if <condition 2 is true>
#         <do B>
#         if <condition 3 is true>
#             <do C>

# Multiple if statements
# if <condition 1 is true>
#     <do A>
# if <condition 2 is true>
#     <do B>
# if <condition 3 is true>
#     <do C>

# In the if/elif/else block, only one of A, B, or C can happen, 
# because if/elif/else are mutually exclusive. 
# The first condition has to fail to go into the elif 
# and the elif (or multiple elif) have to fail to go into the else. 
# Condition 2 is only checked if condition 1 is false.

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0
if height >= 120:
  print("Yes! You can ride the rollercoaster.")
  age = int(input("What's your age?\n"))
  if age < 12:
    bill += 5
    print(f"Your ticket is £{bill}.")
  elif age < 18:
    bill += 7
    print(f"Your ticket is £{bill}.")
  else:
    bill += 12
    print(f"Your ticket is £{bill}.")

  photo = input("Would you like to add a photo?\nType yes or no:\n").lower()
  if photo == "yes":
    total_bill = bill + 3
    print(f"Thank you!\nYour ticket with a photo is £{total_bill}.")
  else:
    print("Thanks for purchasing your ticket!")

else:
  print("Sorry, you have to grow taller before you can ride.")


# Ex05:
# Based on a user's order, work out their final bill. 
# Use the input() function to get a user's preferences 
# and then add up the total for their order and tell them how much they have to pay.

# Small pizza (S): $15
# Medium pizza (M): $20
# Large pizza (L): $25
# Add pepperoni for small pizza (Y or N): +£2
# Add pepperoni for medium or large pizza (Y or N): +£3
# Add extra cheese for any size pizza (Y or N): +£1
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want?\nType S, M or L: ").upper()
pepperoni = input('Would you like to add extra Pepperoni?\nType "Yes" or "No": ').lower()
extra_cheese = input('Would you like to add extra Cheese?\nType "Yes" or "No": ').lower()

S = 15
M = 20
L = 25

bill = 0

if size == "S":
  bill += S
elif size == "M":
  bill += M
elif size == "L":
  bill += L
else:
  print("Enter a valid input please!")

if pepperoni == "yes":
  if size == "S":
    bill += 2
  else:
    bill += 3

if extra_cheese == "yes":
  bill += 1

print(f"Your final bill is £{bill}.") 