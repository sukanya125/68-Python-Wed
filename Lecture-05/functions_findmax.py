def find_max(*arges):
    if not arges:
        return None
    max_value = arges[0]
    for number in arges:
        if number > max_value:
            max_value = number
    return max_value

result = find_max(3, 6, 8, 9, 2)
print(f"The maximum value is: {result}")