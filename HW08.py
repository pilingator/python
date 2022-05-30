# 3.	В заданном списке вещественных чисел найдите разницу между максимальным и минимальным значением 
# дробной части элементов. Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import math
lst = [1.1, 1.2, 3.1, 5.15, 10.01] 
result = []
mapped_lst = list(map(lambda x: math.floor(x), lst)) # Выделение целочисленной части из списка

for i in range(0, len(lst)): # Разность исходного списка и целочисленного 
    result.append(lst[i] - mapped_lst[i])

round_lst = list(map(lambda x: round(x, 2), result)) # Округление списка до десятых 
difference = max(round_lst) - min(round_lst) # Разность максимального и минимального 
print(difference)