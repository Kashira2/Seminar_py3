######################################  кортеж .  неизменяемый список. (можем только прочесть)

# my_list = [23, 424, 241, 12]
# my_tuple = tuple(my_list)

# print(my_tuple)


####################################        функция возвращает а и в не кортежем

# def func():
#     a = 5
#     b = 6
#     return a, b

# result1, result2 = func()

# print(result1)
# print(result2)

################################        функция возвращает а и в  кортежем

# def func():
#     a = 5
#     b = 6
#     return a, b

# result = func()

# print(result)

####################################################################

# def func():
#     a = 5
#     b = 6
#     c = 7
#     return a, b, c

# result1, _,result2 = func()      # черточка пропускает элемент (обозначение ненужной переменной)
# result1, *result2 = func()      # result2 = все значения между result1 и result2

# print(result1)
# print(result2)

#######################################################    множества

# my_set = {234, 214, 124, 43525, 2525, 122, 12}

# print(my_set)                # рандомно выдает значения

# my_set.add(67)   # добавляет число

# print(my_set)

# # дубликатов быть во множестве не может
# my_list = {23, 23, 23, 43525, 2525, 122, 12}

# print(set(my_list))  
# #  перевод из листа в множества так, что он не повторил дубликаты

# ###########################################################             словарииииииии


my_dict = {4: 'sfgf', 6: 'sfgf', 'two' : 'двойка', (1,2,3): 'здесь у нас кортеж', True: 'правда'}

# print(my_dict[4])
# print(my_dict.get(5)) # если значения нет, то выдаст None и программа не сломается
# print(my_dict.get(5), 'Ничего нет') # если значения нет, то выдаст то, что написал, а если есть то выдаст то, что есть

# my_dict[5] = 'это пять'         # добавили значение в словарь

# for

# for i in my_dict:          # ключи вернет
#     print(i)

# for i in my_dict.keys():    # ключи вернет
#     print(i)

# for i in my_dict.values():    # значения вернет
#     print(i)

# for i in my_dict.items():    # все вернет
#     print(i)

# for k, v in my_dict.items():    # все вернет
#     print(k, v)

###############################################################  файлыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыы


# file = open('text.txt', 'w')   # создает файл и перезаписывает туда, даже если файл такой уже был
# file = open('text.txt', 'w', encoding='UTF-8')        #  чтобы работать с кириллицей

# file.write('Записать эту строку')
# file.close()                 # обязательно закрыть


# file = open('text.txt', 'r', encoding='UTF-8')        #  читать файл

# file.read()
# file.readline()        # прочитает одну строку
# data = file.readlines()        # каждую строку засунет в список

# file.close()                 # обязательно закрыть

# print(data)

# file = open('text.txt', 'a', encoding='UTF-8')         # дописывает файл
# file.write('\nеще однаа строка')

# file.close()

# with open('text.txt', 'a', encoding='UTF-8')  as data:        # работать без close
#     data.write('dsadad')