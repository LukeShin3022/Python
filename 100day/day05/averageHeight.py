student_heights_sum = 0
student_heights_avg = 0
# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_hights[n])
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
#   student_heights_sum += student_heights[n]
# student_heights_avg = student_heights_sum / len(student_heights)

student_heights_avg = round(sum(student_heights) / len(student_heights))
print(student_heights_avg)
