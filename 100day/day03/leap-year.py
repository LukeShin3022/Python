year = int(input("Which year do want to check?"))

print(year % 4)
print(year % 400)
print(year % 100)

if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print(f"{year} is Leap Year")
else:
    print(f"{year} is Not Leap Year")