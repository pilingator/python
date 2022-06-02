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
