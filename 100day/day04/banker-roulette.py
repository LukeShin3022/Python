import random

# def choice(names):
#     nameList = names.split(", ")
#     print(nameList)
    
#     choice_num = round(random.random() * (len(nameList) - 1))
#     print(choice_num)
    
#     print(f"{nameList[choice_num]} is going to buy the meal today!")
    
# names = input("Write names: ->  ")
# names ="a, b, c, Luke, MJ, d, e, f, g"
# print(names)
# choice(names)



# Import the random module here

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names_string ="a, b, c, Luke, MJ, d, e, f, g"
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# choice_num = random.randint(0,len(names)-1)

# print(f"{names[choice_num]} is going to buy the meal today!")


#============================

print(f"{random.choice(names)} is going to buy the meal today!")