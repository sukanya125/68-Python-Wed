def main():
    input_file = open("philosophers.txt", "r")
    contents = input_file.read()
    print(contents)
    input_file.close()

main()