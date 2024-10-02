# 100 Days of Python - Day 005
# Ex04: Password Generator Project
import random
print(">> PyPassword Generator")

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

num_letters = int(input("Enter the number of Letters you'd like on your PyPassword:\n"))
num_numbers = int(input("Enter the number of Numbers you'd like on your PyPassword:\n"))
num_symbols = int(input("Enter the number of Symbols you'd like on your PyPassword:\n"))

PyPassword = []
for _ in range(num_letters):
  user_letters = random.choice(letters)
  PyPassword.append(user_letters)

for _ in range(num_numbers):
  user_numbers = random.choice(numbers)
  PyPassword.append(user_numbers)

for _ in range(num_symbols):
  user_symbols = random.choice(symbols)
  PyPassword.append(user_symbols)

random.shuffle(PyPassword)
gen_password = "".join(PyPassword)
print(f"Your PyPassword is: {gen_password}")