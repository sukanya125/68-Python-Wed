inchar = input("Input one character: ")
if inchar >= 'A' and inchar <= 'Z':
    print("You in input Upper Case Letter." , inchar)
elif inchar >= 'a' and inchar <= 'z':
    print("You in input Lower Case Letter." , inchar)
elif inchar >= '0' and inchar <= '9':
    print("You in put Number", inchar)
else:
    print("It's not a letter or number." , inchar)
