def main():
    print("Remainder division")
    num1 = float(input("Enter the number you want to divide: "))
    num2 = float(input("Enter the number you want to divide with: "))

    division = num1 // num2
    remainder = num1 % num2

    print(f"Your division is {division} and the remainder is {remainder}")
if __name__ == '__main__':
    main()