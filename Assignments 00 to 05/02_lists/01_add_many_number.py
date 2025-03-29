def addnums(numbers):
    
    total : int = 0
    for number in numbers:
        total += number 
    return total


def main():
    print("Summing up a list of numbers")
    numbers :list[int] = [1,2,3,4,5,6]
    sum_of_list = addnums(numbers)
    print(f"the sum if given list is {sum_of_list}")

if __name__ == '__main__':
    main()