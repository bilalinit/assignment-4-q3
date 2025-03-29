def pushfunc(list2 , inputuser):
    for i in range(3):
        list2.append(inputuser)

def main():
    print("Flow with data types")
    inputuser = input("Enter the text you want to duplicate : ")
    list2 :list = []
    print(f"before {list2}")
    pushfunc(list2,inputuser)
    print(f"after {list2}")


if __name__ == '__main__':
    main()