import random 

# Number guess game, where the user has to guess a random number between 1-100, the program tells the user is lower
# or higher and prompts ths user repeatedly untill the guess is correct. if the user enters than quit the program.

def guess_game():
    num = random.randint(1, 100) # random number between 0-100.
    game_state = True # If the guess is right quit the loop

    print("""Welcome to my number guessing game. In order to win you have to correctly guess a random number.
    Press 'q' to quit the game.""")
    
    while game_state:
        guess = input("Guess The number between 1-100: ") # User guess input prompt

        message = "{} is {} than the number" # The num is greater or lesser

        msg = "" # Empty message.
        
        if guess != 'q':
            break
        elif int(guess) == num: # If the guess is rught print a message and quit the loop.
            print("Congrate you got it right!")
            message = print(f"{guess} is equal to {num} ")
            game_state = False
        
        elif guess == 'q': # If the user types q the game quits
            game_state = False 

        elif int(guess) < num:
            msg = "Lower"
            print(message.format(guess, msg))
            continue

        elif int(guess) > num:
            msg = "Higher"
            print(message.format(guess, msg))
            continue
        else:
            print("Only Input Numbers!") # Fail-safe for non number inputs
            pass
        
guess_game()
