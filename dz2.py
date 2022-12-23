# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

from random import randint as RI

num1 = int(input('Задайте размер списка: '))
my_array = []

for i in range(num1):
    my_array.append(RI(0,10))
print(my_array)

product = int(1)
product_array = []
if len(my_array) % 2 == 0:
    for i in range(num1//2):
        product = my_array[i] * my_array[len(my_array)-i-1]
        product_array.append(product)
else:
    for i in range(num1//2+1):
        product = my_array[i] * my_array[len(my_array)-i-1]
        product_array.append(product)

print(product_array)
