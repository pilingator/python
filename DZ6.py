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

#3 -  ROT13 - это простой шифр подстановки букв, который заменяет букву буквой, которая идет через 13 букв 
# после нее в алфавите. ROT13 является примером шифра Цезаря.Создайте функцию, которая принимает строку и 
# возвращает строку, зашифрованную с помощью Rot13 . Если в строку включены числа или специальные символы, 
# они должны быть возвращены как есть. Также создайте функцию, которая расшифровывает эту строку обратно 
# (некий начальный аналог шифрования сообщений). Не использовать функцию encode.

text = input('Введите текст: ')
key = 13
 
alphabet = "абвгдеёжзийклмнопзстуфхцчшщъыьэюяАБВГДЕЁЖЗИКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

res = ""
res2 = ""

def encode(text, res):
  
  for char in text:
      if char in alphabet:
          res = res + chr(ord(char)+13)
      else:
          res = res + char
  print(res)
  
def decode(res, res2):
  for char in res:
      if char in alphabet:
          res2 = res2 + chr(ord(char)-13)
      else:
          res2 = res2 + char
  print(res2)

encode(text, res)
decode(res, res2)