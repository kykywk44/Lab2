def max_of_two(x,y):
    a = []
    a.append(x)
    a.append(y)
    return max(a)

try:
    n1 = int(input('Введите 1-ое число: '))
    n2 = int(input('Введите 2-ое число: '))
    print(max_of_two(n1,n2))
except:
    print('числа, не буквы!')