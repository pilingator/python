# 1.Дан список чисел. Создать список, в который попадают числа, описываемые возрастающую последовательность. 
# Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д. 
# Порядок элементов менять нельзя

numbers = [1, 5, 2, 3, 4, 6, 1, 7]
def ascending_list(numbers):
    list = []
    for i in range(len(numbers)):
        if numbers[i] == max(numbers[:i+1:]) and numbers[i] not in list:
            list.append(numbers[i])
    return list
print(ascending_list(numbers))

#2.	Создать и заполнить файл случайными целыми значениями. Выполнить сортировку содержимого файла по 
# возрастанию. 
import random

with open('example2.txt','w') as f:
    for i in range(20):
        number = random.randint(0, 101)
        f.write(str(number))
        f.write("\n")
with open('example2.txt','r') as f2:
    arr = []
    i = 0
    n = f2.readline()
    s = int(n)
    for i in f2:
        arr.append(int(i))
    print(arr)
    arr = sorted(arr)
print(arr)        

# 3. Задача: найти триплеты и просто выводить их на экран. Триплетом называются три числа, которые в сумме дают 0.
# (решение будет долгим, ибо является демонстрационным при теме многопоточного программирования).

with open('1Kints.txt','r') as file:
    arr = []
    i = 0
    n = file.readline()
    s = int(n)
    for i in file:
        arr.append(int(i))

def findTriplets(arr, n):
 
    for i in range(0, n-2): 
     
        for j in range(i+1, n-1):
         
            for k in range(j+1, n):
             
                if (arr[i] + arr[j] + arr[k] == 0):
                    print(arr[i], arr[j], arr[k])

n = len(arr)
findTriplets(arr, n)