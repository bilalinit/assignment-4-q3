def main():
    fruit_prices = {'apple': 10, 'bananas': 5, 'watermelon': 80, 'oranges': 5, 'strawberry': 1.5, 'mango': 15}
    
    total_price = 0
    for fruit in fruit_prices:
        cost_per_unit = fruit_prices[fruit]
        quantity = int(input("How many (" + fruit + ") do you want to buy?: "))
        total_price += (cost_per_unit * quantity)
    
    print("Your total is $" + str(total_price))

if __name__ == '__main__':
    main()
