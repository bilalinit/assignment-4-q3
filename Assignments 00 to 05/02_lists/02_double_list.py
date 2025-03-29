
def main():
    print("This code doubles a list of numbers")
    numbers : list[int] = [2,3,4,5]
    

    for i in range(len(numbers)):
        numbers_on_index = numbers[i]
        numbers[i] = numbers_on_index * 2

    print(numbers)
if __name__ == '__main__':
    main()