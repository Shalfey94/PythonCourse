# Уставшие от необычно теплой зимы, жители решили узнать, 
# действительно ли это самая длинная оттепель за всю историю наблюдений за погодой. 
# Они обратились к синоптикам, а те, в свою очередь, занялись исследованиями статистики за прошлые годы. 
# Их интересует, сколько дней длилась самая длинная оттепель. 
# Оттепелью они называют период, в который среднесуточная температура ежедневно превышала 0 градусов Цельсия. 
# Напишите программу, помогающую синоптикам в работе.
# Пользователь вводит число N – общее количество рассматриваемых дней (1 ≤ N ≤ 100). 
# В следующих строках располагается N целых чисел.
# Каждое число – среднесуточная температура в соответствующий день. 
# Температуры – целые числа и лежат в диапазоне от –50 до 50
# Input: 6 -> -20 30 -40 50 10 -10
# Output: 2

# num_days = int(input('Num days--> '))
# days_list = []
# for i in range(num_days):
#     day = int(input('day--> '))
#     days_list.append(day)
# max_len = 0
# temp_count = 0
# for temp in days_list:
#     if temp > 0:
#         temp_count += 1
#     else:
#         temp_count = 0
#     if temp_count > max_len:
#         max_len = temp_count
# print(max_len)

max_len = temp_count = 0
num_days = int(input('Num days--> '))
for i in range(1, num_days + 1):
    temp = int(input(f'day {i}--> '))
    if temp > 0:
        temp_count += 1
    else:
        temp_count = 0
    if temp_count > max_len:
        max_len = temp_count
print(max_len)