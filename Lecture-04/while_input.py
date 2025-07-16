score = int(input("Enter your score :"))
while score < 0 or score > 100:
    print("ERROR: Score cannot be negative ")
    print("or greter than 100.")
    score = int(input("Enter your score :"))