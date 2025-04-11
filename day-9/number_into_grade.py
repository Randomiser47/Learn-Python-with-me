student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}
student_grades = {}
for student, scores in student_scores.items():
    if scores >= 91 and scores <= 100:
        student_grades[student] = "Outstanding"
    elif scores >=81 and scores <= 90:
        student_grades[student] = "Exceeds Expectations"
    elif scores >=71 and scores <= 80:
        student_grades[student] = "Acceptable"
    elif scores <70:
        student_grades[student] = "Fail"
