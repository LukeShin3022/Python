#Write your code below this row 👇
total = 0
cnt = 0
for n in range(2,101, 2):
    total += n
    cnt += 1
print(total,cnt)

total = 0
cnt = 0
for n in range(1,101,2):
    total += n
    cnt += 1
print(total,cnt)

total = 0

for n in range(1, 101):
    if n % 2 == 0:
        total += n
print(total)