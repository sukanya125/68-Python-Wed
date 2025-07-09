score1 = float(input("Enter score 1: "))
score2 = float(input("Enter score 2: "))
score3 = float(input("Enter score 3: "))
average = (score1 + score2 + score3) / 3
print(f"The average score is {average:.2f}")
if average > 95:
    print("Congratulations!")
    print("That is a great average")
