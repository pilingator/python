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