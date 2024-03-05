import random

def randomGuess():

    n = random.randint(0, 99)
    print("Guess the number between 0 and 99 !")

    for i in range(10):
        nbr = int(input())

        if n == nbr:
            print("GG u got it!")
        elif n > nbr:
            print("Higher")
        else:
            print("Lower")

randomGuess()