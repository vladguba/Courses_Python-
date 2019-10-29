animals = {'a': 'aardvark', 'b': 'baboon', 'c': 'coati'}
print(animals)

animals['d'] = 'hiena'
print(animals)

print(len(animals))

if ('e') in animals:
    print('Є елемент з ключем e')
else:
    print("Немає елемента з ключем e")

if ('c') in animals:
    print('Є елемент з ключем c')
else:
    print("Немає елемента з ключем c")

for k, v in animals.items():
    print(k, v)