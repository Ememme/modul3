import random

number = random.randint(0, 50)

print('Wylosowana liczba to', number)
# List / array
array = [1, 2, 'Ala']

print(array[0])
print(array[2])
print('This string contains a single quote (\') character.')
print('This string contains a double quote ("podwojny cudzyslow") character.')

# Dictionary/ Słownik
MLB_team = {
    'Colorado': 'Rockies',
    'Boston': 'Red Sox',
    'Minnesota': 'Twins',
    'Milwaukee': 'Brewers',
    'Seattle': 'Mariners'
}


print(MLB_team['Colorado'])
