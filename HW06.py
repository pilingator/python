# 4. Написать программу преобразования десятичного числа в двоичное

N = int(input('Введите число N '))
answer = ' '
while N > 0:
    answer = str(N % 2) + answer 
    N = N // 2
        
print(answer)