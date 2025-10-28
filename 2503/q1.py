import math
G = 6.674e-11
def escape(M,r,V):
    v2 = 2*G*M / r
    e2 = V**2 - v2
    if e2 > 0:
        print("Excess speed:", math.sqrt(e2))
    else:
        print("The object won't escape")

# moon example
escape(7.3e22, 1.7e6, 5000)

# earth example
escape(6e24, 5.6e6, 5000)
