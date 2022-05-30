#Реализовать алгоритм перемешивания списка.
import time
random_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
t = time.time_ns()
tS = int(t)
new_list = []
for i in range(100000):
    t1 = int(str(time.time_ns())[-3])
    temp = random_list.pop(t1//2)
    random_list.append(temp)
print(random_list)