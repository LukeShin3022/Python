print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0
if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print(f"Please Pay ${bill}.")
    elif age >= 12 and age <= 18:
        bill = 7
        print(f"Please pay ${bill}")
    else:
        bill = 12
        print(f"Please pay ${bill}.")
    photoFlag = input("Do you want a photo taken? Y or N: ")
    if photoFlag == "Y" or photoFlag == "y":
        bill += 3
    print(f"Your final bill is ${bill}")
else:
    print("Sorry, you have to grow taller befre you can ride")