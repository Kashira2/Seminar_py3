# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на позиции с нечетным индексом.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import randint as RI

num1 = int(input('Задайте размер списка: '))
my_list = []

for i in range(num1):
    my_list.append(RI(0,100))
print(my_list)

sum = int(0)

for i in range(0, num1, 2):
    sum += my_list[i]
print(sum) 