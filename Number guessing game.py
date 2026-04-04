import random
n=random.randint(1,101)
print("welcome! Guess a number")
attempt=0
max_attempt=5

while attempt<max_attempt:
    g= int (input("guess number"))
   

    if g>n:
        print("high")
        attempt+=1
        
    elif g<n:
        print("low")
        attempt+=1
       
    elif g==n:
        print("correct!congrats")
        attempt+=1

        if attempt>1:
             print("the guessed in",attempt,"attempts")
        else:
            print("you guessed in",attempt,"attempt")

        break
        
    if attempt==max_attempt:
        print("game over! The number is ",n)
