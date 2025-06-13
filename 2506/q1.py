
def conic():
    A = float (input("input A:"))
    B = float (input("input B:"))
    C = float (input("input C:"))
    Delta = B*B - 4*A*C
    if Delta < 0:
        if A == C and B == 0:
            print("The function represents a circle")
        else:
            print("The function represents an ellipse")
    elif Delta == 0:
            print("The function represents a parabola")
    else:
        if A + C == 0:
            print("The function represents a rectangular hyperbola")
        else:
            print("The function represents a hyperbola")
