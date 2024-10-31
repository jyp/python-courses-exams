
def main():
    t = int(input("number of tries?"))
    c = int(input("number of conversions?"))
    if c > t:
        print("Error!")
    else:
        p = int(input("number of penalties?"))
        d = int(input("number of drop goals?"))
        print("Total score",t*5+c*2+3*(p+d))

main()
