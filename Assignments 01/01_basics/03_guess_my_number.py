import random

def user_guess(x):
    number = random.randint(1, x)
    guess = 0
    
    while guess != number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        
        if guess < number:
            print("Too low! Try again.")
        elif guess > number:
            print("Too high! Try again.")
    
    print(f"Congratulations! You guessed the number {number} correctly!")

def main():
    user_guess(99)

if __name__ == '__main__':
    main()
