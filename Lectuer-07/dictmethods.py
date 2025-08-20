phonebook ={'Anirach': '777-1111', 'Mickey': '777-2222', 
            'Donald': '777-3333' ,  'Pluto': '777-4444'}

heroesdict = {}
heroesdict['Hulk'] = '888-1111'
heroesdict['Ironman'] = '888-2222'
print(heroesdict.get('Halk', 'Key not found'))  # Accessing value using get method
print(heroesdict.get('Hulk', 'Key not found'))  # Accessing value using get method

for key, value in heroesdict.items():
    print(f"{key}: {value}")  # Iterating through key-value pairs

print(phonebook.keys())  # Display the phonebook
print(phonebook.values())  # Display the phone numbers

print(phonebook.pop('Mick', 'Element not found'))  # Display all items in the phonebook
print(phonebook.pop('Mickey', 'Element not found'))  # Display all items in the phonebook
print(phonebook)
print(phonebook.popitem())  # Remove and return the last item
print(phonebook)
print(phonebook.clear())  # Clear the phonebook
print('After clearing, phonebook is:')
print(phonebook)  # Display the cleared phonebook
