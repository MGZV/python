import random

print("Let's play the game.\nEnter rock, paper or scissors. \nIf you want to exit enter 'q' ")
flag = True
while flag:
    choice = ['rock', 'paper', 'scissors']
    comp = random.choice(choice)

    human = input("You choice: ")
    print()
    human = human.lower()
    if human == 'q':
        flag = False
    else:
        if human == 'rock' or human == 'paper' or human == 'scissors':
            if comp == human:
                print("Ties\n")
            elif (comp == 'rock' and human == 'scissors'
                  or comp == 'paper' and human == 'rock'
                  or comp == 'scissors' and human == 'paper'):
                print("Computer win!\n")
            else:
                print("Human win!\n")

        else:
            print("Please enter right choice\n")
