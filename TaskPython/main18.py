# Требуется найти в массиве A[1..N] 
# самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число 
# N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. 
# Последняя строка содержит число X

# 5
# 1 2 3 4 5
# 6
# -> 5

n = int(input('Введите кол-во эл-ов в массиве: '))
list_a = [int(input(f'Введите элемент [{i}]:')) for i in range(n)]
x = int(input('Введите число X: '))
dif = abs(list_a[0] - x)
result = list_a[0]
for i in range(1, n):
    if dif > abs(list_a[i] - x):
        dif = abs(list_a[i] - x)
        result = list_a[i]
print(result)

