print('hello world')
value = None
print(type(value))

a = 123
b = 1.23
print(type(a))
print(type(b))
value = 12345
print(type(value))

s = 'hello world'

print(s)
print(a,'-',b,'-',s)
print('{1} - {2} - {0}'.format(a, b, s))
print(f'{a} - {b} - {s}')

#f = False
#print(f)
#list = [1, 2, 3]
#col = ['hello', 1,2,4.5,True]
#print(list)
#print(col)

#print('Введите а');
#a = int(input())
#print('Введите b');
#b = int(input())
#print(a, ' + ', b, ' = ', a+b)
#print('{} -- {}'.fotmat(a, b))

a = 1.312333788
b = 3 
c = round(a * b, 7)
print(c)

a = 3 
a += 5
print(a)

c = 1 < 3 < 5 < 10
print(c)

f = 1 > 2 or 4 < 6
print(f)

f = [1,2,3,4]
print(5 in f)

is_odd = f[0] % 2 == 0
print(is_odd)

#a = int(input('a = '))
#b = int(input('b = '))
#if a > b:
#    print(a)
#else:
 #   print(b)

#username = input('Введите имя: ')
#if username == 'Маша':
#    print('Ура, это же МАША!')
#elif username == 'Марина':
#    print('Я так ждала Вас, Марина!')
#elif username == 'Ильнар':
#    print('Ильнар - топ)')
#else:
#    print('Привет, ', username)

#original = 23
#inverted = 0
#while original != 0:
#    inverted = inverted * 10 + (original % 10)
#    original //= 10
#    print(original)
#else:
#    print('Пожалуй')
#    print('хватит )')
#print(inverted)
# Пожалуй
# хватит )
# 32
list = range(10)
for i in list:
    print(i**2)

    text = 'съешь ещё этих мягких французских булок'
print(text[0]) # c
print(text[1]) # ъ
print(text[len(text)-1]) # к
print(text[-5]) # б
print(text[:]) # print(text)
print(text[:2]) # съ
print(text[len(text)-2:]) # ок
print(text[2:9]) # ешь ещё
print(text[6:-18]) # ещё этих мягких
print(text[0:len(text):6]) # сеикакл
print(text[::6]) # сеикакл
text = text[2:9] + text[-5] + text[:2] # ...