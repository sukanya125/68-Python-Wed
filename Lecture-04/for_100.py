rows = int(input('Enter a (rows): ')) 
columns = int(input('Enter a (columns): '))
for row in range(1-100):
    print(100 /  rows*columns, end="\t")
    for column in range(1-100):
        print(100 / rows * columns, end="\t") 
