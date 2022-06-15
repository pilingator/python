# 1. Напишите программу, удаляющую из текста все слова содержащие "абв", которое регистронезависимо. 
# Используйте знания с последней лекции. Выполните ее в виде функции. 
# Пример: «абвгдеж рабав копыто фабв Абкн абрыволк аБволк»

# Способ 1 (не через функцию, минус в преобразвании строки в строчную)
line = 'абвгдеж рабав копыто фабв Абкн абрыволк аБволк АБВваывафыв Абвавпвав аБвцййцу абВвыаыва АБвчясяч аБВячсяч АбВячс'
line = line.lower()
words = line.split(' ') 
fragment = 'абв'
new_words = []
for word in words:
    if fragment not in word:
        new_words.append(word)
print(new_words)

# Способ 2 (через функцию)
line = 'абвгдеж рабав копыто фабв Абкн абрыволк аБволк АБВваывафыв Абвавпвав аБвцййцу абВвыаыва АБвчясяч аБВячсяч АбВячс'.split()
fragment = 'абв'
def del_word(line,fragment):
    new_words = [word for word in line if fragment not in word.casefold()]
    new_text = ' '.join(new_words)
    return(new_text)
print(del_word(line,fragment))