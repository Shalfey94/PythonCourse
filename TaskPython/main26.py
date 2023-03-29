#  Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8

def deg_num(n, m):
    res = 1
    if m == 0:
        return res
    return deg_num(n, m - 1) * n
    

a = int(input('введите a: '))
b = int(input('введите b: '))
print(deg_num(a, b))