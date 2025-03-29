def main():
    print("pythagorean theorem ")
    ab :float = float(input("Enter the length of ab: "))
    ac :float = float(input("Enter the length of ac: "))
    bc2= (ab ** 2 ) + (ac ** 2)
    bc = bc2 ** 0.5

    print(f"The length of bc is {bc}")
if __name__ == '__main__':
    main()