print("Welcome to my maths quiz game!")

playing = input("Do you want to play  :  ")

if playing != "yes":
    quit()

print("Lets play! Try your luck with 3 quiz!!!")

question = input("Tell me about 5+1: ")
if question == "6":
    print("Correct! 2 more quiz to go")
          
else:
    print("Incorrect! :(")

question = input("Tell me about 7*5: ")
if question == "35":
    print("Awesome! 1 more quiz to go")
          
else:
    print("Incorrect! You were close to victory :(")

question = input("Tell me about 85-37: ")
if question == "48":
    print("Bravo!!! You are genious")
          
else:
    print("Hard Luck!!! :(")