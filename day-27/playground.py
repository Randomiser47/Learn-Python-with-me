# def add(*args):
#     sum = 0
#     for n in args:
#         sum += n
#     return sum
#     # or just use this 
#     # return sum(args)




# print(add(1,2,3,4,5,10))



# def calculate(n,**kwargs):
#     # print(kwargs)
#     # for key, value in kwargs.items():
#     #     print(key)
#     #     print(value)
#     n *= kwargs["multiply"]
#     n += kwargs["add"]
#     print(n)

# calculate(2,add =3, multiply =5)

class Car:
    def __init__(self,**kw):
        self.make = kw["make"]
        self.model = kw["model"]
        self.quality = kw.get("quality") #this '.get' allows a call to made with the function even if it has no value


my_car = Car(make = "Nissan", model = "GT-R")
print(my_car.quality)