phonebook = {'anirach' : '777-1111', 'Mickey' : '777-2222', 'Donald' : '777-3333'}

print(phonebook)
print(phonebook.get('Mickey'))
print(phonebook['Donald'])

key = 'Pluto'

if key in phonebook:
    print(phonebook['pluto'])
else:
    print(f"{key} not found in phonebook")

phonebook['Simpson'] = '777-4567'
phonebook['Pluto'] = '777-4444'
phonebook['Mickey'] = '777-2122'
print(phonebook)  # Update Mickey's number

del phonebook['Simpson']  # Remove Donald from the phonebook
print(phonebook)