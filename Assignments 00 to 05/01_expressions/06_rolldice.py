import random


dice_sides = 6 

def main():
    print("\nRoll dice\n")
    die1 = int(random.randint(1, dice_sides))
    die2 = int(random.randint(1, dice_sides))

    total = die1 + die2

    print(f"2 Dices with {dice_sides} sides were rolled\nDice 1 rolled : {die1}\nDice 2 rolled {die2}\nTotal sum of both dice = {total}")

if __name__ == '__main__':
    main()