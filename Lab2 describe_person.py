def describe_person(name, age=30):
    return print('Имя:',name,'''
Возраст:''',age)

try:
    name = input('Укажите ваше имя: ')
    age = int(input('Укажиие возраст(опционально): '))
    if age<0:
        describe_person(name)
    else:
        describe_person(name,age)

except ValueError:
    describe_person(name)