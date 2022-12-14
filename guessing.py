#Takes input of your number, and checks if you guessed the right random number.

import random
def main():


    guess = int(input("Enter your first guess: "))

    for i in range(10):
        if guess == 1:
            print("Congrats!")
            return 1
        else:
            print("Keep guessing!")
        
        guess = int(input("Enter your second guess: "))

    print("You've guessed too many wrong times!")


if __name__ == "__main__":
    main()
