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