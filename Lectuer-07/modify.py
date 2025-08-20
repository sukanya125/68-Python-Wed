student= {"name": "Alice", "age": 25, "grade": "A", "major": "Computer Science"}

student["age"] = 26
student["major"] = "Computer Science"
print(student)

del student["grade"]
print(student)

removed_value = student.pop("major")
print(f"Removed major: {removed_value}")
print(student)