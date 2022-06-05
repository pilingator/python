#Задача: найти триплеты и просто выводить их на экран. Триплетом называются три числа, которые в сумме дают 0.
# (решение будет долгим, ибо является демонстрационным при теме многопоточного программирования).

with open('1Kints.txt','r') as file:
    arr = []
    i = 0
    n = file.readline()
    s = int(n)
    for i in file:
        arr.append(int(i))

def findTriplets(arr, n):
 
    for i in range(0, n-2): 
     
        for j in range(i+1, n-1):
         
            for k in range(j+1, n):
             
                if (arr[i] + arr[j] + arr[k] == 0):
                    print(arr[i], arr[j], arr[k])

n = len(arr)
findTriplets(arr, n)
 