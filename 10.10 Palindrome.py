x = input("Введіть паліндром>>> ")
x_first = x[0::1]
x_last = x[::-1]
if x_first == x_last:
    print("Слово є паліндромом")
else:
    print("Слово не є паліндромом")