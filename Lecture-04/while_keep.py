keep_going = 'y'
while keep_going == 'y':
    sales = float(input("Enter the sales amount: "))
    comm_rate = float(input("Enter the commission rate:"))
    commission = sales * comm_rate 
    print(f"The commission is ${commission:.2f}")
    keep_going = input('Do you want to calculate another commission ? (Y/N)' )