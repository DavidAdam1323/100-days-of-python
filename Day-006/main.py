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


# Ex03: While loops repeat as long as a certain boolean condition is met. 
# For example: Prints out 1,2,3,4,5
count = 1
while count < 6:
    print(f"This is the loop {count}!")
    count += 1

name = input("What is you name? ")
while name == "":
  print("You didn't enter your name!")
  name = input("What is you name? ")
print(f"Hello, {name}!")

age = int(input("Enter your age: "))
while age < 18:
   print("You are not allow to enter!")
   age = int(input("Enter your age: "))
print(f"You are allow to enter!")

chosen_num = int(input("Enter a # between 1 - 10: "))
while chosen_num < 1 or chosen_num > 10:
    print("Invalid Number!")
    chosen_num = int(input("Enter a # between 1 - 10: "))
print(f"Your chosen number is {chosen_num}.")


# Ex 04: Guess the Number Game - Project
# Create a small game where the program randomly selects a number, 
# and the player has to guess the correct number within a certain range (e.g., 1-20). 
# The program will give hints whether the guess was too high or too low 
# and loop until the correct guess is made.
import random

def play_game():
    # Generate a random number between 1 and 20 ✅
    random_number = random.randint(1, 20)

    # Initialize number of attempts ✅
    attempts = 0

    # Start the guessing loop ✅
    while True:
        guess = int(input("Guess a number between 1 and 20: "))
        attempts += 1 # Increment attempts ✅

        # Provide hints based on the guess ✅
        if guess < random_number:
            print("Too low! Try again.")
        elif guess > random_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed it in {attempts} attempts.")
            break  # Exit the loop if the guess is correct ✅


play_game()