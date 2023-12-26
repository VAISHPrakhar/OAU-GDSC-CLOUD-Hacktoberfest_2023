import random

def roll_dice_game():
    user_choice = int(input("Guess the number on the dice (1-6): "))
    dice_number = random.randint(1, 6)
    if user_choice < 1 or user_choice > 6:
        print( "Invalid input. Please choose a number between 1 and 6.")
    if user_choice == dice_number:
        print (f"Congratulations! The dice rolled {dice_number}. You guessed it right!")
    else:
        print (f"Sorry, the dice rolled {dice_number}. Better luck next time!")
