with open("employees.txt", "r") as emp_file:
    for line in emp_file:
        amount = float(line.strip())
        print(f"Sales amount: ${amount:.2f}")
