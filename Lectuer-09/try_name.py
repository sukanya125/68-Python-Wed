filename = input("Enter file name: ")
try:
    infile = open(filename, 'r')
    contents = infile.read()
    print(contents)
    infile.close()
except IOError:
    print('an erroe occurred trying to read the file:', filename)
    print("the file:", filename)

print("The End")
   