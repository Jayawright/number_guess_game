import random
game_state = True

print("Welcome to my number guessing game, to start please guess a number between 1-100")
print("Press q at any time to quit.")

win_num = random.randint(0, 100)

while game_state:
    guess = input("Enter a guess: ")
   
   
    if int(guess) == win_num:
        print("Congrats you guessed the correct number!")
        break
   
    if guess == 'q':
        break
   
    elif int(guess) > win_num:
        print("Too high, guess lower.")
        continue
   
    elif int(guess) < win_num:
        print("Too low, guess higher.")
        continue
   
    else:
        print("Enter a number or 'q'!")
        continue