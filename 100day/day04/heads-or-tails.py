import random

coin = random.random() * 1

coin = round(coin)
if coin:
    print(f"{coin}: Heads")
else:
    print(f"{coin}: Tails")