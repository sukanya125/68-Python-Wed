max = 5 
total = 0.0 
print('This program calculates the sum of')
print(max, 'numbers you will enter')
for count in range(max):
    number = int(input('Enter a number : '))
    total += number
print('The totle is:', total)