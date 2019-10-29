names = ["Vova", "Valja", "Petro", "Ivan"]
years = [1990, 2000, 1995, 2002]
dictionary = dict(zip(names, years))
print(dictionary)

for key in sorted(dictionary):
    print(key, dictionary[key])

print(sorted(dictionary.values()))