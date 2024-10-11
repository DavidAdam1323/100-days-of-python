# 100 Days of Python - Day 006 Functions & While loops.

# Ex01: 
# Its simplest form is just a wrapper name for a block of code. 
# You give it name and then when you call the function by that name, 
# all the code within the function block will be executed. 
# It can help us save time and reduce repeated code.

def my_function():
    print("Hello From My Function!")
    
my_function()

# Functions may also receive arguments (variables passed from the caller to the function). 
# For example:
def my_function_with_args(username, greeting):
    print(f"Hello, {username}, From My Function! I wish you {greeting}")

# Input for user name and greeting
user_name = input("Enter user name: ")
greeting = input("Enter your greeting: ")

# Dictionary with user inputs
data = {
    "user_name": user_name,   # store actual input in the dictionary
    "greeting": greeting
}

# Call the function with user inputs
my_function_with_args(user_name, greeting)

# Ex02:
# Add a function named list_benefits() that returns the following list of strings: 
# ["More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"] ✅
def list_benefits():
    return ["More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"]

# Concatenate to each benefit - " is a benefit of functions!" ✅
def build_sentence(benefit):
    return benefit + " is a benefit of functions!"

# Add a function named build_sentence(info) which receives a single argument containing a string 
# and returns a sentence starting with the given string and ending with the string " is a benefit of functions!" ✅
def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))

name_the_benefits_of_functions()
