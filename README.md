# Number-guessing-game
import random
n=random.randint(1,101)
print("welcome! Guess a number")
attempt=0
while True:
    g=int(input("guess number"))
    if g>n:
        print("high")
        attempt+=1
        print("you Guessed in",attempt,"attempt!")
    elif g<n:
        print("low")
        attempt+=1
        print("you Guessed in",attempt,"attempt!")

    elif g==n:
        print("correct!congrats")
        attempt+=1
        print("you Guessed in",attempt,"attempt!")
        break
