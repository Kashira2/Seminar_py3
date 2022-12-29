# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов, отличной от 0.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random

size = int(input('Задайте размер списка: '))
my_list = []

for i in range(size):
    my_list.append(round(random.uniform(0,10), 4))
print(my_list)
max = int(0)
min = int(500000000)
for i in range(size):
    my_list[i] = str(my_list[i])
    number = my_list[i].split('.')
    number_after_dot = int(number[1])
    if max < number_after_dot:
        max = number_after_dot
    elif min > number_after_dot:
        min = number_after_dot

print(f'Максимальное значение дробной части элементов равно {max}')
print(f'Минимальное значение дробной части элементов равно {min}')
print(f'Разница между максимальным и минимальным значением дробной части элементов равно {max - min}') 