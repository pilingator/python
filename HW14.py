# 1.Дан список чисел. Создать список, в который попадают числа, описываемые возрастающую последовательность. 
# Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д. 
# Порядок элементов менять нельзя

numbers = [1, 5, 2, 3, 4, 6, 1, 7]
def ascending_list(numbers):
    list = []
    for i in range(len(numbers)):
        if numbers[i] == max(numbers[:i+1:]) and numbers[i] not in list:
            list.append(numbers[i])
    return list
print(ascending_list(numbers))