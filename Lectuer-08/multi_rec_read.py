import struct

with open("records.bin", "rb") as file:
    record_size = struct.calcsize('i20sif')
    while True:
        bytes_data = file.read(record_size)
        if not bytes_data:
            break
        id, name, age, gpa = struct.unpack('i20sif', bytes_data)
        name = name.decode().rstrip('\x00')
        print(f"ID: {id}, Name: {name}, Age: {age}, GPA: {gpa}")