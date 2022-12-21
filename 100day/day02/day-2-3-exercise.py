# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

wholeLife = 365 * 90
remainLife = wholeLife - int(age) * 365
remainMonths = round(remainLife / 30)
remainWeeks = round(remainLife / 7)

print(f"You have {remainLife} days, {remainWeeks} weeks and {remainMonths} months left.")