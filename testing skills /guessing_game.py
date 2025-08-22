import random

random_num = random.randint(1, 10)

guess = int(input("Guess a number between 1 and 10: "))
max_attempts = 5


def guess_number():
    for attempts in range(1, max_attempts, +1):
        if guess == random_num:
            print("Congratulations! You guessed the number.")
            break
        elif guess < random_num:
            int(input("Too low! Try again. "))
        elif guess > random_num:
            int(input("Too high! Try again. "))
        elif guess:
            print("Sorry, you've used all your attempts. The number was:", random_num)
            break
        else:
            print("Invalid input. Please enter a number between 1 and 10.")
            break


guess_number()
