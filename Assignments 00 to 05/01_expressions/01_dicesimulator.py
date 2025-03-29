import random

dice_sides = 6


def dice_roll():
    dice1 = int( random.randint(1, dice_sides))
    dice2 = int( random.randint(1, dice_sides))
    total :int = dice1 + dice2
    print(f"dice 1 rolled : {dice1} \ndice 2 rolled : {dice2} \ntotal is : {total}\n")

def main():
    print("dice simulator\n")
    roll_times = int(input("enter how many times you want these dice to roll "))
    dice_roll_times = roll_times
    for i in range(dice_roll_times):
        dice_roll()



if __name__ == '__main__':
    main()