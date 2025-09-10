try:
    Value = int(input("Enter a number: "))
    result = 10 / Value
    
except ValueError:
    print("Invalid input. Please enter a valid integer.")
except ZeroDivisionError:
    print("Caught a division by zero error.")


print("The End")