import random

secret = random.randrange(0, 10)

print("choose a number from 0 to 1000")
guess = 0
tries = 0
while guess != secret:
    guess = int(input("make a guess: "))
    tries = tries + 1
    if guess > secret:
        print("Too High")
    elif guess < secret:
        print("Too low")
    else:
        print("you got it")
    
print("number of tries:",tries)
