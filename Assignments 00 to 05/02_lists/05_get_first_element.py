def get_first_element(list1):
     
     print(list1[0])


def list1():
    list1 = []
    user_input = input("Add and element to the list or press enter to stop this code and return the first index of the list : ")
    while user_input != "":
            list1.append(user_input)
            user_input = input("Add and element to the list or press enter to stop this code and return the first index of the list : ")
    return list1
        

def main():
    print("This code takes a list of elements from user and returns the first index of the list when closed")
    list1val = list1() 
    get_first_element(list1val)

if __name__ == '__main__':
    main()