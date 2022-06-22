# 2 - Реализовать RLE алгоритм. реализовать модуль сжатия и восстановления данных. Входные и выходные данные
#  хранятся в отдельных файлах (в одном файлике отрывок из какой-то книги, а втором файлике — сжатая версия 
# этого текста). 

text = input('Введите строку: ')
result =[]
count = 1
for i in range (len(text)):
    if i == len(text)-1:
        result.append(str(count))
        result.append(text[i])
    elif text[i] == text[i+1]:
        count+=1
    else:
        result.append(str(count))
        result.append(text[i])
        count = 1
print(result)