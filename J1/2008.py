bmi = 0

weight = int(input("Please type in the weight in kilos: "))

height = float(input("Please type in the height in metres: "))

bmi = weight/(height*height)

if bmi > 25:
    print("Overweight");
elif bmi >= 18.5 and bmi <= 25:
    print("Normal weight");
else:
    print("Underweight");
