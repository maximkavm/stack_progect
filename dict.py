# Словарь - dictionary

engDict = dict()
engDict = {'Яблоко': 'Apple','Апельсин': 'Orange'}
print(*engDict.items())
for key, val in engDict.items():
    print(f'{key} - {val}')
