height = float(input("Please Enter your Height(m): "))
weight = float(input("PLease enter your weight(kg): "))

bmi = weight/height ** 2
bmi = int(bmi)
print(bmi)