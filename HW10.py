# Вычислить число Пи c заданной точностью d. Пример: при d = 0.001,  c= 3.141. 
import math
number = float(input("Задайте точность вычисления числа Пи: "))
x = len(str(abs(number)).replace(".", " ")) # Преобразование в строку и удаление точки
print(round(math.pi, x-2)) # При округлении вычитаю 2 чтобы не брать во внимание целую часть и точку