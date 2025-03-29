req_height = 125

def tall_enough(height):

    while req_height > height :
        print("You are not tall enough, maybe in the next life :)")
        height = int(input("Enter your height : ")) 
    print("you are good to go ")

    
def main():
    print("This code checks if you are eligible to get on a ride")
    height = int(input("Enter your height : "))
    tall_enough(height)

if __name__ == '__main__':
    main()