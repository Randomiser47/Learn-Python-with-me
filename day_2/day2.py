# Primitive Data Types
# print("Hello" [4])

#Integer
# print(123+345)

#Float
# 3.14159

#Boolean
#True
#False

# #Checking Data Type of a variable
# num_char = len(input("Enter your name \n" )) #Len is an integer being stored into num_char
# new_num_char = str(num_char)#Converting integer into String
# print("Your name has " + new_num_char +" Characters")
# # print(type(num_char))#Checking data type

#Convering Data types
# a =123
# print(type(a))
# a =str(123)
# print(type(a))
# a =float(123)
# print(type(a))
# print(70 + float("100.5")) #the string is converted into float and added into 70(integer)
# print(str(80)+str(100)) #converting the integers into string and performing concatenation

#Exercise if 39 is entered the program should add 3 and 9 together which = 12
# a = str(input("Please Enter a number: "))
# c = int(a[0])
# d = int(a[1])
# print(c+d)

#Mathematical Operations
# 3 + 5   #Add
# 7 - 4   #Minus
# 3 * 2   #Multiplication 
# 6 / 3   #Division
# 3 ** 2  #Exponent
#Priority order of execution
#PEMDAS = Parantheses --> Exponents --> Multiplication --> Division --> Addition --> Subtraction
# print(3*(3+3)/3-3)

#Number manipulation and F Strings in Python
# print(round(8/3)) #round func rounds decimal numbers
# print(round(2.6666,2)) #the ', 2' after the 2.666 rounds it to 2 decimal places
# print(8//3) # floor division '//'

score =0 
height = 1.8
isWinning = True
#f-string
print(f"your score is {score}, your height is {height}, are you winning? {isWinning}")