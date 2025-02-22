# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# squared_numbers = [number*number for number in numbers]
# print(squared_numbers)



# list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
# numbers = [int(number) for number in list_of_strings]
# result = [number for number in numbers if number%2==0]
# print(result)


with open("file1.txt") as file_1, open("file2.txt") as file_2:
    file_1_read = file_1.read().splitlines()
    file_2_read = file_2.read().splitlines()
    
result = [int(number) for number in file_1_read if number in  file_2_read]
print(result)