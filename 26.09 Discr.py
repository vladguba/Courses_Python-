#5 * x * x + 10 * x + 7 = 0
a = 5
b = + 10
c = + 7
D = b * b - 4 * a * c
print(D)

if D > 0:
    x_1 = (- b + D ** 0.5) / 2 * a
    x_2 = (- b - D ** 0.5) /2 * a
    print(x_1, x_2)
elif D == 0:
    x = - b / 2 * a
    print(x)
elif D < 0:
    print("Коренів немає.")
