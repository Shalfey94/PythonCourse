# Дана последовательность из N целых чисел и число K. 
# Необходимо сдвинуть всю последовательность (сдвиг - циклический)
# на K элементов вправо, K – положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]

n = int(input('N-->'))
k = int(input('k-->'))
list = [i for i in range(1, n + 1)]
step = k % n
while step > 0:
    list.insert(0, list.pop(-1))
    step -= 1

print(list)


