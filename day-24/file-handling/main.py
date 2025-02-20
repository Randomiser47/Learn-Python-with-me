# file = open('my_file.txt')
# contents = file.read()
# print(contents)
# file.close() #if you open the file only via open you have to close it otherwise it eat ram.

# with open('my_file.txt') as file: #This will close file atuomatically
#     contents = file.read()
#     print(contents)


# with open('my_file.txt', mode = "a") as file: #mode is used to define how you want to write, default mode is read.
#     file.write("\n BRrrrrrrrrrrrrrrrrrrrrrruh")

# with open('wow.txt',mode = "w") as file: #if you enter a file name that doesn't exit it will create the file for you
#     file.write("brorororororo")

