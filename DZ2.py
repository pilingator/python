# 1. Найти сумму чисел списка стоящих на нечетной позиции

list = [1, 9, 7, 8, 4, 2, 1, 3, 7, 4]
sum = 0
for i in range(0, len(list), 2):
    sum += list[i]
    
print(f'Сумма чисел нечетных позиций: {sum}')

#2.	Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и 
# предпоследний и т.д. Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15] 
import math
list = [1, 2, 3, 4, 5, 6, 7] 
result = []
length = math.ceil(len(list)/2) # Половина длины списка, округленная в большую сторону
for i in range(0, length):
    result.append(list[i]*list[-1*i-1])
print(result)

# 3.	В заданном списке вещественных чисел найдите разницу между максимальным и минимальным значением 
# дробной части элементов. Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import math
lst = [1.1, 1.2, 3.1, 5.15, 10.01] 
result = []
mapped_lst = list(map(lambda x: math.floor(x), lst)) # Выделение целых чисел из списка

for i in range(0, len(lst)): # Разность исходного списка и целочисленного 
    result.append(lst[i] - mapped_lst[i])

round_lst = list(map(lambda x: round(x, 2), result)) # Округление списка до десятых 
difference = max(round_lst) - min(round_lst) # Разность максимального и минимального 
print(difference)

# 4. Написать программу преобразования десятичного числа в двоичное

N = int(input('Введите число N '))
answer = ' '
while N > 0:
    answer = str(N % 2) + answer 
    N = N // 2
        
print(answer)