import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
# create a code that display the Rock, paper, scissors
def display(choice):
    if choice == "rock":
        print(rock)
    elif choice == "paper":
        print(paper)
    else:
        print(scissors)

# make a list about rock, paper, scissors
rock_paper_scissorsList = ["rock", "paper", "scissors"]

# Create a code that allows the user to enter Rock, Paper, Scissors
user_choice = rock_paper_scissorsList[int(input("Write a Rock, Paper, Scissors(0, 1, 2): "))]

print(f"\nUser chose: {user_choice}")

#create random function between 0 and 2
computer_choice = rock_paper_scissorsList[random.randint(0,len(rock_paper_scissorsList)-1)]

#create some if statements 
display(user_choice)
print(f"Conputer chose: {computer_choice}")
display(computer_choice)
if user_choice == computer_choice:
    print("Result : Draw")
else:
    if user_choice == "rock":
        if computer_choice == "paper":
            print("Result : Lose")
        elif computer_choice == "scissors":
            print("Result : Win")
    elif user_choice == "paper":
        if computer_choice == "rock":
            print("Result : Win")
        elif computer_choice == "scissors":
            print("Result : Lose")          
    else:
        if computer_choice == "paper":
            print("Result : Win")
        elif computer_choice == "rock":
            print("Result : Lose")