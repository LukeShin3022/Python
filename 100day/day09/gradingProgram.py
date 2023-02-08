student_scores = {
    "harry":81,
    "Ron":78,
    "Hermione":99,
    "Draco":74,
    "Neville":62
}
student_grade = {}

for student in student_scores:
    if student_scores[student] >= 91 :
        student_grade[student] = "Outstanding"
    elif student_scores[student] >= 81 :
        student_grade[student] = "Exceeds Expectations"
    elif student_scores[student] >= 71 :
        student_grade[student] = "Acceptable"
    elif student_scores[student] <= 70 :
        student_grade[student] = "Fail"

print(student_grade)
print(student_scores)