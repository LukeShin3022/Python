# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
def chkTrue(name):
    cnt = 0 
    cnt += name.count("t")
    cnt += name.count("r")
    cnt += name.count("u")
    cnt += name.count("e")
    return cnt

def chkLove(name):
    cnt = 0 
    cnt += name.count("l")
    cnt += name.count("o")
    cnt += name.count("v")
    cnt += name.count("e")
    return cnt

# name1 = "Angela Yu"
# name2 = "Jack Bauer"

lower_name = name1 + name2

trueCnt = 0
loveCnt = 0

trueCnt = chkTrue(lower_name)
loveCnt = chkLove(lower_name)

loveScore = str(trueCnt) + str(loveCnt)
loveScore = int(loveScore)

if loveScore < 10 or loveScore > 90:
    print(f"Your score is {loveScore}, you go together like coke and mentos.")
elif loveScore >= 40 and loveScore <= 50:
    print(f"Your score is {loveScore}, you are alright together.")
else:
    print(f"Your score is {loveScore}.")