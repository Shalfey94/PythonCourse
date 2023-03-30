# Даны два массива чисел. 
# Требуется вывести те элементы первого массива 
# (в том порядке, в каком они идут в первом массиве), 
# которых нет во втором массиве. 
# Пользователь вводит число N - количество элементов в первом массиве, 
# затем N чисел - элементы массива. 
# Затем число M - количество элементов во втором массиве. 
# Затем элементы второго массива
# Ввод: Вывод:
# 7 3 3 2 12
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1

def fill_arr(size):
    list = []
    list = [int(input('Введите эл-нт мн-ва n: ')) for i in range(size)]
    return list

def dif_list(list_a, list_b):
    list_d = []
    for i in range(len(list_a)):
        if list_a[i] not in list_b:
            list_d.append(list_a[i])
    return list_d


n = int(input('Введите n: '))
list_n = fill_arr(n)
print(list_n)
m = int(input('Введите m: '))
list_m = fill_arr(m)
print(list_m)
list_n_dif_m = dif_list(list_n, list_m)
print(list_n_dif_m)
