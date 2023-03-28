# Хакер Василий получил доступ к классному журналу 
# и хочет заменить все свои минимальные оценки на максимальные. 
# Напишите программу, которая заменяет оценки Василия, но наоборот: 
# все максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

def change_item(list):
    my_max = max(list)
    my_min = min(list)
    for i in range(len(list)):
        if list[i] == my_max:
            list[i] = my_min
    return list

n = int(input('введите кол-во оценок: '))
list_n = [int(input('введите оценку: ')) for i in range(n)]
print(change_item(list_n))