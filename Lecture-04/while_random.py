import random
print("Random numbers between 1 and 100:")
mynumber = random.randint(1, 100)
ntries = 1
yourguess = -1
while ntries < 7 and yourguess != mynumber:
    yourguess = int(input("Enter your guess: "))
    if yourguess < mynumber:
        print("Too low!")
    elif yourguess > mynumber:
        print("Too high!")
    ntries += 1