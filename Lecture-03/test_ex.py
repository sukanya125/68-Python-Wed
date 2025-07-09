hours_worked = int(input("Enter the number of hours worked: "))
hourly_rate = float(input("Enter the hourly rate: "))
if hours_worked <= 40:
    gross_pay = hours_worked * hourly_rate
    print(f"Gross pay: ${gross_pay:}")
else:
    overtime_hours = hours_worked - 40
    pay = (40 * hourly_rate) + (overtime_hours *  1.5)
    print(f"pay: ${pay:.2f}")