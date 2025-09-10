try:
    Value = int(input("Enter a number: "))
    result = 10 / Value
except ZeroDivisionError:
    print("Cannot a division by zero error.")
else:
    print("The result is:", result)

print("The End")