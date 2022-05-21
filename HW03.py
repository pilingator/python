#Подсчитать сумму цифр в вещественном числе.

N = str(input('Введите число N =>)'))
N = N.replace('.','') 
N = N.replace(',','')
lst_str = list(N)
lst_num = map(int, lst_str)
result = sum(lst_num)
print(result)