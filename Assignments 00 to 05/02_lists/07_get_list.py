def main():
    print("This code takes a list of elements from user and returns the list when closed ")
    lst = []
    user_input = input("\nEnter a element to add to the list or press enter to end : ")

    while user_input != "":
        lst.append(user_input)
        user_input = input("\nEnter a element to add to the list or press enter to end :  ")
    print(f"\nthis your list {lst}")

if __name__ == '__main__':
    main()