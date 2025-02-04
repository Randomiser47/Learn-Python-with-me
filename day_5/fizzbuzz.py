num = 0

for i in range(1,101):
    num=i
    if num%3==0 and num%5==0:
        print("fizzbuzz")
    elif num%3==0:
        print("fizz")
    elif num%5==0:
        print("buzz")
    
    else:
        print(num)