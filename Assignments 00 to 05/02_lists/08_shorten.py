max_length = 3

def limiter_func(list1):
    while len(list1) > max_length:
        deleted = list1.pop()
        print(f"removed {deleted} because it exceded the limit of our list")


def get_list(list1):
    user_input = input("Add an element to the list or press enter to stop : ")
    while user_input != "":
        list1.append(user_input)
        user_input = input("Add an element to the list or press enter to stop : ")
    return list1 

def main():
    print("This code removes elements from the list to a predefined number and returns the predefined number of elements.")
    list1 :list = []
    list1val = get_list(list1)
    print(f"\norignal list {list1val} \n")
    limiter_func(list1val)
    print(f"\nnew list = {list1}")


if __name__ == '__main__':
    main()