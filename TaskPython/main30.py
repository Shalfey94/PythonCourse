# Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

def fill_list_ar(first_el, step, size):
    list_ar = []
    for i in range(size):
        list_ar.append(first_el + i * step)
    return list_ar


a = int(input('Введите первый эл-нт: '))
s = int(input('Введите шаг: '))
n = int(input('Введите кол-во эл-тов: '))
print(fill_list_ar(a, s, n))
