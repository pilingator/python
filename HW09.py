# Найти НОК двух чисел

def calc_NOD(num1, num2):
    if num1 > num2:
        smaller = num2
    else:
        smaller = num1 
    for i in range(1, smaller + 1):
        if((num1 % i == 0) and (num2 % i == 0)):
            result = i
    return result

num1 = int(input('Введите первое число: '))
num2 = int(input('Введите второе число: '))
print(f'Наименьшее общее кратное числа {num1} и {num2} число', calc_NOD(num1, num2))