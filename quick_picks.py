import random

CONSTANTS = []

quick_picks = int(input("How many quick picks? "))

for i in range(quick_picks + 1):
    for j in range(quick_picks + 1):
        print(f"{random.randrange(1, 46): >2}", end=' ')
    print()
