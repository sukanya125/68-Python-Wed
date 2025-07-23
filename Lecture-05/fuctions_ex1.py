def is_armstrong_number(num):
    """Check if a number is an Armstrong number."""
    string_num = str(num)
    num_digits = len(string_num)
    total = sum(int(digit) ** num_digits for digit in string_num)
    return total == num
print(is_armstrong_number(153))  # True
print(is_armstrong_number(123))  # False    
print(is_armstrong_number(9474))