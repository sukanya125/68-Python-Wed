try:
    numerator = float(input("Enter a numerator: "))
    denominator = float(input("Enter a denominator: "))

    result = numerator / denominator
    print("The result is:", result)

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

except ValueError:
    print("Invalid input. Please enter numeric values.")

finally:
    print("Execution completed.")

print("The End")