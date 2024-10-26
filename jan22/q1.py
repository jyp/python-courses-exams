w = float(input("weight"))
h = float(input("height"))

bmi = w / (h*h)

if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal")
elif bmi < 30:
    print("Overweight")
else:
    print("Obese")


