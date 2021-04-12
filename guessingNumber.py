import random
import time
import os

attempts=0
retry="\nOops..You missed it. Retry!!\n"

#generating ramdom number between one to twenty
number=random.randint(1,20)

os.system("cowsay 'Wait, I am thinking of a number... between 1 to 20'")
time.sleep(3)
print("\nOkay.. So let's see if you can guess it.\nI will give you 6 attempts.\n\n")

while attempts < 6:
    guess=int(input("Guess the number :"))

    attempts+=1
    if attempts == 3:
        os.system("clear")

    if guess < number:
        print("Guess is lesser than the actual. Try increasing it.")
        print(retry)
        time.sleep(2)

    elif guess > number:
        print("Guess is greater than the actual. Try decreasing it.")
        print(retry)
        time.sleep(2)

    elif guess == number:
        print("Boom! You did it.")
        time.sleep(2)
        break
    
    else:
        print("Please give a valid input..between 1 to 20.")
        attempts-=1

if guess == number and attempts > 1:
    attempts=str(attempts)
    print(f" \n\nYou found out in your {attempts}/6 attempts of guesses.")

if guess == number and attempts == 1:
    attempts=str(attempts)
    print(f"\n\nYou found out in your very first attempt of guess. \n")

if guess!=number and attempts == 6:
    print("\nNot a Problem. Better Luck next time. \n")

os.system("cowsay 'Thanks for playing with me.\nHope you like it.'")


