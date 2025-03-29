def main():
    print("This code returns the first 20 even numbers")
    number = []
    num = 0
    while len(number) < 20:
        num += 2
        number.append(num)
        print(num)

    print("\nWith 0 in our output using for loop : ")

    for i in range(20):
        print(i * 2) 
if __name__ == '__main__':
    main()
