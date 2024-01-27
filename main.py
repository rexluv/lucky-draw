# Import the random module for generating random choices
import random

print("Lucky Draw Game\n")

notice = "The rule of the game is to draw a card between \'A, 2, 3, 4, 5'\n"\
         "if your card is the correct one your money gets doubled\nelse you lose the bet amount"

# Get initial balance from the user and outputs it
balance = int(input("Enter your top-up amount : $"))
print(f"your balance is now ${balance}")

# Define the set of cards to choose from
cards = ["A", "2", "3", "4", "5"]

# Randomly choose a card as the lucky card for each game
luck = random.choice(cards)

# Set new_balance as a global variable with balance
new_balance = balance

# Function to play the game
def game():
    global new_balance # Use the global variable for balance
    amount = int(input("Enter your bet amount : "))
    bet_amount = amount
    new_balance -= amount
    print(f'you have successfully placed a bet of {bet_amount} '
          f'your balance is now {new_balance} make sure you win')
    choices = input("Enter your selection between \"A, 2, 3, 4, 5\" : ")

    if choices == luck: 
        cashout = bet_amount * 2
        new_balance += cashout
        print(f"Congratulations you have won ${cashout} your new balance is {new_balance}")
    else:
        print(f"Sorry you lost but you can still try again \n your balance is now {new_balance}")

while True:
    try:
        print("1. Play game\n2. Help\n3. check balance\n4. exit")
        choice = int(input("Enter Your Selection : "))
        if choice == 1:
            print(notice)
            game()
        elif choice == 2:
            print(notice)
        elif choice == 3:
            print(f"your balance is {new_balance}")
        elif choice == 4:
            break
        else:
            print("Invalid Option try again")
    except:
        break