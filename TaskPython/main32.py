# Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

def fill_list(size):
    list = []
    list = [int(input('Введите эл-нт мн-ва n: ')) for i in range(size)]
    return list

def elem_of_range(list, el_min, el_max):
    res = dict()
    for i in range(len(list)):
        if el_min <= list[i] <= el_max:
            res[i] = list[i]
    return res

n = int(input('Введите n: '))
list_n = fill_list(n)
print(list_n)
min_n = int(input('Введите min: '))
max_n = int(input('Введите max: '))
print(elem_of_range(list_n, min_n, max_n))