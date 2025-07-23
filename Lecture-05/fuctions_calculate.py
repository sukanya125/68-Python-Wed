def calculate_stats(numbers):
    total_sum = sum(numbers)
    average = total_sum / len(numbers)
    maximum = max(numbers)
    minimum = min(numbers)
    return total_sum, average, maximum , minimum

numbers = [5, 10, 15, 20, 25]
total, avg, maximum,minimum= calculate_stats(numbers)

print(f"Total Sum: {total}")
print(f"Average: {avg}")
print(f"Maximum Value: {maximum}")
print(f"Minimum Value: {minimum}")

