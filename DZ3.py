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

# Вычислить число Пи c заданной точностью d. Пример: при d = 0.001,  c= 3.141. 
import math
number = float(input("Задайте точность вычисления числа Пи: "))
x = len(str(abs(number)).replace(".", " ")) # Преобразование в строку и удаление точки
print(round(math.pi, x-2)) # При округлении вычитаю 2 чтобы не брать во внимание целую часть и точку

# Составить список простых множителей натурального числа N

N=int(input("Введите натуральное число N: "))

i = 2 
factors = []
while i * i <= N: 
    while (N % i == 0):
        factors.append(i)
        N = N / i
    i = i + 1
if N > 1: 
    factors.append(N)

print(factors)

# Дана последовательность чисел. Получить список неповторяющихся элементов исходной последовательности
# Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [1, 2, 3, 5, 10]

list1 = [1, 2, 3, 5, 1, 5, 3, 10]
list2 = list(set(list1))
print(list2)

# Дан текстовый файл, содержащий целые числа. Удалить из него все четные числа.
import random

with open('example.txt','w') as f:
    for i in range(20):
        number = random.randint(0, 101)
        f.write(str(number))
        f.write("\n")
        print(number)
with open('example.txt','r') as f2:
    arr = []
    i = 0
    n = f2.readline()
    s = int(n)
    for i in f2:
        if int(i) % 2 != 0:
            arr.append(int(i))
print(arr)
with open('example.txt','a') as f:
    f.write(str(arr))
    f.write("\n")