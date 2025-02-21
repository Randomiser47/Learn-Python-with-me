import pandas

data = pandas.read_csv("Squirrel_Census.csv")
grey =len(data[data["Primary Fur Color"]=="Gray"])
red =len(data[data["Primary Fur Color"]=="Cinnamon"])
black =len(data[data["Primary Fur Color"]=="Black"])

squirrel_dict = {
    "Fur Color":["grey","red","black"],
    "Amount":[grey,red,black]
}

print(squirrel_dict)

new_squirrel_data = pandas.DataFrame(squirrel_dict)
print(new_squirrel_data)

new_squirrel_data.to_csv("Squirrel Color Count.csv") #new file name



# Alternate solution
# grey =0 
# cinnamon = 0 
# black = 0

# for color in colors:
#     if color == "Gray":
#         grey +=1
#     elif color == "Cinnamon":
#         cinnamon +=1
#     elif color == "Black":
#         black +=1

# # print (grey,cinnamon,black)
