def main():
    print("Contvert fahrenheit to celcious")

    temp_fahrenheit = int(input("enter the temprature in fahrenheit\t"))

    degrees_celsius = (temp_fahrenheit - 32) * 5.0/9.0

    print(f"Temperature: {temp_fahrenheit}F = {degrees_celsius}C")

if __name__ == '__main__':
    main()