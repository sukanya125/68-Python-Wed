score1 = float(input("Enter score 1: "))
score2 = float(input("Enter score 2: "))
score3 = float(input("Enter score 3: "))

# คำนวณค่าเฉลี่ย
average = (score1 + score2 + score3) / 3

# แสดงผล
print(f"The average score is {average:.2f}")

# เงื่อนไขแสดงข้อความ
if average > 95:
    print("Congratulations!")
