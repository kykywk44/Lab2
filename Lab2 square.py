def square(number):
    number = number ** 2
    return number

try:
    number = int(input('Введите число: '))
    print(square(number))
except ValueError:
    print('число, не буквы!')