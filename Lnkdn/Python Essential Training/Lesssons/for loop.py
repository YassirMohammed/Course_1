dictionaryOfFamily = {
    'father': ['Nabil'],
    'mother': ['Salwa'],
    'children': ['Yassir', 'Ahmed', 'Israa']
}

for status, name in dictionaryOfFamily.items():
    if len(name) == 1:
        continue
    print(f'The children are {name}')


for status, name in dictionaryOfFamily.items():
    if len(name) > 1:
        print(f'found {len(name)}: {name}')
        break






    
    


