# Напишите программу, которая принимает на вхд строку, 
# и отслеживает, сколько раз каждый символ уже встречался. 
# Количество повторов добавляется к символам с помощью постфикса формата _n.
# a a a b c a a d c d d
# a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
a = 'a a a b c a a d c d d'
list_a = a.split()
dic = {}
for i in list_a:
    if i not in dic:
        dic[i] = 0
        print(i, end=' ')
    elif i in dic:
        dic[i] += 1
        print(f'{i}_{dic[i]}', end=' ')
         