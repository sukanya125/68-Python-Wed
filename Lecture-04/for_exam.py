print('Mph\tKph')
print('-----------------')
for mph in range(50, 131):
    kph = mph / 0.6214
    print(f'{mph}\t{kph:.2f}')
