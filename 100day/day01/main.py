# print("Hello \n Hello World")
# print("Hello" + " " +"Luke")
#===============================
# print("Hello" + input("What is your name?"))
# print(input("What is your name: ").__len__())
# print(len(input("What is your name: ")))
#===============================
# name = input("What is your name?")
# print(name)


#===============================
# # 🚨 Don't change the code below 👇
# a = input("a: ")
# b = input("b: ")
# # 🚨 Don't change the code above 👆

# ####################################
# #Write your code below this line 👇

# tmp = a
# a = b
# b = tmp

# #Write your code above this line 👆
# ####################################

# # 🚨 Don't change the code below 👇
# print("a: " + a)
# print("b: " + b)

#===============================

# Day - 01 Project : band name generator

#1. Createa greeting for your program.
print("Thank you for comming Band name Generator")
#2 Ask the user for the city that they grew up in.
cityName = input("What is the city that you have grew up?\n")
if cityName.__len__() <= 0:
    cityName = "Seoul"
#3 Ask the user for the name of a pet.
petName = input("What is your pet name?\n")
if petName.__len__() <= 0:
    petName = "Puppy"
    
#4 Combine the name of their city and pet and show them their band name.
print("Band Name is " + cityName + " " + petName)
#5 Make sure the input cursor shows on a new line, see the example at:
# https://band-name generator-end.appbrewery.repl.run/