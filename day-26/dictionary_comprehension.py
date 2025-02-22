student_score = {
    "Alex":90,
    "Beth":80,
    "Caroline":40,
}
#^^^^^^^^^^^ to get that we can do this 



# import random
# names = ['Alex','Beth','Caroline','Dave','Eleanor','Freddie']
# student_score = {student:random.randint(1,100) for student in names} # is a dictionary that is being made with a list
# print(student_score)

# passed_students = {student:numbers for (student,numbers) in student_score.items() if numbers>=50} #dictionary comprehension by a dictionary
# print(passed_students)


# #Sentence split and word length calculation via comprehension
# sentence = "What is the Airspeed Velocity of an Unladen Swallow?".split()
# result = {word:len(word) for (word) in sentence}

# #Changing temp just via comprehension
# weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
# weather_f = {day:temp* 9/5 + 32 for (day,temp) in weather_c.items()}
# print(weather_f)


import pandas
students = {
    "Student":["Alex","Beth","Caroline"],
    "Scores":[90,80,40,]
}

student_data_frame = pandas.DataFrame(students)
print(student_data_frame)

#loop through each of the rows of a data frame
for (index,row) in student_data_frame.iterrows():
    if row.Student == "Alex":
        print(row.Scores)