# За день машина проезжает n километровю
# Сколько дней нужно, чтобы проехать маршрут длиной m километров?
# При решении этой задачи нельзя пользоваться условной инструкцией if и циклами.
# Input: n = 700; m = 750 Output: 2

import math
n = int(input('Введите сколько машина проезжает за день: '))
m = int(input('Введите сколько машине нужно проехать: '))
c = math.ceil(m / n)
print(f'Дней необходимое для преодоления маршрута: {c}')
