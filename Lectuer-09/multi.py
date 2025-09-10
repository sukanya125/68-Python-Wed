try:
    Value = int(input("Enter a number: "))
    result = 10 / Value
    
except ValueError:
    print("Error: Invalid input. Please enter a valid integer.")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")


print("The End")