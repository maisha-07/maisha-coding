import random

secret = random.randint(1, 100)
tries = 0

print("I'm thinking of a number 1-100. Try to guess!")

while True:
    guess = int(input("Guess: "))
    tries = tries + 1

    if guess < secret:
        print("Too low")
    elif guess > secret:
        print("Too high")
    else:
        print(f"Correct! It took you {tries} tries.")
        break
