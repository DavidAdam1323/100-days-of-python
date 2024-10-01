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

# Ex02: Challenge - Print the highest score of the list.
# Use For Loops and Conditionals to print out the highest score in the list of student_scores. 
# For example, if the scores were: 8 65 89 86 55 91 64 89
# Your code should print 91.
student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
highest_score = 0
for score in student_scores:
   if score > highest_score:
      highest_score = score

print(highest_score)