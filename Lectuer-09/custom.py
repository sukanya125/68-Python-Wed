class NegatieveValueError(Exception):
    def __init__(self, value):
        self.value = value
        super().__init__(f"Negative value error: {value}")

def check_positive(num):
    if num < 0:
        raise NegatieveValueError(num)
    else:
        print(f"{num} is a positive number.")

try:
    number = int(input("Enter a positive number: "))
    check_positive(number)
except NegatieveValueError as e:
    print(e)
except ValueError:
    print("Error: Invalid input. Please enter a valid integer.")

finally:
    print("Execution completed.")

print("The End")
   