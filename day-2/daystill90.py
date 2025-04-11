age = input("Please enter your age: \n")

age = int(age)
years_left= 90- age
months_left = years_left*12
days_left = years_left*365
weeks_left = years_left*52
print(f"You have {days_left} days, {weeks_left} weeks left,{months_left} months, {years_left}years left till the age of 90")