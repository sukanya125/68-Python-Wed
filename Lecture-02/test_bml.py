weight = input('Enter your weight in kilograms: ')
height = input('Enter your height in meters: ')


weight = float(weight)
height = float(height)

bmi = weight / (height * height)  
print(f'Your BMI is {bmi:.2f}')
