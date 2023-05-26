# 17. Дан список чисел. Определите, сколько в нем встречается различных чисел.

# n = int(input('Введите кол-во элементов: '))
# list_1 = []
# for _ in range(n):
#     list_1.append(int(input('Введите значения: ')))
# print(list_1)

# list_2 = []

# for elem in list_1:
#     if elem not in list_2:
#         list_2.append(elem)

# print(len(list_2))

# 19. Дана последовательность из N целых чисел и число K. Необходимо сдвинуть 
# всю последовательность (сдвиг - циклический) на K элементов вправо,
# K – положительное число.

# Var1.
# n = int(input('Введите кол-во элементов списка: '))
# k = int(input('Введите кол-во сдвигов: '))
# some_list = []
# some_list_2 = []
# for _ in range(n):
#     some_list.append(int(input('Введите элементы списка: ')))
# for _ in range(k-1):
#     some_list.insert(0, some_list[-1])
#     some_list.pop(-1)
# print(some_list)

# Var2.
# n = int(input('Введите кол-во элементов: '))
# list_1 = []
# for _ in range(n):
#     list_1.append(int(input('Введите значения: ')))
# print(list_1)

# k = int(input('Введите число K: '))

# for i in range(k-1):
#     list_1.insert(0,list_1[-1])
#     list_1.pop(-1)
# print(list_1)

# 23. Дан массив, состоящий из целых чисел. Напишите программу, 
# которая подсчитает количество элементов массива, больших предыдущего
# (элемента с предыдущим номером)


# n = int(input('Введите кол-во элементов: '))
# list_1 = []
# for _ in range(n):
#     list_1.append(int(input('Введите значения: ')))
# print(list_1)

# count = 0
# for i in range(1, len(list_1)):
#     if list_1[i] > list_1[i - 1]:
#         count += 1
# print(count)

# # 1.Создайте список из случайных чисел. 
# # Найдите номер его последнего локального максимума 
# # (локальный максимум — это элемент, который больше любого из своих соседей).

# n = int(input('Введите кол-во элементов: '))
# list_1 = []
# for _ in range(n):
#     list_1.append(int(input('Введите значения: ')))
# print(list_1)

# indexMax = 0
# for i in range(1, len(list_1) -1):
#     if list_1[i] > list_1[i - 1] and list_1[i] > list_1[i + 1]:
#         indexMax = list_1[i]
# print(indexMax)
# # print(i)

