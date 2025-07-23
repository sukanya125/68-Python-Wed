import random

HEADS = 1
TAILS = 2
TOSSES = 10

def toss_coin():
    for toss in range(TOSSES):
        if random.randint(HEADS, TAILS) == HEADS:
            print("Heads")
        else:
            print("Tails")
toss_coin()