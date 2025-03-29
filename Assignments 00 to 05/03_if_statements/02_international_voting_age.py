Peturksbouipo = 16
Stanlau = 25
Mayengua = 48

def main():
    print(">> Voting age checker\n")
    
    try:
        age = int(input(">> Enter your age to find out where you can vote: "))
        
        if age >= Peturksbouipo:
            print(f"\nYou are eligible to vote in Peturksbouipo because the voting age is {Peturksbouipo}\n")
        else:
            print("You are not eligible to vote in Peturksbouipo\n")
            
        if age >= Stanlau:
            print(f"\nYou are eligible to vote in Stanlau because the voting age is {Stanlau}\n")
        else:
            print("You are not eligible to vote in Stanlau\n")
            
        if age >= Mayengua:
            print(f"\nYou are eligible to vote in Mayengua because the voting age is {Mayengua}\n")
        else:
            print("You are not eligible to vote in Mayengua\n")
    
    except:
        print("\nInvalid input. Please enter a valid numeric age.\n")

if __name__ == '__main__':
    main()
