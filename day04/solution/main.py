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

well = '''

'             '
'             '
'             '
'             '
'             '
'_____________'
'''

while True:
    choice = input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors, 3 for Well, or 'out' to quit. You choose:")

    if choice.lower() == "out":
        print("Thanks for playing! Goodbye!")
        break

    computers_choice = random.randint(0,3)

    if not choice.isdigit():
        print("You've entered an invalid value, try again and choose a number between 0-2.")
        continue
    else:
        choice = int(choice)
        if choice > 3:
            print("You've entered an invalid number, try again and choose a number between 0-3.")
            continue
        elif choice == 0 or choice == 1 or choice == 2 or choice == 3:
            if choice == 0:
                print(f"You chose: Rock {rock}")
            elif choice == 1:
                print(f"You chose: paper {paper}")
            elif choice == 2:
                print(f"You chose: scissors {scissors}")
            elif choice == 3:
                print(f"You chose: well {well}")

            if computers_choice == 0:
                print(f"The computer chose: Rock {rock}")             
                if choice == 2:
                    print("You lose, Rock wins against scissors.")
                elif choice == 3:
                    print("you win")
                elif choice == 0:
                    print("It's a draw!") 
                else:
                    print("You win!")
            
            elif computers_choice == 1:
                print(f"The computer chose: Paper {paper}")
                if choice == 0:
                    print("You lose, Paper wins against rock.")
                elif choice == 1:
                    print("It's a draw!")
                elif choice == 2:
                    print("You win!")
                else:
                    print("You win!")

            elif computers_choice == 2:
                print(f"The computer chose: Scissors {scissors}")
                if choice == 1:
                    print("You lose, Scissors win against paper.")
                elif choice == 2:
                    print("It's a draw!")
                elif choice == 0:
                    print("You win!")    
                else:
                    print("You win!")

            elif computers_choice == 3:
                print(f"The computer chose: well {well}")
                if choice == 2:
                    print("You lose, well win against paper.")
                elif choice == 3:
                    print("It's a draw!")
                elif choice == 0:
                    print("You lose, well win against Rock.")
                else:
                    print("You win!")
                                            