def prime(n):
    d = 2
    while n % d != 0:
        d = d + 1
    return d == n
try:
    i = int(input('Введите число: '))
    if i > 1:
        print(prime(i))
except ValueError:
    print('ошибка')