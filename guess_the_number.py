import random

number = random.randint(1, 1000)
user_guess = 0
while user_guess != number:
    user_guess = int(input("Guess the number from 1 to 1000: "))
    if user_guess > number:
        print("You guessed too high!")
    elif user_guess < number:
        print("You guessed too low!")
    
print("WOOOW! Your guess is so correct.")
