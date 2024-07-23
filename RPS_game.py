#use case - This is a program which allows the user to play a rock, paper and scisors game
import random 

def main():
    choice = ("rock","paper","scissor")
    player = input("Enter your choice (rock,paper,scissor):")
    Computer = random.choice(choice) #random function is used to select a random choice as the computer's move

    print("Player's Choice:",player)
    print("Computer's Choice:",Computer)

    #These are the basic rules for the game which decides the winner for the game between the player and computer which are applied by using the if else statements
    if player == Computer:
        print("It's a Tie!")
    elif player == 'rock' and Computer == 'scissor':
        print("You Win!")
    elif player == 'paper' and Computer == 'rock':
        print("You Win!")
    elif player == "scissor" and Computer == 'paper':
        print("You Win!")
    else:
        print("You Lose!")  

#This part of the code is used to ask the user if he/she wants to play the game again or not 
def play_again():
    while True:
        play = input("Do you want to play again? (yes/no):").lower()
        if play == 'yes':
            main()
        else:
            print("Thank you for playing the game!")
            break  

main()
play_again()          



