#Write your code below this line 👇
def prime_checker(number):
    sqrt = round(number**(1/2))
    primeFlag = True
    if number < 2:
        print("It's not a prime number.")
    elif number >= 100:
        print("please, put in the number less than 100")
    else:
        for n in range(sqrt, 1, -1):
            if number%n == 0:
                primeFlag = False
        if primeFlag == True:
            print("It's a prime number.")
        else:
            print("It's not a prime number.")



#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)