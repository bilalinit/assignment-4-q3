def get_numbers():
    phonebook = {}

    while True:
        name = input("Enter a name : ").strip()  
        if name == "":
            break
        try:
            phone = int(input("Enter a number : "))
            phonebook[name] = phone
        except ValueError:
            print("Enter a valid number")
    return phonebook

def search(phonebook):
    while True:
        name = input("Enter a name you want to search: ").strip()  
        if name == "":
            break
        if name not in phonebook:
            print(f"{name} was not found in your phone book")
        else:
            print(phonebook[name])

def print_phone(phonebook):
    for name in phonebook:
        print(str(name) + " = " + str(phonebook[name]))

def main():
    print("This code takes a dictionary of phone numbers, allows users to look up contacts, and print all contacts in the phonebook")
    numbers = get_numbers()
    print_phone(numbers)
    search(numbers)

if __name__ == '__main__':
    main()
