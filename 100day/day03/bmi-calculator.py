# ๐จ Don't change the code below ๐
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# ๐จ Don't change the code above ๐

#Write your code below this line ๐
bmi = weight / (height ** 2)

print(f"{weight} รท ({height} x {height}) = {bmi}")
if bmi < 18.5:
    print(f"Your BMI is {round(bmi)}, you are under weight")
elif bmi < 25:
    print(f"Your BMI is {round(bmi)}, you are normal weight")
elif bmi < 30:
    print(f"Your BMI is {round(bmi)}, you are slightly overweight")
elif bmi < 35:
    print(f"Your BMI is {round(bmi)}, you are obese")
else:
    print(f"Your BMI is {round(bmi)}, you are clinically obese")