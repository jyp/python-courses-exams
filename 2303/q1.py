def flowers():
    flowers = int(input("Number of flowers: "))
    week = int(input("Week number: "))
    price = flowers*20

    price1 = price
    if 14 <= week <= 17:
        price1 = (flowers//2 + flowers%2)*20

    price2 = price
    if flowers >= 200:
        price2 = price2*0.80

    price = min(price1,price2)
    print("The price is "+str(price))

flowers()
