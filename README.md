# Number-guessing-game
import random
# Generate a random number between 1 and 101
n=random.randint(1,101)
print("welcome! Guess a number")
# Start attempt counter
attempt=0
while True:
# Take user's guess
    g=int(input("guess number"))
    if g>n:
    # Guess is too high
        print("high")
        attempt+=1
        print("you Guessed in",attempt,"attempt!")
    elif g<n:
     # Guess is too low
        print("low")
        attempt+=1
        print("you Guessed in",attempt,"attempt!")

    elif g==n:
    # Correct guess!
        print("correct!congrats")
        attempt+=1
        print("you Guessed in",attempt,"attempt!")
        break
