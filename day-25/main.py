# # with open ("weather_data.csv") as file:
# #     data = file.readlines()
# # print(data)

# # import csv

# # with open ("weather_data.csv") as data_file:
# #     data = csv.reader(data_file)
# #     tempreature = []
# #     for row in data:
# #         if row[1] != 'temp':
# #             tempreature.append(int(row[1]))

# # print(tempreature)


# import pandas

# data = pandas.read_csv('weather_data.csv')
# # print(data['temp'])
# # temp_list = data['temp'].tolist()

# # max_temp = data['temp'].max()
# # # print(data[data.temp == max_temp])

# # monday = data[data.day == "Monday"]
# # print(monday.temp * (9/5) +32)


# #creating dataframe from scratch
# data_dict = {
#     "students":["amy","james","angela"],
#     "scores": [76,56,65],
# }

# data = pandas.DataFrame(data_dict)
# print(data)

# data.to_csv("new_data.csv")
