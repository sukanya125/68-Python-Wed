totalseles = 0.0
with open("sales.txt", "r") as sales_file:
    for line in sales_file:
        amount = float(line.strip())
        print(f"Sales amount: ${amount:.2f}")
        totalseles += amount
print(f"Total sales: ${totalseles:.2f}")