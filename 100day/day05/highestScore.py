# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
highest_score = 0
for score in student_scores:
    if highest_score < score:
        highest_score = score
print(highest_score)

highest_score = 0

for n in range(0, len(student_scores)):
  if highest_score < student_scores[n]:
    highest_score = student_scores[n]
    # print(highest_score)
print(highest_score)