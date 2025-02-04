year=int(input("which year do you want to check?: \n"))

if year%4==0:
    if year%400==0:
        print("The year is leap year")
    elif year%100==0:
        print("The year is not a leap year")
    else:
        print("It is a leap year")
else:
    print("The year is not a leap year")