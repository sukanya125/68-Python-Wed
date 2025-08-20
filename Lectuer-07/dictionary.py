student= {'name': 'Alice', 'age': 25, 'grade': 'A', 'major': 'Computer Science'}

print(student.keys())

print(student.values())

print(student.items())

print(student.get('name'))
print(student.get('grade', 'Not Found'))  # Default value if key not found

major = student.pop('major')
print(major)
print(student)

last_item = student.popitem()
print(last_item)
print(student)

student.clear()
print(student)