num_emps = int(input("How many employees do you want to save records?: "))
with open("employees.txt", "w") as emp_file:
    for count in range(1, num_emps + 1):
        print('Enter data for employee', count, sep='')
        name = input(f"Enter the name of employee {count}: ")
        id_num = input(f"Enter the ID number of employee {count}: ")
        dept = input(f"Enter the department of employee {count}: ")
        
        emp_file.write(name + "\n")
        emp_file.write(id_num + "\n")
        emp_file.write(dept + "\n")
        print()

print("Employee records saved to employees.txt")