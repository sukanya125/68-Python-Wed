input_string = input("Enter a string: ")
modified_sting = ""
vowels = "aeiouAEIOU"
for char in input_string:
    upper_char = char.upper()
    if upper_char in vowels:
        modified_sting += "*"
    else:
        modified_sting += upper_char
print("Modified string:", modified_sting)