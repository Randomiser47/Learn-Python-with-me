try: 
    age=int(input("How old are you?")) 
except ValueError: 
    print("You have given an invalid input. Please give a numerical input e.g., 21")
age = int(input("How old are you?")) 
if age > 18: 
   print("You can drive at age (age).")