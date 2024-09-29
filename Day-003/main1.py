# 100 Days of Python - Day 003

# Ex07: Game Project
def game_over(reason):
    print("""
     ____                         ___                
    / ___| __ _ _ __ ___   ___   / _ \__   _____ _ __ 
   | |  _ / _` | '_ ` _ \ / _ \ | | | \ \ / / _ \ '__|
   | |_| | (_| | | | | | |  __/ | |_| |\ V /  __/ |   
    \____|\__,_|_| |_| |_|\___|  \___/  \_/ \___|_|   
    """)
    print(f"{reason} Game Over!")
    exit()

def get_valid_input(prompt, options):
  while True:
    choice = input(prompt).lower()
    if choice in options:
      return choice
    print(f"Invalid choice. Please choose from {', '.join(options)}.")

def javascript_quiz():
  print("Welcome to JavaScript Quiz.")
  print("Answer the question correctly to pass the quiz. Let's begin!")

  # level 1:
  question1 = """
  Which of the following is the correct way to declare a variable in JavaScript?
    a) let variableName;
    b) var variableName;
    c) const variableName = value;
    d) All of the above

  To enter your answer, please type a, b, c, or d. 
  """
  answer1 = get_valid_input(question1, ["a", "b", "c", "d"])
  if answer1.lower() != "d":
      game_over("I'm sorry, wrong answer - better luck next time.")

  # level 2:
  question2 = """
  Which of the following is a valid way to define a function in JavaScript?
    a) function myFunction() { ... }
    b) const myFunction = function() { ... }
    c) const myFunction = () => { ... }
    d) All of the above

  To enter your answer, please type a, b, c, or d.
  """
  answer2 = get_valid_input(question2, ["a", "b", "c", "d"])
  if answer2.lower() != "d":
      game_over("I'm sorry, wrong answer - better luck next time.")

  # level 3:
  question3 = """
  What will be the output of the following JavaScript code?
  console.log(2 + '2');
    a) 4
    b) 22
    c) undefined
    d) NaN
  
  To enter your answer, please type a, b, c, or d.
  """
  answer3 = get_valid_input(question3, ["a", "b", "c", "d"])
  if answer3.lower() != "b":
      game_over("I'm sorry, wrong answer - better luck next time.")

  else:
     print("Congratulations! You passed the quiz and have a solid grasp of JavaScript basics!")
    
javascript_quiz()


