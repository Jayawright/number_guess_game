import random 

# Number guess game, where the user has to guess a random number between 1-100, the program tells the user is lower
# or higher and prompts ths user repeatedly untill the guess is correct. if the user enters than quit the program.

def guess_game(num):

    game_state = True # If the guess is right quit the loop
    #guess_num = random.randint(0, 100) # Random num between 0-100
    
    while game_state:
        guess = input("Guess The number between 1-100: ") # User guess input prompt

        message = "{} is {} than the number" # The num is greater or lesser

        msg = "" # Empty message.
        
        if guess == num: # If the guess is rught print a message and quit the loop.
            print("Congrate you got it right!")
            message = print(f"{guess} is equal to {num} ")
            game_state = False

        elif guess < num:
            msg = "Lower"
            message.format(guess, msg)

        elif guess > num:
            msg = "Higher"
            message.format(guess, msg)
        

num_list = range(100) # List of  numbers 0-100


