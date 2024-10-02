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

# Ex03: For Loops with Range
# Range function "range()": range(1, 10)
# This code doesn't do anything by itself. 
# For example, if you tried to print it, it would not give you individual numbers.
# But it can be used in conjunction with For Loops.
for number in range(1, 10):
    print(number)
# This will print out each of the numbers 1 - 9. 
# So the range can also be expressed like this: "a <= range(a, b) < b"

# In the code:
# The `range()` function generates a sequence of numbers based on three parameters: `start`, `stop`, and `step`.
for num in range(1, 11, 3): # The `3` dictates how much the `num` increases after each iteration (the step size).
    print(num)
#     a. `1` is the starting value (inclusive). The loop starts at 1.
#     b. `11` is the stopping value (exclusive). The loop will stop before reaching 11.
#     c. `3` is the step value. This means the loop will increment the variable `num` by 3 after each iteration.

# The loop will generate numbers starting from 1, and with each iteration, it will increase by 3. 
# The numbers printed will be:
#                             First iteration: `1`
#                             Second iteration: `4`
#                             Third iteration: `7`
#                             Fourth iteration: `10`

# Ex04: The Gauss Challenge
# Work out the total of the numbers between 1 and 100, inclusive of both 1 and 100.
total = 0
for number in range(1, 101):
   total += number

print(total)