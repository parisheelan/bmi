h=float(input("Enter height(m): "))
w=float(input("Enter weight(kg): "))
bmi=w/h**2
print("BMI= ",bmi)
if bmi<=18.5:
    print("Underweight")
elif bmi>=25:
    if bmi>=30:
        print("Obese")
    else:
        print("Overweight")
else:
    print("Normal")