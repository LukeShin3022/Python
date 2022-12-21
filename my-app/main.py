#Recap study

# my_name = "noco"
# age = 12
# dead = True
# print('hello my name is', my_name)
# print('and I"m ', age, ' years old')


#Function study

# def say_hello(user_name, user_age):
#  print("hello how r u",user_name,"?")
#  print("I am ",user_age,"years old")
 

# say_hello("luke", 29)
# ====================================
# def say_hello(Obj):
#     print(f"Hello I'm {Obj.name} and my age is {Obj.age}")

# a = {
#     "name" : "luke",
#     "age" : 23
# }

# say_hello(a)
# =====================================

# calculator

# def calcNum(num1=0, num2=0, operator = '+'):
#     print(type(num1),type(num2))
#     if  isinstance(num1,(int,float)) and isinstance(num2,(int,float)):
#         match operator:
#             case '+':
#                 return print(num1 + num2)
#             case '-':
#                 return print(num1 - num2)
#             case '*':
#                 return print(num1 * num2)
#             case '/':
#                 return print(num1 / num2)
#             case '**':
#                 return print(num1 ** num2)
#     else:
#         print("Put the number please")
            
# calcNum('8','4','**')

# Casino
# from random import randint, random

# print("Welcome to Python Casino")
# pc_choice = randint(1,50)

# print("Answer: ",pc_choice)

# while True:
#     user_choice = int(input("Choose number: "))
#     if user_choice == pc_choice:
#         print("You Won")
#         break
#     elif user_choice > pc_choice:
#         print("Higher!")
#     elif user_choice < pc_choice:
#         print("Lower!")
# =====================================       
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
result = [num + 3 for num in numbers if num % 2 == 0]
print(result)
# =====================================