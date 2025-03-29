import random
min_number: int = 1
max_number: int = 100
amount: int = 10

def main():
    print("\nThis code genrates 10 random numbers between 1 to 100\n")
    for i in range(amount):
        random_nums = int(random.randint(min_number, max_number))
        print(f">> {random_nums}")

if __name__ == '__main__':
    main()