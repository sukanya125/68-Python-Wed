import struct

num_records = int(input("How number number of records: "))

with open("records.bin", "wb") as file:
    for _ in range(num_records):
        id = int(input("Enter ID: "))
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        gpa = float(input("Enter GPA: "))

        data = struct.pack('i20sif', id, name.encode(), age, gpa)
        file.write(data)