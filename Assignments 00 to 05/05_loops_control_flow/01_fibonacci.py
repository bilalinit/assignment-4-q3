LIMIT: int = 10000

def main():
    a = 0
    b = 1
    while a <= LIMIT:
        print(a)  
        c = a + b
        a = b
        b = c

if __name__ == '__main__':
    main()
