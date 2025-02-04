student_scores = input("Input a list of Students Scores").split()
for n in range (0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)
compare_score = 0
#78 65 89 55 91 64 89
for big_score in student_scores: # big score will get value of student_score
    if big_score>compare_score:
        compare_score = big_score
print(f"The highest Score is {compare_score}")
