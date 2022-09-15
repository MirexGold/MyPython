# from math import sqrt
# a, b = int(input()), int(input())
# print(a + b)  # сумму чисел a и b;
# print(a - b)  # разность чисел a и b;
# print(a * b)  # произведение чисел a и b;
# print(a / b)  # частное чисел a и b;
# print(a // b)  # целую часть от деления числа a на b;
# print(a % b)  # остаток от деления числа a на b;
# print(sqrt(a**10 + b**10))  # корень квадратный из суммы их 10-х степеней: sqrt{a^{10} + b^{10}}

# Индекс массы тела
# def my_imt(m, r):
#     imt = m / (r * r)
#     if 18.5 <= imt <= 25:
#         return "Оптимальная масса"
#     elif imt < 18.5:
#         return "Недостаточная масса"
#     elif imt > 25:
#         return "Избыточная масса"
#
#
# m = float(input())
# r = float(input())
#
# print(my_imt(m, r))


# Стоимость строки
# def coast(text):
#     rub = len(text) * 0.6
#     kop = len(text) * 60 % 100
#     return f'{int(rub)} р. {kop} коп.'
#
# stroka = input()
# print(coast(stroka))


# string = input()
# price = 60 * len(string)
#
# print(f'{price // 100} р. {price % 100} коп.')


##Количество слов
# print(len(list(input().split())))

# Зодиак
# sp = ['Дракон', 'Змея', 'Лошадь', 'Овца', 'Обезьяна', 'Петух', 'Собака', 'Свинья', 'Крыса', 'Бык', 'Тигр', 'Заяц',
#       'Дракон']
# print(sp[(int(input())-8) % 12])
#
#
# # 8,9,10,11,0,1,2,3,4,5,6,7  - %
# #
# # 0,1,2,3,4,5,6,7,8,9,10,11

# Переворот числа
# a = input()
# if len(a) == 5:
#       print(int(a[::-1]))
# elif len(a) == 6:
#       print(int(a[0]+a[-1:0:-1]))


# Standard American Convention
# print(f"{int(input()):,}")


# Задача Иосифа Флавия 🌶️🌶️
# n, k = int(input()), int(input())
# counter = 0
# for i in range(1, n + 1):
#     counter = (counter + k) % i
# print(counter + 1)


# Координатные четверти
# n = int(input())
# counter1 = counter2 = counter3 = counter4 = 0
# for i in range(n):
#     x, y = map(int, input().split())
#     if x > 0 and y > 0:
#         counter1 += 1
#     elif x < 0 and y > 0:
#         counter2 += 1
#     elif x < 0 and y < 0:
#         counter3 += 1
#     elif x > 0 and y < 0:
#         counter4 += 1
# print(f'Первая четверть: {counter1}')
# print(f'Вторая четверть: {counter2}')
# print(f'Третья четверть: {counter3}')
# print(f'Четвертая четверть: {counter4}')

# Больше предыдущего
# s = list(map(int, input().split()))
# counter = 0
# for i in range(len(s)-1):
#     if s[i+1] > s[i]:
#         counter += 1
# print(counter)


# Назад, вперёд и наоборот
# s = input().split()
# for i in range(0, len(s)-1, 2):
#     s[i], s[i+1] = s[i+1], s[i]
# print(*s, end=' ')

# Сдвиг в развитии
# s = input().split()
# s.insert(0, s[-1])
# del s[-1]
# print(*s)

# Различные элементы
# s = input().split()
# s1 = []
# for i in s:
#     if i not in s1:
#         s1.append(i)
# print(len(s1))

# Произведение чисел
# l = [int(input()) for n in range(int(input()))]
# n = int(input())
# fl = False
#
# for i in range(len(l)):
#     for j in range(i + 1, len(l)):
#         if l[i] * l[j] == n:
#             fl = True
#             break
#
# print('ДА' if fl == True else 'НЕТ')

# Камень, ножницы, бумага
# t, r = input(), input()
# if t == r:
#     print('ничья')
# elif t == 'камень' and r == 'ножницы' or t == 'ножницы' and r == 'бумага' or t == 'бумага' and r == 'камень':
#     print('Тимур')
# else:
#     print('Руслан')


# Камень, ножницы, бумага, ящерица, Спок 🌶️
# timur = input()
# ruslan = input()
# result = {'камень': ['ножницы', 'ящерица'],
#           'ножницы': ['бумага', 'ящерица'],
#           'бумага': ['камень', 'Спок'],
#           'Спок': ['ножницы', 'камень'],
#           'ящерица': ['бумага', 'Спок']}
# if timur == ruslan:
#     print('ничья')
# else:
#     if ruslan in result[timur]:
#         print('Тимур')
#     else:
#         print('Руслан')

# Орел и решка
# stroka = input().split('О')
# res = max(stroka, key=len)
# print(len(res))

# Кремниевая долина 🌶️🌶️
# for i in range(int(input())):
#     s, virus, x  = input(), 'anton', 0
#     for sym in s:
#         if sym == virus[x]:
#             x += 1
#         if x == 5:
#             print(i + 1, end=' ')
#             break


# Роскомнадзор запретил букву а 🌶️🌶️
# word = input() + ' запретил букву'
# alpha = [chr(i) for i in range(1072, 1104)]
#
# for letter in alpha:
#     if letter in word:
#         print(word, letter)
#         word = word.replace(letter, '').replace('  ', ' ').strip()

# Предикат делимости
# объявление функции
# def func(num1, num2):
#     if num1 % num2 == 0:
#         return True
#
# # считываем данные
# num1, num2 = int(input()), int(input())
#
# # вызываем функцию
# if func(num1, num2):
#     print('делится')
# else:
#     print('не делится')

'''
метод append() добавляет новый элемент в конец списка.
метод extend() расширяет один список другим списком.
метод insert() вставляет значение в список в заданной позиции.
метод index() возвращает индекс первого элемента, значение которого равняется переданному в метод значению.
метод remove() удаляет первый элемент, значение которого равняется переданному в метод значению.
метод pop() удаляет элемент по указанному индексу и возвращает его.
метод count() возвращает количество элементов в списке, значения которых равны переданному в метод значению.
метод reverse() инвертирует порядок следования значений в списке, то есть меняет его на противоположный.
метод copy() создает поверхностную копию списка.
метод clear() удаляет все элементы из списка.
оператор del позволяет удалять элементы списка по определенному индексу.
Примечание 2. Методы строк, работающие со списками:
метод split() разбивает строку на слова, используя в качестве разделителя последовательность пробельных символов,
символ табуляции (\t) или символ новой строки (\n).
метод join() собирает строку из элементов списка, используя в качестве разделителя строку,
к которой применяется метод.
'''


# list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# list1[2][2].append(7000)
# # print(list1)  #-> [10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]

# list1 = ['a', 'b', ['c', ['d', 'e', ['f', 'g'], 'k'], 'l'], 'm', 'n']
# sub_list = ['h', 'i', 'j']
# list1[2][1][2].extend(sub_list)
# print(list1)   #->['a', 'b', ['c', ['d', 'e', ['f', 'g', 'h', 'i', 'j'], 'k'], 'l'], 'm', 'n']


# list1 = [[1, 7, 8], [9, 7, 102], [6, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
# maximum = -1
# for i in list1:
#     if max(i) > maximum:
#         maximum = max(i)
# print(maximum)


# list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
# for i in list1:
#     i.reverse()
#
# print(list1)  #->[[8, 7, 1], [102, 7, 9], [105, 106, 102], [103, 98, 99, 100], [3, 2, 1]]

# list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
# total = 0
# counter = 0
# for i in list1:
#     total += sum(i)
#     counter += len(i)
#
#
# print(total)
# print(counter)
# print(total/counter)


# n, m = int(input()), int(input())    # считываем значения n и m
# my_list = [[0] * m for _ in range(n)]
# print(my_list)

# Считывание вложенных списков
# n = 4                                          # количество строк (элементов)
# my_list = []
#
# for _ in range(n):
#     elem = [int(i) for i in input().split()]   # создаем список из элементов строки
#     my_list.append(elem)

# Перебор и вывод элементов вложенного списка
# my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# for i in range(len(my_list)):
#     for j in range(len(my_list[i])):
#         print(my_list[i][j], end=' ')   # используем необязательный параметр end
#     print()                             # перенос на новую строку


# my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# for row in my_list:
#     for elem in row:
#         print(elem, end=' ')
#     print()

# my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# for i in range(len(my_list)):
#     for j in range(len(my_list[i])):
#         print(my_list[j][i], end=' ')    # выводим my_list[j][i] вместо my_list[i][j]
#     print()


# Обработка вложенных списков
# по индексу
# my_list = [[1, 9, 8, 7, 4], [7, 3, 4], [2, 1]]
# total = 0
# for i in range(len(my_list)):
#     for j in range(len(my_list[i])):
#         total += my_list[i][j]
# print(total)

# по значениям
# my_list = [[1, 9, 8, 7, 4], [7, 3, 4], [2, 1]]
# total = 0
# for row in my_list:
#     for elem in row:
#         total += elem
# print(total)


# n = 3
# list1 = []
# for _ in range(n):
#     row = input().split()
#     list1.extend(row)
# print(list1)   #-> ['9', '7', '6', '2', '1', '3', '4', '45', '67']


# my_list = [[12, 221, 3], [41, 5, 633], [71, 8, 99]]
#
# maximum = my_list[0][0]
# minimum = my_list[0][0]
#
# for row in my_list:
#     if max(row) > maximum:
#         maximum = max(row)
#     if min(row) < minimum:
#         minimum = min(row)
#
# print(maximum + minimum)


# Список по образцу 1
# n = int(input())
# matrix = [[i for i in range(1, n + 1)] for j in range(1, n + 1)]
# print(*matrix, sep='\n')

# n = int(input())
# matrix = []
# for i in range(1, n + 1):
#    matrix.append(i)
# for j in range(1, n + 1):
#    print(matrix)

# Список по образцу 2
# n = int(input())
# matrix = [[j for j in range(1, i + 1)] for i in range(1, n + 1)]
# print(*matrix, sep='\n')

# n = int(input())
# matrix = []
# for i in range(1, n + 1):
#     matrix.append(i)
#     print(matrix)

# Треугольник Паскаля 1 🌶️
# n = int(input())
#
# li = [1]
# for i in range(n):
#     for j in range(len(li) - 1):
#         li[j] = li[j] + li[j + 1]
#     li.insert(0, 1)
#
# print(li)
#
# from math import factorial
# n = int(input())
# b = []
# for i in range(n+1):
#     b.append (int((factorial(n))/(factorial(i)*factorial(n-i))))
# print(b)


# a = [1]
# for i in range(int(input())):
#     a = [x + y for x, y in zip([*a, 0], [0, *a])]
# print(a)

# Треугольник Паскаля 2
# n = int(input())
# P=[]
# for i in range(0,n):
#     row=[1]*(i+1)
#     for j in range(i+1):
#         if j!=0 and j!=i:
#             row[j]=P[i-1][j-1]+P[i-1][j]
#     P.append(row)
#
# for r in P:
#     print(*r)

# # -------------------ФУНКЦИЯ-------------------
# def pascal(n):
#     triangle = [[1]]
#
#     for i in range(n - 1):
#         row = [1]
#         for j in range(1, len(triangle[i])):
#             row += [sum(triangle[i][j - 1: j + 1])]
#         row += [1]
#         triangle.append(row.copy())
#
#     return triangle
#
#
# # --------------------ВЫЗОВ--------------------
# [print(*row) for row in pascal(int(input()))]


# Упаковка дубликатов 🌶️
# res = []
# for el in input().split():
#     if res and el in res[-1]:
#         res[-1].append(el)
#     else:
#         res.append([el])
# print(res)
#
# #Разбиение на чанки 🌶️
# def chunked(st, n):
#     st = st.split()
#     a = [[] for _ in range(0, len(st), n)]
#     for i in range(len(a)):
#         a[i].extend(st[:n])
#         st = st[n:]
#     return a
#
# string = input()
# num = int(input())
#
# print(chunked(string, num))

# Подсписки списка 🌶️🌶️
# n = input().split()
# sp = [[]]
# k = 1
# while k != len(n) + 1:
#     for j in range(len(n)):
#         if len(n[j:j + k]) == k:
#             sp.append(n[j:j + k])
#     k += 1
# print(sp)

# ///////////////////////////////////////////////////////////
# 4.4 Матрицы. Часть 1
##матрицу можно создать с помощью генератора:
# [[input() for _ in range(m)] for _ in range(n)]


# matrix  = [[2, -5, -11, 0],
#            [-9, 4, 6, 13],
#            [4, 7, 12, -2]]
#
# print(matrix[1][2])  # вывод элемента на позиции (2, 3)  -->6

# Перебор элементов матрицы

# перебирая по строкам:
# rows, cols = 3, 4           # rows - количество строк, cols - количество столбцов
# matrix  = [[2, 3, 1, 0],
#            [9, 4, 6, 8],
#            [4, 7, 2, 7]]
# for r in range(rows):
#     for c in range(cols):
#         print(matrix[r][c], end=' ')
#     print()

# перебирая по столбцам
# rows, cols = 3, 4           # rows - количество строк, cols - количество столбцов
# matrix  = [[2, 3, 1, 0],
#            [9, 4, 6, 8],
#            [4, 7, 2, 7]]
# for c in range(cols):
#     for r in range(rows):
#         print(matrix[r][c], end=' ')
#     print()

# Функции ljust() и rjust()

# Строковый метод ljust() выравнивает текст по ширине, добавляя пробелы в конец текста.
# print('a'.ljust(3))
# print('ab'.ljust(3))
# print('abc'.ljust(3))

# Строковый метод ljust() использует вместо пробела другой символ, если передать ему второй аргумент,
# необязательный.
# print('a'.ljust(5, '*'))
# print('ab'.ljust(5, '$'))
# print('abc'.ljust(5, '#'))


# Строковый метод rjust() выравнивает текст по ширине, добавляя пробелы в начало текста.
# print('a'.rjust(3))
# print('ab'.rjust(3))
# print('abc'.rjust(3))

# Строковый метод rjust() использует вместо пробела другой символ,
# если передать ему второй аргумент, необязательный.
# print('a'.rjust(5, '*'))
# print('ab'.rjust(5, '$'))
# print('abc'.rjust(5, '#'))


# Применив метод ljust() для выравнивания столбцов при выводе таблицы мы получим
# rows, cols = 3, 4                # rows - количество строк, cols - количество столбцов
# matrix  = [[277, -930, 11, 0],
#            [9, 43, 6, 87],
#            [4456, 8, 290, 7]]
# for r in range(rows):
#     for c in range(cols):
#         print(str(matrix[r][c]).ljust(8), end='')
#     print()

# Элементы с равными индексами i == j находятся на главной диагонали. Такие элементы обозначаются matrix[i][i].
# Элементы с индексами i и j, связанными соотношением i + j + 1 = n (или j = n - i - 1), где n — размерность матрицы,
# находятся на побочной диагонали.

# n = 8
# matrix = [[0]*n for _ in range(n)]    # создаем квадратную матрицу размером 8×8
# for i in range(n):             # заполняем главную диагональ единицами, а побочную двойками
#     matrix[i][i] = 1
#     matrix[i][n-i-1] = 2
# for r in range(n):             # выводим матрицу
#     for c in range(n):
#         print(matrix[r][c], end=' ')
#     print()

# Индексы i и j элементов на главной диагонали связаны соотношением i = j. Индексы i и jэлементов на
# побочной диагонали связанны соотношением i + j + 1 = n (или  j = n - i - 1), где n — размерность матрицы


## Используйте функцию print_matrix() для вывода квадратной матрицы размерности n:
# def print_matrix(matrix, n, width=1):
#     for r in range(n):
#         for c in range(n):
#             print(str(matrix[r][c]).ljust(width), end=' ')
#         print()
#
## Для считывания матрицы из n строк, заполненной числами, удобно использовать следующий код:
# n = int(input())
# matrix = []
# for i in range(n):
#     temp = [int(num) for num in input().split()]
#     matrix.append(temp)


# n = 3
# a = [[1, 2, 3],             #->  9 8 7
#      [4, 5, 6],             #->  6 5 4
#      [7, 8, 9]]             #->  3 2 1
#
# for i in range(n):
#     for j in range(n):
#         print(a[n - i - 1][n - j - 1], end=' ')
#     print()


# считаем максимальное значение главной диагонали  и минимальной  значение побочной диагонали
# n = 5
# a = [[19, 21, 33, 78, 99],
#      [41, 53, 66, 98, 76],
#      [79, 80, 90, 60, 20],
#      [33, 11, 45, 67, 90],
#      [45, 67, 12, 98, 23]]
#
# maximum = -1
# minimum = 100
#
# for i in range(n):
#     if a[i][i] > maximum:
#         maximum = a[i][i]
#     if a[i][n - i - 1] < minimum:
#         minimum = a[i][n - i - 1]
# print(minimum + maximum)   #-->101

# ----------------------------------
# создания матрицы
# ----------------------------------

# N = int(input())
# M = int(input())
# matrix = [[0] * M for i in range(N)]
#
# # Заполнение матрицы произвольными значениями
# for i in range(N):
#     for j in range(M):
#         matrix[i][j] = input()
#
# # вывести матрицу на экран построчно
# for i in range(len(matrix)):  # len(A) - возвращает количество строк в матрице А
#     for j in range(len(matrix[i])):  # len(A[i]) - возвращает количество элементов в строке i
#         print(matrix[i][j], end=' ')
#     print()

# ----------------------------------
# ----------------------------------

# Вывести матрицу 1
# n, m = int(input()), int(input())
# matrix = [[0] * m for i in range(n)]
#
# # Заполнение матрицы
# for i in range(n):
#     for j in range(m):
#         matrix[i][j] = input()
#
# # вывести матрицу на экран построчно
# for i in range(len(matrix)):  # возвращает количество строк в матрице
#     for j in range(len(matrix[i])):  # возвращает количество элементов в строке i
#         print(matrix[i][j], end=' ')
#     print()

# # ------------------------------------
# n, m = int(input()), int(input())
# [print(*[input() for i in range(m)]) for i in range(n)]
# # -------------------------------------
# # -------------------------------------
# def input_matrix(rows, cols):
#     matrix = [[input() for _ in range(cols)] for _ in range(rows)]
#     return matrix
#
# def print_matrix(matrix):
#     for r in range(len(matrix)):
#         print(*matrix[r])
#     return None
#
# n, m = int(input()), int(input())
# print_matrix(input_matrix(n, m))
# # -------------------------------------
# # -------------------------------------
# Вывести матрицу 2
# rows, cols = int(input()), int(input())  # rows - количество строк, cols - количество столбцов
# matrix = [[0] * cols for i in range(rows)]
#
# for i in range(rows):
#     for j in range(cols):
#         matrix[i][j] = input()
#
# for i in range(rows):
#     for j in range(cols):
#         print(matrix[i][j], end=' ')
#     print()
# print()
#
# for j in range(cols):
#     for i in range(rows):
#         print(matrix[i][j], end=' ')
#     print()
# -----------------------
# def print_matrix(matrix, rows, cols, width=1):
#     for i in range(rows):
#         for j in range(cols):
#             print(matrix[i][j].ljust(width), end=' ')
#         print()
#
#
# def print_transposed_matrix(matrix, rows, cols, width=1):
#     for j in range(cols):
#         for i in range(rows):
#             print(matrix[i][j].ljust(width), end=' ')
#         print()
#
#
# n, m = int(input()), int(input())
# matrix = [[input() for j in range(m)] for i in range(n)]
# print_matrix(matrix, n, m)
# print()
# print_transposed_matrix(matrix, n, m)

##След матрицы
# n = int(input())
# maximum = 0
# matrix = [list(map(int, input().split())) for __ in range(n)]
# for i in range(n):
#     maximum += matrix[i][i]
# print(maximum)


# res = 0
# for i in range(int(input())):
#     res += int(input().split()[i])
# print(res)

# Больше среднего
# n = int(input())
# counter = 0
# matrix = [list(map(int, input().split())) for _ in range(n)]
# for i in matrix:
#     sr = (sum(list(map(int, i)))) / len(i)
#     for j in i:
#         if int(j) > sr:
#             counter += 1
#     print(counter)
#     counter = 0


# Максимальный в области 1
# n = int(input())
# maximum = []
# matrix = [list(map(int, input().split())) for __ in range(n)]
# for i in range(n):
#     for j in range(n):
#         if i >= j:
#             maximum.append(matrix[i][j])
# print(max(maximum))


# Максимальный в области 2 🌶️
# n = int(input())
# maximum = []
# matrix = [list(map(int, input().split())) for __ in range(n)]
# for i in range(n):
#     for j in range(n):
#         if (i >= j and i <= n - 1 -j) or (i <= j and i >= n - 1 -j) or (i == j) or (i + j + 1 == n):
#             maximum.append(matrix[i][j])
# print(max(maximum))

# Суммы четвертей
# n = int(input())
# up = []
# left = []
# down = []
# right = []
# matrix = [list(map(int, input().split())) for __ in range(n)]
# for i in range(n):
#     for j in range(n):
#         if (i < j and i < n - 1 -j):
#             up.append(matrix[i][j])
#         elif (i > j and i < n - 1 -j):
#             left.append(matrix[i][j])
#         elif (i > j and i > n - 1 -j):
#             down.append(matrix[i][j])
#         elif (i < j and i > n - 1 -j):
#             right.append(matrix[i][j])
# print(f'Верхняя четверть: {sum(up)}')
# print(f'Правая четверть: {sum(right)}')
# print(f'Нижняя четверть: {sum(down)}')
# print(f'Левая четверть: {sum(left)}')


# Таблица умножения
# n, m = int(input()), int(input())
# for i in range(n):
#     mult = []
#     for j in range(m):
#         mult.append(str(i*j).ljust(3))
#     print(*mult)
#
# n, m = int(input()), int(input())
# mult = [[i * j for j in range(m)] for i in range(n)]
# for i in range(n):
#     for j in range(m):
#         print(str(mult[i][j]).ljust(3), end='')
#     print()


# Максимум в таблице
# n, m = int(input()), int(input())
# row, col = 0, 0
# matrix = [[int(i) for i in input().split()] for _ in range(n)]
# for i in range(n):
#     for j in range(m):
#         if matrix[i][j] > matrix[row][col]:
#             row, col = i, j
# print(row, col)


# Обмен столбцов
# n, m = int(input()), int(input())
# matrix = [[int(i) for i in input().split()] for _ in range(n)]
# a, b = [int(i) for i in input().split()]
#
# for i in range(n):
#     matrix[i][a], matrix[i][b] = matrix[i][b], matrix[i][a]
# for i in matrix:
#     print(*i)

# Симметричная матрица
# n = int(input())
# flag = True
# matrix = [list(map(int, input().split())) for __ in range(n)]
# for i in range(n):
#     for j in range(n):
#         if matrix[i][j] != matrix[j][i]:
#             flag = False
#     if flag == False:
#         print('NO')
#         break
# else:
#     print('YES')


# Обмен диагоналей
# n = int(input())
# matrix = [[int(i) for i in input().split()] for _ in range(n)]
#
# for i in range(n):
#     matrix[i][i], matrix[n - i - 1][i] = matrix[n - i - 1][i], matrix[i][i]
#
# for row in matrix:
#     print(*row)

#
# # Зеркальное отображение
# n = int(input())
# matrix = [input().split() for _ in range(n)]
#
# for i in range(n // 2):
#     matrix[i], matrix[n - i - 1] = matrix[n - i - 1], matrix[i]
# for row in matrix:
#     print(*row)


# n = int(input())
# matrix = [[int(i) for i in input().split()] for _ in range(n)]
# matrix.reverse()
#
# for row in matrix:
#     print(*row)

# # Поворот матрицы
# n = int(input())
# matrix = [[int(i) for i in input().split()] for _ in range(n)]
#
# for j in range(n):
#     for i in range(n - 1, -1, -1):
#         print(matrix[i][j], end=' ')
#     print()


# Ходы коня
# col, row = input().strip()
# coor_col = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
# coor_row = {'1': 7, '2': 6, '3': 5, '4': 4, '5': 3, '6': 2, '7': 1, '8': 0}
# arr = [["N" if [i, j] == [coor_row[row], coor_col[col]] else '.' for j in range(8)] for i in range(8)]
# for i in range(8):
#     for j in range(8):
#         if (coor_row[row] - i) * (coor_col[col] - j) in [-2, 2]: arr[i][j] = "*"
# for line in arr:
#     print(*line, sep = ' ')
#
# x, y = input()
# n = 8
# board = [['.'] * n for _ in range(n)]
# x = ord(x) - 97
# y = n - int(y)
# board[y][x] = 'N'
#
# for i in range(n):
#     for j in range(n):
#         if abs(y - i) * abs(x - j) == 2:
#             board[i][j] = '*'
#
# for row in board:
#     print(*row)


# Магический квадрат 🌶️
# n = int(input())
# matrix = [[int(i) for i in input().split()] for j in range(n)]
#
# magic = sum(matrix[0])
# flag = 'YES'
# digits = [i for i in range(1, n ** 2 + 1)]
#
# for i in range(n):
#     for j in range(n):
#         if matrix[i][j] in digits:
#             digits.remove(matrix[i][j])
#     if i == n - 1 and j == n - 1 and digits != []:
#         flag = 'NO'
#
# for i in range(n):
#     if sum(matrix[i]) != magic:
#         flag = 'NO'
#         break
#
# for j in range(n):
#     result = 0
#     for i in range(n):
#         result += matrix[i][j]
#         if i == n - 1 and result != magic:
#             flag = 'NO'
#             break
#
# print(flag)

# Шахматная доска
# x, y = [int(i) for i in input().split()]
# matrix = [['.'] * y for _ in range(x)]
#
# for i in range(x):
#     if i == 0 or i % 2 == 0:
#         for j in range(1, y, 2):
#             matrix[i][j] = '*'
#     else:
#         for j in range(0, y, 2):
#             matrix[i][j] = '*'
#
# for row in matrix:
#     print(*row)

# n, m = map(int, input().split())
# for i in range(n):
#     row = ['.' if (i + j) % 2 == 0 else '*' for j in range(m)]
#     print(*row)

# Побочная диагональ
# n = int(input())
# matrix = [[0] * n for _ in range(n)]
# for i in range(n):
#     matrix[i][n - 1 - i] = 1
#     for j in range(n):
#         if i > n - 1 - j:
#             matrix[i][j] = 2
#         print(matrix[i][j], end=" ")
#     print()

# def matrix(i, j, n):
#     if i == n - j - 1:
#         return 1
#     elif i < n - j - 1:
#         return 0
#     else:
#         return 2
# n = int(input())
# res = [[matrix(i, j, n) for j in range(n)] for i in range(n)]
# for x in res:
#     print(*x)


# Заполнение 1
# n, m = map(int, input().split())
# matrix = []
# counter = 1
#
# for i in range(n):
#     matrix.append([])
#     for j in range(m):
#         matrix[i].append(counter)
#         counter += 1
#
#         print(f'{matrix[i][j]}'.ljust(3), end='')
#     print()

# Заполнение 2
# n, m = [int(i) for i in input().split()]
# matrix = [[0] * m for _ in range(n)]
#
# for j in range(m):
#     for i in range(n):
#         matrix[i][j] = j * n + i + 1
#
# for i in range(n):
#     for j in range(m):
#         print(str(matrix[i][j]).ljust(3), end=' ')
#     print()


# Заполнение 3
# n = int(input())
# matr = [[0] * n for _ in range(n)]
# for i in range(n):
#     matr[i][i] = 1
#     matr[i][n - 1 - i] = 1
# for i in range(n):
#     for j in range(n):
#         print(str(matr[i][j]).ljust(3), end='')
#     print()

# Заполнение 4
# n = int(input())
# matrix = [[0] * n for _ in range(n)]
#
# for i in range(n):
#     for j in range(n):
#         if (i <= j and i + j + 1 <= n) or (i >= j and i + j + 1 >= n):
#             matrix[i][j] = 1
#
# for i in range(n):
#     for j in range(n):
#         print(str(matrix[i][j]).ljust(3), end=' ')
#     print()


# Заполнение 5 🌶️
# n, m = [int(i) for i in input().split()]
# matrix = [[0] * m for _ in range(n)]
#
# for i in range(n):
#     for j in range(m):
#         matrix[i][j] = (i + j) % m + 1
#
# for i in range(n):
#     for j in range(m):
#         print(str(matrix[i][j]).ljust(3), end=' ')
#     print()


# Заполнение змейкой
# s=input().split()
# n=int(s[0])
# m=int(s[1])
# matrix=[[0 for i in range(m)] for _ in range(n)]
# count =1
# for i in range(n):
#     for j in range(m):
#         matrix[i][j] += count
#         count+=1
# for i in range(n):
#     if i%2==0:
#         print(*matrix[i])
#     else:
#         matrix[i].reverse()
#         print(*matrix[i])


# n, m = [int(i) for i in input().split()]
# matrix = [[0] * m for _ in range(n)]
#
# for i in range(n):
#     for j in range(m):
#         matrix[i][j] = i * m + j + 1
#     if i % 2:
#         matrix[i].reverse()
#
# for i in range(n):
#     for j in range(m):
#         print(str(matrix[i][j]).ljust(3), end=' ')
#     print()

# Заполнение диагоналями 🌶️
# n, m = [int(i) for i in input().split()]
# mtx = [[0] * m for _ in range(n)]
# sequence, k = 1, 0
#
# while sequence != n * m + 1:
#     for i in range(n):
#         for j in range(m):
#             if i + j == k:
#                 mtx[i][j] = sequence
#                 sequence += 1
#     k += 1
#
# for i in range(n):
#     for j in range(m):
#         print(str(mtx[i][j]).ljust(3), end='')
#     print()


# n, m = [int(i) for i in input().split()]
#
# matrix = [[1] * m for _ in range(n)]
# row, col, diag = 0, 0, 0
#
# for i in range(1, n * m):
#     col -= 1
#     row += 1
#     if col < 0 or row == n:
#         diag += 1
#         col = diag if diag < m else m - 1
#         row = diag - col
#
#     matrix[row][col] += i
#
# [print(*i) for i in matrix]

# # Принимаем параметры матрицы
# n, m = map(int, input().split())
# # Создаем скелет матрицы
# matrix = [[0] * m for i in range(n)]
# # Задаем отсчет с единицы
# d = 1
#
# for k in range(1, n + m):               # Цикл перебирающий сумму индексов в диагонали
#     for i in range(n):                  # Перебираем строки
#         for j in range(m):              # Перебираем столбцы
#             if i + j + 1 == k:          # Выявляем ячейки, относящиеся к искомой диагонали
#                 matrix[i][j] = d        # Присваиваем обнаруженной ячейке порядковый номер
#                 d += 1                  # Обновляем счетчик
#
# # Распечатываем полученную матрицу
# for row in range(n):
#     for col in range(m):
#         print(str(matrix[row][col]).ljust(3), end=' ')
#     print()


# Заполнение спиралью 😈😈
# n, m = map(int, input().split())
# l = [[0] * m for _ in range(n)]
# num = 1
# k = 0                                 # уровень квадрата: 0 - внешний, 1 - вложенный и т.д.
# product = n * m + 1                   # вынесено в переменную, т.к. n и m меняются в цикле
#
# while num < product:
#     for j in range(k, m):             # верхняя сторона
#         l[k][j] = num
#         num += 1
#     for i in range(k + 1, n):         # правая сторона
#         l[i][j] = num
#         num += 1
#     if num == product:                # костыль для случаев с маленькими n, m
#         break
#     for j in range(m - 2, k - 1, -1): # нижняя сторона
#         l[i][j] = num
#         num += 1
#     for i in range(n - 2, k, -1):     # левая сторона
#         l[i][j] = num
#         num += 1
#     m -= 1                            # изменяю размер сторон для будущего квадрата
#     n -= 1
#     k += 1
#
# for row in l:
#     for el in row:
#         print(str(el).ljust(3), end='')
#     print()


# 4.7 Операции над матрицами в математике
# Сложение матриц
# n, m = [int(i) for i in input().split()]
# matrix1 = [[int(i) for i in input().split()] for _ in range(n)]
# _ = input()
# matrix2 = [[int(i) for i in input().split()] for _ in range(n)]
# matrix3 = [[0] * m for _ in range(n)]
#
# for i in range(n):
#     for j in range(m):
#         matrix3[i][j] += matrix1[i][j] + matrix2[i][j]
#
# for row in matrix3:
#     print(*row)

# n, m = [int(x) for x in input().split()]
# A = [[int(x) for x in input().split()] for _ in range(n)]
# input()
# B = [[int(x) for x in input().split()] for _ in range(n)]
# C = [[A[i][j] + B[i][j] for j in range(m)] for i in range(n)]
# [print(*i) for i in C]

# Умножение матриц 🌶️
# n, m = [int(x) for x in input().split()]
# matrix1 = [[int(x) for x in input().split()] for _ in range(n)]
# input()
# m, k = [int(x) for x in input().split()]
# matrix2 = [[int(x) for x in input().split()] for _ in range(m)]
# matrix3 = [[0] * k for i in range(n)]
# for i in range(n):
#     for j in range(k):
#         for q in range(m):
#             matrix3[i][j] += matrix1[i][q] * matrix2[q][j]
# [print(*i) for i in matrix3]


# Возведение в степень каждого элемента матрицы
# n = int(input())
# a = [list(map(int, list(input().split()))) for _ in range(n)]
# m = int(input())
#
# def multi(a, b):
#     n = len(a)
#     b = list(zip(*b))
#     return [[sum([a[i][r] * b[j][r] for r in range(n)]) for j in range(n)] for i in range(n)]
#
# def expo(a, m):
#     c = list(a)
#     for _ in range(m-1):
#         c = multi(c, a)
#     return c
#
# result = expo(a, m)
#
# [print(*row) for row in result]

# Каждый n-ый элемент
# s = input().split()
# n = int(input())
# res = []
# for i in range(n):
#     res.append(s[i::n])
# print(res)

# Максимальный в области 2
# n = int(input())
# arr = []
# maximum = 0
# for i in range(n):
#     arr.append([int(elem) for elem in input().split()])
# for i in range(n):
#     for j in range(n):
#         if i >= n - 1 - j and arr[i][j] > maximum:
#             maximum = arr[i][j]
# print(maximum)

#  берем размер матрицы
# n = int(input())
# #  выпиливаем матрицу из входных данных
# matrix = [[int(x) for x in input().split()] for i in range(n)]
# #  вычисляем больший (элемент) из больших (элементов) в бегущем срезе
# answer = max(max(matrix[i][n-i-1:]) for i in range(n))
# #  закидываем результат
# print(answer)

# Транспонирование матрицы
# import numpy as np
# n = int(input())
# arr = []
# for i in range(n):
#     arr.append([int(elem) for elem in input().split()])
# a_t = np.matrix(arr).transpose().tolist()
# for i in range(n):
#     print(*a_t[i])

# n = int(input())
# matrix = [input().split() for _ in range(n)]
#
# for i in range(n):
#     for j in range(i, n):
#         matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
#
# for row in matrix:
#     print(*row)


# Снежинка
# n = int(input())
# arr = []
#
# for i in range(n):
#     arr.append([])
#     for j in range(n):
#         if i == n//2 or j == n//2 or i == j or i == n-j-1:
#             arr[i].append('*')
#         else:
#             arr[i].append('.')
#
# for i in range(n):
#     print(*arr[i])


# Симметричная матрица
# def is_symmetric(arr, n):
#     for i in range(n):
#         for j in range(n):
#             if arr[i][j] != arr[n-j-1][n-i-1]:
#                 return 'NO'
#     return 'YES'
#
# n = int(input())
# arr = []
#
# for i in range(n):
#     arr.append([int(elem) for elem in input().split()])
#
# print(is_symmetric(arr, n))

# n = int(input())
# arr = [list(map(int, input().split())) for _ in range(n)]
# res = 'YES'
# for i in range(n - 1):
#     for j in range(n - i - 1):
#         if arr[i][j] != arr[n - j - 1][n - i - 1]:
#             res = 'NO'
#             break
#     if res == 'NO':
#         break
# print(res)


# Латинский квадрат 🌶️
# import numpy as np
#
# def is_every_digit_in_arr(arr, n):
#     for i in range(1, n + 1):
#         if i not in arr:
#             return False
#     return True
#
# def is_latin_square(arr, n):
#     result = []
#     a_t = np.matrix(arr).transpose().tolist()
#     for i in range(n):
#         arr[i] = sorted(arr[i])
#         if (result != [] and result != arr[i]) or not is_every_digit_in_arr(arr[i], n):
#             return 'NO'
#         result = arr[i]
#     result = []
#     for i in range(n):
#         a_t[i] = sorted(a_t[i])
#         if (result != [] and result != a_t[i]) or not is_every_digit_in_arr(arr[i], n):
#             return 'NO'
#         result = a_t[i]
#
#     return 'YES'
#
# n = int(input())
# arr = []
#
# for i in range(n):
#     arr.append([int(elem) for elem in input().split()])
#
# print(is_latin_square(arr, n))

# n = int(input())
# matrix = [[int(i) for i in input().split()] for _ in range(n)]
# numbers = list(range(1, n + 1))
# result = 'YES'
#
# for i in range(n):
#     row_nums = sorted(matrix[i])
#     col_nums = sorted([matrix[j][i] for j in range(n)])
#     if row_nums != numbers or col_nums != numbers:
#         result = 'NO'
#         break
#
# print(result)

# # Ходы ферзя
# slovarx = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7}
# slovary = {'8':0, '7':1, '6':2, '5':3, '4':4, '3':5, '2':6, '1':7, '0':8}
#
# position = input()
# arr = []
#
# for i in range(8):
#     arr.append([])
#     for j in range(8):
#         if j == slovarx[position[0]] and i == slovary[position[1]]:
#             arr[i].append('Q')
#         elif j == slovarx[position[0]] or i == slovary[position[1]]:
#             arr[i].append('*')
#         elif abs(slovarx[position[0]] - j) == abs(slovary[position[1]] - i):
#             arr[i].append('*')
#         else:
#             arr[i].append('.')
#
# for i in range(8):
#     print(*arr[i])
#
# # Диагонали параллельные главной
# n = int(input())
# arr = []
#
# for i in range(n):
#     arr.append([])
#     for j in range(n):
#         arr[i].append(abs(i-j))
#
# for i in range(n):
#     print(*arr[i])

# //////////////////////////////  6.1 Введение в кортежи   //////////////////////////////
# Кортежи поддерживают:
# 
# доступ к элементу по индексу (только для получения значений элементов);
# методы, в частности index(), count();
# встроенные функции, в частности len(), sum(), min() и max();
# срезы;
# оператор принадлежности in;
# операторы конкатенации (+) и повторения (*).

# 6 elementov
# primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71)
# print(primes[:6])

# кроме первых двух.
# countries = ('Russia', 'Argentina', 'Slovakia', 'Canada', 'Slovenia', 'Italy', 'Spain', 'Ukraine', 'Chile', 'Cameroon')
# print(countries[2:])


# # кроме последних трех.
# countries = ('Russia', 'Argentina', 'Slovakia', 'Canada', 'Slovenia', 'Italy', 'Spain', 'Ukraine', 'Chile', 'Cameroon')
# print(countries[:-3])

# кроме двух последних и трех первых.
# countries = ('Russia', 'Argentina', 'Slovakia', 'Canada', 'Slovenia', 'Italy', 'Spain', 'Ukraine', 'Chile', 'Cameroon')
# print(countries[3:-2])

# # количество элементов кортежа
# countries = ('Romania', 'Poland', 'Estonia', 'Bulgaria', 'Slovakia', 'Slovenia', 'Hungary')
# number = len(countries)
# print(number)

# # сумму минимального и максимального элементов кортежа
# numbers = (12.5, 3.1415, 2.718, 9.8, 1.414, 1.1618, 1.324)
# print(min(numbers)+max(numbers))

# # переменная index содержала индекс элемента «Slovenia»
# countries = ('Russia', 'Argentina', 'Spain', 'Slovakia', 'Canada', 'Slovenia', 'Italy')
# index = countries.index('Slovenia')
# print(index)


# # number, содержала количество вхождений «Spain»
# countries = ('Russia', 'Argentina', 'Spain', 'Slovakia', 'Canada', 'Slovenia', 'Italy', 'Spain', 'Ukraine', 'Chile', 'Spain', 'Cameroon')
# number = countries.count('Spain')
# print(number)


# # чтобы он вывел кортеж:  (1, 2, 3, 1, 2, 3, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 8, 9, 10, 11, 12, 13)
# numbers1 = (1, 2, 3)
# numbers2 = (6,)
# numbers3 = (7, 8, 9, 10, 11, 12, 13)
#
# print(numbers1 * 2 + numbers2 * 9 + numbers3)
#
# city_name = input()
# city_year = int(input())
# city = (city_name, city_year)
# print(city)


# получить список, содержащий только непустые кортежи
# tuples = [(), (), ('',), ('a', 'b'), (), ('a', 'b', 'c'), (1,), (), (), ('d',), ('', ''), ()]
# # non_empty_tuples = [tuples[2],tuples[3],tuples[5],tuples[6],tuples[9],tuples[10]]
# non_empty_tuples = [i for i in tuples if i]
# print(non_empty_tuples)

# # Дополните приведенный код так, чтобы переменная new_tuples, содержала список кортежей на основе
# # списка tuples с последним элементом каждого кортежа, замененным на численное значение 100.
# tuples = [(10, 20, 40), (40, 50, 60), (70, 80, 90), (10, 90), (1, 2, 3, 4), (5, 6, 10, 2, 1, 77)]
# new_tuples = [i[:-1] + (100,) for i in tuples]
# print(new_tuples)


# # вывел список, содержащий средние арифметические значения чисел каждого вложенного кортежа
# numbers = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4), (90, 10))
# # tupl = []
# # for i in range(len(numbers)):
# #     tupl.append(sum(numbers[i])/len(numbers[i]))
# # print(tupl)
#
# print([sum(i) / len(i) for i in numbers])

# Вершина параболы
# a, b, c = int(input()), int(input()), int(input()),
# print([(- (b / (2 * a))), (((4 * a * c) - b**2)/ (4 * a))])


# Конкурсный отбор
# n = int(input())
# sp = [input().split() for _ in range(n)]
# for i in sp:
#     print(*i)
# print()
# for i in sp:
#     if i[-1] == '5' or i[-1] == '4':
#         print(*i)
# --
# pup = [input() for _ in range(int(input()))]
# print(*pup, sep='\n')
# print()
# [print(x) for x in pup if int(x[-1]) > 3]

# colors = ('red', 'green', 'blue', 'cyan')
# a, b, c, d = colors
# print(a, d)


# 8.3 Введение в множества в Python
# numbers = {1.414, 12.5, 3.1415, 2.718, 9.8, 1.414, 1.1618, 1.324, 2.718, 1.324}
# print(min(numbers)+max(numbers))

#
# numbers = {20, 6, 8, 18, 18, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 12, 8, 8, 10, 4, 2, 2, 2, 16, 20}
# average = sum(numbers)/len(numbers)
#
# print(average)

# Перебор элементов множества
# numbers = {0, 1, 1, 2, 3, 3, 3, 5, 6, 7, 7}
# for num in numbers:
#     print(num)

# можем использовать операцию распаковки множества.
# numbers = {0, 1, 1, 2, 3, 3, 3, 5, 6, 7, 7}
# print(*numbers, sep='\n')

# # Если нужно гарантировать порядок вывода элементов (по возрастанию / убыванию)
# numbers = {0, 1, 1, 2, 3, 3, 3, 5, 6, 7, 7}
# sorted_numbers = sorted(numbers)
# print(*sorted_numbers, sep='\n')

# numbers = {0, 1, 1, 2, 3, 3, 3, 5, 6, 7, 7}
# sortnumbers = sorted(numbers, reverse=True)
# print(*sortnumbers, sep='\n')


# сумму квадратов
# numbers = {9089, -67, -32, 1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111, 111, 1, 23}
# summa = 0
# for i in numbers:
#     summa += i ** 2
# print(summa)
#
# print(sum([i*i for i in numbers]))


# элементы множества fruits, каждый на отдельной строке, отсортированные по убыванию
# fruits = {'apple', 'banana', 'cherry', 'avocado', 'pineapple', 'apricot', 'banana', 'avocado', 'grapefruit'}
# print(*sorted(fruits, reverse=True), sep='\n')

# # Количество различных символов
# print(len(set(input())))

# Неповторимые цифры
# s = list(input())
# print('YES' if len(s) == len(set(s)) else 'NO')

# верно ли, что в записи этих двух строк используются все 10 цифр?
# a, b = input(), input()
# print('YES' if len(set(a+b)) == 10 else 'NO')


# # Одинаковые наборы
# # a, b = input(), input()
# print('YES' if set(input()) == set(input()) else 'NO')

# # Верно ли, что для записи всех трех слов был использован один и тот же набор букв?
# s = input().split()
# print(('NO', 'YES')[set(s[0]) == set(s[1]) == set(s[2])])

# 8.5 Методы множеств. Часть 1
# Для добавления нового элемента в множество используется метод add().
# Метод remove() — удаляет элемент из множества с генерацией исключения (ошибки) в случае, если такого элемента нет.
# Метод discard() — удаляет элемент из множества без генерации исключения (ошибки), если элемент отсутствует.
# Метод pop() — удаляет и возвращает 1ый элемент из множества с генерацией исключения (ошибки) при попытке
# удаления из пустого множества.

# numbers = {1, 2, 3, 4, 5}
#
# print('до удаления:', numbers)
# num = numbers.pop()                 # удаляет 1ый элемент множества, возвращая его
# print('удалённый элемент:', num)
# print('после удаления:', numbers)

# Метод clear() удаляет все элементы из множества.

# Уникальные символы 1
# sp = [input().lower() for _ in range(int(input()))]
# for i in sp:
#     print(len(set(i)))
#
# [print(len(set(input().lower()))) for x in range(int(input()))]

# Уникальные символы 2
# sp = [input().lower() for _ in range(int(input()))]
# s = ''.join(sp)
# print(len(set(s)))

# Количество слов в тексте
# words = [word.lower().strip('.,;:-?!') for word in input().split()]
# print(len(set(words)))

# Встречалось ли число раньше?
# t = input().split()
# m = set()
# for i in t:
#     if i.lstrip('0') in m:
#         print('YES')
#     else:
#         m.add(i)
#         print('NO')

# 8.6 Методы множеств. Часть 2
# Объединение множеств: метод union()
# myset1 = {1, 2, 3, 4, 5}
# myset2 = {3, 4, 6, 7, 8}
# myset3 = myset1.union(myset2)
# print(myset3)   #->{1, 2, 3, 4, 5, 6, 7, 8}

# Для объединения двух множеств можно также использовать оператор |
# myset1 = {1, 2, 3, 4, 5}
# myset2 = {3, 4, 6, 7, 8}
# myset3 = myset1 | myset2
# print(myset3)

# Пересечение множеств: метод intersection(), можно также использовать оператор &
# myset1 = {1, 2, 3, 4, 5}
# myset2 = {3, 4, 6, 7, 8}
# myset3 = myset1.intersection(myset2)
# print(myset3)  #--> {3, 4}

# Разность множеств: метод difference(), можно также использовать оператор -
# myset1 = {1, 2, 3, 4, 5}
# myset2 = {3, 4, 6, 7, 8}
# myset3 = myset1.difference(myset2)
# print(myset3)    #-->{1, 2, 5}

# Симметрическая разность: метод symmetric_difference(), можно также использовать оператор ^
# myset1 = {1, 2, 3, 4, 5}
# myset2 = {3, 4, 6, 7, 8}
# myset3 = myset1.symmetric_difference(myset2)
# print(myset3)   # -->{1, 2, 5, 6, 7, 8}


# Методы union(), intersection(), difference(), symmetric_difference() не изменяют исходные множества,
# а возвращают новые. Часто на практике нужно изменять исходные множества. Для таких целей используются
# парные методы update(), intersection_update(), difference_update(), symmetric_difference_update().


# Метод update() изменяет исходное множество по объединению., |=
# myset1 = {1, 2, 3, 4, 5}
# myset2 = {3, 4, 6, 7, 8}
# myset1.update(myset2)      # изменяем множество myset1
# print(myset1)   # --> {1, 2, 3, 4, 5, 6, 7, 8}

# Метод intersection_update() изменяет исходное множество по пересечению.
# myset1 = {1, 2, 3, 4, 5}
# myset2 = {3, 4, 6, 7, 8}
# myset1.intersection_update(myset2)      # изменяем множество myset1
# print(myset1)   # --> {3, 4}

# Метод difference_update() изменяет исходное множество по разности.
# myset1 = {1, 2, 3, 4, 5}
# myset2 = {3, 4, 6, 7, 8}
# myset1.difference_update(myset2)      # изменяем множество myset1
# print(myset1) # -->{1, 2, 5}

# Метод symmetric_difference_update() изменяет исходное множество по симметрической разности.
# myset1 = {1, 2, 3, 4, 5}
# myset2 = {3, 4, 6, 7, 8}
# myset1.symmetric_difference_update(myset2)      # изменяем множество myset1
# print(myset1)   # --> {1, 2, 5, 6, 7, 8}


# mylist = [2021, 2020, 2019, 2018, 2017, 2016]
# mytuple = (2021, 2020, 2016)
# mystr = 'abcd'
# myset = {2009, 2010, 2016}
# print(myset.union(mystr))              # объединяем со строкой
# print(myset.intersection(mylist))      # пересекаем со списком
# print(myset.difference(mytuple))       # находим разность с кортежем


# A | B , A.union(B) - Возвращает множество, являющееся объединением множеств A и B
# A |= B , A.update(B) - Добавляет в множество A все элементы из множества B
# A & B, A.intersection(B) - Возвращает множество, являющееся пересечением множеств A и B
# A &= B, A.intersection_update(B) - Оставляет в множестве A только те элементы, которые есть в множестве B
# A - B , A.difference(B) - Возвращает разность множеств A и B
# A -= B , A.difference_update(B) - Удаляет из множества A все элементы, входящие в B
# A ^ B , A.symmetric_difference(B) - Возвращает симметрическую разность множеств A и B
# A ^= B,  A.symmetric_difference_update(B) - Записывает в A симметрическую разность множеств A и B

# Количество совпадающих
# a = set(list(map(int, input().split())))
# b = set(list(map(int, input().split())))
# print(len(a.intersection(b)))


# # Общие числа
# a = set(list(map(int, input().split())))
# b = set(list(map(int, input().split())))
# print(*sorted(a.intersection(b)))

# Числа первой строки
# a = set(map(int, input().split()))
# b = set(map(int, input().split()))
# print(*sorted(a - b))

# Общие цифры
# n = int(input())
# numbers = [input() for _ in range(n)]
#
# num_set = set(numbers[0]).intersection(*numbers)
# print(*sorted(num_set))

# 8.7 Методы множеств. Часть 3
# Для определения, является ли одно из множеств подмножеством другого, используется метод issubset()
# также применяются операторы <= (нестрогое подмножество) и < (строгое подмножество).
# set1 = {2, 3}
# set2 = {1, 2, 3, 4, 5, 6}
# print(set1.issubset(set2))    #--> True
# В этом примере set2 содержит все элементы set1. Это означает,
# что set1 – подмножество set2. Это также означает, что set2 – надмножество set1.


# Для определения, является ли одно из множеств надмножеством другого, используется метод issuperset()
# set1 = {'a', 'b', 'c', 'd', 'e'}
# set2 = {'c', 'e'}
# print(set1.issuperset(set2))    #--> True
# В этом примере set1 содержит все элементы set2. Это означает,
# что set1 – надмножество set2. Это также означает, что set2 – подмножество set1.

# Для определения отсутствия общих элементов в множествах используется метод isdisjoint()
# Данный метод возвращает значение True, если множества не имеют общих элементов, и  False, когда
# множества имеют общие элементы.

# set1 <= set2 , set1.issubset(set2) - Возвращает True, если set1 является подмножеством set2
# set1 >= set2 , set1.issuperset(set2) - Возвращает True, если set1 является надмножеством set2
# set1 < set2 - Эквивалентно set1 <= set2 and set1 != set2 (строгое подмножество)
# set1 > set2 - Эквивалентно set1 >= set2 and set1 != set2 (строгое надмножество)


# Одинаковые цифры
# print(("YES", "NO")[set(input()).isdisjoint(input())])

# Все цифры
# print(['NO', 'YES'][set(input()) >= set(input())])

# Урок информатики
# a, b, c = (set(int(i) for i in input().split()) for i in range(3))
# print(*sorted(set(a.intersection(b).difference(c)))[::-1])

# Урок математики
# set1, set2, set3 = [set([int(i) for i in input().split()]) for k in range(3)]
# print(*sorted((set1 | set2 | set3) - (set1 & set2 & set3)))


# Урок физики
# set_1, set_2, set_3 = (set(input().split()) for _ in range(3))
# print(*(sorted(set_3 - (set_1 | set_2), key=int, reverse=True)))

# Урок биологии
# a = set(input().split() + input().split() + input().split())
# b = set(map(str, range(11)))
# print(*sorted(b - a, key=int))

# 8.8 Генераторы множеств и frozenset
# digits = set(input())
# при вводе строки '12345' создает множество символов {'1', '2', '3', '4', '5'},
# а не множество цифр {1, 2, 3, 4, 5}.

# digits = {int(c) for c in input()}
#
# Примеры использования генератора множеств
# 1. Создать множество, заполненное квадратами целых чисел от 0 до 9 можно так:
#
# squares = {i ** 2 for i in range(10)}
# 2. Создать множество, заполненное кубами целых чисел от 10 до 20 можно так:
#
# cubes = {i ** 3 for i in range(10, 21)}
# 3. Создать множество, заполненное символами строки можно так:
#
# chars = {c for c in 'abcdefg'}
#
# В генераторах множеств можно использовать условный оператор. Например, если требуется создать
# множество, заполненное только цифрами некоторой строки, то мы можем написать такой код:
#
# digits = {int(d) for d in 'abcd12ef78ghj90' if d.isdigit()}


# получить множество, содержащее первую букву каждого слова (в нижнем регистре) списка words
# items = [10, '30', 30, 10, '56', 34, '12', 90, 89, 34, 45, '67', 12, 10, 90, 23, '45', 56, '56', 1, 5, '6', 5]
# myset = {int(d) for d in items}
# print(*sorted(myset))
#
#
# получить множество, содержащее первую букву каждого слова (в нижнем регистре) списка words
# words = ['Plum', 'Grapefruit', 'apple', 'orange', 'pomegranate', 'Cranberry', 'lime', 'Lemon', 'grapes', 'persimmon',
#          'tangerine', 'Watermelon', 'currant', 'Almond']
# myset = {d[0].lower() for d in words}
# print(*sorted(myset))
#

# получить множество, содержащее уникальные слова (в нижнем регистре) строки sentence
# sentence = '''My very photogenic mother died in a freak accident (picnic, lightning) when I was three, and, save for a pocket of warmth in the darkest past, nothing of her subsists within the hollows and dells of memory, over which, if you can still stand my style (I am writing under observation), the sun of my infancy had set: surely, you all know those redolent remnants of day suspended, with the midges, about some hedge in bloom or suddenly entered and traversed by the rambler, at the bottom of a hill, in the summer dusk; a furry warmth, golden midges.'''
# myset = {d.lower().strip('.,;:-?!()') for d in sentence.split()}
# print(*sorted(myset))

# получить множество, содержащее уникальные слова строки sentence длиною меньше 4 символов
# sentence = '''My very photogenic mother died in a freak accident (picnic, lightning) when I was three, and, save for a pocket of warmth in the darkest past, nothing of her subsists within the hollows and dells of memory, over which, if you can still stand my style (I am writing under observation), the sun of my infancy had set: surely, you all know those redolent remnants of day suspended, with the midges, about some hedge in bloom or suddenly entered and traversed by the rambler, at the bottom of a hill, in the summer dusk; a furry warmth, golden midges.'''
# myset = {d.lower().strip('.,:():;!?') for d in sentence.split() if len(d.strip('.,:():;!?')) < 4}
# print(*sorted(myset))

# выбрал из списка files уникальные имена файлов c расширением .png

# files = ['python.png', 'qwerty.py', 'stepik.png', 'beegeek.org', 'windows.pnp', 'pen.txt', 'phone.py', 'book.txT',
#          'board.pNg', 'keyBoard.jpg', 'Python.PNg', 'apple.jpeg', 'png.png', 'input.tXt', 'split.pop', 'solution.Py',
#          'stepik.org', 'kotlin.ko', 'github.git']
# myset = {d.lower() for d in files if d[-3::].lower() == 'png'}
# print(*sorted(myset))

# Frozenset
# Кортеж (тип tuple) – неизменяемая версия списка (тип list), а замороженное множество (тип frozenset) – неизменяемая
# версия обычного множества (тип set).
# myset1 = frozenset({1, 2, 3})                         # на основе множества
# myset2 = frozenset([1, 1, 2, 3, 4, 4, 4, 5, 6, 6])    # на основе списка
# myset3 = frozenset('aabcccddee')                      # на основе строки
#
# print(myset1)
# print(myset2)
# print(myset3)

# Над замороженными множествами можно производить все операции, которые можно производить над обычными множествами:
#
# объединение множеств: метод union() или оператор |;
# пересечение множеств: метод intersection() или оператор &;
# разность множеств: метод difference() или оператор -;
# симметрическая разность множеств: метод symmetric_difference() или оператор ^.
# Приведенный ниже код:
#
# myset1 = frozenset('hello')
# myset2 = frozenset('world')
#
# print(myset1 | myset2)
# print(myset1 & myset2)
# print(myset1 ^ myset2)

# Методы изменяющие множество отсутствуют у замороженных множеств:
# add()
# remove()
# discard()
# pop()
# clear()
# update()
# intersection_update()
# difference_update()
# symmetric_difference_update()


# n = int(input())
# m = int(input())
# k = int(input())
# p = int(input())
#
# print(n+p-m-k)

# arr = [int(elem) for elem in input().split()]
# print(len(arr) - len(set(arr)))

# def is_repeat(arr, n):
#     for i in range(n + 1):
#         s = input()
#         length = len(arr)
#         arr.add(s)
#         if length == len(arr):
#             return 'REPEAT'
#     return 'OK'
#
#
# print(is_repeat(arr, n))


# m = int(input())
# n = int(input())
# library = []
# toRead = []
#
# for i in range(m):
#     library.append(input())
#
# for i in range(n):
#     toRead.append(input())
#
# for elem in toRead:
#     if elem in library:
#         print('YES')
#     else:
#         print('NO')


# arr1 = {int(elem) for elem in input().split()}
# arr2 = {int(elem) for elem in input().split()}
#
# if len(arr1.intersection(arr2)) == 0:
#     print('BAD DAY')
# else:
#     print(*sorted(arr1.intersection(arr2), reverse=True))


# arr1 = {int(elem) for elem in input().split()}
# arr2 = {int(elem) for elem in input().split()}
# if arr1 == arr2:
#     print('YES')
# else:
#     print('NO')


# m = int(input())
# n = int(input())
# maths = set()
# informatics = set()
# for i in range(m):
#     maths.add(input())
# for i in range(n):
#     informatics.add(input())
# print(len(maths.difference(informatics)))


# m = int(input())
# n = int(input())
# maths = set()
# informatics = set()
# for i in range(m):
#     maths.add(input())
# for i in range(n):
#     informatics.add(input())
# if len(maths.symmetric_difference(informatics)) == 0:
#     print('NO')
# else:
#     print(len(maths.symmetric_difference(informatics)))

# ///////////////////////////// 10.1 Введение в словари в Python ////////////////////////////////////
# my_dict = dict{}
# print(my_dict)

# my_dict = {1.12: 'aa', 67.9: 45, 3.11: 'ccc', 7.9: 'dd', 9.2: 'ee', 7.1: 'ff', 0.12: 'qq', 1.91: 'aa', 10.12: [1, 2, 3],
#            99.0: {9, 0, 1}}
# print(min(my_dict) + max(my_dict))

# Перебор элементов словаря
# Для вывода ключей словаря каждого на отдельной строке
# capitals = {'Россия': 'Москва', 'Франция': 'Париж', 'Чехия': 'Прага'}
# for key in capitals:
#     print(key)

# Для вывода значений словаря каждого на отдельной строке
# capitals = {'Россия': 'Москва', 'Франция': 'Париж', 'Чехия': 'Прага'}
# for key in capitals:
#     print(capitals[key])

# Для вывода элементов словаря каждого на отдельной строке
# capitals = {'Россия': 'Москва', 'Франция': 'Париж', 'Чехия': 'Прага'}
# for key in capitals:
#     print('Столица', key, '- это', capitals[key])

# Словарный метод keys() возвращает список ключей всех элементов словаря.
# capitals = {'Россия': 'Москва', 'Франция': 'Париж', 'Чехия': 'Прага'}
# for key in capitals.keys():     # итерируем по списку ['Россия', 'Франция', 'Чехия']
#     print(key)

# Словарный метод values() возвращает список значений всех элементов словаря.
# capitals = {'Россия': 'Москва', 'Франция': 'Париж', 'Чехия': 'Прага'}
# for value in capitals.values():     # итерируем по списку ['Москва', 'Париж', 'Прага']
#     print(value)


# Словарный метод items() возвращает список всех элементов словаря, состоящий из кортежей пар (ключ, значение)
# capitals = {'Россия': 'Москва', 'Франция': 'Париж', 'Чехия': 'Прага'}
# for item in capitals.items():
#     print(item)


# Используя магию распаковки кортежей, можно писать такой код:
# capitals = {'Россия': 'Москва', 'Франция': 'Париж', 'Чехия': 'Прага'}
# for key, value in capitals.items():
#     print(key, '-', value)


# Распаковка ключей словаря
# capitals = {'Россия': 'Москва', 'Франция': 'Париж', 'Чехия': 'Прага'}
# print(*capitals, sep='\n')

# Так как словарь состоит из пар, то и отсортировать его можно как по ключам, так и по значениям.
# Сортировка по ключам выполняется с использованием функции sorted().
# capitals = {'Россия': 'Москва', 'Англия': 'Лондон', 'Чехия': 'Прага', 'Бразилия':'Бразилиа'}
# for key in sorted(capitals):
#     print(key)

# Для сортировки словаря по значениям можно использовать функцию sorted() вместе с методом items().
# capitals = {'Россия': 'Москва', 'Англия': 'Лондон', 'Чехия': 'Прага', 'Бразилия':'Бразилиа'}
# for key, value in sorted(capitals.items(), key = lambda x: x[1]):
#     print(value)

# Проверка наличия ключа в словаре:
# capitals = {'Россия': 'Москва', 'Франция': 'Париж', 'Чехия': 'Прага'}
# if 'Россия' in capitals:
#     print('В словаре есть ключ Россия')
#
# Проверка наличия значения в словаре:
# capitals = {'Россия': 'Москва', 'Франция': 'Париж', 'Чехия': 'Прага'}
# if 'Париж' in capitals.values():
#     print('В словаре есть значение Париж')

# вывел имена всех пользователей (в алфавитном порядке), чей номер оканчивается на 88.
# users = [{'name': 'Todd', 'phone': '551-1414', 'email': 'todd@gmail.com'},
#          {'name': 'Helga', 'phone': '555-1618', 'email': 'helga@mail.net'},
#          {'name': 'Olivia', 'phone': '449-3141', 'email': ''},
#          {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@gmail.net'},
#          {'name': 'Ruslan', 'phone': '422-145-9098', 'email': 'rus-lan.cha@yandex.ru'},
#          {'name': 'John', 'phone': '233-421-32', 'email': ''},
#          {'name': 'Lara', 'phone': '+7998-676-2532', 'email': 'g.lara89@gmail.com'},
#          {'name': 'Alina', 'phone': '+7948-799-2434', 'email': 'ali.ch.b@gmail.com'},
#          {'name': 'Robert', 'phone': '420-2011', 'email': ''},
#          {'name': 'Riyad', 'phone': '128-8890-128', 'email': 'r.mahrez@mail.net'},
#          {'name': 'Khabib', 'phone': '+7995-600-9080', 'email': 'kh.nurmag@gmail.com'},
#          {'name': 'Olga', 'phone': '6449-314-1213', 'email': ''},
#          {'name': 'Roman', 'phone': '+7459-145-8059', 'email': 'roma988@mail.ru'},
#          {'name': 'Maria', 'phone': '12-129-3148', 'email': 'm.sharapova@gmail.com'},
#          {'name': 'Fedor', 'phone': '+7445-341-0545', 'email': ''},
#          {'name': 'Tim', 'phone': '242-449-3141', 'email': 'timm.ggg@yandex.ru'}]
# # sp = []
# # for i in users:
# #     if i['phone'][-1] == '8':
# #         sp.append(i['name'])
# # print(*sorted(sp))
#
# result = [user['name'] for user in users if user['phone'].endswith('8')]
# print(*sorted(result))


# # вывел имена всех пользователей (в алфавитном порядке), у которых нет информации об электронной почте.
# users = [{'name': 'Todd', 'phone': '551-1414', 'email': 'todd@gmail.com'},
#          {'name': 'Helga', 'phone': '555-1618'},
#          {'name': 'Olivia', 'phone': '449-3141', 'email': ''},
#          {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@gmail.net'},
#          {'name': 'Ruslan', 'phone': '422-145-9098', 'email': 'rus-lan.cha@yandex.ru'},
#          {'name': 'John', 'phone': '233-421-32', 'email': ''},
#          {'name': 'Lara', 'phone': '+7998-676-2532', 'email': 'g.lara89@gmail.com'},
#          {'name': 'Alina', 'phone': '+7948-799-2434'},
#          {'name': 'Robert', 'phone': '420-2011', 'email': ''},
#          {'name': 'Riyad', 'phone': '128-8890-128', 'email': 'r.mahrez@mail.net'},
#          {'name': 'Khabib', 'phone': '+7995-600-9080', 'email': 'kh.nurmag@gmail.com'},
#          {'name': 'Olga', 'phone': '6449-314-1213', 'email': ''},
#          {'name': 'Roman', 'phone': '+7459-145-8059'},
#          {'name': 'Maria', 'phone': '12-129-3148', 'email': 'm.sharapova@gmail.com'},
#          {'name': 'Fedor', 'phone': '+7445-341-0545', 'email': ''},
#          {'name': 'Tim', 'phone': '242-449-3141', 'email': 'timm.ggg@yandex.ru'}]
#
# result = [user['name'] for user in users if len(user) < 3 or user['email'] == '']
# print(*sorted(result))

# Строковое представление
# sp = {'0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five', '6': 'six', '7': 'seven',
#       '8': 'eight', '9': 'nine'}
# for i in input():
#     print(sp[i], end=' ')


# Информация об учебных курсах
# data = {
#     "CS101": "CS101: 3004, Хайнс, 8:00",
#     "CS102": "CS102: 4501, Альварадо, 9:00",
#     "CS103": "CS103: 6755, Рич, 10:00",
#     "NT110": "NT110: 1244, Берк, 11:00",
#     "CM241": "CM241: 1411, Ли, 13:00"
# }
# print(data[input()])


# Набор сообщений
# d = {".": '1', ",": '11', "?": '111', "!": '1111', ":": '11111',
#      "A": '2', "B": '22', "C": '222',
#      "D": '3', "E": '33', "F": '333',
#      "G": '4', "H": '44', "I": '444',
#      "J": '5', "K": '55', "L": '555',
#      "M": '6', "N": '66', "O": '666',
#      "P": '7', "Q": '77', "R": '777', "S": '7777',
#      "T": '8', "U": '88', "V": '888',
#      "W": '9', "X": '99', "Y": '999', "Z": '9999',
#      " ": '0', '"':''
#      }
# for i in input().upper():
#     print(d[i], end='')

# Код Морзе
# morze = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..',
#          'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
#          'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '0': '-----',
#          '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
#          '9': '----.'}
# for i in input().upper():
#      if i in morze:
#           print(morze[i], end=' ')
# -----------------

# letters = [c for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789']
# morse = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '-----', '.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.']
# mydict = dict(zip(letters, morse))
# for i in input().upper():
#      if i in mydict:
#           print(mydict[i], end=' ')


# 10.3 Методы словарей

# метод items() – возвращает словарные пары ключ: значение, как соответствующие им кортежи;
# метод keys() – возвращает список ключей словаря;
# метод values() – возвращает список значений словаря.

# info = {'name': 'Sam',
#         'age': 28,
#         'job': 'Teacher'}
# info['name'] = 'Timur'                    # изменяем значение по ключу name
# info['email'] = 'timyr-guev@yandex.ru'    # добавляем в словарь элемент с ключом email
# print(info)

# Решим следующую задачу: пусть задан список чисел numbers , где некоторые числа встречаются неоднократно.
# Нужно узнать, сколько именно раз встречается каждое из чисел.
#
# numbers = [9, 8, 32, 1, 10, 1, 10, 23, 1, 4, 10, 4, 2, 2, 2, 2, 1, 10, 1, 2, 2, 32, 23, 23]
# Первый код, который приходит в голову имеет вид:
#
# numbers = [9, 8, 32, 1, 10, 1, 10, 23, 1, 4, 10, 4, 2, 2, 2, 2, 1, 10, 1, 2, 2, 32, 23, 23]
#
# result = {}
# for num in numbers:
#     result[num] += 1
# Однако, просто так сделать result[num] += 1 нельзя, так как если ключа num в словаре еще нет,
# то возникнет ошибка KeyError.
#
# Следующий программный код, полностью решает поставленную задачу:
#
# numbers = [9, 8, 32, 1, 10, 1, 10, 23, 1, 4, 10, 4, 2, 2, 2, 2, 1, 10, 1, 2, 2, 32, 23, 23]
#
# result = {}
# for num in numbers:
#     if num not in result:
#         result[num] = 1
#     else:
#         result[num] += 1
# Цикл for перебирает все элементы списка numbers и для каждого проверяет,
# присутствует ли он уже в качестве ключа в словаре result. Если значение отсутствует,
# значит число встретилось впервые и мы инициируем значение result[num] = 1. Если значение
# уже присутствует в словаре, увеличим result[num] на единицу.
#

# Этот код можно улучшить с помощью метода get().
# numbers = [9, 8, 32, 1, 10, 1, 10, 23, 1, 4, 10, 4, 2, 2, 2, 2, 1, 10, 1, 2, 2, 32, 23, 23]
#
# result = {}
# for num in numbers:
#     result[num] = result.get(num, 0) + 1
# Цикл for перебирает все элементы списка numbers и для каждого элемента с помощью метода get() мы
# получаем либо его значение из словаря result, либо значение по умолчанию, равное 0. К данному значению
# прибавляется единица, и результат записывается обратно в словарь по нужному ключу.


# Метод update() – реализует своеобразную операцию конкатенации для словарей. Он объединяет ключи и значения
# одного словаря с ключами и значениями другого. При совпадении ключей в итоге сохранится значение словаря,
# указанного в качестве аргумента метода update().

# info1 = {'name': 'Bob',
#         'age': 25,
#         'job': 'Dev'}
#
# info2 = {'age': 30,
#         'city': 'New York',
#         'email': 'bob@web.com'}
#
# info1.update(info2)
#
# print(info1)  #--> {'name': 'Bob', 'age': 30, 'job': 'Dev', 'city': 'New York', 'email': 'bob@web.com'}

# В Python 3.9 появились операторы | и |= которые реализуют операцию конкатенации словарей.
# Приведенный ниже код:
#
# info1 = {'name': 'Bob',
#         'age': 25,
#         'job': 'Dev'}
#
# info2 = {'age': 30,
#         'city': 'New York',
#         'email': 'bob@web.com'}
#
# info1 |= info2
#
# print(info1)
# аналогичен предыдущему коду.

# Метод setdefault() позволяет получить значение из словаря по заданному ключу, автоматически добавляя элемент словаря, если он отсутствует.
# Метод принимает два аргумента:
#      key: ключ, значение по которому следует получить, если таковое имеется в словаре, либо создать.
#      default: значение, которое будет использовано при добавлении нового элемента в словарь.

# В зависимости от значений параметров key и default возможны следующие сценарии работы данного метода.
# Сценарий 1. Если ключ key присутствует в словаре, то метод возвращает значение по заданному ключу
# (независимо от того, передан параметр default или нет).
# Приведенный ниже код:
#
# info = {'name': 'Bob',
#         'age': 25}
#
# name1 = info.setdefault('name')           # параметр default не задан
# name2 = info.setdefault('name', 'Max')    # параметр default задан
# print(name1)
# print(name2)
# выводит:
# Bob
# Bob
# Сценарий 2. Если ключ key отсутствует в словаре, то метод вставляет переданное значение default по заданному ключу.
# Приведенный ниже код:
# info = {'name': 'Bob',
#         'age': 25}
#
# job = info.setdefault('job', 'Dev')
# print(info)
# print(job)
# выводит:
# {'name': 'Bob', 'age': 25, 'job': 'Dev'}
# Dev
# При этом если значение default не передано в метод, то вставится значение None.

# Удаление элементов из словаря
# Существует несколько способов удаления элементов из словаря:
#
# оператор del;
# метод pop();
# метод popitem();
# метод clear().

# С помощью оператора del можно удалять элементы словаря по определенному ключу.
# Следующий программный код:
#
# info = {'name': 'Sam',
#         'age': 28,
#         'job': 'Teacher',
#         'email': 'timyr-guev@yandex.ru'}
#
# del info['email']    # удаляем элемент имеющий ключ email
# del info['job']      # удаляем элемент имеющий ключ job
#
# print(info)
# выводит (порядок элементов может отличаться):
## {'name': 'Sam', 'age': 28}

# Оператор del удаляет из словаря элемент по заданному ключу вместе с его значением.
# Если требуется получить само значение удаляемого элемента, то нужен метод pop().
# Следующий программный код:
#
# info = {'name': 'Sam',
#         'age': 28,
#         'job': 'Teacher',
#         'email': 'timyr-guev@yandex.ru'}
#
# email = info.pop('email')          # удаляем элемент по ключу email, возвращая его значение
# job = info.pop('job')              # удаляем элемент по ключу job, возвращая его значение
#
# print(email)
# print(job)
# print(info)
# выводит:
#
# timyr-guev@yandex.ru
# Teacher
# {'name': 'Sam', 'age': 28}

# позволяет реализовать безопасное удаление элемента из словаря:
# surname = info.pop('surname', None)
# Если ключа surname в словаре нет, то в переменной surname будет храниться значение None.

# Метод popitem() удаляет из словаря последний добавленный элемент и возвращает удаляемый элемент в
# виде кортежа (ключ, значение).
#
# info = {'name': 'Bob',
#      'age': 25,
#      'job': 'Dev'}
#
# info['surname'] = 'Sinclar'
#
# item = info.popitem()
#
# print(item)
# print(info)
# выводит:
#
# ('surname', 'Sinclar')
# {'name': 'Bob', 'age': 25, 'job': 'Dev'}

# Метод clear() удаляет все элементы из словаря.
# Метод copy() создает поверхностную копию словаря.
# Оператор присваивания (=) не копирует словарь, а лишь присваивает ссылку на старый словарь новой переменной.


# Примечание 1. Словарь можно использовать вместо нескольких вложенных условий,
# если вам нужно проверить число на равенство. Например вместо

# num = int(input())
# if num == 1:
#     description = 'One'
# elif num == 2:
#     description = 'Two'
# elif num == 3:
#     description = 'Three'
# else:
#     description = 'Unknown'
# print(description)
#
# можно написать
#
# num = int(input())
# description = {1: 'One', 2: 'Two', 3: 'Three'}
# print(description.get(num, 'Unknown'))


# # чтобы в переменной result хранился словарь, в котором ключи
# # – числа от 1 до 15 (включительно), а значения представляют собой квадраты ключей.
# key = [i for i in range(1,16)]
# value = [i**2 for i in range(1,16)]
# result = dict(zip(key, value))
# print(result)
#
# result = {}
# for i in range(1, 16):
#     result[i] = i * i
#
# result = {}
# result = {i: i**2 for i in range(1, 16)}

# result = {i: i ** 2 for i in range(1, 16)}


# объединил содержимое двух словарей dict1 и dict2 по ключам, складывая значения по одному и тому же ключу,
# # в случае, если ключ присутствует в обоих словарях
# dict1 = {'a': 100, 'z': 333, 'b': 200, 'c': 300, 'd': 45, 'e': 98, 't': 76, 'q': 34, 'f': 90, 'm': 230}
# dict2 = {'a': 300, 'b': 200, 'd': 400, 't': 777, 'c': 12, 'p': 123, 'w': 111, 'z': 666}
#
# for key, value in dict2.items():
#     dict1[key] = dict1.setdefault(key, 0) + value
# result = dict1.copy()


# Дополните приведенный код так, чтобы в переменной result хранился словарь,
# в котором для каждого символа строки text будет подсчитано количество его вхождений.
# text = 'footballcyberpunkextraterritorialityconversationalistblockophthalmoscopicinterdependencemamauserfff'
# result = {l: text.count(l) for l in set(text)}
# print(result)


# s = 'orange strawberry barley gooseberry apple apricot barley currant orange melon pomegranate banana banana orange barley apricot plum grapefruit banana quince strawberry barley grapefruit banana grapes melon strawberry apricot currant currant gooseberry raspberry apricot currant orange lime quince grapefruit barley banana melon pomegranate barley banana orange barley apricot plum banana quince lime grapefruit strawberry gooseberry apple barley apricot currant orange melon pomegranate banana banana orange apricot barley plum banana grapefruit banana quince currant orange melon pomegranate barley plum banana quince barley lime grapefruit pomegranate barley'
#
# result = {}  # создаем словарь
#
# for i in s.split():  # проводим подсчет слов в тексте
#     result[i] = result.get(i, 0) + 1  # если слова нет то значение = 0 иначе добавляем +1
#
# s = max(result.values())  # узнаем максимальное значение повторяющегося слова и сохраняем его в переменной s
#
# print(min([key for key, value in result.items() if
#            value == s]))  # создаем список в который, способом перебора добовляем слова повторение которых равно значению s, с помощью min узнаем ккакое зи максимально одинаково аовторяются являются меньше в лексикографическом порядке

#
# pets = [('Hatiko', 'Parker', 'Wilson', 50),
#         ('Rusty', 'Josh', 'King', 25),
#         ('Fido', 'John', 'Smith', 28),
#         ('Butch', 'Jake', 'Smirnoff', 18),
#         ('Odi', 'Emma', 'Wright', 18),
#         ('Balto', 'Josh', 'King', 25),
#         ('Barry', 'Josh', 'King', 25),
#         ('Snape', 'Hannah', 'Taylor', 40),
#         ('Horry', 'Martha', 'Robinson', 73),
#         ('Giro', 'Alex', 'Martinez', 65),
#         ('Zooma', 'Simon', 'Nevel', 32),
#         ('Lassie', 'Josh', 'King', 25),
#         ('Chase', 'Martha', 'Robinson', 73),
#         ('Ace', 'Martha', 'Williams', 38),
#         ('Rocky', 'Simon', 'Nevel', 32)]
#
# result = {}
# for p, *name in pets:
#     result.setdefault(tuple(name), []).append(p)

# # Самое редкое слово 🌶️
# li = [word.strip(".,!?:;-").lower() for word in input().split()]
# di = {word: li.count(word) for word in li}
# m = min(di.values())
#
# for k, v in sorted(di.items(), key=lambda t: t[0]):
#     if v == m:
#         print(k)
#         break


# # Исправление дубликатов 🌶️
# d, l = {}, []
#
# for c in input().split():
#     if c not in l:
#         l.append(c)
#     else:
#         d[c] = d.get(c, 0) + 1
#         l.append(c + '_' + str(d[c]))
#
# print(*l)


# # Словарь программиста
# data =  [(input().split(':')) for i in range(int(input()))]
# data = {i[0].lower(): i[1].strip() for i in data}
# for i in [input().lower() for i in range(int(input()))]:
#     print(data.get(i, "Не найдено"))


# Анаграммы 1
# s = sorted(input())
# dct1 = dict(zip(range(len(s)), s))
#
# s = sorted(input())
# dct2 = dict(zip(range(len(s)), s))
#
# print('YES' if dct1 == dct2 else 'NO')

# print('YES' if sorted(input()) == sorted(input()) else 'NO')

# # Анаграммы 2
# s1 = [i for i in input().lower() if i.isalpha()]
# s2 = [i for i in input().lower() if i.isalpha()]
# print('YES' if sorted(s1) == sorted(s2) else 'NO')

# Словарь синонимов
# lovar=dict([[i for i in input().split(' ')] for i in range(int(input()))])
# a=input()
# for key,value in lovar.items():
#     if key==a:
#         print(value)
#     if value==a:
#         print(key)


# # Страны и города
# d = {}
# for _ in range(int(input())):
#     s = input().split()
#     d[s[0]] = s[1:]
# for _ in range(int(input())):
#     city = input()
#     for country, cities in d.items():
#         if city in cities:
#             print(country)

# Телефонная книга
# res = {}
# for i in range(int(input())):
#     a, b = input().lower().split()
#     res[b] = res.get(b, []) + [a]
#
# for i in range(int(input())):
#     name = input().lower()
#     print(*res.get(name, ['абонент не найден']))


# # Секретное слово
# f = input()
# d = {}
# for u in f:
#     d.setdefault(f.count(u), u)
#
# for _ in range(int(input())):
#     key, value = input().split(':')
#     f = f.replace(d[int(value)], key)
# print(f)

# 10.5 Вложенные словари и генераторы словарей
# ids = ['emp1', 'emp2', 'emp3']
# emp_info = [{'name': 'Timur', 'job': 'Teacher'},
#             {'name': 'Ruslan', 'job': 'Developer'},
#             {'name': 'Rustam', 'job': 'Tester'}]
# info = dict(zip(ids, emp_info))


# Чтобы изменить значение определенного элемента во вложенном словаре, необходимо обратиться
# к его ключу и использовать оператор присвоения (=).
#
# Приведенный ниже код:
#
# info = {'emp1': {'name': 'Timur', 'job': 'Teacher'},
#         'emp2': {'name': 'Ruslan', 'job': 'Developer'},
#         'emp3': {'name': 'Rustam', 'job': 'Tester'}}
#
# info['emp1']['job'] = 'Manager'
#
# print(info['emp1'])
# выводит:
#
# {'name': 'Timur', 'job': 'Manager'}


# Итерация по вложенным словарям
# Итерации по вложенным словарям осуществляются как правило двумя циклами for (иногда достаточно одного цикла).
#
# info = {'emp1': {'name': 'Timur', 'job': 'Teacher'},
#         'emp2': {'name': 'Ruslan', 'job': 'Developer'},
#         'emp3': {'name': 'Rustam', 'job': 'Tester'}}
# for emp in info:
#     print('Employee ID:', emp)
#     for key in info[emp]:
#         print(key + ':', info[emp][key])
#     print()
# выводит:
# Employee ID: emp1
# name: Timur
# job: Teacher
#
# Employee ID: emp2
# name: Ruslan
# job: Developer
#
# Employee ID: emp3
# name: Rustam
# job: Tester
#


# Аналогичного результата можно было добиться с помощью метода items():
#
# info = {'emp1': {'name': 'Timur', 'job': 'Teacher'},
#         'emp2': {'name': 'Ruslan', 'job': 'Developer'},
#         'emp3': {'name': 'Rustam', 'job': 'Tester'}}
#
# for emp, inf in info.items():
#     print('Employee ID:', emp)
#     for key in inf:
#         print(key + ':', inf[key])
#     print()


# Генераторы словарей
# squares = {i: i**2 for i in range(6)}
# {ключ: значение for переменная in последовательность}

## 1. Генератор словаря при итерировании по строке.
# dct = {c: c * 3 for c in 'ORANGE'}
# print(dct)  #--> {'O': 'OOO', 'R': 'RRR', 'A': 'AAA', 'N': 'NNN', 'G': 'GGG', 'E': 'EEE'}


##2. Для вычисления ключа и значения в генераторе словаря могут быть использованы выражения.
# lst = ['ReD', 'GrEeN', 'BlUe']
# dct = {c.lower(): c.upper() for c in lst}
# print(dct)   #-->  {'red': 'RED', 'green': 'GREEN', 'blue': 'BLUE'}

# ##3. Извлечение из словаря элементов с определенными ключами.
# dict1 = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F'}
# selected_keys = [0, 2, 5]
# dict2 = {k: dict1[k] for k in selected_keys}
# print(dict2)   #-->  {0: 'A', 2: 'C', 5: 'F'}

##Условия в генераторе словарей
# squares = {i: i**2 for i in range(10) if i % 2 == 0}
# print(squares)


##Генераторы вложенных словарей
# squares = {i: {j: j**2 for j in range(i + 1)} for i in range(5)}
# for value in squares.values():
#     print(value)
# выводит:
#
# {0: 0}
# {0: 0, 1: 1}
# {0: 0, 1: 1, 2: 4}
# {0: 0, 1: 1, 2: 4, 3: 9}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
#


# получить словарь result , в котором ключом будет позиция числа в списке numbers (начиная с 00),
# а значением – его квадрат.
# numbers = [34, 10, -4, 6, 10, 23, -90, 100, 21, -35, -95, 1, 36, -38, -19, 1, 6, 87]
# result = {i:numbers[i]**2 for i in range(len(numbers))}
# print(result)


# # получить словарь result, состоящий из всех элементов словаря colors, кроме тех,
# # у которых значением является None.
# colors = {'c1': 'Red', 'c2': 'Grey', 'c3': None, 'c4': 'Green', 'c5': 'Yellow', 'c6': 'Pink', 'c7': 'Orange', 'c8': None, 'c9': 'White', 'c10': 'Black', 'c11': 'Violet', 'c12': 'Gold', 'c13': None, 'c14': 'Amber', 'c15': 'Azure', 'c16': 'Beige', 'c17': 'Bronze', 'c18': None, 'c19': 'Lilac', 'c20': 'Pearl', 'c21': None, 'c22': 'Sand', 'c23': None}
# result = {key: value for key, value in colors.items() if value != None}


# получить словарь result, состоящий из всех элементов словаря favorite_numbers ,
# значения которых являются двузначными числами.
# favorite_numbers = {'timur': 17, 'ruslan': 7, 'larisa': 19, 'roman': 123, 'rebecca': 293, 'ronald': 76, 'dorothy': 62, 'harold': 36, 'matt': 314, 'kim': 451, 'rosaly': 18, 'rustam': 89, 'soltan': 111, 'amir': 654, 'dima': 390, 'amiran': 777, 'geor': 999, 'sveta': 75, 'rita': 909, 'kirill': 404, 'olga': 271, 'anna': 55, 'madlen': 876}
# result = {i: favorite_numbers[i] for i in favorite_numbers if int(favorite_numbers[i]/10)  in range(1, 10)}


# # получить словарь result, состоящий из всех элементов словаря months,
# # в которых ключ и значение поменялись местами.
# months = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}
# result = {value: key for key, value in months.items()}


# # В переменной s хранится строка пар число:слово. Дополните приведенный код, используя генератор,
# # # чтобы получить словарь result, в котором числа будут ключами, а слова – значениями.
# #
# # s = '1:men 2:kind 90:number 0:sun 34:book 56:mountain 87:wood 54:car 3:island 88:power 7:box 17:star 101:ice'
# # result = {int(key): value for key, value in (a.split(':') for a in s.split())}


# # спользуя генератор, дополните приведенный код, чтобы получить словарь result , где ключом будет элемент
# # списка numbers, а значением – отсортированный по возрастанию список всех его делителей начиная с 1.
# numbers = [34, 10, 4, 6, 10, 23, 90, 100, 21, 35, 95, 1, 36, 38, 19, 1, 6, 87, 1000, 13456, 360]
# result = {key: sorted([n for n in range(1, key + 1) if key % n == 0]) for key in numbers}


# # получить словарь result, в котором ключом будет строка – элемент списка words, а значением – список соответствующих
# # кодов ASCII символов данной строки
# words = ['hello', 'bye', 'yes', 'no', 'python', 'apple', 'maybe', 'stepik', 'beegeek']
# result = {word: [ord(w) for w in word] for word in words}


# получить словарь result, состоящий из всех элементов словаря letters , за исключением тех, ключи которых
# есть в списке remove_keys.
# letters = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J', 10: 'K', 11: 'L', 12: 'M', 13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T', 20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y', 26: 'Z'}
# remove_keys = [1, 5, 7, 12, 17, 19, 21, 24]
# result = {key: value for key, value in letters.items() if key not in remove_keys}


# # олучить словарь result, состоящий из всех элементов словаря students,
# # где указан рост больше 167 см, а вес меньше 75 кг.
# students = {'Timur': (170, 75), 'Ruslan': (180, 105), 'Soltan': (192, 68), 'Roman': (175, 70), 'Madlen': (160, 50), 'Stefani': (165, 70), 'Tom': (190, 90), 'Jerry': (180, 87), 'Anna': (172, 67), 'Scott': (168, 78), 'John': (186, 79), 'Alex': (195, 120), 'Max': (200, 110), 'Barak': (180, 89), 'Donald': (170, 80), 'Rustam': (186, 100), 'Alice': (159, 59), 'Rita': (170, 80), 'Mary': (175, 69), 'Jane': (190, 80)}
# result = {key: value for key, value in students.items() if value[0] > 167 and value[1] < 75}


# # получить словарь result, в котором ключом является первый элемент каждого кортежа, а значением – кортеж
# # из оставшихся двух элементов.
# tuples = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12), (13, 14, 15), (16, 17, 18), (19, 20, 21), (22, 23, 24), (25, 26, 27), (28, 29, 30), (31, 32, 33), (34, 35, 36)]
# result = {k: tuple(v) for k, *v in tuples}


# # получить список result, содержащий вложенные словари в соответствии с образцом:
# # [{'S001': {'Camila Rodriguez': 86}}, {'S002': {'Juan Cruz': 98}},...].
# student_ids = ['S001', 'S002', 'S003', 'S004', 'S005', 'S006', 'S007', 'S008', 'S009', 'S010', 'S011', 'S012', 'S013']
# student_names = ['Camila Rodriguez', 'Juan Cruz', 'Dan Richards', 'Sam Boyle', 'Batista Cesare', 'Francesco Totti', 'Khalid Hussain', 'Ethan Hawke', 'David Bowman', 'James Milner', 'Michael Owen', 'Gary Oldman', 'Tom Hardy']
# student_grades = [86, 98, 89, 92, 45, 67, 89, 90, 100, 98, 10, 96, 93]
# result = [{student_ids[i]: {student_names[i]: student_grades[i]}} for i in range(len(student_ids))]


# # вывел все электронные адреса в алфавитном порядке, каждый на отдельной строке, в формате username @ domain.
# emails = {'nosu.edu': ['timyr', 'joseph', 'svetlana.gaeva', 'larisa.mamuk'],
#           'gmail.com': ['ruslan.chaika', 'rustam.mini', 'stepik-best'],
#           'msu.edu': ['apple.fruit', 'beegeek', 'beegeek.school'],
#           'yandex.ru': ['surface', 'google'],
#           'hse.edu': ['tomas-henders', 'cream.soda', 'zivert'],
#           'mail.ru': ['angel.down', 'joanne', 'the.fame.moster']}
# arr = []
#
# for elem in emails:
#         for address in emails[elem]:
#                 arr.append(address + '@' + elem)
#
# for elem in sorted(arr):
#         print(elem)


# # Минутка генетики
# d = {'A': 'U', 'C': 'G', 'G': 'C', 'T': 'A'}
# arr = [d[elem] for elem in input()]
#
# print(''.join(arr))

# # Порядковый номер
# s = input().split()
# arr = []
# d = {}
#
# for elem in s:
#     if elem in d:
#         d[elem] += 1
#         arr.append(d[elem])
#     else:
#         d[elem] = 1
#         arr.append(d[elem])
#
# print(*arr)

# # Scrabble game
# d = {'A': 1, 'E': 1, 'I': 1, 'L': 1, 'N': 1, 'O': 1, 'R': 1, 'S': 1, 'T': 1, 'U': 1, 'D': 2, 'G': 2, 'B': 3, 'C': 3,
#      'M': 3, 'P': 3, 'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4, 'K': 5, 'J': 8, 'X': 8, 'Q': 10, 'Z': 10}
#
# summa = 0
#
# for elem in input():
#     summa += d[elem]
#
# print(summa)

# # Строка запроса
# def build_query_string(params):
#     result = ''
#     for elem in sorted(params):
#         result += elem
#         result += '='
#         result += str(params[elem])
#         result += '&'
#     return result[:-1]


# # Слияние словарей 🌶️
# def merge(values):
#     result = {}
#     for elem in values:
#         for i in elem:
#             if i in result:
#                 result[i].add(elem[i])
#             else:
#                 result[i] = set()
#                 result[i].add(elem[i])
#
#     return result

# # Опасный вирус 😈
# s = {'write': 'W', 'read': 'R','execute': 'X'}
# d = {}
#
# n = int(input())
#
# for i in range(n):
#     arr = input().split()
#     d[arr[0]] = arr[1:]
#
# m = int(input())
#
# for i in range(m):
#     arr = input().split()
#     if s[arr[0]] in d[arr[1]]:
#         print('OK')
#     else:
#         print('Access denied')

# # Покупки в интернет-магазине 🌶️
# n = int(input())
# d = {}
#
# for i in range(n):
#     arr = input().split()
#     if arr[0] in d:
#         if arr[1] in d[arr[0]]:
#             d[arr[0]][arr[1]] += int(arr[2])
#         else:
#             d[arr[0]][arr[1]] = int(arr[2])
#     else:
#         d[arr[0]] = {arr[1]: int(arr[2])}
#
# for name in sorted(d):
#     print(name + ':')
#     for product in sorted(d[name]):
#         print(product + ' ' + str(d[name][product]))
#
#
# 12.1 Модуль random. Часть 1

# Функция randint() принимает два обязательных аргумента a и b и возвращает
# псевдослучайное целое число из отрезка [a;b], Левая и правая граница a и b включаются в диапазон
# import random
# num1 = random.randint(0, 17)

# Функция randrange() возвращает случайно выбранное число из последовательности чисел.
# import random
# num = random.randrange(10)
# возвратит случайно выбранное число из последовательности чисел от 0 до конечного предела, исключая сам предел

# Функции randint() и randrange() возвращают псевдослучайное целое число. А вот функция random() возвращает
# псевдослучайное число с плавающей точкой (вещественное число). В функцию random() никаких аргументов
# не передается. Функция random() возвращает случайное число с плавающей точкой в
# диапазоне от 0 до 1 (исключая 1).
# import random
# num = random.random()

# Функция uniform() тоже возвращает случайное число с плавающей точкой, но при этом она позволяет
# задавать диапазон для отбора значений.
# псевдослучайное число с плавающей точкой из диапазона [1.5;17.3] (включительно):
# import random
# num = random.uniform(1.5, 17.3)

# Функция seed() явно устанавливает начальное значение для генератора случайных чисел
# import random
#
# random.seed(17)   # явно устанавливаем начальное значение для генератора случайных чисел
#
# for _ in range(10):
#     print(random.randint(1, 100))
#

# import random
# for i in range(int(input())):
#     if random.randint(0,1):
#         print('Орел')
#     else:
#         print('Решка')

# import random
# n = int(input())    # количество попыток
# for _ in range(n):
#     num = random.randint(0, 1)
#     if num == 0:
#         print('Орел')
#     else:
#         print('Решка')

# import random
# n = int(input())    # количество попыток
# for _ in range(n):
#     num = random.randint(1, 6)
#     print(num)


# генерирует случайный пароль
# import random
# length = int(input())    # длина пароля
# for _ in range(length):
#     r = random.randint(0,1)  #регистр
#     if r == 0:
#         pas = random.randint(65,90)
#     else:
#         pas = random.randint(97, 122)
#     print(chr(pas),end='')

# # Лотерейный билет
# import random
# s = set()
# while len(s) < 7:
#     s.add(random.randint(1, 49))
# print(*sorted(s))


# Метод shuffle() принимает список в качестве обязательного аргумента и перемешивает его случайным образом.
# import random
# numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# random.shuffle(numbers)
# print(numbers)   #--> [4, 7, 8, 1, 2, 3, 6, 5]

# Метод choice() принимает список (строку, кортеж) в качестве обязательного аргумента и возвращает один
# случайный элемент.

# Метод sample() принимает два обязательных аргумента: первый – список (строка, кортеж, множество),
# второй – количество случайных элементов. Возвращает список из указанного количества уникальных
# (имеющих разные индексы) случайных элементов.

# # в модуле string остались удобные константные строки
# import string
#
# print(string.ascii_letters)
# print(string.ascii_uppercase)
# print(string.ascii_lowercase)
# print(string.digits)
# print(string.hexdigits)
# print(string.octdigits)
# print(string.punctuation)
# print(string.printable)
# выводит:
#
# abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
# ABCDEFGHIJKLMNOPQRSTUVWXYZ
# abcdefghijklmnopqrstuvwxyz
# 0123456789
# 0123456789abcdefABCDEF
# 01234567
# !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
# 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ \t\n\r\x0b\x0c


# generate_ip()
# import random
# def generate_ip():
#     numbers = [i for i in range(256)]
#     ip = str(random.choice(numbers)) + '.' + str(random.choice(numbers)) + '.' + str(random.choice(numbers)) + '.' + str(random.choice(numbers))
#     return ip
#
# from random import randrange as r
# def generate_ip():
#     return f'{r(256)}.{r(256)}.{r(256)}.{r(256)}'

# генерирует и возвращает случайный корректный почтовый индекс Латверии.
# import string, random
# from random import randrange as r
# def generate_index():
#     return f'{random.choice(string.ascii_uppercase)}{random.choice(string.ascii_uppercase)}{r(1,9)}{r(1,9)}_{r(1,9)}{r(1,9)}{random.choice(string.ascii_uppercase)}{random.choice(string.ascii_uppercase)}'
#
# print(generate_index())


# перемешивает случайным образом содержимое матрицы (двумерного списка).
# import random
# matrix = [[1, 2, 3, 4],
#           [5, 6, 7, 8],
#           [9, 10, 11, 12],
#           [13, 14, 15, 16]]
# random.shuffle(matrix)
# print(matrix)

# с помощью модуля random генерирует 100 случайных номеров лотерейных билетов
# и выводит их каждый на отдельной строке

# from random import randrange
# tickets = set()
# while len(tickets) != 100:
#     tickets.add(randrange(1000000, 10000000))
# print(*tickets, sep='\n')

# Напишите программу, которая считывает одно слово и выводит с помощью модуля random его случайную анаграмму.
# import random
# a = list(input())
# random.shuffle(a)
# print(''.join(a))
#


# с помощью модуля random генерирует и выводит случайную карточку для игры в бинго.
# import random
# num = random.sample(range(1, 76), 25)
# num[12] = 0
# for i in range(len(num)):
#     print(str(num[i]).ljust(3), end = '')
#     if i in [4, 9, 14, 19]:
#         print()


# Тайный друг 🌶️
# from random import *
# fri = [input() for _ in range(int(input()))]
# fricop = fri.copy()
# a = 0
# def rand(a, b):
# 	r = 0
# 	for i, j in zip(a, b):
# 		if i!=j:
# 			r+=1
# 	return r
# while a != len(fri):
# 	shuffle(fricop)
# 	a = rand(fri, fricop)
# for k, l in zip(fri, fricop):
# 	print(k,'-',l)


# Генератор паролей 1
# import random
# n, m = int(input()), int(input())
# s = [i for i in '23456789']
# s.extend([chr(i) for i in range(ord('a'), ord('z')) if i not in [ord('l'),ord('i'), ord('o')] ])
# s.extend([chr(i) for i in range(ord('A'), ord('Z')) if i not in [ord('L'),ord('I'), ord('O')] ])
# for _ in range(n):
#     random.shuffle(s)
#     p = ""
#     for i in range(m):
#         p += s[i][0]
#     print(p)

# from string import *
# from random import sample
#
# LETTER = ''.join((set(ascii_letters) | set(digits)) - set('lI1oO0'))
#
# def generate_password(length):
#     return ''.join(sample(LETTER, length))
#
# def generate_passwords(count, length):
#     return [generate_password(length) for _ in range(count)]
#
# n, m = int(input()), int(input())
# print(*generate_passwords(n, m), sep='\n')

# Генератор паролей 2 🌶️
# import string
# import random
# def generate_password(length):
#     s = ''.join([i for i in (string.printable[:62]) if i not in '10OolI'])
#     return (''.join(random.sample(s[:8], 1) + random.sample(s[8:30], 1) + random.sample(s[30:], length - 2)))
# def generate_passwords(count):
#     return [generate_password(m) for _ in range(count)]
# n, m = int(input()), int(input())
# print(*generate_passwords(n), sep='\n')

# import random
#
# n = 10 ** 6
# k = 0
# s0 = 16
# for _ in range(n):
#     x = random.uniform(-2, 2)  # случайное число с плавающей точкой от 0 до 1
#     y = random.uniform(-2, 2)  # случайное число с плавающей точкой от 0 до 1
#
#     if x ** 3 + y ** 4 + 2 >= 0 and 3 * x + y ** 2 <= 2:  # если попадает в нужную область
#         k += 1
#
# print((k / n) * s0)

# import random
#
# n = 10 ** 6
# k = 0
# s0 = 4
# for _ in range(n):
#     x = random.uniform(-1, 1)  # случайное число с плавающей точкой от 0 до 1
#     y = random.uniform(-1, 1)  # случайное число с плавающей точкой от 0 до 1
#
#     if x ** 2 + y ** 2 <= 1:  # если попадает в нужную область
#         k += 1
#
# print((k / n) * s0)

# Болотная сортировка
# import random
#
# def is_sort(nums):                   # отсортирован ли список?
#     for i in range(len(nums) - 1):
#         if nums[i] > nums[i + 1]:
#             return False
#     return True
#
# def bogosort(nums):                  # реализация алгоритма болотной сортировки
#     while not is_sort(nums):
#         random.shuffle(nums)
#     return nums
#
# numbers = list(range(10))
# random.shuffle(numbers)              # перемешиваем начальный список
# print(numbers)                       # выводим начальный список
#
# sorted_numbers = bogosort(numbers)
#
# print(sorted_numbers)

# 13.1 Модуль decimal
# from decimal import *
#
# s = '9.73 8.84 8.92 9.60 9.32 8.97 8.53 1.26 6.62 9.85 1.85 1.80 0.83 6.75 9.74 9.11 9.14 5.03 5.03 1.34 3.52 8.09 7.89 8.24 8.23 5.22 0.30 2.59 1.25 6.24 2.14 7.54 5.72 2.75 2.32 2.69 9.32 8.11 4.53 0.80 0.08 9.36 5.22 4.08 3.86 5.56 1.43 8.36 6.29 5.13'
# numbers = sorted([Decimal(i) for i in s.split()])
# print(sum(numbers))
# print(*numbers[-1:-6:-1])

# from decimal import *
# num = abs(Decimal(input()))
# if num < 1:
#     a = num.as_tuple().digits
#     print(max(a))
# else:
#     print(max(num.as_tuple().digits) + min(num.as_tuple().digits))
#
#
# from decimal import *
# num = Decimal(input())
# cyphers = num.as_tuple().digits
# print(max(cyphers) + min(cyphers) * (abs(num) >= 1))

# from decimal import *
#
# d = Decimal(input())
# print(Decimal.sqrt(d) + Decimal.exp(d) + Decimal.ln(d) + Decimal.log10(d))


# 13.2 Модуль fractions
# from fractions import Fraction
## num1 = Fraction(3, 4)     # 3 - числитель, 4 - знаменатель
# num2 = Fraction('0.55')
# num3 = Fraction('1/9')
## print(num1, num2, num3, sep='\n')

# from fractions import Fraction
# num1 = Fraction(5, 1)        # 5/1 = 5
# num2 = Fraction(23, 23)      # 23/23 = 1
# print(num1, num2, sep='\n')


# Cвойства numerator и denominator
# Для получения числителя и знаменателя Fraction числа используются свойства numerator и denominator.
# Приведенный ниже код:
#
# from fractions import Fraction
# num = Fraction('5/16')
# print('Числитель дроби равен:', num.numerator)
# print('Знаменатель дроби равен:', num.denominator)
# выводит:
# Числитель дроби равен: 5
# Знаменатель дроби равен: 16


# В Python 3.8 появился метод as_integer_ratio(), который возвращает кортеж, состоящий из числителя
# и знаменателя данного Fraction числа.
# Приведенный ниже код:
# from fractions import Fraction
# num = Fraction('-5/16')
# print(num.as_integer_ratio())
# выводит:
# (-5, 16)
#
# Метод limit_denominator()
# Метод limit_denominator() возвращает самую близкую к данному числу рациональную дробь
# чей знаменатель не превосходит переданного аргумента.
# Приведенный ниже код:
# from fractions import Fraction
# import math
# print('PI =', math.pi)
# num = Fraction(str(math.pi))
# print('No limit =', num)
# for d in [1, 5,  50, 90, 100, 500, 1000000]:
#     limited = num.limit_denominator(d)
#     print(limited)
# выводит:
# PI = 3.141592653589793
# No limit = 3141592653589793/1000000000000000
# 3
# 16/5
# 22/7
# 267/85
# 311/99
# 355/113
# 3126535/995207
# Метод limit_denominator() позволяет получить очень точные рациональные приближения иррациональных чисел,
# что очень удобно во многих математических задачах.

# Примечание 1. Для того, чтобы каждый раз не писать название типа, можно использовать следующий код:
# from fractions import Fraction as F
# num1 = F('1/5') + F('3/2')
# num2 = F('1/4') * F('2/5')
# print(num1)
# print(num2)


# from fractions import Fraction
#
# numbers = ['6.34', '4.08', '3.04', '7.49', '4.45', '5.39', '7.82', '2.76', '0.71', '1.97', '2.54', '3.67', '0.14',
#            '4.29', '1.84', '4.07', '7.26', '9.37', '8.11', '4.30', '7.16', '2.46', '1.27', '0.29', '5.12', '4.02',
#            '6.95', '1.62', '2.26', '0.45', '6.91', '7.39', '0.52', '1.88', '8.38', '0.75', '0.32', '4.81', '3.31',
#            '4.63', '7.84', '2.25', '1.10', '3.35', '2.05', '7.87', '2.40', '1.20', '2.58', '2.46']
#
# # for i in numbers:
# #     print(f'{i} = {Fraction(i)}')
#
# [print(f'{i} = {Fraction(i)}') for i in numbers]

# вывел сумму наибольшего и наименьшего числа в виде обыкновенной дроби
# from fractions import Fraction as F
# from decimal import Decimal as D
# s = '0.78 4.3 9.6 3.88 7.08 5.88 0.23 4.65 2.79 0.90 4.23 2.15 3.24 8.57 0.10 8.57 1.49 5.64 3.63 8.36 1.56 6.67 1.46 5.26 4.83 7.13 1.22 1.02 7.82 9.97 5.40 9.79 9.82 2.78 2.96 0.07 1.72 7.24 7.84 9.23 1.71 6.24 5.78 5.37 0.03 9.60 8.86 2.73 5.83 6.50 0.123 0.00021'
# print(F(D(min(s.split())) + D(max(s.split()))))

# # Сократите дробь
# from fractions import Fraction as F
# print(F(int(input()), int(input())))

# Операции над дробями
# from fractions import Fraction as F
#
# a, b = input(), input()
# print(f'{a} + {b} = {F(a)+F(b)}')
# print(f'{a} - {b} = {F(a)-F(b)}')
# print(f'{a} * {b} = {F(a)*F(b)}')
# print(f'{a} / {b} = {F(a)/F(b)}')


# # Сумма дробей 1
# from fractions import Fraction
# n = int(input())
# p = 0
# for i in range(1, n + 1):
#     a = Fraction(1, i) ** 2
#     p += a
# print(Fraction(p))

# Сумма дробей 2
# from fractions import Fraction as F
#
#
# def fact(n):
#     res = 1
#     for i in range(1, n + 1): res *= i
#     return res
#
#
# n = int(input())
# print(sum([F(1, fact(i)) for i in range(1, n + 1)]))

# # Юный математик 🌶️
# from fractions import Fraction
# from math import gcd
#
# n = int(input())
#
# for i in range((n-1)//2, 0, -1):
#     if gcd(i, n-i) == 1:
#         print(Fraction(i, n-i))
#         break

# # Упорядоченные дроби
# from math import gcd
# from fractions import Fraction
# n = int(input())
# result = []
# while n != 1:
#     for i in range(1, n):
#         if gcd(i, n) == 1:
#             result.append(f'{i}/{n}')
#     n -= 1
# answer = sorted(map(Fraction, result))
# print(*answer, sep='\n')

# matrix() — возвращает матрицу 1 \times 11× 1, в которой единственное число равно нулю;
# matrix(n) — возвращает матрицу n \times nn× n, заполненную нулями;
# matrix(n, m) — возвращает матрицу из nn строк и mm столбцов, заполненную нулями;
# matrix(n, m, value) — возвращает матрицу из nn строк и mm столбцов, в которой каждый элемент равен числу value.
#
# def matrix(n=1, m=0, a=0):
#     if n == 1 and not m:
#         m = 1
#     elif n != 1 and not m:
#         m = n
#     return [[a] * m for _ in range(n)]

# 15.2 Функции с переменным количеством аргументов
# def my_sum(*args):
#     return sum(args)
#
# print(my_sum(*[1, 2, 3, 4, 5]))   #  распаковка списка
# print(my_sum(*(1, 2, 3)))         #  распаковка кортежа
# print(my_sum(1, 2, *[3, 4, 5], *(7, 8, 9), 10))

# Позиционные аргументы можно получать в виде *args, причём произвольное их количество.
# Такая возможность существует и для именованных аргументов. Только именованные аргументы
# получаются в виде словаря, что позволяет сохранить имена аргументов в ключах.
# Рассмотрим определение функции my_func():
#
# def my_func(**kwargs):
#     print(type(kwargs))
#     print(kwargs)
# Приведенный ниже код:
#
# my_func()
# my_func(a=1, b=2)
# my_func(name='Timur', job='Teacher')
# выводит:
#
# <class 'dict'>
# {}
# <class 'dict'>
# {'a': 1, 'b': 2}
# <class 'dict'>
# {'name': 'Timur', 'job': 'Teacher'}

# # Передача именованных аргументов в форме словаря
# Рассмотрим определение функции my_func():
#
# def my_func(**kwargs):
#     print(type(kwargs))
#     print(kwargs)
# Приведенный ниже код:
#
# info = {'name':'Timur', 'age':'28', 'job':'teacher'}
#
# my_func(**info)
# выводит:
#
# <class 'dict'>
# {'name': 'Timur', 'age': '28', 'job': 'teacher'}
#

# def func(*args):
#     return max(args) + min(args)
#
#
# print(func(10, 15, *[31, 42, 5, 1], *(17, 28, 19, 100), 13, 12))

# def count_args(*args):
#     return len(args)

# принимает произвольное количество числовых аргументов и возвращает сумму их квадратов.
# def sq_sum(*args):
#     return sum(i ** 2 for i in args)


# принимает произвольное количество аргументов и возвращает среднее арифметическое переданных
# в нее числовых (int или float) аргументов.

# def mean(*args):
#     sp = [i for i in args if type(i) == int or type(i) == float]
#     if len(sp) != 0:
#         return sum(sp)/len(sp)
#     else:
#         return 0.0
#
# print(mean())
# print(mean(7))
# print(mean(1.5, True, ['stepik'], 'beegeek', 2.5, (1, 2)))
# print(mean(True, ['stepik'], 'beegeek', (1, 2)))
# print(mean(-1, 2, 3, 10, ('5')))
# print(mean(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))


# принимает произвольное количество аргументов строк имен (как минимум одно)
# и возвращает приветствие в соответствии с образцом.
# def greet(name, *args):
#     sp = ' and '.join((name,) + args)
#     return f"Hello, {sp}!"


# выводит список продуктов (любая непустая строка) по образцу: <номер продукта>) <название продукта>
# (нумерация продуктов начинается с единицы). Если среди переданных аргументов нет ни одного продукта,
# необходимо вывести текст Нет продуктов.

# def print_products(*products):
#     filtered = [product for product in products if product and isinstance(product, str)]
#     if filtered:
#         for indx, product in enumerate(filtered, 1):
#             print(f"{indx}) {product}")
#     else:
#         print("Нет продуктов")

# def print_products(*args):
#     i = 0
#     for elem in args:
#         if type(elem) is str and elem:
#             i += 1
#             print(f'{i}) {elem}')
#     if not i: print('Нет продуктов')
#
#
#
# print_products('Бананы', [1, 2], ('Stepik',), 'Яблоки', '', 'Макароны', 5, True)


# Напишите функцию info_kwargs(), которая принимает произвольное количество именованных аргументов
# и печатает именованные аргументы в соответствии с образцом: <имя аргумента>: <значение аргумента>,
# при этом имена аргументов следуют в алфавитном порядке (по возрастанию).
# def info_kwargs(**kwargs):
#     for key, value in sorted(kwargs.items()):
#         print(key + ": " + str(value))


# Дан список numbers, содержащий кортежи чисел. Напишите программу, которая с помощью встроенных
# функций min() и max() выводит те кортежи (каждый на отдельной строке), которые имеют минимальное
# и максимальное среднее арифметическое значение элементов.

# numbers = [(10, 10, 10), (30, 45, 56), (81, 39), (1, 2, 3), (12,), (-2, -4, 100), (1, 2, 99), (89, 9, 34),
#            (10, 20, 30, -2), (50, 40, 50), (34, 78, 65), (-5, 90, -1, -5), (1, 2, 3, 4, 5, 6), (-9, 8, 4),
#            (90, 1, -45, -21)]
#
# def f(x):
#     return sum(x)/len(x)
#
# print(min(numbers, key=f))
# print(max(numbers, key=f))

#
# points = [(-1, 1), (5, 6), (12, 0), (4, 3), (0, 1), (-3, 2), (0, 0), (-1, 3), (2, 0), (3, 0), (-9, 1), (3, 6), (8, 8)]
# def f(n):
#     return 0.5 ** (n[0] ** 2 + n[1] ** 2)
#
# points.sort(key=f, reverse=True)
# print(points)

# numbers = [(10, 10, 10), (30, 45, 56), (81, 80, 39), (1, 2, 3), (12, 45, 67), (-2, -4, 100), (1, 2, 99), (89, 90, 34), (10, 20, 30), (50, 40, 50), (34, 78, 65), (-5, 90, -1)]
# f = lambda x: min(x) + max(x)
# numbers.sort(key=f)
#
# print(numbers)

# Сортируй как хочешь
# v = int(input())
# athletes = [('Дима', 10, 130, 35), ('Тимур', 11, 135, 39), ('Руслан', 9, 140, 33), ('Рустам', 10, 128, 30),
#             ('Амир', 16, 170, 70), ('Рома', 16, 188, 100), ('Матвей', 17, 168, 68), ('Петя', 15, 190, 90)]
# stroka = sorted(athletes, key=lambda x: x[v - 1])
# for i in stroka:
#     print(*i)


# Математические функции
# from math import *
# def get_res(n, f):
#     funcs = {'квадрат': n**2,
#              'куб': n**3,
#              'корень': n**0.5,
#              'модуль': abs(n),
#              'синус': sin(n)}
#     return funcs[f]
# a, b = int(input()), input().lower()
# print(get_res(a, b))

# Интересная сортировка-1
# nums = input().split()
# def cmp(num):
#     n = [int(i) for i in num]
#     return sum(n)
# nums.sort(key=cmp)
# print(*nums)


# # Интересная сортировка-2
# def sum_nums(numstr):
#     nums = list(map(int, list(numstr)))
#     return sum(nums), int(numstr)
#
# s = input().split()
# print(*sorted(s, key=sum_nums))

# 15.5 Функции высшего порядка

# Функция map()
# def f(x):
#     return x**2     # тело функции, которая преобразует аргумент x
#
#
# old_list = [1, 2, 4, 9, 10, 25]
# new_list = []
# for item in old_list:
#     new_item = f(item)
#     new_list.append(new_item)
#
# print(old_list)
# print(new_list)
# Результатом работы такого кода будет:
#
# [1, 2, 4, 9, 10, 25]
# [1, 4, 16, 81, 100, 625]

# Несложно понять, что цикл будет выглядеть одинаково практически во всех случаях.
# Меняться будет только преобразование, то есть применяемая функция f().

# def map(function, items):
#     result = []
#     for item in items:
#         new_item = function(item)
#         result.append(new_item)
#     return result
# # Теперь мы можем совершать преобразования, используя функцию высшего порядка map().
# def square(x):
#     return x**2
#
#
# def cube(x):
#     return x**3
#
#
# numbers = [1, 2, -3, 4, -5, 6, -9, 0]
#
# strings = map(str, numbers)        # используем в качестве преобразователя - функцию str
# abs_numbers = map(abs, numbers)    # используем в качестве преобразователя - функцию abs
#
# squares = map(square, numbers)     # используем в качестве преобразователя - функцию square
# cubes = map(cube, numbers)         # используем в качестве преобразователя - функцию cube
#
# print(strings)
# print(abs_numbers)
# print(squares)
# print(cubes)


# Приведенный ниже код, при условии, что функция map() определена как указано выше:
#
# strings = ['10', '12', '-4', '-9', '0', '1', '23', '100', '99']
#
# numbers1 = [int(c) for c in strings]   # используем списочное выражение для преобразования
# numbers2 = map(int, strings)               # используем функцию map() для преобразования
#
# print(numbers1)
# print(numbers2)
# выводит:
#
# [10, 12, -4, -9, 0, 1, 23, 100, 99]
# [10, 12, -4, -9, 0, 1, 23, 100, 99]

# Цепочки преобразований
# Мы также можем строить цепочки преобразований, несколько раз вызывая функцию map().
#
# Приведенный ниже код, при условии, что функция map() определена как указано выше:
#
# numbers = ['-1', '20', '3', '-94', '65', '6', '-970', '8']
#
# new_numbers = map(abs, map(int, numbers))
#
# print(new_numbers)
# выводит:
#
# [1, 20, 3, 94, 65, 6, 970, 8]
# То есть, сначала мы преобразуем список строк в список чисел с помощью кода map(int, numbers),
# получая список [-1, 20, 3, -94, 65, 6, -970, 8]. Далее с помощью еще одного вызова функции map()
# трансформируем полученный список в список [1, 20, 3, 94, 65, 6, 970, 8].
#

# Функция filter()
# def filter(function, items):
#     result = []
#     for item in items:
#         if function(item):
#             result.append(item)  # добавляем элемент item если функция function вернула значение True
#     return result

# Например, чтобы из исходного списка чисел получить список с элементами, большими 10, можно написать такой код:
#
# def is_greater10(num):   # функция возвращает значение True если число больше 10 и False в противном случае
#     return num > 10
#
#
# numbers = [12, 2, -30, 48, 51, -60, 19, 10, 13]
#
# large_numbers = filter(is_greater10, numbers)   #  список large_numbers содержит элементы, большие 10
#
# print(large_numbers)
# Этот код, при условии, что функция filter() определена как указано выше выводит:
#
# [12, 48, 51, 19, 13]

# Функция reduce()
# Реализованные нами функции map() и filter() работали с отдельными элементами списка независимо.
# Но встречаются циклы с агрегацией результата — формированием одного результирующего значения при
# комбинации элементов с использованием аргумента-аккумулятора.
# # Типичные примеры агрегации — сумма всех элементов списка или их произведение.
# # Приведенный ниже код:
#
# numbers = [1, 2, 3, 4, 5]
# # total = 0
# product = 1
# # for num in numbers:
#     total += num
#     product *= num
# # print(total)
# print(product)
# вычисляет сумму и произведение элементов списка и выводит:
# # 15
# 120

# С точки зрения математики сумма 1 + 2 + 3 + 4 + 5 может быть выражена как:
# (((((0+1)+2)+3)+4)+5).
# Ноль здесь тот самый аккумулятор, точнее его начальное значение. Он не добавляет к сумме ничего, поэтому может
# служить отправной точкой. А еще будет результатом, если входной список пуст.
# Несложно понять, что этот цикл будет выглядеть одинаково практически во всех случаях. Меняться будет
# только начальное значение аккумулятора (0 для суммы, 1 для произведения и т.д.) и операция, которая
# комбинирует элемент и аккумулятор. Так почему бы не обобщить этот код? Так и сделаем:

# def reduce(operation, items, initial_value):
#     acc = initial_value
#     for item in items:
#         acc = operation(acc, item)
#     return acc
# # Приведенный ниже код, при условии, что функция reduce() определена как указано выше:
#
# def add(x, y):
#     return x+y
# def mult(x, y):
#     return x*y
# numbers = [1, 2, 3, 4, 5]
# total = reduce(add, numbers, 0)
# product = reduce(mult, numbers, 1)
# print(total)
# print(product)
# # выводит:
# # 15
# # 120
# #
# words = ['abba', 'qwerty', 'python', 'a', 'deed', 'nun', 'level', 'deified', 'bbbbb', 'mother', 'surface', 'sister']
#
# words_len = map(len, words)
# print(max(words_len))
#

# функция считает кол - во палиндромов в списке
#
# def predicate(word):
#     return word == word[::-1]
#
#
# words = ['abba', 'qwerty', 'python', 'a', 'deed', 'nun', 'level', 'language', 'deified', 'bbbbb', 'mother', 'sister', 'surface', '1234321']
# filtered = filter(predicate, words)
# print(len(filtered))
# Функция filter():
#
# def filter(function, items):
#     result = []
#     for item in items:
#         if function(item):
#             result.append(item)
#     return result
#

# numbers = [-2, 45, 45, -7, -45, 37, -42, 27, -58, -58, -12, -27, -49, -27, -56, 4, -99, -11, 86]
#
# var1 = max(numbers, key=abs)
# var2 = min(map(abs, numbers))
# print(var1 + var2)

# Напишите программу, которая с помощью функции map() округляет все элементы списка numbers до 2 десятичных знаков
# а затем выводит их, каждый на отдельной строке.
#
# def map(function, items):
#     result = []
#     for item in items:
#         result.append(function(item))
#     return result
#
#
# numbers = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.12013, 23.22222, 90.09873, 45.45, 314.1528, 2.71828,
#            1.41546]
# result = map(lambda x: round(x, 2), numbers)
#
# for elem in result:
#     print(elem)

# # Напишите программу, которая с помощью функций filter() и map() отбирает из заданного списка
# # numbers трёхзначные числа, дающие при делении на 5 остаток 2, и выводит их кубы, каждый в отдельной строке.
# def map(function, items):
#     result = []
#     for item in items:
#         result.append(function(item))
#     return result
#
#
# def filter(function, items):
#     result = []
#     for item in items:
#         if function(item):
#             result.append(item)
#     return result
#
#
# numbers = [1014, 1321, 675, 1215, 56, 1386, 1385, 431, 1058, 486, 1434, 696, 1016, 1084, 424, 1189, 475, 95, 1434, 1462,
#            815, 776, 657, 1225, 912, 537, 1478, 1176, 544, 488, 668, 944, 207, 266, 1309, 1027, 257, 1374, 1289, 1155,
#            230, 866, 708, 144, 1434, 1163, 345, 394, 560, 338, 232, 182, 1438, 1127, 928, 1309, 98, 530, 1013, 898, 669,
#            105, 130, 1363, 947, 72, 1278, 166, 904, 349, 831, 1207, 1496, 370, 725, 926, 175, 959, 1282, 336, 1268, 351,
#            1439, 186, 273, 1008, 231, 138, 142, 433, 456, 1268, 1018, 1274, 387, 120, 340, 963, 832, 1127]
#
#
# def tu(a):
#     return a % 5 == 2 and len(str(a)) == 3
#
#
# def coub(x):
#     return x ** 3
#
#
# map(print, map(coub, filter(tu, numbers)))


# вычисления и вывода суммы квадратов элементов списка numbers.
# def reduce(operation, items, initial_value):
#     acc = initial_value
#     for item in items:
#         acc = operation(acc, item)
#     return acc
#
# numbers = [97, 42, 9, 32, 3, 45, 31, 77, -1, 11, -2, 75, 5, 51, 34, 28, 46, 1, -8, 84, 16, 51, 90, 56, 65, 90, 23, 35, 11, -10, 70, 90, 90, 12, 96, 58, -8, -4, 91, 76, 94, 60, 72, 43, 4, -6, -5, 51, 58, 60, 30, 38, 67, 62, 36, 72, 34, 82, 62, -1, 60, 82, 87, 81, -7, 57, 26, 36, 17, 43, 80, 40, 75, 94, 91, 64, 38, 72, 29, 84, 38, 35, 7, 54, 31, 95, 78, 27, 82, 1, 64, 94, 31, 29, -8, 98, 24, 61, 7, 73]
#
# print (sum([pow(elem, 2) for elem in numbers]))

# вычисления и вывода суммы квадратов двузначных чисел, которые делятся на 7 без остатка.
# numbers = [77, 293, 28, 242, 213, 285, 71, 286, 144, 276, 61, 298, 280, 214, 156, 227, 228, 51, -4, 202, 58, 99, 270,
#            219, 94, 253, 53, 235, 9, 158, 49, 183, 166, 205, 183, 266, 180, 6, 279, 200, 208, 231, 178, 201, 260, -35,
#            152, 115, 79, 284, 181, 92, 286, 98, 271, 259, 258, 196, -8, 43, 2, 128, 143, 43, 297, 229, 60, 254, -9, 5,
#            187, 220, -8, 111, 285, 5, 263, 187, 192, -9, 268, -9, 23, 71, 135, 7, -161, 65, 135, 29, 148, 242, 33, 35,
#            211, 5, 161, 46, 159, 23, 169, 23, 172, 184, -7, 228, 129, 274, 73, 197, 272, 54, 278, 26, 280, 13, 171, 2,
#            79, -2, 183, 10, 236, 276, 4, 29, -10, 41, 269, 94, 279, 129, 39, 92, -63, 263, 219, 57, 18, 236, 291, 234,
#            10, 250, 0, 64, 172, 216, 30, 15, 229, 205, 123, -105]
# print (sum([pow(elem, 2) for elem in numbers if abs(elem)//100 == 0 and abs(elem)//10 > 0 and elem%7==0]))


# Напишите функцию func_apply(), принимающую на вход функцию и список значений и возвращающую список,
# в котором каждое значение будет результатом применения переданной функции к переданному списку.
#
# Примечание 1. Приведенный ниже код, при условии, что функция func_apply() написана правильно
#
# def add3(x):
#     return x + 3
#
#
# def mul7(x):
#     return x * 7
#
#
# print(func_apply(mul7, [1, 2, 3, 4, 5, 6]))
# print(func_apply(add3, [1, 2, 3, 4, 5, 6]))
# print(func_apply(str, [1, 2, 3, 4, 5, 6]))
# должен выводить:
#
# [7, 14, 21, 28, 35, 42]
# [4, 5, 6, 7, 8, 9]
# ['1', '2', '3', '4', '5', '6']


# Встроенная функция map()
# Приведенный ниже код:
# circle_areas = [3.56773, 5.57668, 4.31914, 6.20241, 91.01344, 32.01213]
#
# result1 = list(map(round, circle_areas, [1]*6))         # округляем числа до 1 знака после запятой
# result2 = list(map(round, circle_areas, range(1, 7)))   # округляем числа до 1,2,...,6 знаков после запятой
#
# print(circle_areas)
# print(result1)
# print(result2)
# выводит:
#
# [3.56773, 5.57668, 4.31914, 6.20241, 91.01344, 32.01213]
# [3.6, 5.6, 4.3, 6.2, 91.0, 32.0]
# [3.6, 5.58, 4.319, 6.2024, 91.01344, 32.01213]

# Встроенная функция filter()

# В качестве параметра func указывается ссылка на функцию, которой будет передаваться текущий
# элемент последовательности. Внутри функции func необходимо вернуть значение True или False.
# Для примера, удалим все отрицательные значения из списка.
#
# Приведенный ниже код:
# # def func(elem):
#     return elem >= 0
# numbers = [-1, 2, -3, 4, 0, -20, 10]
# positive_numbers = list(filter(func, numbers))  #  преобразуем итератор в список
# print(positive_numbers)
# выводит:
# [2, 4, 0, 10]

# Функция reduce()
# Для использования функции reduce() необходимо подключить специальный модуль functools.
# Функция reduce() имеет сигнатуру reduce(func, iterable, initializer=None). Если начальное
# значение не установлено, то в его качестве используется первое значение из последовательности iterable.

# from functools import reduce
#
# def func(a, b):
#     return a + b
#
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# total = reduce(func, numbers, 0)   # в качестве начального значения 0
# print(total)
# выводит: 55
# Обратите внимание на то, что мы могли вызвать функцию так:
# total = reduce(func, numbers)   # в качестве начального значения первый элемент списка numbers

# Модуль operator
# Чтобы не писать каждый раз функции, определяющие такие стандартные математические
# операции как сумма или произведение:
#
# def sum_func(a, b):
#     return a + b
#
#
# def mult_func(a, b):
#     return a * b
# можно использовать уже реализованные функции из модуля operator.
# Операция	        Синтаксис	Функция
# Addition	        a + b	    add(a, b)
# Containment Test	obj in seq	contains(seq, obj)
# Division	        a / b	    truediv(a, b)
# Division	        a // b	    floordiv(a, b)
# Exponentiation	a ** b	    pow(a, b)
# Modulo	        a % b	    mod(a, b)
# Multiplication	a * b	    mul(a, b)
# Negation (Arithmetic)	-a	    neg(a)
# Subtraction	    a - b	    sub(a, b)
# Ordering	        a < b	    lt(a, b)
# Ordering	        a <= b	    le(a, b)
# Equality	        a == b	    eq(a, b)
# Difference	    a != b	    ne(a, b)
# Ordering	        a >= b	    ge(a, b)
# Ordering	        a > b	    gt(a, b)

# from operator import *     #  импортируем все функции
# print(add(10, 20))         #  сумма
# print(floordiv(20, 3))     #  целочисленное деление
# print(neg(9))              #  смена знака
# print(lt(2, 3))            #  проверка на неравенство <
# print(lt(10, 8))           #  проверка на неравенство <
# print(eq(5, 5))            #  проверка на равенство ==
# print(eq(5, 9))            #  проверка на равенство ==

# from functools import reduce
# import operator
# words = ['Testing ', 'shows ', 'the ', 'presence', ', ', 'not ', 'the ', 'absence ', 'of ', 'bugs']
# numbers = [1, 2, -6, -4, 3, 9, 0, -6, -1]
# opposite_numbers = list(map(operator.neg, numbers))    #  смена знаков элементов списка
# concat_words = reduce(operator.add, words)             #  конкатенация элементов списка
# print(opposite_numbers)    #--> [-1, -2, 6, 4, -3, -9, 0, 6, 1]
# print(concat_words)         #--> "Testing shows the presence, not the absence of bugs"

# pets = ['alfred', 'tabitha', 'william', 'arla']
# chars = ['x', 'y', '2', '3', 'a']
#
# uppered_pets = list(map(str.upper, pets))
# capitalized_pets = list(map(str.capitalize, pets))
# only_letters = list(filter(str.isalpha, chars))
#
# print(uppered_pets)
# print(capitalized_pets)
# print(only_letters)
# выводит:
#
# ['ALFRED', 'TABITHA', 'WILLIAM', 'ARLA']
# ['Alfred', 'Tabitha', 'William', 'Arla']
# ['x', 'y', 'a']
#
#


# 15.7 Анонимные функции. Часть 1
# def standard_function(x):            #  стандартное объявление функции
#     return x*2
# lambda_function = lambda x: x*2      #  объявление анонимной функции

# f1 = lambda: 10 + 20               # функция без параметров
# f2 = lambda х, у: х + у            # функция с двумя параметрами
# f3 = lambda х, у, z: х + у + z     # функция с тремя параметрами
#
# print(f1())
# print(f2(5, 10))
# print(f3(5, 10, 30))

# def compare_by_second(point):
#     return point[1]
#
# def compare_by_sum(point):
#     return point[0] + point[1]
#
# points = [(1, -1), (2, 3), (-10, 15), (10, 9), (7, 18), (1, 5), (2, -4)]
#
# print(sorted(points, key=compare_by_second))   # сортируем по второму значению кортежа
# print(sorted(points, key=compare_by_sum))      # сортируем по сумме кортежа

# # логично их заменить на анонимные функции:
# points = [(1, -1), (2, 3), (-10, 15), (10, 9), (7, 18), (1, 5), (2, -4)]
#
# print(sorted(points, key=lambda point: point[1]))                 # сортируем по второму значению кортежа
# print(sorted(points, key=lambda point: point[0] + point[1]))      # сортируем по сумме элементов кортежа

# Передача анонимных функций в качестве аргументов другим функциям
# numbers = [1, 2, 3, 4, 5, 6]
#
# new_numbers1 = list(map(lambda x: x+1, numbers))      #  увеличиваем на 1
# new_numbers2 = list(map(lambda x: x*2, numbers))      #  удваиваем
# new_numbers3 = list(map(lambda x: x**2, numbers))     #  возводим в квадрат
#
# print(new_numbers1) #--> [2, 3, 4, 5, 6, 7]
# print(new_numbers2)  #-->  [2, 4, 6, 8, 10, 12]
# print(new_numbers3) #-->  [1, 4, 9, 16, 25, 36]

# -----

# strings = ['a', 'b', 'c', 'd', 'e']
# numbers = [3, 2, 1, 4, 5]
# new_strings = list(map(lambda x, y: x*y, strings, numbers))
#
# print(new_strings) #--> ['aaa', 'bb', 'c', 'dddd', 'eeeee']

# ----------
# numbers = [-1, 2, -3, 4, 0, -20, 10, 30, -40, 50, 100, 90]
#
# positive_numbers = list(filter(lambda x: x > 0, numbers))      #  положительные числа
# large_numbers = list(filter(lambda x: x > 50, numbers))        #  числа, большие 50
# even_numbers = list(filter(lambda x: x % 2 == 0, numbers))     #  четные числа
#
# print(positive_numbers) #--> [2, 4, 10, 30, 50, 100, 90]
# print(large_numbers) #--> [100, 90]
# print(even_numbers) #--> [2, 4, 0, -20, 10, 30, -40, 50, 100, 90]

# ---------------
# words = ['python', 'stepik', 'beegeek', 'iq-option']
#
# new_words1 = list(filter(lambda w: len(w) > 6, words))    #  слова длиною больше 6 символов
# new_words2 = list(filter(lambda w: 'e' in w, words))      #  слова содержащие букву e
#
# print(new_words1) #--> ['beegeek', 'iq-option']
# print(new_words2) #--> ['stepik', 'beegeek']
#
# -----------------
#
# from functools import reduce
#
# words = ['python', 'stepik', 'beegeek', 'iq-option']
# numbers = [1, 2, 3, 4, 5, 6]
#
# summa = reduce(lambda x, y: x + y, numbers, 0)
# product = reduce(lambda x, y: x * y, numbers, 1)
# sentence = reduce(lambda x, y: x + ' loves ' + y, words, 'Everyone')
#
# print(summa) #--> 21
# print(product) #--> 720
# print(sentence) #-->  Everyone loves python loves stepik loves beegeek loves iq-option

# Возвращение функции в качестве результата другой функции
# Анонимные функции могут быть результатом работы других функций.
#
# Приведенный ниже код по значениям a, \, b, \, ca,b,c строит и возвращает квадратный трехчлен:
#
# def generator_square_polynom(a, b, c):
#     def square_polynom(x):
#         return a*x**2 + b*x + c
#     return square_polynom
# Такой код можно переписать так:
#
# def generator_square_polynom(a, b, c):
#     return lambda x: a*x**2 + b*x + c
# Этот пример показывает, что анонимные функции являются замыканиями: возвращаемая функция запоминает значения
# переменных a, b, c из внешнего окружения.


# Условный оператор в теле анонимной функции
# В теле анонимной функции не получится выполнить несколько действий и не получится
# использовать многострочные конструкции вроде циклов for и while. Однако можно использовать тернарный условный оператор.
#
# Приведенный ниже код:
#
# numbers = [-2, 0, 1, 2, 17, 4, 5, 6]
#
# result = list(map(lambda x: 'even' if x % 2 == 0 else 'odd', numbers))
#
# print(result)
# выводит:
#
# ['even', 'even', 'odd', 'even', 'odd', 'even', 'odd', 'even']
# Общий вид тернарного условного оператора в теле анонимной функции выглядит так:
#
# значение1 if условие else значение2
# Если условие истинно, возвращается значение1 , если нет – значение2.
#
#
# Передача аргументов в анонимную функцию
# Как и обычные функции, определенные с помощью ключевого слова def , анонимные функции
# поддерживают все способы передачи аргументов:
#
# позиционные аргументы;
# именованные аргументы;
# переменный список позиционных аргументов (*args);
# переменный список именованных аргументов (**kwargs);
# обязательные аргументы (*).
# Приведенный ниже код:
#
# f1 = lambda x, y, z: x + y + z
# f2 = lambda x, y, z=3: x + y + z
# f3 = lambda *args: sum(args)
# f4 = lambda **kwargs: sum(kwargs.values())
# f5 = lambda x, *, y=0, z=0: x + y + z
#
#
# print(f1(1, 2, 3))
# print(f2(1, 2))
# print(f2(1, y=2))
# print(f3(1, 2, 3, 4, 5))
# print(f4(one=1, two=2, three=3))
# print(f5(1))
# print(f5(1, y=2, z=3))

#
# Примечание 1. Интересная особенность анонимных функций (лямбда-функций)
# – они являются выражениями. После определения лямбда-функции ее можно сразу же вызвать.
#
# Приведенный ниже код:
#
# print((lambda х, у: х + у)(5, 10))     # 5 + 10
# print(1 + (lambda x: x*5)(10) + 2)     # 1 + 50 + 2


# numbers = [1, 2, 5, 3, 4]
# numbers.sort(key=lambda x: -x)
# print(numbers)   --> [5, 4, 3, 2, 1]

# напишите функцию func, используя синтаксис анонимных функций, которая принимает целочисленный аргумент
# и возвращает значение True, если он делится без остатка на 19 или на 13 и False в противном случае.

# func = lambda x: x % 19 == 0 or x % 13 == 0

# Напишите функцию func, используя синтаксис анонимных функций, которая принимает строковый аргумент
# и возвращает значение True, если переданный аргумент начинается и заканчивается на английскую букву a
# (регистр буквы неважен) и False в противном случае.
# func = lambda x: x[0].lower() == 'a' and x[-1].lower() == 'a'
# print(func('abcdA'))


# Напишите функцию is_non_negative_num, используя синтаксис анонимных функций, которая принимает
# строковый аргумент и возвращает значение True, если переданный аргумент является неотрицательным числом
# (целым или вещественным) и False в противном случае.
# is_non_negative_num = lambda x: set(x.replace('.', '', 1)) <= set('0123456789')
# print(is_non_negative_num('10.34ab'))
# print(is_non_negative_num('10.45'))


# Напишите функцию is_num, используя синтаксис анонимных функций, которая принимает строковый аргумент и возвращает
# значение True, если переданный аргумент является числом (целым или вещественным) и False в противном случае.
# is_num = lambda x: "-" not in x[1:] and x.replace('.', '', 1).replace("-",'').isdigit()

# words = ['beverage', 'monday', 'abroad', 'bias', 'abuse', 'abolish', 'abuse', 'abuse', 'bid', 'wednesday', 'able', 'betray', 'accident', 'abduct', 'bigot', 'bet', 'abandon', 'besides', 'access', 'friday', 'bestow', 'abound', 'absent', 'beware', 'abundant', 'abnormal', 'aboard', 'about', 'accelerate', 'abort', 'thursday', 'tuesday', 'sunday', 'berth', 'beyond', 'benevolent', 'abate', 'abide', 'bicycle', 'beside', 'accept', 'berry', 'bewilder', 'abrupt', 'saturday', 'accessory', 'absorb']
# print(*sorted(filter(lambda x: len(x) == 6, words)))

# Напишите программу, которая с помощью встроенных функций map() и filter() удаляет из списка numbers все
# нечетные элементы, большие 47, а все четные элементы нацело делит на два (целочисленное деление – //).
# Полученные числа следует вывести на одной строке, разделив символом пробела и сохранив исходный порядок.

# nums = [46, 61, 34, 17, 56, 26, 93, 1, 3, 82, 71, 37, 80, 27, 77, 94, 34, 100, 36, 81, 33, 81, 66, 83, 41, 80, 80, 93,
#         40, 34, 32, 16, 5, 16, 40, 93, 36, 65, 8, 19, 8, 75, 66, 21, 72, 32, 41, 59, 35, 64, 49, 78, 83, 27, 57, 53, 43,
#         35, 48, 17, 19, 40, 90, 57, 77, 56, 80, 95, 90, 27, 26, 6, 4, 23, 52, 39, 63, 74, 15, 66, 29, 88, 94, 37, 44, 2,
#         38, 36, 32, 49, 5, 33, 60, 94, 89, 8, 36, 94, 46, 33]
#
# res = list(map(lambda x: x // 2 if x % 2 == 0 else x, filter(lambda x: x % 2 == 0 or (x % 2 != 0 and x < 47), nums)))
# print(*res)

# программу сортировки по убыванию списка data на основании последнего символа в названии штата. Затем
# распечатайте элементы этого списка, каждый на новой строке в формате:
# data = [(19542209, 'New York'), (4887871, 'Alabama'), (1420491, 'Hawaii'), (626299, 'Vermont'), (1805832, 'West Virginia'), (39865590, 'California'), (11799448, 'Ohio'), (10711908, 'Georgia'), (10077331, 'Michigan'), (10439388, 'Virginia'), (7705281, 'Washington'), (7151502, 'Arizona'), (7029917, 'Massachusetts'), (6910840, 'Tennessee')]
#
# for i in sorted(data, key=lambda x: x[1][-1], reverse=True):
#     print(f"{i[1]}: {i[0]}")


# data = ['год', 'человек', 'время', 'дело', 'жизнь', 'день', 'рука', 'раз', 'работа', 'слово', 'место', 'лицо', 'друг', 'глаз', 'вопрос', 'дом', 'сторона', 'страна', 'мир', 'случай', 'голова', 'ребенок', 'сила', 'конец', 'вид', 'система', 'часть', 'город', 'отношение', 'женщина', 'деньги']
# print(*sorted(data, key=lambda x: (len(x), x)))


# Список mixed_list содержит целочисленные и строковые значения. Напишите программу, которая с помощью
# # встроенной функции max() находит и выводит наибольшее числовое значение в указанном списке.
#
# mixed_list = ['tuesday', 'abroad', 'abuse', 'beside', 'monday', 'abate', 'accessory', 'absorb', 1384878, 'sunday',
#               'about', 454805, 'saturday', 'abort', 2121919, 2552839, 977970, 1772933, 1564063, 'abduct', 901271,
#               2680434, 'bicycle', 'accelerate', 1109147, 942908, 'berry', 433507, 'bias', 'bestow', 1875665, 'besides',
#               'bewilder', 1586517, 375290, 1503450, 2713047, 'abnormal', 2286106, 242192, 701049, 2866491, 'benevolent',
#               'bigot', 'abuse', 'abrupt', 343772, 'able', 2135748, 690280, 686008, 'beyond', 2415643, 'aboard', 'bet',
#               859105, 'accident', 2223166, 894187, 146564, 1251748, 2851543, 1619426, 2263113, 1618068, 'berth',
#               'abolish', 'beware', 2618492, 1555062, 'access', 'absent', 'abundant', 2950603, 'betray', 'beverage',
#               'abide', 'abandon', 2284251, 'wednesday', 2709698, 'thursday', 810387, 'friday', 2576799, 2213552,
#               1599022, 'accept', 'abuse', 'abound', 1352953, 'bid', 1805326, 1499197, 2241159, 605320, 2347441]
# print(max(mixed_list, key=lambda x: x if isinstance(x,int) else 0))


# mixed_list = ['beside', 48, 'accelerate', 28, 'beware', 'absorb', 'besides', 'berry', 15, 65, 'abate', 'thursday', 76, 70, 94, 35, 36, 'berth', 41, 'abnormal', 'bicycle', 'bid', 'sunday', 'saturday', 87, 'bigot', 41, 'abort', 13, 60, 'friday', 26, 13, 'accident', 'access', 40, 26, 20, 75, 13, 40, 67, 12, 'abuse', 78, 10, 80, 'accessory', 20, 'bewilder', 'benevolent', 'bet', 64, 38, 65, 51, 95, 'abduct', 37, 98, 99, 14, 'abandon', 'accept', 46, 'abide', 'beyond', 19, 'about', 76, 26, 'abound', 12, 95, 'wednesday', 'abundant', 'abrupt', 'aboard', 50, 89, 'tuesday', 66, 'bestow', 'absent', 76, 46, 'betray', 47, 'able', 11]
# print(*sorted(mixed_list, key=lambda x: str(x) ))

# Противоположный цвет
# print(*list(map(lambda x: 255 - x, [int(i) for i in input().split()])))

# # Значение многочлена 🌶️
# from functools import reduce as r
#
# eval = lambda coef, x: r(lambda v, c: c + v * x, map(int, coef))
# print(eval(input().split(), int(input())))

# 15.9 Встроенные функции any(), all(), zip(), enumerate()

# Встроенная функция all() возвращает значение True, если все элементы переданной ей последовательности (итерируемого
# объекта) истинны (приводятся к значению True), и False в противном случае.

# Встроенная функция any() возвращает значение True, если хотя бы один элемент переданной ей последовательности
# (итерируемого объекта) является истинным (приводится к значению True), и False в противном случае.

# Функция enumerate()
# Встроенная функция enumerate() возвращает кортеж из индекса элемента и самого элемента переданной
# ей последовательности (итерируемого объекта).
# Приведенный ниже код:
# colors = ['red', 'green', 'blue']
# for pair in enumerate(colors):
#     print(pair)
# выводит:
# (0, 'red')
# (1, 'green')
# (2, 'blue')
#
# Если счет нужно начать с отличного от нуля числа, то нужно передать значение аргумента start.
# Приведенный ниже код:
# colors = ['red', 'green', 'blue']
# for pair in enumerate(colors, 100):
#     print(pair)
# выводит:
# (100, 'red')
# (101, 'green')
# (102, 'blue')
# Обратите внимание, функция enumerate() возвращает не список, а специальный объект,
# который называется итератором. Такой объект похож на список тем, что его можно перебирать циклом for, то есть итерировать. Итератор можно преобразовать в список с помощью функции list().
#
# Приведенный ниже код:
#
# colors = ['red', 'green', 'blue']
#
# pairs = enumerate(colors)
#
# print(pairs)
# print(list(pairs))
# выводит:
#
# <enumerate object at 0x...>
# [(0, 'red'), (1, 'green'), (2, 'blue')]
# Мы также можем использовать распаковку кортежей при итерировании с помощью цикла for.
#
# Приведенный ниже код:
#
# colors = ['red', 'green', 'blue']
# for index, item in enumerate(colors):
#     print(index, item)
# выводит:
#
# 0 red
# 1 green
# 2 blue
# Такой код является альтернативой коду:
#
# colors = ['red', 'green', 'blue']
# for i in range(len(colors)):
#     print(i, colors[i])
#
# Функция zip()
# Встроенная функция zip() объединяет отдельные элементы из каждой переданной ей
# последовательности (итерируемого объекта) в кортежи.
# Приведенный ниже код:
# numbers = [1, 2, 3]
# words = ['one', 'two', 'three']
# for pair in zip(numbers, words):
#     print(pair)
# выводит:
# (1, 'one')
# (2, 'two')
# (3, 'three')
# Частые сценарии использования функции zip()
# Сценарий 1. Функция zip() удобна для создания словарей, когда ключи и значения находятся в разных списках.
# Приведенный ниже код:
# keys = ['name', 'age', 'gender']
# values = ['Timur', 28, 'male']
# info = dict(zip(keys, values))
# print(info)
# выводит:
# {'name': 'Timur', 'age': 28, 'gender': 'male'}

# Сценарий 2. Функция zip() удобна для одновременного (параллельного) итерирования сразу по нескольким коллекциям.
# Приведенный ниже код:
# name = ['Timur', 'Ruslan', 'Rustam']
# age = [28, 21, 19]
# for x, y in zip(name, age):
#     print(x, y)
# выводит: 
# Timur 28
# Ruslan 21
# Rustam 19

# Примечание 2. Реализация встроенных функций all() и any() выглядит примерно так:
# def all(iterable):
#     for item in iterable:
#        if not item:
#            return False
#     return True
#
# def any(iterable):
#     for item in iterable:
#         if item:
#             return True
#     return False
# Примечание 3. Мы можем использовать одновременно функции zip() и enumerate():
#
# Приведенный ниже код:
#
# list1 = ['a1', 'a2', 'a3']
# list2 = ['b1', 'b2', 'b3']
#
# for index, (item1, item2) in enumerate(zip(list1, list2)):
#     print(index, item1, item2)
# выводит:
#
# 0 a1 b1
# 1 a2 b2
# 2 a3 b3


# Используя параллельную итерацию сразу по трем спискам countries, capitals и population
# выведите информацию о стране в формате:
# <capital> is the capital of <country>, population equal <population> people.

# countries = ['Russia', 'USA', 'UK', 'Germany', 'France', 'India']
# capitals = ['Moscow', 'Washington', 'London', 'Berlin', 'Paris', 'Delhi']
# population = [145_934_462, 331_002_651, 80_345_321, 67_886_011, 65_273_511, 1_380_004_385]
# for country, capital, people in zip(countries, capitals, population):
#     print(f'{capital} is the capital of {country}, population equal {people} people.')

# Внутри шара
# abscissas = [float(i) for i in input().split()]
# ordinates = [float(i) for i in input().split()]
# applicates = [float(i) for i in input().split()]
# print(all(map(lambda x: x[0]**2 + x[1]**2 + x[2]**2 <= 4, zip(abscissas, ordinates, applicates))))

# # # Корректный IP-адрес
# ip=input().split('.')
# print(all(map(lambda n:n.isdigit() and int(n)<=255,ip)))


# Интересные числа
# a, b = int(input()), int(input())
# print(*filter(lambda n: all(map(lambda x: x != 0 and n % x == 0, map(int, str(n)))), range(a, b+1)))


# Хороший пароль
# s = input()
# print('YES' if all((any(i.isupper() for i in s),
#                     any(i.islower() for i in s),
#                     any(i.isdigit() for i in s),
#                     len(s) >= 7)) else 'NO')

# Отличники
# progress = []
# for i in range(int(input())):
#     progress.append(any(['5' in input().split() for j in range(int(input()))]))
#
# print('YES' if all(progress) else 'NO')

# Письмо для экзамена
# def generate_letter(mail, name, date, time, place, teacher = 'Тимур Гуев', number = 17):
#     return 'To: ' + mail + \
#     '\nПриветствую, ' + name + \
#     '!\nВам назначен экзамен, который пройдет ' + date + ', в ' + time + \
#     '.\nПо адресу: ' + place + \
#     '.\nЭкзамен будет проводить ' + teacher + ' в кабинете ' + str(number) + '.\nЖелаем удачи на экзамене!'

# # Pretty print
# def pretty_print(data, side = '-', delimiter = '|'):
#     mainStr = delimiter + ' ' + (' ' + delimiter + ' ').join(map(str, data)) + ' ' + delimiter
#     print(' ' + side * (len(mainStr) - 2))
#     print (mainStr)
#     print(' ' + side * (len(mainStr) - 2))


# def concat(*elems, sep = ' '):
#     return sep.join([str(elem) for elem in elems])

# from functools import reduce
# def product_of_odds(data):
#     return reduce(lambda a,b: a*b, [elem for elem in data if elem%2==1], 1)

# words = 'the world is mine take a look what you have started'.split()
# print(*map(lambda x: '\"' + x + '\"',words))

# numbers = [18, 191, 9009, 5665, 78, 77, 45, 23, 19991, 908, 8976, 6565, 5665, 10, 1000, 908, 909, 232, 45654, 786]
# print(*list(filter(lambda x: str(x) != str(x)[::-1], numbers)))

# numbers = [(10, -2, 3, 4), (-13, 56), (1, 9, 2), (-1, -9, -45, 32), (-1, 5, 1), (17, 0, 1), (0, 1), (3,), (39, 12), (11, -23), (10, -100, 21, 32), (3, -8), (1, 1)]
# sorted_numbers = sorted(numbers, key=lambda x: sum(x)/len(x), reverse=True)
# print(sorted_numbers)

# def call(func, *args):
#     return func(*args)

# def compose(f, g):
#     return lambda x: f(g(x))

# def arithmetic_operation(operation):
#     if operation == '+':
#         return lambda a,b: a + b
#     if operation == '-':
#         return lambda a,b: a - b
#     if operation == '*':
#         return lambda a,b: a * b
#     if operation == '/':
#         return lambda a,b: a / b

# В одну строку
# words = input().split()
# sorted_words = sorted(words, key=lambda a: a.lower())
# print(*sorted_words)

# Гематрия слова
# n = int(input())
# words = []
#
# def calculate_gematry(word):
#     summa = 0
#     word = word.upper()
#     for elem in word:
#         summa += ord(elem) - ord('A')
#     return summa
#
# for i in range(n):
#     words.append(input())
#
# sorted_words = sorted(words)
# sorted_words = sorted(sorted_words, key=calculate_gematry)
#
# for elem in sorted_words:
#     print(elem)

# Сортировка IP-адресов
# n = int(input())
# ip_addresses = []
#
#
# def calculate_digit(ip):
#     arr = [int(elem) for elem in ip.split('.')]
#     return arr[0] * pow(256, 3) + arr[1] * pow(256, 2) + arr[2] * pow(256, 1) + arr[3] * pow(256, 0)
#
#
# for i in range(n):
#     ip_addresses.append(input())
#
# ip_addresses = sorted(ip_addresses, key=calculate_digit)
# for elem in ip_addresses:
#     print(elem)

# 17.1 Файловый ввод и вывод
# Чтение содержимого файла
# Как уже сказано, при открытии файла с помощью функции open() в файловую переменную
# попадает не содержимое файла, а ссылка на файл (дескриптор файла).
#
# Приведенный ниже код:
#
# file = open('info.txt', 'w', encoding='utf-8')    # открываем файл для записи
#
# print(file)
# выводит:
#
# <_io.TextIOWrapper name='info.txt' mode='w' encoding='utf-8'>
# read() – читает все содержимое файла;
# readline() – читает одну строку из файла;
# readlines() – читает все содержимое файла и возвращает список строк.


# Предположим, в папке с исполняемой программой есть текстовый файл languages.txt с содержимым:
#
# Python
# Java
# Javascript
# C#
# C
# C++
# PHP
# R
# Objective-C
# Метод read()
# Файловый метод read() считывает все содержимое из файла и возвращает строку, которая может содержать символы
# перехода на новую строку '\n'.
#
# Приведенный ниже код:
#
# file = open('languages.txt', 'r', encoding='utf-8')
#
# content = file.read()
#
# file.close()
# считывает содержимое файла languages.txt в переменную content. В переменной content будет
# содержаться строка 'Python\nJava\nJavascript\nC#\nC\nC++\nPHP\nR\nObjective-C'.
#
# Таким образом метод read() считывает все содержимое файла, включая переносы строк:
#
# Если методу read() передать целочисленный параметр, то будет считано не более заданного количества
# символов. Например, считывать файл посимвольно можно при помощи метода read(1).


# Метод readline()
# Файловый метод readline() считывает одну строку из файла (до символа конца строки '\n'),
# при этом возвращается считанная строка вместе с символом '\n'. Если считать строку не удалось – достигнут конец файла и больше строк в нем нет, возвращается пустая строка.
# Приведенный ниже код:
#
# file = open('languages.txt', 'r', encoding='utf-8')
#
# language = file.readline()
#
# file.close()
# считывает содержимое первой строки файла languages.txt в переменную language. В переменной language
# будет содержаться строка 'Python\n'.
# Для удаления символа '\n' из конца считанной строки удобно использовать строковый метод rstrip().
# Приведенный ниже код:
#
# line = 'Python\n'
# line = line.rstrip()
# удаляет символ \n из содержимого строки line, в результате чего в переменной line содержится строка 'Python'.

# Прочитать содержимое всего файла построчно можно двумя способами.
# С помощью цикла while:

# file = open('languages.txt', 'r', encoding='utf-8')
# line = file.readline()  # считываем первую строку
# while line != '':  # пока не конец файла
#     print(line.strip())  # обрабатываем считанную строку
#     line = file.readline()  # читаем новую строку
# file.close()
#
# С помощью цикла for (предпочтительный вариант):
# file = open('languages.txt', 'r', encoding='utf-8')
# for line in file:
#     print(line.strip())
# file.close()
#
# Файловый метод readlines() считывает все строки из файла и возвращает список из всех считанных
# строк (одна строка — один элемент списка). При этом, каждая строка в списке заканчивается символом переноса строки  '\n'😅.
#
# Приведенный ниже код:
# file = open('languages.txt', 'r', encoding='utf-8')
# languages = file.readlines()
# file.close()
# считывает содержимое файла languages.txt в переменную languages. В переменной languages
# будет содержаться список:
# ['Python\n', 'Java\n', 'Javascript\n', 'C#\n', 'C\n', 'C++\n', 'PHP\n', 'R\n', 'Objective-C']
# Чтобы удалить символ '\n' можно использовать списочное выражение:
# languages = [line.strip() for line in file.readlines()]
# либо функцию map()
# languages = list(map(str.strip, file.readlines()))
# либо анонимную функцию:
# languages = list(map(lambda line: line.strip(), file.readlines()))
# Если передать в функцию list() ссылку на файловый объект list(file) ,
# получим тот же результат, что при вызове метода file.readlines().
#
#
# Примечание 4. Существуют специальные символы:

# \n – перемещает позицию печати на одну строку вниз;
# \r – перемещает позицию печати в крайнее левое положение строки.
# Приведенный ниже код:
#
# print('aaaaaa\nbb')
# выводит:
#
# aaaaaa
# bb
#  Приведенный ниже код:
#
# print('aaaaaa\rbb')
# выводит:
#
# bbaaaa
# Приведенный ниже код:
#
# print(ord('\n'))
# print(ord('\r'))
# выводит:
# 10
# 13

# file = open(input(), 'r', encoding='utf-8')
# for line in file:
#     print(line.strip())
# file.close()
#
# with open(input()) as f:
#     print(f.read())

# file = open('languages.txt', 'r', encoding='utf-8')
# languages = file.readlines()
# file.close()
# print(languages[-2])

# Случайная строка
# import random
# file = open('lines.txt', 'r', encoding='utf-8')
# text = file.readlines()
# file.close()
# print(text[random.randrange(0, len(text))])

# Сумма двух-1
# file = open('numbers.txt')
# print(sum(map(int, file)))
# file.close()

# l = [int(i) for i in open('numbers.txt')]
# print(sum(l))

# Сумма двух-2
# file = open('nums.txt')
# print(sum(map(int, file.read().split())))
# file.close()

# file = open('nums.txt')
# summa = 0
# for line in file.read().split():
#     summa += int(line)
# print(summa)
# file.close()


# Общая стоимость
# file = open('prices.txt', 'r', encoding='utf-8')
# s = 0
# for line in file:
#     tovar, count, price = line.split()
#     s += int(count) * int(price)
# print(s)
# file.close()

# import pandas as pd
#
# df = pd.read_csv('prices.txt', sep ='\t', header = None)
# df.columns = ['Товар', 'Количество', 'Цена']
# df['Итого'] = df['Количество'] * df['Цена']
# summa_zakaza = sum(df['Итого'])
# print(summa_zakaza)


# Файловый метод seek()
# Файловый метод seek() задаёт позицию курсора в байтах от начала файла. Чтобы перевести курсор в самое
# начало файла необходимо вызвать метод seek(), передав ему в качестве аргумента значение 0.
# Приведенный ниже код:

# file = open('languages.txt', 'r', encoding='utf-8')
# line1 = file.readline()
# file.seek(0)               # переводим курсор в самое начало
# line2 = file.readline()
#
# print(line1, line2)
#
# file.close()
# выводит:
# Python
# Python

# Если метод seek() устанавливает курсор (текущую позицию), то метод tell() получает ее.
# Приведенный ниже код:
#
# file = open('languages.txt', 'r', encoding='utf-8')
# print(file.tell())
# line1 = file.readline()
# print(file.tell())
#
# file.close()
# выводит:
#
# 0
# 8
# В самом начале курсор (текущая позиция) равен нулю, после считывания первой строки, курсор смещается на 8 байт
# (по байту на каждый из символов 'P', 'y', 't', 'h', 'o', 'n' и два байта на символ перевода строки '\n').


# # Менеджер контекста
# with object as name:
#     # Здесь нам доступен ресурс name.
#     # Это тело with-блока.
# # А здесь ресурс name уже освобождён, даже если в теле with-блока произошла ошибка.

# with open('languages.txt', 'r', encoding='utf-8') as file:
#     for line in file:
#         print(line)
#                           # автоматическое закрытие файла
# print('Файл закрыт')


# Переворот строки
# with open('text.txt', 'r', encoding='utf-8') as file:
#     print(file.read()[::-1])

# Обратный порядок
# with open('data.txt', 'r', encoding='utf-8') as file:
#     lines = file.readline()
#     for i in range(len(lines)):
#         print(lines[len(lines) - 1 - i].strip())
#
# with open('data.txt', encoding='utf-8') as file:
#     print(*file.readlines()[::-1], sep='')


# Длинные строки
# with open('lines.txt', 'r', encoding='utf-8') as file:
#     lines = file.readlines()
#     for line in lines:
#         if len(line) == len(max(lines, key=len)):
#             print(line.strip())

# Сумма чисел в строках
# with open('numbers.txt') as file:
#     for line in file.readlines():
#         print(sum([int(elem) for elem in line.split()]))

# with open('numbers.txt') as f:
#     for line in f:
#         print(sum(map(int, line.split())))


# # Сумма чисел в файле
# with open('numbers.txt', encoding='utf-8') as file:
#     row = ''.join(c if c.isdigit() else ' ' for c in file.read())
#     print(sum(map(int, row.split())))


# Статистика по файлу
# linesNum = 0
# wordsNum = 0
# lettersNum = 0
#
# with open('file.txt') as file:
#     for line in file.readlines():
#         linesNum += 1
#         wordsNum += len(line.split())
#         lettersNum += len([elem for elem in line if elem.isalpha()])
#
# print("Input file contains:\n" + str(lettersNum) + " letters\n" + str(wordsNum) + " words\n" + str(linesNum) + " lines")


# with open('lines.txt') as f:
#     txt = f.read()
#     print('Input file contains:')
#     print(sum(map(str.isalpha, txt)), 'letters')
#     print(len(txt.split()), 'words')
#     print(txt.count('\n') + 1, 'lines')


# # Random name and surname
# from random import randint
#
# firstNames = []
# lastNames = []
#
# with open('first_names.txt') as file:
#     for line in file.readlines():
#         firstNames.append(line)
#
# with open('last_names.txt') as file:
#     for line in file.readlines():
#         lastNames.append(line)
#
# for i in range(3):
#     print(firstNames[randint(0, len(firstNames))].strip() + ' ' + lastNames[randint(0, len(lastNames))].strip())


# Необычные страны
# with open('population.txt') as file:
#     for line in file.readlines():
#         if (line.startswith('G') and int(line.strip().split()[-1]) > 500000):
#             print(line.strip().split()[0])

# with open('population.txt') as f:
#     for line in f:
#         n, p = line.split('\t')
#         if n.startswith('G') and int(p) > 500000:
#             print(n)

# with open('population.txt',encoding='utf-8') as pop:
#     spisok=[str(i).rstrip().split() for i in pop.readlines() ]
#     for i in spisok:
#         if i[0][0]=='G' and int(i[-1])>500000:
#             print(i[0])


# # CSV-файл
# def read_csv():
#     with open('data.csv') as file:
#         keys = file.readline().strip().split(',')
#         return [dict(zip(keys, line.strip().split(','))) for line in file]


# 'r' - Read (чтение) Открыть файл только для чтения. Такой файл не может быть изменен.
# 'w'	 - Write (запись)	Открыть файл для записи. Если файл уже существует, то стереть его содержимое.
# Если файл не существует, он будет создан.
# 'a'	 - Append (добавление)	Открыть файл для записи. Все записываемые в файл данные будут
# добавлены в его конец. Если файл не существует, то он будет создан.
# 'r+' - 	Read + Write	Открыть файл для чтения и записи. В этом режиме происходит частичная перезапись
# содержимого файла с самого начала.
# 'x' - Create (создание)	Создать новый файл. Если файл уже существует, произойдет ошибка.

# Для записи используются два файловых метода:
# write() – записывает переданную строку в файл;
# writelines() – записывает переданный список строк в файл.

# Метод write()
# Общий формат применения файлового метода write():
# файловая_переменная.writе(строковое_значение)
#
# файловая переменная – это имя переменной, которая ссылается на файловый объект;
# строковое значение – это символьная последовательность, которая будет записана в файл.
# Для записи данных в файл он должен быть открыт для записи (режимы 'w', 'а', 'r+'), иначе произойдет ошибка.
# Если файл открыт в режиме 'w', то его содержимое сначала полностью стирается, а уже затем
# в него добавляются данные.
#
# После выполнения следующего кода:
#
# with open('myfile.txt', 'w', encoding='utf-8') as file:
#     file.write('Python and beegeek forever\n')
#     file.write('We love stepik <3')
# файл myfile.txt будет содержать:
#
# Python and beegeek forever
# We love stepik <3

# Если файл открыт в режиме 'a', то запись происходит в самый конец файла.
# После выполнения следующего кода:
#
# with open('myfile.txt', 'a', encoding='utf-8') as file:
#     file.write('Python and beegeek forever\n')
#     file.write('We love stepik <3')
# файл myfile.txt будет содержать:
#
# First line of the file.
# Second line of the file.
# Third line of the file.Python and beegeek forever
# We love stepik <3

# Если файл открыт в режиме 'r+', то происходит частичная перезапись его содержимого.
# После выполнения следующего кода:
#
# with open('myfile.txt', 'r+', encoding='utf-8') as file:
#     file.write('Python and beegeek forever\n')
#     file.write('We love stepik.')
# файл myfile.txt будет содержать:
#
# Python and beegeek forever
# We love stepik. file.
# Third line of the file.


# Метод writelines()
# Последовательные вызовы метода write() дописывают текст в конец файла.
#
# Приведенный ниже код создает файл philosophers.txt и записывает в него три строки текста:
#
# with open('philosophers.txt', 'w', encoding='utf-8') as file:
#     file.write('Джoн Локк\n')
#     file.write('Дэвид Хьюм\n')
#     file.write('Эдмyнд Берк\n')
# На практике часто приходится записывать в файл содержимое целого списка. Это можно сделать
# с помощью цикла или метода writelines(), что удобнее. Метод writelines() принимает в качестве
# аргумента список строк и записывает его в файл.
#
# Приведенный ниже код создает файл philosophers.txt и записывает в него содержимое списка philosophers:
#
# philosophers = ['Джoн Локк\n', 'Дэвид Хьюм\n', 'Эдмyнд Берк\n']
#
# with open('philosophers.txt', 'w', encoding='utf-8') as file:
#     file.writelines(philosophers)


# Запись в файл с помощью функции print()
# Для записи данных в файл можно также использовать встроенную функцию print().
# Для этого нужно передать ей еще один именованный аргумент file, указывающий на открытый файл.
# При этом функция print() автоматически добавляет переход на новую строку.
#
# Приведенный ниже код:
#
# with open('philosophers.txt', 'w', encoding='utf-8') as output:
#     print('Джoн Локк', file=output)
#     print('Дэвид Хьюм', file=output)
#     print('Эдмyнд Берк', file=output)
# создает файл philosophers.txt с содержимым:
#
# Джoн Локк
# Дэвид Хьюм
# Эдмyнд Берк
# Мы можем использовать всю мощность встроенной функции print() для форматирования выводимого текста.
#
# Приведенный ниже код:
#
# with open('philosophers.txt', 'w', encoding='utf-8') as output:
#     print('Джoн Локк', 'Дэвид Хьюм', 'Эдмyнд Берк', sep='***', file=output)
# создает файл philosophers.txt с содержимым:
#
# Джoн Локк***Дэвид Хьюм***Эдмyнд Берк

# Входная строка
# with open('output.txt', 'w') as output:
#     output.write(input())


# Случайные числа
# from random import randint
#
# with open('random.txt', 'w') as file:
#     arr = [str(randint(111, 777)) + '\n' for i in range(25)]
#     file.writelines(arr)


# Нумерация строк
# arr = []
# counter = 1
#
# with open('input.txt') as file:
#     for line in file.readlines():
#         arr.append(str(counter) + ') ' + line)
#         counter += 1
#
# with open('output.txt', 'w') as file:
#     file.writelines(arr)

# with open('input.txt') as inp, open('output.txt', 'w') as out:
#     for i, j in enumerate(inp, start=1):
#         print(f'{i}) {j}', end='', file=out)


# Подарок на новый год
# arr = []
#
# with open('class_scores.txt') as file:
#     for line in file.readlines():
#         arr.append(line.strip().split()[0] + ' ' + str(int(line.strip().split()[1]) + 5 if int(line.strip().split()[1]) < 95 else 100) + '\n')
#
# with open('new_scores.txt', 'w') as file:
#     file.writelines(arr)

# Загадка от Жака Фреско 🌶️
# with open('goats.txt', 'r', encoding='utf-8') as file, open('answer.txt', 'w', encoding='utf-8') as answer:
#     lst = []
#     for string in file.read().split('GOATS'):
#         lst.append(string.strip('COLOURS').strip('\n').strip(' goat ').split(' goat\n'))
#     for c in lst[0]:
#         if lst[1].count(c) > len(lst[1]) * 0.07:
#             print(f'{c} goat', file=answer)

# Конкатенация файлов 🌶️
# n = int(input())
# result = ''
#
# for i in range(n):
#     with open(input()) as file:
#         result += file.read()
#
# with open('output.txt', 'w') as file:
#     file.write(result)


# # Лог файл 🌶️
# import io
#
# result = []
#
# with io.open('logfile.txt', encoding='utf-8') as file:
#     for line in file:
#         name = line.strip().split(', ')[0]
#         startTime = line.strip().split(', ')[1]
#         endTime = line.strip().split(', ')[2]
#         if int(endTime.split(':')[0]) - int(startTime.split(':')[0]) > 1:
#             result.append(name + '\n')
#         if int(endTime.split(':')[0]) - int(startTime.split(':')[0]) == 1 and int(endTime.split(':')[1]) - int(startTime.split(':')[1]) >= 0:
#             result.append(name + '\n')
#
# with open('output.txt', 'w') as file:
#     file.writelines(result)
#


# if (n := int(input())) <= 10000:
#     print(f'Сумма {n} не превышает лимит, проходите')
# else:
#     print(f'Ого! {n}! Куда вам столько? Мы заберем {n - 10000}')

# if 'walrus' in (a := input()):
#     print('Нашли моржа')
# else:
#     print('Никаких моржей тут нет')

# match n := int(input()):
#     case 1:
#         print('Совсем еще зеленый студентик')
#     case 2:
#         print('Джун-студент')
#     case 3:
#         print('Мидл-студент')
#     case 4:
#         print('Сеньер-студент')
#     case 5:
#         print('Босс качалки')
#     case _:
#         print('Неизвестный курс')


# match n:= int(input()):
#     case 1|3|5|7|8|10|12:
#         print('31')
#     case 4|6|9|11:
#         print('30')
#     case 2:
#         print('28')

# match n:= input():
#     case 'Овен'|'Лев'|'Стрелец':
#         print('Огненный')
#     case 'Телец'|'Дева'|'Козерог':
#         print('Земной')
#     case 'Близнецы'|'Весы'|'Водолей':
#         print('Воздушный')
#     case 'Рак'|'Скорпион'|'Рыбы':
#         print('Водный')


# value = [1, 2, 3]
# match value:
#     case int() | float():
#         print("Имеем дело с числом")
#     case str():
#         print("Имеем дело со строкой")
#     case list():
#         print("Имеем дело со списком")
#     case  _:
#         print(f"Лучше с этим дел не иметь")

# my_tuple = (
# 32, 45, 32, 60, 43, 19, 39, 75, 50, 12, 53, 13, 28, 70, 68, 5, 64, 55, 30, 47, 23, 20, 17, 36, 45, 31, 46, 50, 33, 45,
# 9, 41, 12, 57, 40, 43, 47, 51, 56, 54, 40, 30, 37, 23, 43, 66, 64, 27, 44, 75, 51, 2, 19, 72, 30, 8, 29, 43, 7, 73, 34,
# 65, 54, 50, 43, 6, 50, 45, 49, 30, 39, 50, 41, 70, 38, 16, 31, 51, 72, 45, 58, 39, 50, 56, 24, 30, 9, 53, 27, 31, 68,
# 56, 26, 39, 34, 50, 10, 12, 3, 27)
#
# slice_5_10 = my_tuple[5:11]
# slice_from_20 = my_tuple[20::]
# slice_to_35 = my_tuple[0:35]
#
# print(slice_5_10)
# print(slice_from_20)
# print(slice_to_35)

# for i in [
#     [109, 121, 95, 116, 117, 112, 108, 101, 91, 53, 58, 49, 49, 93],
#     [109, 121, 95, 116, 117, 112, 108, 101, 91, 50, 48, 58, 93],
#     [109, 121, 95, 116, 117, 112, 108, 101, 91, 58, 51, 54, 93]
# ]:
#     print(''.join(chr(j) for j in i))

# words_tuple = ('quaint', 'leftovers', 'thesis', 'density', 'retired', 'weak', 'tolerate',
#                'sensitivity', 'primary', 'definition', 'determine', 'bring', 'monstrous',
#                'hurl', 'timetable', 'month', 'advocate', 'provoke', 'stress', 'omission')
# for i in words_tuple:
#     print(f'Длина слова {i} = {len(i)}')

# my_tuple = (
# -214, 181, -139, 448, -664, -66, 213, 832, 717, -462, -924, -706, -85, -244, -222, -340, -482, -518, -781, 759, -593,
# 905, -354, -377, -141, -742, 383, -381, 109, -639, -480, -810, -686, 892, -612, 696, 993, 791, 631, -493, -218, -829,
# -275, 619, -628, -241, -565, -835, -69, 747, 711, -252, -811, -407, -153, 904, 933, -254, 307, -493, -419, -109, -543,
# 155, -127, 613, -452, -459, 856, 562, 333, -66, -77, -598, -779, -278, 867, 321, -20, -415, -357, 735, -906, -14, -370,
# 453, -630, -736, -830, -917, 32, 422, -895, 198, 284, 472, -986, -964, -73, 29)
# l = []
# for i in my_tuple:
#     if i %2!=0:
#         l.append(i)
# print(sum(l)/len(l))

# currencies = {
#     'Argentine Peso': 118362.205708,
#     'Australian Dollar': 1586.232315,
#     'Bahraini Dinar': 423.780164,
#     'Botswana Pula': 13168.450636,
#     'Brazilian Real': 5954.781483,
#     'British Pound': 834.954104,
#     'Bruneian Dollar': 1520.451015,
#     'Bulgarian Lev': 1955.83,
#     'Canadian Dollar': 1430.54405,
#     'Chilean Peso': 898463.818465,
#     'Chinese Yuan Renminbi': 7171.445692,
#     'Colombian Peso': 4447741.922165,
#     'Croatian Kuna': 7527.744707,
#     'Czech Koruna': 24313.797041,
#     'Danish Krone': 7440.613895,
#     'Emirati Dirham': 4139.182587,
#     'Hong Kong Dollar': 8786.255952,
#     'Hungarian Forint': 355958.035747,
#     'Icelandic Krona': 143603.932438,
#     'Indian Rupee': 84241.767127,
#     'Indonesian Rupiah': 16187150.010697,
#     'Iranian Rial': 47534006.535121,
#     'Israeli Shekel': 3569.191411,
#     'Japanese Yen': 129149.364679,
#     'Kazakhstani Tenge': 489292.515538,
#     'Kuwaiti Dinar': 340.959682,
#     'Libyan Dinar': 5196.539901,
#     'Malaysian Ringgit': 4717.485104,
#     'Mauritian Rupee': 49212.933037,
#     'Mexican Peso': 23130.471272,
#     'Nepalese Rupee': 134850.008728,
#     'New Zealand Dollar': 1703.649473,
#     'Norwegian Krone': 9953.078431,
#     'Omani Rial': 433.360301,
#     'Pakistani Rupee': 198900.635421,
#     'Philippine Peso': 57574.278782,
#     'Polish Zloty': 4579.273862,
#     'Qatari Riyal': 4102.552652,
#     'Romanian New Leu': 4946.638369,
#     'Russian Ruble': 86197.012666,
#     'Saudi Arabian Riyal': 4226.530892,
#     'Singapore Dollar': 1520.451015,
#     'South African Rand': 17159.831129,
#     'South Korean Won': 1355490.097163,
#     'Sri Lankan Rupee': 228245.645722,
#     'Swedish Krona': 10439.125427,
#     'Swiss Franc': 1037.792217,
#     'Taiwan New Dollar': 31334.286611,
#     'Thai Baht': 37436.518169,
#     'Trinidadian Dollar': 7636.35428,
#     'Turkish Lira': 15078.75981,
#     'US Dollar': 1127.074905,
#     'Venezuelan Bolivar': 511082584.868731
# }
# val = input()
# # if val in currencies:
# #     print(currencies[val])
# # else:
# #     print(f'Нет данных по {val}')
#
#
# print(currencies[val] if val in currencies else f'Нет данных по {val}')

# account = {
#   "id": 3136,
#   "uid": "1359acc6-f07a-4a2a-984e-3fb809982948",
#   "account_number": "0847799459",
#   "iban": "GB90XTND56373623909314",
#   "bank_name": "ABN AMRO HOARE GOVETT CORPORATE FINANCE LTD.",
#   "routing_number": "126602476",
#   "swift_bic": "BCYPGB2LHGB"
# }
# # keys = []
# # for i in account:
# #     keys.append(i)
# # print(keys)
# print(keys := list(account))
#
# user = {
#     "id": 4170,
#     "uid": "5e941db5-9e0f-4f94-9fc5-734110c6be14",
#     "password": "SyUpfo1ljm",
#     "first_name": "Teresa",
#     "last_name": "Wehner",
#     "username": "teresa.wehner",
#     "email": "teresa.wehner@email.com",
#     "gender": "Non-binary",
#     "phone_number": "+674 424.561.2776",
#     "social_insurance_number": "637316241",
#     "date_of_birth": "1993-08-17"
# }
# user.pop('password')
# user.pop('last_name')
# user.setdefault("secret", "SyUpfo1ljm")
# user.setdefault("surname", "Wehner")
# print(user)


# s = input('Введите строку! Подсчитваем ее буквы: ')
# d = {}
# for i in s:
#     if i in d:
#         d[i] += 1
#     else:
#         d[i] = 1
# print(d)
# for letter, count in d.items():
#     print(letter, count)

# workers = {
#     'employer1': {'name': 'Jhon', 'salary': 7500},
#     'employer2': {'name': 'Emma', 'salary': 8000},
#     'employer3': {'name': 'Brad', 'salary': 500}
# }
# workers['employer3']['salary']=8500
# print(workers)

# supermarket = {
#     "milk": {"quantity": 20, "price": 1.19},
#     "biscuits": {"quantity": 32, "price": 1.45},
#     "butter": {"quantity": 20, "price": 2.29},
#     "cheese": {"quantity": 15, "price": 1.90},
#     "bread": {"quantity": 15, "price": 2.59},
#     "cookies": {"quantity": 20, "price": 4.99},
#     "yogurt": {"quantity": 18, "price": 3.65},
#     "apples": {"quantity": 35, "price": 3.15},
#     "oranges": {"quantity": 40, "price": 0.99},
#     "bananas": {"quantity": 23, "price": 1.29}
# }
# coast = 0
# for i in supermarket:
#     coast += supermarket[i]["quantity"] * supermarket[i]["price"]
# print(coast)
#
# s = 0
# for v in supermarket.values():
#     s += v.get('quantity') * v.get('price')
# print(s)

# my_list = [56, 59, 53, 75, 62, 61, 75, 65, 59, 62, 64, 53,
#            54, 62, 69, 53, 55, 62, 54, 66, 55, 57, 58, 75,
#            72, 55, 51, 56, 71, 66, 57, 56, 59, 73, 68, 57,
#            50, 54, 62, 68, 59, 64, 59, 59, 71, 68, 57, 54, 53, 72]
# my_set = set(my_list)
# print(sum(my_set)/len(my_set))

# name = set(input())
# print('CHAT WITH HER!' if len(name) % 2 == 0 else 'IGNORE HIM!')

# print(['NO', 'YES'][len(set(input().lower())) == 26])

# y = int(input()) + 1
# while len(set(str(y))) != 4:
#     y += 1
# print(y)
#
# user = {
#     "id": 4170,
#     "uid": "5e941db5-9e0f-4f94-9fc5-734110c6be14",
#     "password": "SyUpfo1ljm",
#     "first_name": "Teresa",
#     "last_name": "Wehner",
#     "username": "teresa.wehner",
#     "email": "teresa.wehner@email.com",
#     "gender": "Non-binary",
#     "phone_number": "+674 424.561.2776",
#     "social_insurance_number": "637316241",
#     "date_of_birth": "1993-08-17",
#     "employment": {
#         "title": "Central Hospitality Liaison",
#         "key_skill": "Organisation"
#     },
#     "subscription": {
#         "plan": "Essential",
#         "status": "Idle",
#         "payment_method": "Debit card",
#         "term": "Annual"
#     }
# }
# print({key: user[key] for key in input().split()})

#
# set_a = {31, 37, 39, 41, 47, 58, 60, 62, 70, 75,
#          76, 77, 78, 79, 80, 81, 85, 86, 88, 90, 93, 96, 98, 99}
#
# set_b = {0, 1, 8, 16, 17, 18, 22, 24, 29, 31,
#          33, 34, 36, 42, 46, 47, 51, 53, 62, 64, 65, 66, 67}
#
# print(len(set_a ^ set_b))
# print(len(set_b - set_a))

# A = {'a', 'b', 'c', 'd'}
# B = {'c', 'd', 'e'}
# print(B - A)

# words = ['mention', 'soup', 'pneumonia', 'tradition', 'concert', 'tease', 'generation',
#          'winter', 'national', 'jacket', 'winter', 'wrestle', 'proposal', 'error',
#          'pneumonia', 'concert', 'value', 'value', 'disclose', 'glasses', 'tank',
#          'national', 'soup', 'feel', 'few', 'concert', 'wrestle', 'proposal', 'soup',
#          'sail', 'brown', 'service', 'proposal', 'winter', 'jacket', 'mention', 'tradition',
#          'value', 'feel', 'bear', 'few', 'value', 'winter', 'proposal', 'government',
#          'control', 'value', 'few', 'generation', 'service', 'national',
#          'tradition', 'government', 'mention', 'proposal']
# print(len([i for i in set(words) if len(i) > 6]))

# english_words = ('attack', 'bless', 'look', 'reckless', 'short', 'monster', 'trolley', 'sound',
#                  'ambiguity', 'researcher', 'trunk', 'coat', 'quantity', 'question', 'tenant',
#                  'miner', 'definite', 'kit', 'spectrum', 'satisfied', 'selection', 'carve',
#                  'ask', 'go', 'suggest')
#
# for index, value in enumerate(english_words,1):
#   print(f'Word № {index} = {value}')
#
# [print(f'Word № {key} = {value}') for key, value in enumerate(english_words, 1)]

# lst = list(map(int, input()))
# for i in range (len(lst)):
#     if i % 2 == 0:
#         if lst[i] * 2 > 9:
#             lst[i] = lst[i] * 2 - 9
#         else:
#             lst[i] *= 2
# if sum(lst) % 10 == 0:
#     print(True)
# else:
#     print(False)


# keys = ['Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety', 'One hundred']
# values = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# result = dict(zip(keys, values))
# print(result)

# employees = [
#     'Pankratiy', 'Innokentiy', 'Anfisa', 'Yaroslava', 'Veniamin',
#     'Leonti', 'Daniil', 'Mishka', 'Lidochka',
#     'Terenti', 'Vladik', 'Svetka', 'Maks', 'Yura', 'Sergei'
# ]
#
# identifiers = [77, 48, 88, 85, 76, 81, 62, 43, 5, 56, 17, 20, 37, 32, 96]
#
# employees_data = dict(zip(sorted(identifiers), sorted(employees)))
# print(employees_data)

# def fake_bin(x):
#     res = ''
#     for i in x:
#         if int(i) < 5:
#             res += '0'
#         else:
#             res += '1'
#     return res
#
#
# x = input()
# print(fake_bin(x))

# def count_sheep(n):
#     res = ''
#     for i in range(1, n+1):
#         res += f"{i} sheep..."
#     return res
#
# print(count_sheep(int(input())))

# def remove_char(s):
#     return s[1:-1]
#
# print(remove_char('qwerty'))

# def remove_exclamation_marks(s):
#     return s.replace('!', '')

# def abbrev_name(name):
#     return ".".join([w[0].upper() for w in name.split()])

# def area_or_perimeter(l, w):
#     return l * w if l == w else 2 * (l + w)

# def dna_to_rna(dna):
#     return dna.replace('T','U')
#
# print( dna_to_rna("GACCGCCGCC"))


# def rps(p1, p2):
#     if p1 == p2:
#         return "Draw!"
#     elif p1 == "scissors" and p2 == "paper" or p1 == "paper" and p2 == "rock" or p1 == "rock" and p2 == "scissors":
#         return "Player 1 won!"
#     else:
#         return "Player 2 won!"

#
# def basic_op(operator, value1, value2):
#     if operator =='+': return int(value1) + int(value2)
#     if operator =='-': return int(value1) - int(value2)
#     if operator =='*': return int(value1) * int(value2)
#     if operator =='/': return int(value1) / int(value2)
#
# print(basic_op("+", 2, 3))

# def disemvowel(string):
#     for i in "aeiouAEIOU":
#         string = string.replace(i, "")
#     return string
#
# def disemvowel(string):
#     return "".join(c for c in string if c.lower() not in "aeiou")
#
# print(disemvowel('This website is for losers LOL'))
#
#
# def high_and_low(numbers):
#     a, b = max(numbers.split()), min(numbers.split())
#     return ' '.join([(a), (b)])
#
# print(high_and_low("1 2 3 4 5"))  # return "5 1")
# print(high_and_low("1 2 -3 4 5")) # return "5 -3")
# print(high_and_low("1 9 3 4 -5")) # return "9 -5")

# def longest(a1, a2):
#     return ''.join(sorted(set(a1+a2)))
#
# a = "xyaabbbccccdefww"
# b = "xxxxyyyyabklmopq"
# print(longest(a, b)) #-> "abcdefklmopqwxy"


# def get_middle(s):
#     if len(s) % 2 == 0:
#         return s[1:-1]
#     else:
#         return s[int(len(s)/2-0.5)]
#
#     return s[len(s) // 2] if len(s) % 2 != 0 else s[len(s) // 2 - 1:len(s) // 2 + 1]
#
# print(get_middle('id'))

# def descending_order(num):
#     return num[::-1].sort
#
# print(descending_order(145263))


# def get_count(sentence):
#     cnt = 0
#     for i in sentence:
#         if i in "aeiou":
#             cnt += 1
#     return cnt
#
# print(get_count('asdfe'))

# def friend(x):
#     a = []
#     for i in x:
#         if len(i) == 4:
#             a.append(i)
#     return a
#
# print(friend(["Ryan", "Kieran", "Mark",]))

# def is_isogram(string):
#     return len(string) == len(set(string.lower()))
#
# def generate_hashtag(s):
#     return '#'+''.join(s.replace(' ', ''))
#
# print(generate_hashtag('Codewars Is Nice'))

# def reverse_words(text):
#   return ' '.join([word[::-1] if len(word)>=5 else word for word in text.split(' ') ])
#
# print(reverse_words("This is an example!"))

# def spin_words(sentence):
#   return ' '.join([word[::-1] if len(word)>=5 else word for word in sentence.split(' ') ])
#
# print(spin_words("This is an example"))

# def is_divisible(n,x,y):
#     return n%x == 0 and n%y == 0
#
# print(is_divisible(12,2,6))

# def make_readable(seconds):
#     h = seconds // 3600
#     m = (seconds - h * 3600) // 60
#     s = seconds - (h * 3600) - (m * 60)
#     return f"{h:0>2d}:{m:0>2d}:{s:0>2d}"

# print(sum([int(input()) for i in range(int(input()))]))

# x = [1, 2, 3]
# y = x
# y.append(4)
#
# s = "123"
# t = s
# t = t + "4"
#
# print(str(x) + " " + s)

# # objects = [1, 2, 1, 2, 3]
# ans = 0
# objA = []
# for obj in objects:
#     if id(obj) not in objA:
#         ans += 1
#         objA.append(id(obj))
#
# print(ans)

# a = []
# def foo(arg1, arg2):
#   a.append("foo")
# foo(a.append("arg1"), a.append("arg2"))
# print(a)

# class Stack:
#     def __init__(self):
#         self.values = []
#         self.size = 0
#         self.maxsize = 0
#
#     def push(self, element):
#         self.values.append(element)
#         self.size += 1
#         if self.maxsize < self.size:
#             self.maxsize = self.size
#
#         print(self.values, '| size =', self.size, '| maxsize =', self.maxsize)
#
#     def pop(self):
#         assert self.size > 0, 'Нельзя удалять элементы из пустого стека'
#         element = self.values.pop()
#         self.size -= 1
#         print(self.values, '| size =', self.size, '| maxsize =', self.maxsize)
#         return element
#
# stack = Stack()
# stack.push('module')
#
# def h():
#     stack.push('h')
#     stack.push('print')
#     print(12)
#     stack.pop()  # print
#     stack.pop()  # h
#
# def f():
#     stack.push('f')
#     g(h)
#     stack.pop()  # f
#
# def g(a):
#     stack.push('g')
#     a()
#     stack.pop()  # g
#
# g(f)
# print('\nМаксимальный размер стека (maxsize) =', stack.maxsize)


# def closest_mod_5(x):
#     if x % 5 == 0:
#         return x
#     return "I don't know :("

# def C(n, k):
#     if k == 0:
#         return 1
#     elif k > n:
#         return 0
#     else:
#         return C(n - 1, k) + C(n - 1, k - 1)
#
#
# n, k = map(int, input().split())
# print(C(n, k))


# class A:
#     def __init__(self, val=0):
#         self.val = val
#
#     def add(self, x):
#         self.val += x
#
#     def print_val(self):
#         print(self.val)
#
#
# a = A()
# b = A(2)
# c = A(4)
# a.add(2)
# b.add(2)
#
# a.print_val()
# b.print_val()
# c.print_val()

# class MoneyBox:
#     def __init__(self, capacity):
#         self.capacity = capacity
#         self.count = 0
#
#     def can_add(self, v):
#         return self.count + v <= self.capacity
#
#     def add(self, v):
#         if self.can_add(v):
#             self.count += v

# class Buffer:
#
#     def __init__(self):
#         self.current_part = []
#
#     def add(self, *a):
#         self.current_part.extend(a)
#         while len(self.current_part) - 5 >= 0:
#             print(sum(self.current_part[0:5]))
#             self.current_part = self.current_part[5:]
#
#     def get_current_part(self):
#         return self.current_part
#
# buf = Buffer()
# buf.add(1, 2, 3)
# buf.get_current_part() # вернуть [1, 2, 3]
# buf.add(4, 5, 6) # print(15) – вывод суммы первой пятерки элементов
# buf.get_current_part() # вернуть [6]
# buf.add(7, 8, 9, 10) # print(40) – вывод суммы второй пятерки элементов
# buf.get_current_part() # вернуть []
# buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1) # print(5), print(5) – вывод сумм третьей и четвертой пятерки
# buf.get_current_part() # вернуть [1]

# class A:
#     val = 1
#
#     def foo(self):
#         A.val += 2
#
#     def bar(self):
#         self.val += 1
#
#
# a = A()
# b = A()
#
# a.bar()
# a.foo()
#
# c = A()
#
# print(a.val)
# print(b.val)
# print(c.val)

# classes = {}
#
# def add_class(classes, class_name, parents):
#     if class_name not in classes:
#         classes[class_name] = []
#     classes[class_name].extend(parents)
#     for parent in parents:
#         if parent not in classes:
#             classes[parent] = []
#
# def found_path(classes, start, end, path=[]):
#     path = path + [start]
#     if start == end:
#         return path
#     if start not in classes:
#         return None
#     for node in classes[start]:
#         if node not in path:
#             newpath = found_path(classes, node, end, path)
#             if newpath: return newpath
#     return None
#
# def answer(classes, parent, child):
#     if not(parent or child) in classes or not found_path(classes, child, parent):
#         return 'No'
#     return 'Yes'
#
# n = int(input())
# for _ in range(n):
#     class_description = input().split()
#     class_name = class_description[0]
#     class_parents = class_description[2:]
#     add_class(classes, class_name, class_parents)
#
# q = int(input())
# for _ in range(q):
#     question = input().split()
#     parent = question[0]
#     child = question[1]
#     print(answer(classes, parent, child))


# class LoggableList(Loggable, list):
#     def append(self, arg):
#         super(LoggableList, self).append(arg)
#         self.log(arg)

# class Color:
#     red = 0
#     green = 0
#     blue = 0
#
#     def __init__(self, r, g, b):
#         red = r
#         green = g
#         blue = b
#
#     def toHex(self):
#         return '#%02x%02x%02x' % (red, green, blue)
#
#
# grey = Color(80, 80, 80)

# class Point(object):
#     def __init__(self, x, y, z):
#         self.coord = (x, y, z)
#
# p = Point(13, 14, 15)
# print(p.coord) # (13, 14, 15)


# class Point:
#     color = 'red'
#     circle = 2
#
#     def set_coords(self, x, y):
#         self.x = x
#         self.y = y
#
# pt = Point()
# pt.set_coords(10, 20)
#
# print(pt.__dict__)


# class Calculator:
#     def add(self, a, b):
#         return a + b
#
#     def subtract(self, a, b):
#         return a - b
#
#     def multiply(self, a, b):
#         return a * b
#
#     def divide(self, a, b):
#         return a / b


# # create a calculator object
# my_calc = Calculator()
#
# while True:
#
#     print("1: Add")
#     print("2: Subtract")
#     print("3: Multiply")
#     print("4: Divide")
#     print("5: Exit")
#
#     operation = int(input("Select operation: "))
#
#     # Make sure the user have entered the valid choice
#     if operation in (1, 2, 3, 4, 5):
#
#         # first check whether user want to exit
#         if (operation == 5):
#             break
#
#         # If not then ask fo the input and call appropiate methods
#         a = int(input("Enter first number: "))
#         b = int(input("Enter second number: "))
#
#         if (operation == 1):
#             print(a, "+", b, "=", my_calc.add(a, b))
#         elif (operation == 2):
#             print(a, "-", b, "=", my_calc.subtract(a, b))
#         elif (operation == 3):
#             print(a, "*", b, "=", my_calc.multiply(a, b))
#         elif (operation == 4):
#             print(a, "/", b, "=", my_calc.divide(a, b))
#
#     else:
#         print("Invalid Input")






