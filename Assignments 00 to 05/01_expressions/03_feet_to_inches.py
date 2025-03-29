
inches_in_feet = 12

def main():
    print("convert feet into inches")
    input_feet = float(input("enter your height in feet: "))
    inches: float = input_feet * inches_in_feet
    print(f"{input_feet} Feet is equal to {inches} inches")
if __name__ == '__main__':
    main()