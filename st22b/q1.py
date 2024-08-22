import math


current = float(input("Current pension?"))
actual = 1.05 * current
if actual < 450:
    actual = 450
if actual > 2500:
    actual = 2500
actual=math.ceil(actual)
actual=int(actual)
print(actual)
    
# What if you don't want to use math.ceil?

def my_ceil(x):
    if int(x) == x:
        return int(x)
    else:
        return int(x+1)
