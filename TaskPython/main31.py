# Последовательностью Фибоначчи называется последовательность чисел 
# a0, a1, ..., an, ..., где a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 21

def fib(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else: 
        return fib(num - 1) + fib(num - 2)

n = int(input('Введите число: '))
print(fib(n))
