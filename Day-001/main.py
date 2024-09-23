# 100 Days of Python - Day 001

# Ex01: Printing
# Print out the words "Hello, World!"
print("Hello, World!")

# Ex02: String Manipulation
# Use '\n' to add another two lines of "Hello, World!"
print("Hello, World!\nHello, World!\nHello, World!")

# Add a space between the strings
print("Hello," + " " + "World!")

# Ex03: Inputs
# Use the Python 'input()' function to collect user input and use it within the code
# e.g. Hello, 'user_input'! 
print("Hello, " + input("what's your name? ") + "!")

# Ex04: Variables
# Check the length of the input
print(len(input("what is your name? ")))
# Split everything into variables, one variable called username and one called length.
# Use the variable username in the len calculation.
user_name = input("What is your name? ")
length = len(user_name)
print(f"Your name is {length} characters long!")

# Ex05: Variable Naming
#   Learn the rules of variable naming in Python.
#     1. Make sure your variable names are descriptive
#     2. Don't have spaces between words
#     3. Don't start with numbers
#     4. Don't use special words like print or input
#     5. Choose simple words that are less likely to become typos
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
print(f"Your full name is: {first_name} {last_name}")

# Ex06: Band Name Generator - Project
#   Create a greeting for your program.
#   Ask the user for the city that they grew up in and store it in a variable.
#   Ask the user for the name of a pet and store it in a variable.
#   Combine the name of their city and pet and show them their band name.
print("Welcome to the Band Generator Name!")
city_name = input("Enter a city name: ")
pet_name = input("Enter your pet name: ")
print(f"Your Band name is: The {pet_name}'s {city_name}")