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
hand = [rock,paper,scissors]
user = int(input("What do you choose? Type 0 for rock, 1 for Paper, 2 for Scissors.\n"))
if user >= 3 or user < 0:
    print("You input invalid number.")
else:
    print(hand[user])

    computer = random.randint(0,2)
    print(f"Computer choose:")
    print(hand[computer])

    if user == 0 and computer == 2:
        print("You win!")
    elif user == 2 and computer ==0:
        print("You loose!")
    elif computer > user:
        print("You loose!")
    elif user > computer:
        print("You win!")
    elif computer == user:
        print("Tie")
