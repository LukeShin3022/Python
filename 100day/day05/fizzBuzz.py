#Write your code below this row 👇
result = ""
for n in range(1,101):
    if n % 3 == 0 or n % 5 == 0:
        if n % 3 == 0:
            result += "Fizz"
            
        if n % 5 == 0:
            result += "Buzz"
        print(result)
        result = ""
    else:
        print(n)
        
#Another Solution 👇
result = ""
for n in range(1,101):
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)