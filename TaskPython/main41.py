# Дан массив, состоящий из целых чисел.
# Напишите программу, которая в данном массиве определит количество элементов, 
# у которых два соседних и, при этом, оба соседних элемента меньше данного.
# Сначала вводится число N — количество элементов в массиве 
# Далее записаны N чисел — элементы массива. Массив состоит из целых чисел.
# Ввод:          Ввод:
# 5              5
# 1 2 3 4 5      1 5 1 5 1
# Вывод:         Вывод:
# 0              2

def fill_arr(size):
    list = []
    list = [int(input('Введите эл-нт мн-ва n: ')) for i in range(size)]
    return list

def el_high_near(list):
    count = 0
    for i in range(1, len(list) - 1):
        if list[i-1] < list[i] > list[i+1]:
            count += 1
    return count


n = int(input('Введите n: '))
list_n = fill_arr(n)
print(list_n)
print(el_high_near(list_n))