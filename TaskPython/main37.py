# Дано натуральное число N и последовательность из N элементов.
# Требуется вывести эту последовательность в обратном порядке.
# Примечание. В программе запрещается объявлять массивы и
# использовать циклы (даже для ввода и вывода).

# Input: 2 -> 3 4
# Output: 4 3

def rev(num):
    el = input('введите эл-нт: ')
    if num == 1:
        return el
    return rev(num - 1)+ ' ' + el

n = int(input('введите N: '))
print(rev(n))