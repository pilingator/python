#Пользователь задаёт две строки. Определить количество вхождений одной строки в другой.

a = input('Введите исходную строку строку')
b = input('Введите строку для поиска строку')
count = a.count(b)
print(f'Количество вхождений строки {b} в строку {a} => {count} раз')