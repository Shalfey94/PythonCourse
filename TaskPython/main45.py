# Два различных натуральных числа n и m называются дружественными,
# если сумма делителей числа n (включая 1, но исключая само n)
# равна числу m и наоборот. Например, 220 и 284 – дружественные числа.
# По данному числу k выведите все пары дружественных чисел,
# каждое из которых не превосходит k.
# Программа получает на вход одно натуральное число k, не превосходящее 105.
# Программа должна вывести все пары дружественных чисел,
# каждое из которых не превосходит k. Пары необходимо выводить по одной в строке,
# разделяя пробелами. Каждая пара должна быть выведена только один раз
# (перестановка чисел новую пару не дает).
# Ввод: Вывод:
# 300 220 284
import datetime
a = datetime.datetime.now()
def sum_div(num):
    sum = 1
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            sum += i
    return sum

k = int(input('Введите k: '))
res = dict()
for i in range(2, k):
    j = sum_div(i)
    if i < j < k and sum_div(j) == i: 
        res[i] = j
print(res)
print(datetime.datetime.now() -a)