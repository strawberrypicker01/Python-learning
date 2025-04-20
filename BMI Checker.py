height = float(input("Enter height in cm"))
weight = float(input("Enter weight in kg"))
BMI = weight / (height / 100) ** 2
print("Your BMI is: {0} and you are: ".format(BMI), end='')
if BMI <= 18.4:
    print("Underweight")
elif BMI <= 24.9:
    print("Healthy")
elif BMI <= 29.9:
    print("Overweight")
elif BMI <= 34.9:
    print("Severely Overweight")
elif BMI <= 39.9:
    print("Obesity")
else:
    print("Morbid Obesity")