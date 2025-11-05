import math

def poisson(k, lam):
    return (lam ** k) * math.exp(-lam) / math.factorial(k)

def main():
    try:
        k = int(input("k: "))
        lam = float(input("lambda: "))
        if k < 0 or lam < 0:
            raise ValueError
        print(poisson(k, lam))
    except ValueError:
        print("invalid parameters")

