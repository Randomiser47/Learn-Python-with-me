height=float(input("Please enter your height: \n"))
weight=float(input("Please enter your weight: \n"))

bmi = round(weight/height**2 ,2)

if bmi<18.5:
    print(f"your bmi is {bmi} You are underweight")
elif 18.5<= bmi <25:
    print(f"your bmi is {bmi} You have normal weight")
elif 25<=bmi<30:
    print(f"your bmi is {bmi} You are overweight")
elif 30<= bmi<35:
    print(f"your bmi is {bmi} You are Obese")
else:
    print(f"your bmi is {bmi} You are clinically obese")