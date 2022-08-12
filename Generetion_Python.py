# a, b, c, d = input(), input(), input(), input()
# print(b, c, d, sep=a)

# print('Привет,',input(), end='!')

# a = int(input())
# print(a, a+1, a+2, sep='\n' )

# print(int(input()) + int(input()) + int(input()))

# a = int(input())
# print('Объем =', a ** 3)
# print('Площадь полной поверхности =', 6 * a ** 2)

# a, b = int(input()), int(input())
# print(3 * (a + b) ** 3 + 275 * b ** 2 - 127 * a - 41)

# a = int(input())
# print('Следующее за числом', a, 'число:', a + 1)
# print('Для числа', a, 'предыдущее число:', a - 1)

# print((int(input()) + int(input()) + int(input()) + int(input()))*3)

# a, b = int(input()),int(input())
# print(a, '+', b, "=", a + b)
# print(a, '-', b, "=", a - b)
# print(a, '*', b, "=", a * b)

# a, d, n = int(input()), int(input()), int(input())
# print(a + d*(n - 1))

# a = int(input())
# print(a, a*2, a*3, a*4, a*5, sep='---')

# b, q, n = int(input()), int(input()), int(input())
# print(b * q**(n - 1))

# полное число метров по заданному числу сантиметров
# print(int(input())//100)

# a, b = int(input()), int(input())   #количество школьников и количество мандаринов
# print(b // a)  #количество мандаринов, которое достанется каждому школьнику
# print(b % a)  #количество мандаринов, которое останется в корзине

# Сама неотвратимость
# a = int(input())
# print(a // 2 + a % 2)

# вывести число – номер купе, в котором находится указаное место
# a = int(input())
# print((a + 3) // 4)

# a = int(input())
# print(a,'мин - это', a//60, 'час', a%60, 'минут.')

# num = 754
# a = num % 10
# b = (num % 100) // 10
# c = num // 100
# print(a)
# print(b)
# print(c)

# Последняя цифра: (num % 10**1) // 100;
# Предпоследняя цифра: (num % 10**2) // 101;
# Предпредпоследняя цифра: (num % 10**3) // 102;
# .....
# Вторая цифра: (num % 10**n-1) // 10**n-2;
# Первая цифра: (num % 10**n) // 10**n-1.

# n = 45238
# digit1 = n // 10000
# digit2 = n % 10000 // 1000
# digit3 = n % 1000 // 100
# digit4 = n % 100 // 10
# digit5 = n % 10
# print(digit1,digit2,digit3,digit4,digit5)

# num = int(input())
# last_digit = num % 10
# first_digit = num // 10
# print('Число десятков =', first_digit)
# print('Число единиц =', last_digit)

# вводится трёхзначное число и которая выводит на экран его цифры
# num = int(input())
# digit3 = num % 10
# digit2 = (num // 10) % 10
# digit1 = num // 100
# print(digit1, digit2, digit3, sep=',')

# a = int(input())
# print('Сумма цифр =', (a // 100) + (a // 10 % 10) + (a % 10))
# print('Произведение цифр =', (a // 100) * (a // 10 % 10) * (a % 10))


# n = int(input())
# c = n % 10
# b = (n // 10) % 10
# a = n // 100
# print(a, b, c,sep='')
# print(a, c, b,sep='')
# print(b, a, c,sep='')
# print(b, c, a,sep='')
# print(c, a, b,sep='')
# print(c, b, a,sep='')
#
# a,b,c = input()
# print(a+b+c, a+c+b, b+a+c, b+c+a, c+a+b, c+b+a, sep='\n')

# n = int(input())
# a, b, c = str(n // 100), str(n // 10 % 10), str(n % 10)
# print(a+b+c, a+c+b, b+a+c, b+c+a, c+a+b, c+b+a, sep='\n')


# num = input()
# digit4 = num % 10
# digit3 = (num // 10) % 10
# digit2 = (num // 100) % 10
# digit1 = num // 1000

# print('Цифра в позиции тысяч равна', num[0])
# print('Цифра в позиции сотен равна', num[1])
# print('Цифра в позиции десятков равна', num[2])
# print('Цифра в позиции единиц равна', num[3])

# a, b, c, d = input()
# print('Цифра в позиции тысяч равна ' + a, 'Цифра в позиции сотен равна ' + b, 'Цифра в позиции десятков равна ' + c,
#       'Цифра в позиции единиц равна ' + d, sep='\n')

# a, b = int(input()), int(input())
# print('Квадрат суммы', a, 'и', b, 'равен', (a+b)**2)
# print('Сумма квадратов', a, 'и', b, 'равна', a**2 + b**2)

# a, b, c, d = int(input()), int(input()), int(input()), int(input())
# print(a ** b + c ** d)


# Программа должна вывести число n + nn + nnn
#
# n = int(input())
# nn = n * 10 + n
# nnn = n * 100 + n * 10 + n
# print(n + nn + nnn)
#
# n = input()
# print(int(n) + int(n * 2) + int(n * 3))

# a, b = input(), input()
# if a == b:
#     print('Пароль принят')
# else:
#     print('Пароль не принят')
#
# print('Пароль принят' if input() == input() else 'Пароль не принят')

# сумма первой и последней цифр равна разности второй и третьей цифр
# a = input()
# print('ДА' if int(a[0]) + int(a[3]) == int(a[1]) - int(a[2]) else 'НЕТ')

# print('Доступ разрешен' if int(input()) >= 18 else 'Доступ запрещен')

# a,b,c = int(input()),int(input()),int(input())
# print('YES' if b - a == c - b else 'NO')

# a, b = int(input()), int(input())
# print(a if a < b else b)


# print(min(int(input()),int(input()),int(input()),int(input())))
# a = int(input())
# if a <= 13:
#     print('детство');
# if 14 <= a <= 24:
#     print('молодость')
# if 25 <= a <= 59:
#     print('зрелость')
# if a>=60:
#     print('старость')

# a, b, c = int(input()), int(input()), int(input())
# sum = 0
# if a >= 0:
#     sum += a
# if b >= 0:
#     sum += b
# if c >= 0:
#     sum += c
# print(sum)

# определяет номер координатной четверти, в которой она находится
# x = int(input())
# y = int(input())
# if x > 0 and y > 0:
#     print('1 четверть')
# if x < 0 and y > 0:
#     print('2 четверть')
# if x < 0 and y < 0:
#     print('3 четверть')
# if x > 0 and y < 0:
#     print('4 четверть')

# x = int(input())
# print('Принадлежит' if -30 < x <= -2 or 7 < x <= 25 else 'Не принадлежит')

# является четырехзначным и делится нацело на 77 или на 1717
# x = input()
# print('YES' if len(x) == 4 and (int(x) % 7 == 0 or int(x) % 17 == 0) else 'NO')

# x = input()
# if len(x)==4 and (int(x) % 7 == 0 or int(x) % 17 == 0):
#     print('YES')
# else:
#     print('NO')

# Неравенство треугольника
# a, b, c = int(input()), int(input()), int(input())
# print('YES' if a + b > c and a + c > b and b + c > a else 'NO')

# Високосный год
# Год является високосным, если его номер кратен 4, но не кратен 100, или если он кратен 400
# a = int(input())
# print('YES' if a % 400 == 0 or (a % 4 == 0 and a % 100 != 0) else 'NO')

# Ход ладьи
# x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
# print('YES' if x1 == x2 or y1 == y2 else 'NO')

# Ход короля
# x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
# print('YES' if -1 <= (x2 - x1) <= 1 and -1 <= (y2 - y1) <= 1 else 'NO')

# n, k = int(input()), int(input())  #zoomm/flash
# if n>k:
#     print('NO')
# elif k>n:
#     print('YES')
# else:
#     print("Don't know")

# n, k = int(input()), int(input())
# print("Don't know" if n == k else "YES" if n < k else "NO")

# a, b, c = int(input()), int(input()), int(input())
# print("Разносторонний" if a!=b!=c!=a else "Равносторонний" if a==b==c else "Равнобедренный")

# Среднее число
# a, b, c = int(input()), int(input()), int(input())
# if c > a > b or c < a < b:
#     print(a)
# elif a > b > c or a < b < c:
#     print(b)
# elif b > c > a or b < c < a:
#     print(c)

# a, b, c = int(input()), int(input()), int(input())
# print(a if c > a > b or c < a < b else b if a > b > c or a < b < c else c)

# Количество дней в месяце
# a = int(input())
# if a in (1, 3, 5, 7, 8, 10, 12):
#     print('31')
# elif a in (4, 6, 9, 11):
#     print("30")
# elif a == 2:
#     print('28')

# a = int(input())
# if a<60:
#     print('Легкий вес')
# elif 60<=a<64:
#     print('Первый полусредний вес')
# elif 64<=a<69:
#     print("Полусредний вес")
#

# Самописный калькулятор
# a, b, z = int(input()),int(input()),input()
# if z not in ('+', '-', '*', '/'):
#     print('Неверная операция')
# elif z == '+':
#     print(a+b)
# elif z == '-':
#     print(a-b)
# elif z == '*':
#     print(a*b)
# elif z == '/':
#     if b == 0:
#         print('На ноль делить нельзя!')
#     else:
#         print(a / b)

# Цветовой микшер
# если смешать красный и синий, то получится фиолетовый;
# если смешать красный и желтый, то получится оранжевый;
# если смешать синий и желтый, то получится зеленый.

# a, b = input(), input()
# if a not in ('синий', 'красный', 'желтый') or b not in ('синий', 'красный', 'желтый'):
#     print('ошибка цвета')
# elif a == "красный" and b == "синий" or b == "красный" and a == "синий":
#     print("фиолетовый")
# elif a == "красный" and b == "желтый" or b == "красный" and a == "желтый":
#     print("оранжевый")
# elif a == "синий" and b == "желтый" or b == "синий" and a == "желтый":
#     print("зеленый")
# elif a == "синий" and b == "синий":
#     print("синий")
# elif a == "красный" and b == "красный":
#     print("красный")
# elif a == "желтый" and b == "желтый":
#     print("желтый")

# Цвета колеса рулетки
# a = int(input())
# if a < 0 or a > 36:
#     print('ошибка ввода')
# elif a == 0:
#     print('зеленый')
# elif 1 <= a <= 10:
#     if a % 2 != 0:
#         print('красный')
#     else:
#         print('черный')
# elif 11 <= a <= 18:
#     if a % 2 != 0:
#         print('черный')
#     else:
#         print('красный')
# elif 19 <= a <= 28:
#     if a % 2 != 0:
#         print('красный')
#     else:
#         print('черный')
# elif 29 <= a <= 36:
#     if a % 2 != 0:
#         print('черный')
#     else:
#         print('красный')


# a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())
# if a2 > b1 or a1 > b2:  # отсекаем отсутствие пересечений и общей точки
#     print('пустое множество')
# elif a1 == b2:  # первое условие общей точки
#     print(a1)
# elif a2 == b1:  # второе условие общей точки
#     print(a2)
# else:  # осталось найти только пересечение
#     if a1 > a2:  # получаем первую точку пересечения путем отсечения лишней точки
#         a2 = a1
#     if b1 < b2:  # получаем вторую точку пересечения
#         b2 = b1
#     print(a2, b2)

# a = input()
# if a[-1] == '0' and a[-2] == '0':
#     print('YES')
# else:
#     print('NO')

# x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
# print('YES' if (x1 + x2 + y1 + y2) % 2 == 0 else 'NO')

# x, s = int(input()), input()
# print('YES' if 10 <= x <= 15 and s == 'f' else 'NO')

# n = int(input())
# if n < 1 or n > 10:
#     print('ошибка ввода')
# elif n == 1:
#     print('I')
# elif n == 2:
#     print('II')
# elif n == 3:
#     print('III')
# elif n == 4:
#     print('IV')
# elif n == 5:
#     print('V')
# elif n == 6:
#     print('VI')
# elif n == 7:
#     print('VII')
# elif n == 8:
#     print('VIII')
# elif n == 9:
#     print('IX')
# elif n == 10:
#     print('X')

# sp = 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X'

# a = int(input())
# if a%2 != 0:
#     print('YES')
# elif a%2 == 0 and 2<=a<=5:
#     print('NO')
# elif a%2 == 0 and 6<=a<=20:
#     print('YES')
# elif a%2 == 0 and 20<a:
#     print('NO')

# Ход слона
# Условие x1 - y1 == x2 - y2 соответствует одной диагонали, а условие x1 + y1 == x2 + y2 -- другой диагонали.
# Так как слон ходит по обоим диагоналям, то используем логическую операцию or
# x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
# print('YES' if (x1 - y1 == x2 - y2) or (x1 + y1 == x2 + y2) else 'NO')

# Ход коня
# Разница координат по оси х == 1, разница координат по оси y == 2
# или
# Разница координат по оси х == 2, разница координат по оси y == 1
# Разница координат может быть как положительная, так и отрицательная - берем модуль
# x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
# print('YES' if (x1 - x2) ** 2 + (y1 - y2) ** 2 == 5 else 'NO')


# Ход ферзя
# x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
# print('YES' if abs(x1 - x2) == abs(y1 - y2) or x1 == x2 or y1 == y2 else 'NO')

# Площадь треугольника
# a, b = float(input()), float(input())
# print(0.5 * a * b)

# s, v1, v2 = float(input()), float(input()), float(input())
# print(s/(v1 + v2))

# Обратное число
# x = float(input())
# print('Обратного числа не существует' if x == 0 else (1/x))

# какой температуре по шкале Цельсия соответствует указанное значение по шкале Фаренгейта
# print(5/9*(float(input())-32))

# Dog age
# age = int(input())
# if 0 < age <= 2:
#     print(age * 10.5)
# else:
#     print(2 * 10.5 + (age - 2) * 4)


# Первая цифра после точки
# умножить на 10, для того что бы перевести значение после запятой в целые,
# потом посмотреть остаток через "%" и показать только целочисленное значение.
# a = float(input())
# print(int(a*10%10))

# Выведите его дробную часть.
# a = float(input())
# print(a % int(a))

# print(float(input()) % 1)

# a, b, c, d, e = int(input()), int(input()), int(input()), int(input()), int(input())
# print('Наименьшее число =', min(a, b, c, d, e))
# print('Наибольшее число =', max(a, b, c, d, e))

# Сортировка трёх
# num = int(input()), int(input()), int(input())
# print(*sorted(num,reverse=True), sep='\n')

# Интересное число
# разность максимальной и минимальной цифры равняется средней
# n = sorted(input())
# print('Число интересное' if int(n[2]) - int(n[0]) == int(n[1]) else'Число неинтересное')

# Абсолютная сумма
# a, b, c, d, e = float(input()), float(input()), float(input()), float(input()), float(input())
# print(abs(a) + abs(b) + abs(c) + abs(d) + abs(e))

# Манхэттенское расстояние
# p1, p2, q1, q2 = int(input()), int(input()), int(input()), int(input())
# print(abs(p1-q1)+abs(p2-q2))

# print(f'Hello {input()} {input()}! You just delved into Python')

# n = input()
# print(f'Футбольная команда {n} имеет длину {len(n)} символов')

# Три города
# вывести самое короткое и длинное название города, каждое на отдельной строке
# a, b, c = input(), input(), input()
# # if min(len(a), len(b), len(c)) == len(a):
# #     print(a)
# # elif min(len(a), len(b), len(c)) == len(b):
# #     print(b)
# # else: print(c)
# # if max(len(a), len(b), len(c)) == len(a):
# #     print(a)
# # elif max(len(a), len(b), len(c)) == len(b):
# #     print(b)
# # else: print(c)
# print(a if min(len(a), len(b), len(c)) == len(a) else b if min(len(a), len(b), len(c)) == len(b) else c)
# print(a if max(len(a), len(b), len(c)) == len(a) else b if max(len(a), len(b), len(c)) == len(b) else c)

# Арифметические строки
# можно ли из длин этих строк построить возрастающую арифметическую прогрессию
# a = len(input())
# b = len(input())
# c = len(input())
#
# if a + b + c == (min(a, b, c) + max(a, b, c))/2*3:
#     print("YES")
# else:
#     print("NO")

# print('YES' if 'синий' in input() else 'NO')

# print(*[f"Футбольная команда {name} имеет длину {len(name)} символов" for name in input().split("\n")])
# С версии 3.8 можно использовать выражения присваивания (PEP 572)
# print(f"Футбольная команда {(name := input())} имеет длину {len(name)} символов")


# s = input()
# if 'суббота' in s or 'воскресенье' in s:
#     print('YES')
# else:
#     print('NO')
#
# s = input()
# print("YES" if "суббота" in s or "воскресенье" in s else "NO")

# print('YES' if 'суббота' in (text := input()) or 'воскресенье' in text else 'NO')

# text = input()
# print('YES' if '@' in text and '.' in text else 'NO')

# Евклидово расстояние
# from math import sqrt
#
# x1, y1, x2, y2 = float(input()), float(input()), float(input()), float(input())
# print(sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2))

# Площадь и длина
# from math import pi
#
# r = float(input())
# print(pi*r**2)
# print(2*pi*r)

# Средние значения
# from math import sqrt
#
# a, b = float(input()), float(input())
# print((a + b) / 2)
# print(sqrt(a * b))
# print(2 * a * b / (a + b))
# print(sqrt((a ** 2 + b ** 2 )/ 2))

# Тригонометрическое выражение
# from math import sin, cos, tan, radians
# r = radians(float(input()))
# print(sin(r)+cos(r)+tan(r)**2)


# Пол и потолок
# from math import floor, ceil
# x = float(input())
# print(ceil(x) + floor(x))


# Квадратное уравнение
# from math import *
#
# a = float(input())
# b = float(input())
# c = float(input())
# d = b**2-4*a*c        # Ищем дискриминант
#
# if d < 0:
#     print('Нет корней')
# elif d == 0:          # если дискриминант ==0 (имеет один корень)
#     print(-b / (2*a))
# elif d > 0:           # Если дискриминант >0 то два корня
#     x1 = (-b - d ** 0.5) / (2*a)
#     x2 = (-b + d ** 0.5) / (2*a)
#     print(min(x1, x2))
#     print(max(x1, x2))
#
# Правильный многоугольник
# from math import *
# n, a = float(input()), float(input())
# ans = (n * pow(a, 2)) / (4 * tan(pi / n))
# print(ans)

# for i in range(10):
#     print('Python is awesome!')

# t = input()
# for i in range(int(input())):
#     print(t)

# for a in range(6):
#     print('AAA')
# for a in range(5):
#     print('BBBB')
# print('E')
# for a in range(9):
#     print('TTTTT')
# print("G")

# for a in range(int(input())):
#     print('*'*19)

# a = input()
# for i in range(10):
#     print(i, a)
#
# s = str(input())
# [print(i, s) for i in range(10)]

# for i in range(int(input())+1):
#     print(f'Квадрат числа {i} равен {i**2}')

# n = int(input())
# for i in range(n+1):
#     print('*'*(n-i))
#
# for i in range(int(input()), 0, -1):
#     print("*" * i)

# Популяция
# m, p, n = int(input()), int(input()), int(input())
# for i in range(n):
#     print(i+1, m * (p / 100+1) ** i)

# Последовательность чисел
# n,m = int(input()),int(input())
# for i in range(n,m+1):
#     print(i)
#
# print(*range(int(input()), int(input()) + 1), sep='\n')

# Последовательность чисел 2
# n, m = int(input()), int(input())
#
# if n < m:
#     for i in range(n, m + 1):
#         print(i)
# else:
#     for i in range(n, m-1, -1):
#         print(i)

# Последовательность чисел 3
# n, m = int(input()), int(input())
# for i in range(((n - 1) // 2) * 2 + 1, m - 1, -2):
#     if i % 2 != 0:
#         print(i)

# Последовательность чисел 4
# m = int(input())
# n = int(input())
#
# for i in range(m, n + 1):
#     if i % 17 == 0 or i % 10 == 9 or i % 15 == 0:
#         print(i)

# Таблица умножения на N
# n = int(input())
# for i in range(1,11):
#     print(f'{n} x {i} = {n*i}')
#
# n = int(input())
# [print(f'{n} x {i} = {n * i}') for i in range(1, 11)]
#
# (lambda n: [print(f'{n} x {i} = {n*i}') for i in range(1, 11)])(int(input()))

# Количество чисел
# a, b = int(input()), int(input())
# count = 0
# for i in range(a, b + 1):
#     if i ** 3 % 10 == 4 or i ** 3 % 10 == 9:
#         count += 1
# print(count)

# # Сумма чисел
# n = int(input())
# count = 0
# for i in range(n):
#     b = int(input())
#     count += b
# print(count)

# Асимптотическое приближение
# from math import log        # Импортируем из math функцию log
# diff = 0                       # Задаем стартовое значение переменной для скобок
# n = int(input())               # получаем число n
# for i in range(1, n + 1):      # Интервал начинаем с единицы, чтобы не делить на 0
#     diff += (1 / i)            # Набиваем скобки суммами частных
# print(diff - log(n))           # и дописываем формулу

# Сумма чисел 2
# n = int(input())
# count = 0
# for i in range(1, n+1):
#     if i ** 2 % 10 == 2 or i ** 2 % 10 == 5 or i ** 2 % 10 == 8:
#         count += i
# print(count)
#
# print(sum([i for i in range(1,int(input())+1) if i**2%10 in (2,5,8)]))

# Факториал
# n = int(input())
# pr = 1
# for i in range(1, n+1):
#     pr *= i
# print(pr)

# n = int(input())
# for i in range(1, int(input())):
#     n *= i
# print(n)

# Без нулей
# count = 1
# for i in range(1, 11):
#     n = int(input())
#     if n != 0:
#         count *= n
# print(count)

# Сумма делителей
# n = int(input())
# count = 0
# for i in range(1, n+1):
#     if n % i == 0:
#         count += i
# print(count)

# Знакочередующаяся сумма
# n = int(input())
# res = 0
# for i in range(1, n + 1): # цикл от 1 до числа n
#     if i % 2 == 0:
#         res -= i  # если i делиться без остатка то вычитает из предыдущего результата
#     if i % 2 != 0:
#         res += i  # если i делиться с остатком то прибавляет к предыдущему результату
# print(res)

# Наибольшие числа
# n = int(input())
# max1 = max2 = 1         # пусть самое большое число это минимально возможное
# for i in range(1, n+1): # цикл от 1 до n
#     a = int(input())    # получаем следующее число
#     if a > max1:        # если введенное число больше нашего максимума, то это новый максимум
#         max2 = max1     # запоминаем предыдущее наибольшее число в переменной max2
#         max1 = a        # а само это число на входе становится наибольшим
#     elif a > max2:      # если число не больше max1, то проверяем больше ли оно второго max2
#         max2 = a
# print(max1)
# print(max2)

# n, s = int(input()), []
# while len(s) != n: s.append(int(input()))
# print(*sorted((s[-2:]), reverse=True), sep='\n')
# # s.sort()
# # print(*(s[-1], s[-2]),sep='\n')
#
#
# # print(*sorted([int(input()) for i in range(int(input()))], reverse=True)[:2], sep='\n')

# Only even numbers
# fl = 'YES'
# for _ in range(10):
#     n = int(input())
#     if n % 2 != 0:
#         fl = 'NO'
# print(fl)

# Последовательность Фибоначчи
# n = int(input())
# pr = 0
# sl = 1
# for i in range(1, n + 1):
#     sl = pr + sl
#     pr = sl - pr
#     print(pr, end=' ')
#
# a, b = 1, 0
# for _ in range(int(input())):
#     print(a, end = ' ')
#     a, b = a + b, a

# ----------
# WHILE
# ----------

# text = input()
# total = 0
# while text != 'stop':
#     num = int(text)
#     total += num
#     text = input()
# print('Сумма чисел равна', total)


# До КОНЦА 1
# text = input()
# while text !='КОНЕЦ':
#     print(text)
#     text = input()
#
# text = input()
# t = ''
# while text != 'КОНЕЦ':
#     t += text + '\n'
#     text = input()
# print(t)

# До КОНЦА 2
# text = input()
# t = ''
# while text != 'КОНЕЦ' and text != 'конец':
#     t += text + '\n'
#     text = input()
# print(t)

# # Количество членов
# text = input()
# count = 0
# while text != 'стоп' and text != 'хватит' and text != 'достаточно':
#     count += 1
#     text = input()
# print(count)
#
# a = 0
# while input() not in ("стоп", "хватит", "достаточно"):
#     a+=1
# print(a)

# Пока делимся
# digit = int(input())
# while digit % 7 == 0:
#     print(digit)
#     digit = int(input())
#
# while True:
#     s = int(input())
#     if s % 7 != 0:
#         break
#     print(s)

# while not (x := int(input())) % 7:
#     print(x)

# Сумма чисел
# digit = int(input())
# count = 0
# while digit >= 0:
#     count += digit
#     digit = int(input())
# print(count)

# Количество пятерок
# digit = int(input())
# count = 0
# while digit > 0 and digit < 6:
#     if digit == 5:
#         count += 1
#     digit = int(input())
# print(count)

# Ведьмаку заплатите чеканной монетой
# монеты с номиналами 1, 5, 10, 25
# n = int(input())
# counter = 0
# while n >= 25:
#     counter += 1
#     n -= 25
# while n >= 10:
#     counter += 1
#     n -= 10
# while n >= 5:
#     counter += 1
#     n -= 5
# while n >= 1:
#     counter += 1
#     n -= 1
# print(counter)

# ------------------
# n = int(input())
# while n != 0:  # пока в числе есть цифры
#     last_digit = n % 10  # получить последнюю цифру
#     # код обработки последней цифры
#     n = n // 10  # удалить последнюю цифру из числа
#
# Цикл while работает до тех пор пока в числе есть необработанные цифры. Тело цикла содержит:
# процедуру получения последней цифры last_digit = n % 10;
# код обработки последней цифры;
# процедуру удаления последней цифры из числа n = n // 10.

# ------------------
# Напишем программу, которая определяет есть ли в числе цифра 7.
#
# num = int(input())
# has_seven = False  # сигнальная метка
#
# while num != 0:
#     last_digit = num % 10
#     if last_digit == 7:
#         has_seven = True
#     num = num // 10
#
# if has_seven == True:
#     print('YES')
# else:
#     print('NO')
# ---------
# Обратный порядок 1

# for i in (reversed(input())):
#     print(i)

# n = int(input())
# while n != 0:
#     print(n % 10)  # печатаем последнюю цифру
#     n = n // 10  # убираем последнюю цифру

# Обратный порядок 2
# n = int(input())
# while n != 0:
#     print(n % 10, end='')
#     n //= 10

# print(*reversed(input()), sep= '')

# max и min
# n = input()
# print(f'Максимальная цифра равна {max(n)}')
# print(f'Минимальная цифра равна {min(n)}')

# n = int(input())
# maks = 0
# minim = 1
# while n != 0:
#     last_digit = n % 10
#     if last_digit > maks:
#         maks = last_digit
#     if last_digit < minim:
#         minim = last_digit
#     n //= 10
# print(f'Максимальная цифра равна {maks}\nМинимальная цифра равна {minim}')

# Все вместе
# n = int(input())
# sum_all = 0
# counter = 0
# pr = 1
# sr_ar = 1
# digit1 = 0
# digit_last = n % 10
# sum_1_2 = 0
# while n != 0:
#     last_digit = n % 10
#     sum_all += last_digit
#     counter += 1
#     pr *= last_digit
#     sr_ar = sum_all / counter
#     digit1 = last_digit
#     sum_1_2 = digit1 + digit_last
#     n //= 10
# print(sum_all, counter, pr, sr_ar, digit1, sum_1_2, sep='\n')
# -------------------------

# Вторая цифра
# n = int(input())
# while n > 9:  #второе число
#     dig = n % 10
#     n //= 10
# print(dig)

# Одинаковые цифры
# n = int(input())
# counter = 0
# dig = n % 10
# while n != 0:
#     ld = n % 10
#     if dig != ld:
#         counter += 1
#
#     n //= 10
# if counter != 0:
#     print('NO')
# else:
#     print('YES')

# n = int(input())
# m = n % 10
# answer = 'YES'
# while n != 0:
#     if m != n % 10:
#         answer = 'NO'
#     n = n // 10
# print(answer)


# Упорядоченные цифры
# n = int(input())
# m = n % 10
# answer = 'YES'
# while n != 0:
#     t = n % 10
#     if m > t:
#         answer = 'NO'
#     m = t
#     n = n // 10
# print(answer)

# 7.6 Циклы, break, continue и else
# Наименьший делитель
# n = int(input())
# for i in range(2, n+1):
#     if n % i == 0:
#         break
# print(i)

# Следуй правилам
# выводит числа от 11 до n включительно за исключением:
# чисел от 5 до 9 включительно;
# чисел от 17 до 37 включительно;
# чисел от 78 до 87 включительно.

# n = int(input())
# for i in range(1, n+1):
#     if 5 <= i <= 9 or 17 <= i <= 37 or 78 <= i <= 87:
#         continue
#     print(i)

# ------------------------
# import time
# start_time = time.time()
# n = 123456789
# sum_all = 0
# counter = 0
# pr = 1
# sr_ar = 1
# digit1 = 0
# digit_last = n % 10
# sum_1_2 = 0
# while n != 0:
#     last_digit = n % 10
#     sum_all += last_digit
#     counter += 1
#     pr *= last_digit
#     sr_ar = sum_all / counter
#     digit1 = last_digit
#     sum_1_2 = digit1 + digit_last
#     n //= 10
# print(sum_all, counter, pr, sr_ar, digit1, sum_1_2, sep='\n')
# print("--- %s seconds ---" % (time.time() - start_time))

# ------------------
# import time
# start_time = time.time()
# import numpy
# nums = [1,2,3,4,5,6,7,8,9]
# print(sum(nums), len(nums), numpy.prod(nums), numpy.mean(nums), nums[0], nums[0] + nums[-1], sep='\n')
# print("--- %s seconds ---" % (time.time() - start_time))

# 7.7 Поиск ошибок и ревью кода
# Ревью кода-1
# count = 0
# p = 1
# for i in range(1, 11):
#     x = int(input())
#     if x >= 0:
#         p = p * x
#         count = count + 1
# if count > 0:
#     print(count)
#     print(p)
# else:
#     print('NO')

# Ревью кода-2
# mx = pow(10, 6)
# s = 0
# for i in range(1, 11):
#     x = int(input())
#     if x < 0:
#         s += x
#     if x > mx:
#         mx = x
# if s < 0:
#     print(s)
#     print(mx)
# else:
#     print('NO')

# Ревью кода-3
# s = 0                 # неверно задана переменная (было 1)
# for i in range(7):    # неверно заданы границы диапозона (было (1, 7))
#     n = int(input())  # отсутствие преобразования в целое число (не было int())
#     if n % 2 == 0:    # неправильная переменная в условии (была i)
#         s = s + n
# print(s)

# Ревью кода-4
# n = int(input())
# max_digit = -1  # отталкиваться надо от -1, чтобы любая подходящая цифра могла заменить его
# while n > 0:
#     digit = n % 10
#     if digit % 3 == 0:
#         if digit > max_digit:  # нужно найти большее число
#             max_digit = digit  # перепутал местами
#     n //= 10                   # нужно откинуть последнюю цифру
# if max_digit == -1:            # сравнивать нужно не с 0
#     print('NO')
# else:
#     print(max_digit)

# Ревью кода-5
# n = int(input())
# while n > 9:  # Ошибка - цикл имеет смысл только в случае если данное натурально число дву- и  более -значное.
#     n //= 10  # Ошибка - нам необходимо постепенно отбрасывать числа до первого, а не выяснять последние из них.
# print(n)

# Ревью кода-6
# n = int(input())   # вводим число, а не текст
# product = 1        # число может быть любым, даже 0, а в цикле у нас произведение, получим ошибку
# while n > 0:       # цикл должен начинаться с 0, иначе мы потеряем цикл
#     digit = n % 10
#     product = product * digit
#     n //= 10
# print(product)

# 7.8 Вложенные циклы. Часть 1
# for i in range(8):
#     for j in range(i + 1):
#         print('*', end='')
#     print()

# Таблица-размером n×3
# n = int(input())
# for i in range(n):
#     for j in range(3):
#         print(n, end=' ')
#     print()


# Таблица-2  размером n×5 где в i-ой строке указано число i
# n = int(input())
# for i in range(1,n+1):
#     for j in range(5):
#         print(i, end=' ')
#     print()

# Таблица-3 печатает таблицу сложения для всех чисел от 1 до n
# n = int(input())
# for i in range(1, n + 1):
#     for j in range(1, 10):
#         print(i, '+', j, '=', i + j)
#     print()

# Звездный треугольник
# n = int(input())
# centr = n // 2 + 1  # находим середину
# count = 0  # кол-во звезд в строке
# for i in range(1, n + 1):
#     if i > centr:
#         count -= 1  # если перешли за середину то убавляем кол-во звезд
#     else:
#         count += 1  # иначе прибавляем кол-во звезд
#
#     for _ in range(count):  # выполняем цикл сколько нужно звезд
#         print('*', end='')
#     print()

# n = abs(int(input()))
# for i in range(1, n + 1):
#     for j in range(i):
#         if i + j <= n:
#             print('*', end='')
#     print()

# Численный треугольник 1
# for i in range(1,int(input())+1):
#     for j in range(1, i + 1):
#         print(i, end='')
#     print()
#
# for i in range(1, int(input()) + 1):
#     print(str(i) * i)

# 12 месяцев, 28n + 30k + 31m = 365.
# for n in range(1, 13):
#     for k in range(1, 12):
#         for m in range(1, 11):
#             if 28 * n + 30 * k + 31 * m == 365:
#                 print('n =', n, 'k =', k, 'm =', m)

# Старинная задача  ->    Быков: 1 Коров: 9 Телят: 90
# for x in range(1, 101):
#     for y in range(1, 101):
#         for z in range(1, 101):
#             if x * 10 + y * 5 + z * 0.5 == 100 and x + y + z == 100:
#                 print('Быков:', x, 'Коров:', y, 'Телят:', z)
#
# # Гипотеза Эйлера о сумме степеней
# for a in range(1, 151):
#     for b in range(a + 1, 151):
#         for c in range(b + 1, 151):
#             for d in range(c + 1, 151):
#                 e = int(((a ** 5) + (b ** 5) + (c ** 5) + (d ** 5)) ** 0.2)
#                 if e ** 5 == int((a ** 5) + (b ** 5) + (c ** 5) + (d ** 5)):
#                     print(a + b + c + d + e)
#
#
# 7.9 Вложенные циклы. Часть 2
# # Численный треугольник 3
# num = int(input())             # Определение высоты массива
# count = 0                      # Порядковый номер цифры = число в массиве
# for y in range(1, num + 1):    # Первый цикл высоты массива
#     for x in range(y):         # Второй цикл длины массива
#         count += 1             # увеличиваем счетчик
#         print(count, end=' ')  # Вывод текущего числа и в конце пробел
#     print()                    # Переход к новой строке

# Численный треугольник 4
# num = int(input())
#
# for i in range(1, num + 1):   # цикл отвечающий за количество рядов
#     count = 0                 # счетчик для ряда, при каждом новом цикле обнуляется
#     for j in range(i):        # 1й вложенный
#         count += 1            # увеличиваем цифру в ряду
#         print(count, end='')  # вывод на печать без пробелов
#     for k in range(i, 1, -1): # 2й вложенный
#         count -= 1            # уменьшаем цифру в ряду
#         print(count, end='')  # вывод на печать без пробелов
#     print()                   # переход на новую строку


# Делители-1
# a, b = int(input()), int(input())
# total_maximum = 0                    # сумма делителей
# digit = 0                            # число с максимальной суммой делителей
#
# for i in range(a, b + 1):             # цикл перебирающий все числа от a до b включительно
#     maximum = 0                       # обнуление суммы делителей, для нового цикла
#     for j in range(1, i + 1):         # проверяем все числа от 1 до числа не превышающего проверяемое
#         if i % j == 0:                # проверка на деление без остатка
#             maximum += j              # суммируем делители
#         if maximum >= total_maximum:  # если сумма делителей больше max суммы делителей
#             total_maximum = maximum   # записываем в переменную максимальную
#             digit = j
# print(digit, total_maximum)           # вывод


# Делители-2
# n = int(input())
#
# for i in range(1, n+1):        # циклом перебираем все числа от 1 до n включительно
#     print(i, end='')         # вывод текущего числа
#     for j in range(1, i+1):    # цикл поиска делителя
#         if i % j == 0:         # если число делится без остатка
#             print('+', end='') # то печатаем + без пробела
#     print()                    # переход на новую строку

# Цифровой корень
# n = int(input())  # ввод числа
#
# while n > 9:  # до тех пор, пока в числе n не останется одна цифраа
#     s = 0
#     while (n > 0):
#         last_digit = n % 10  # получить последнюю цифру
#         s += last_digit  # к числу прибавляем последнюю цифру
#         n = n // 10  # удалить последнюю цифру из числа
#     n = s
#
# print(n)

# Сумма факториалов
# num = int(input())           # кол-во факториалов
# total = 0                    # сумма факториалов
# factorial = 1                # вычисляемый факториал
#
# for i in range(1, num+1):    # перебираем факториалы
#     for j in range(1, i+1):  # вычисляем каждый факториал
#         factorial *= j       # вычисляем факториал
#     total += factorial       # Суммируем факториалы чисел.
#     factorial = 1            # "обнуляем факториал"
# print(total)


# Простые числа
# a, b, = int(input()), int(input())
# for i in range(a, b + 1):
#     if i == 1:                # 1 не является простым числом
#         continue              # пропускаем цикл
#     for j in range(2, i):     # перебираем делители от 2 до i
#         if i % j == 0:        # если делится без остатка, то оно не простое
#             break             # завершаем вложенный цикл
#     else:
#         print(i)

# 8. Итоговая работа на циклы

# Ревью кода - 7
# n = int(input())
# s = 0
# while n > 0:
#     if n % 2 == 0:
#         s += n % 10
#     n //= 10
# print(s)


# Ревью кода - 8
# n = 8 # n = 7, по условию чисел 8
# count = 0
# maximum = -10**6 - 1 # maximum = 1000, все случаи, когда все числа меньше 1000, обрабатываются неверно
# for i in range(1, n + 1):
#     x = int(input())
#     if x % 4 == 0: # x // 4 == 0, по условию нужно найти числа, дел. на 4 без остатка
#         count += 1
#         if x > maximum: # if x < maximum, если число больше максимума, оно его заменяет, не если меньше максимума
#             maximum = x
# if count > 0:
#     print(count)
#     print(maximum)
# else:
#     print('NO')

# Ревью кода - 9
# count = 0
# maximum = -1
# for i in range(4):
#     x = int(input())
#     if x % 2 != 0:
#         count += 1
#         if x > maximum:
#             maximum = x
# if count > 0:
#     print(count)
#     print(maximum)
# else:
#     print('NO')

# Звездная рамка
# n = int(input())
# for i in range(1, n + 1):
#     if i == 1 or i == n:
#         print('*' * 19)
#     else:
#         print('*' + ' ' * 17 + '*')
#
#
# # Третья цифра
# n = int(input())
# while n > 999:
#     n //= 10
# print(n % 10)

#
# # Все вместе 2
# n = int(input())
# count3 = 0
# countLast = 0
# countChet = 0
# sumBig5 = 0
# multyBig7 = 1
# count05 = 0
# last = n % 10
# while n > 0:
#     x = n % 10
#     if x == 3:
#         count3 += 1
#     if x == last:
#         countLast += 1
#     if x % 2 == 0:
#         countChet += 1
#     if x > 5:
#         sumBig5 += x
#     if x > 7:
#         multyBig7 *= x
#     if x == 0 or x == 5:
#         count05 += 1
#     n //= 10
# print(count3)
# print(countLast)
# print(countChet)
# print(sumBig5)
# print(multyBig7)
# print(count05)


# Числа Рамануджана
#
# for i in range(1, 40):
#     for j in range(1, 40):
#         for k in range(1, 40):
#             for l in range(1, 40):
#                 if i != k and i != l and j != k and j != l and i ** 3 + j ** 3 == k ** 3 + l ** 3:
#                     print(i ** 3 + j ** 3)

# 9.1 Индексация строк
# s = 'All you need is love'
# if 'love' in s:
#     print('❤️')
# else:
#     print('💔')
# s = input()
# for i in range(0, len(s), 2):
#     print(s[i])

# В столбик 2
# s = input()
# for i in (s[::-1]):
#     print(i)

# ФИО
# i,f,o = input(),input(),input()
# print(f[0],i[0],o[0], sep='')

# Цифра 1
# n = input()
# s = 0
# for i in n:
#     s += int(i)
# print(s)

# Цифра 2
# a = input()
# flag = False
# for i in a:
#     if i.isdigit():
#         flag = True
# if flag == True:
#     print('Цифра')
# else:
#     print('Цифр нет')
#

# for i in input():
#     if i in '01234567890':
#         print("Цифра")
#         break
# else:
#     print("Цифр нет")
#
#
# print('Цифра' if [i for i in input() if i.isdigit()] else 'Цифр нет')

# Сколько раз?
# a = b = 0
# for i in input():
#     if i == '+':
#         a += 1
#     if i == '*':
#         b += 1
#
# print('Символ + встречается', a, 'раз')
# print('Символ * встречается', b, 'раз')

# Одинаковые соседи
# count = 0
# a = 0
# for i in input():
#     if i == a:
#         count += 1
#     a = i
# print(count)

# # Гласные и согласные
# gl = sgl = 0
# for i in input():
#     if i in 'ауоыиэяюёеАУОЫИЭЯЮЁЕ':
#         gl += 1
#     if i in 'бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ':
#         sgl += 1
#
# print('Количество гласных букв равно', gl)
# print('Количество согласных букв равно', sgl)

# Decimal to Binary

# a = int(input())
# a = format(a, 'b')
# print(a)


# a = format(a, 'b') , b в этом случае и переводит значение нашей переменной в 2-ичную систему.
#
# s - строка, можно не указывать, используется по умолчанию;
# b - двоичный формат;
# с - преобразует целое число в символ Unicode;
# d - десятичный формат;
# e - научный формат, со строчной буквой e;
# E - научный формат, с E верхним регистром;
# f - формат чисел с плавающей запятой;
# F - формат чисел с плавающей запятой, верхний регистр;
# g - общий формат, нижний регистр;
# G - общий формат, верхний регистр;
# o - Восьмеричный формат;
# x - шестнадцатеричный формат, нижний регистр;
# X - шестнадцатеричный формат, верхний регистр;
# n - формат целых чисел;
# %- Процентный формат. Умножает число на 100 и использует f для вывода. В конце ставится %;
# #- альтернативный вариант вывода указанного формата, работает с форматами b, o, x.

# n = int(input())  # число
# d = ''            # строка
# while n > 0:
#     d = str(n % 2) + d   # при сложении (конкатенации) строк важен порядок
#     n //= 2
# print(d)

# s = "In 2010, someone paid 10k Bitcoin for two pizzas."
# print(s[::7])

# Палиндром
# s = input()
# p = s[::-1]  # переворачиваем строку s
# if s == p:  # если строка равно с перевернутой строкой
#     print('YES')
# else:
#     print('NO')

# Делаем срезы 1
# s = input()
# print(len(s))
# print(s*3)
# print(s[0])
# print(s[:3])
# print(s[-3::])
# print(s[::-1])
# print(s[1:-1])

# Делаем срезы 2
# s = input()
# print(s[2])      # третий символ этой строки
# print(s[-2])     # предпоследний символ этой строки
# print(s[:5])     # первые пять символов этой строки
# print(s[:-2])    # всю строку, кроме последних двух символов
# print(s[::2])    # все символы с четными индексами
# print(s[1::2])   # все символы с нечетными индексами
# print(s[::-1])   # все символы в обратном порядке
# print(s[::-2])   # все символы строки через один в обратном порядке, начиная с последнего


# Две половинки
# s = input()
# print(s[(len(s) + 1) // 2:] + s[:(len(s) + 1) // 2])


# 9.3 Методы строк. Часть 1
# capitalize — писать прописными буквами, закрепить.
# swapcase — обменять регистр. swap — гл. обмениваться, case — случай, регистр, падеж, дело, расследование...
# title — заголовок, титул.
# lower — нижний.
# upper — верхний

# Заглавные буквы
# n = input().split()
# print('YES' if n[0] == n[0].capitalize() and n[1] == n[1].capitalize() else 'NO')

# a = input()
# print('YES' if a==a.title() else 'NO')

# sWAP cASE
# print(input().swapcase())

# Хороший оттенок
# print('YES' if 'хорош' in input().lower() else 'NO')

# Нижний регистр
# # подсчитывает количество буквенных символов в нижнем регистре
# n = input()
# count = 0
# for i in range(len(n)):
#     if "a" <= n[i] <= "z":
#         count += 1
# print(count)
#
# s, counter = input(), 0
# for i in s:
#     if i != i.upper():  # условие выполняется только для букв в нижнем регистре
#         counter += 1
# print(counter)

# print(sum(s.islower() for s in input()))

# Количество слов
# s = input()
# print(len(s.split()))

# print(input().count(' ') + 1)

# Минутка генетики
# s = input().upper()
# print('Аденин:', s.count('А'))
# print('Гуанин:', s.count('Г'))
# print('Цитозин:', s.count('Ц'))
# print('Тимин:', s.count('Т'))

# Очень странные дела
# n = int(input())
# cnt = 0
# for i in range(n):
#     s = input()
#     if s.count('11') >= 3:
#         cnt += 1
# print(cnt)

# Количество цифр
# n = input()
# cnt = 0
# for i in n:
#     if i.isdigit():
#         cnt += 1
# print(cnt)
#
# print(sum(i.isdigit() for i in input()))

# .com or .ru
# n = input()
# print('YES' if n.endswith('.com') or n.endswith('.ru') else 'NO')

# print('YES' if input().endswith(('.com','.ru')) else 'NO')


# Самый частотный символ
# s = input()
# ch = 0
# st = " "
# for i in s:
#     if s.count(i) >= ch:
#         ch = s.count(i)
#         st = i
# print(st)


# Первое и последнее вхождение
# получаем строку
# если каунт символа == 1, выводим строка.финд
# если каунт символа >= 1, выводим строка.финд и строка.рфинд
# иначе, выводим НО

# s = input()
# if s.count('f') == 0:
#     print('NO')
# if s.count('f') == 1:
#     print(s.find('f'))
# elif s.count('f') >=1:
#     print(s.find('f'), s.rfind('f'))


# Удаление фрагмента
# s = input()                # Получаем строку
# a = s.find('h')            # Индекс первого вхождения
# b = s.rfind('h')           # Индекс последнего вхождения
# c = s[a:b+1]               # Получаем текст между начальным и конечным индексом
# print(s.replace(c, ''))    # Выводим результат делая замену на пустую строку


# print('In {0}, someone paid {1} {2} for two pizzas.'.format('2010', '10k', 'Bitcoin'))

# year = 2010
# amount = '10K'
# currency = 'Bitcoin'
#
# print(f'In {year}, someone paid {amount} {currency} for two pizzas.')


# for i in range(26):
#     print(chr(ord('A') + i))

# Функция ord позволяет определить код некоторого символа в таблице символов Unicode
# Функция chr позволяет определить по коду символа сам символ

# Символы в диапазоне
# for i in range(int(input()), int(input())+1):
#     print(chr(i),end=' ')

# print(*[chr(i) for i in range(int(input()), int(input()) + 1)])


# Простой шифр
# print(*[ord(i) for i in input()])
#
# print(*map(ord, input()))

# Шифр Цезаря
# n = int(input())
# text = input()
# for i in text:
#     decr = ord(i) - n
#     if decr < 97:
#         decr +=26
#     print(chr(decr), end='')


# s = 'Python rocks!'
# print(s.replace('o','@'))


# 11.1 Введение в списки

# print(list(range(1,int(input())+1)))

# Список, состоящий из n букв английского алфавита ['a', 'b', 'c', ...]
# print([chr(i) for i in range(97, 97+int(input()))])

#           1  2  3  4  5   6   7   8   9   10  11  12  13  14  15  16  17  18  19  20
# primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
#           0  1  2  3  4   5   6   7   8   9   10  11  12  13  14  15  16  17  18  19
# print(primes[16])


# numbers = [12.5, 3.1415, 2.718, 9.8, 1.414, 1.1618, 1.324]
# print(min(numbers)+max(numbers))


# evens = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
# average = sum(evens)/len(evens)
# print(average)


# rainbow = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']
# rainbow[3] = 'Зеленый'
# rainbow[-1] = 'Фиолетовый'
#
# print(rainbow)


# numbers1 = [1, 2, 3]
# numbers2 = [6]
# numbers3 = [7, 8, 9, 10, 11, 12, 13]
#
# print(numbers1*2+numbers2*9+numbers3)

# colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'brown', 'magenta']
# del colors[2]
# del colors[6]
# print(colors)

# numbers = [2, 6, 3, 14, 10, 4, 11, 16, 12, 5, 4, 16, 1, 0, 8, 16, 10, 10, 8, 5, 1, 11, 10, 10, 12, 0, 0, 6, 14, 8, 2,
#            12, 14, 5, 6, 12, 1, 2, 10, 14, 9, 1, 15, 1, 2, 14, 16, 6, 7, 5]
# print(len(numbers))  # Вывел длину списка;
# print(numbers[-1])  # Вывел последний элемент списка;
# print(numbers[::-1])  # Вывел список в обратном порядке (вспоминаем срезы);
# print('YES' if ((5 or 17)) in numbers else 'NO')  # Вывел YES если список содержит числа 5 и 17, и NO в противном случае;
# print(numbers[1:-1])            # Вывел список с удаленным первым и последним элементами.


# Список строк
# print([input() for i in range(int(input()))])

# Алфавит

# l = []
# for i in range(ord('z') - ord('a') + 1):
#     l.append(chr(ord('a') + i) * (i + 1))
# print(l)
#
# print([chr(97 + i) * (i + 1) for i in range(26)])

# Список кубов
# ls = []
# n = int(input())
# for i in range(1,n+1):
#     a = int(input())
#     ls.append(a**3)
# print(ls)

# print([int(input())**3 for i in range(1,int(input())+1)])


# Список делителей
# n = int(input())
# sp = []
# for i in range(1, n+1):
#     if n % i == 0:
#         sp.append(i)
# print(sp)

# Суммы двух
# n = int(input())
# sp = []
# new_sp = []
# for i in range(n):
#     b = int(input())
#     sp.append(b)
# for j in range(len(sp)-1):
#     new_sp.append(sp[j]+sp[j+1])
# print(new_sp)
#
# Удалите нечетные индексы
# n = int(input())
# sp = []
# for i in range(n):
#     b = int(input())
#     sp.append(b)
# del sp[1::2]
# print(sp)
#
# a = [int(i) for i in [input() for _ in range(int(input()))]]
# del a[1::2]
# print(a)


# k-ая буква слова
# n = int(input())
# sp = []
# new_sp = []
# for i in range(n):
#     b = input()
#     sp.append(b)
# k = int(input())
# for j in range(len(sp)):
#     new_sp.append(sp[j][k-1:k])
# print(*new_sp,sep='')
#
# data = [input() for i in range(int(input()))]
# k = int(input())
# for i in data:
#     if len(i) >= k:
#         print(i[k - 1], end='')

# Символы всех строк
# print([].extend([input() for i in range(int(input()))]))

# a = [input() for i in range(int(input()))]
# b = []
# for j in range(len(a)):
#     b.extend(a[j])
# print(b)
#
# n = int(input())
# sp = []
# for _ in range(n):
#     sp.extend(input())
# print(sp)


# Функция sum() оказывается может принимать второй аргумент - начальное значение (по умолчанию равное нулю),
# к которому будут прибавляться все значения итерируемого списка.
# Кладём в функцию вместо этого начального значения пустой список.
# И все элементы итерируемого списка списков будут по очереди прибавляться к этому пустому списку.
#
# >>> a = [[1, 2], [3, 4], [5, 6]]
# >>> sum(a, [])
# [1, 2, 3, 4, 5, 6]
# print(sum((list(input()) for _ in range(int(input()))), []))


# 11.4 Вывод элементов списка

# Для вывода элементов списка каждого на отдельной строке
#
# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for i in range(len(numbers)):
#     print(numbers[i])

# Если индексы не нужны:
# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for num in numbers:
#     print(num)

# Вывод с помощью распаковки списка
# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(*numbers)

# Вариант 2. Вывод элементов списка, каждого на отдельной строке
# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(*numbers, sep='\n')

# можем использовать распаковку строк точно так же, как и распаковку списков.
# s = 'Python'
# print(*s)
# print()
# print(*s, sep='\n')

# сумму квадратов элементов списка
# numbers = [1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111]
# numbers2 = []
# for i in numbers:
#     numbers2.append(i**2)
# print(sum(numbers2))
#
# numbers = [1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111]
# print(sum([i**2 for i in numbers]))

# Значение функции
# f(j)=j**2+2*j+1=4
# sp = [int(input()) for i in range(int(input()))]
# sp2 = []
# for j in sp:
#     sp2.append(j**2+2*j+1)
# print(*sp, sep='\n')
# print()
# print(*sp2, sep='\n')

# Remove outliers - удалить самое большое и самое маленькое значение.
# sp = [int(input()) for i in range(int(input()))]
# sp.remove(min(sp))
# sp.remove(max(sp))
# print(*sp, sep='\n')

# Без дубликатов
# sp = [input() for i in range(int(input()))]
# sp2 = []
# for i in sp:
#     if i not in sp2:
#         sp2.append(i)
# print(*sp2,sep='\n')

# z = []
# for i in range(int(input())):
#     s = input()
#     if s not in z:
#         z.append(s)
#
# print(*z, sep='\n')


# # Google search - 1
# sp = [input() for i in range(int(input()))]
# zapros = input()
# for i in sp:
#     if zapros.lower() in i.lower():
#         print(i)
#  ------
# s = [input() for _ in range(int(input()))]
# word = input().lower()
# print(*[i for i in s if word in i.lower()], sep='\n')

# Google search - 2 🌶️🌶️

# sp = [input() for i in range(int(input()))]
# zapros = [input() for i in range(int(input()))]
# for i in sp:
#     for j in zapros:
#         if j.lower() not in i.lower():
#             break
#     else:
#         print(i)


# Negatives, Zeros and Positives
# sp = [int(input()) for i in range(int(input()))]
# [print(i) for i in sp if i < 0]
# [print(i) for i in sp if i == 0]
# [print(i) for i in sp if i > 0]

# Метод split()
# s = 'Python is the most powerful language'
# words = s.split()
# print(words) -> ['Python', 'is', 'the', 'most', 'powerful', 'language']

# s = '192.168.1.1'
# num = s.split('.')
# print(num)

# Метод join()
# words = ['Python', 'is', 'the', 'most', 'powerful', 'language']
# s = ' '.join(words)
# print(s)  -> 'Python is the most powerful language'

# Строковый метод split() служит для преобразования строки в список,
# а метод join() — для преобразования списка в строку.

# s = 'Python'
# s2 = ' '.join(s)  # Разбивает строку на символы
# s3 = s2.split()  # Преобразует символы в список
# print(s3)

# Output
# >>> ['P', 'y', 't', 'h', 'o', 'n']

# Построчный вывод
# print(*input().split(),sep='\n')


# Инициалы
# a = input().split()
# for i in a:
#     print(i[0], end='.')

# for i in input().split():
#     print(i[0], end=".")

# print(*input().split('\\'), sep='\n')

# Диаграмма
# a = input().split()
# for i in a:
#     print('+'*int(i))

# Корректный ip-адрес
# a = input().split('.')
# flag = 0
# for i in a:
#     if 0 <= int(i) <= 255:
#         flag += 1
# if flag == 4:
#     print('ДА')
# else:
#     print('НЕТ')

# Добавь разделитель
# a = ''.join(input())
# b = input()
# print(*a, sep=b)
#
# print(*list(input()), sep=input())


# Количество совпадающих пар
# a = input().split()
# s = 0
# for i in range(len(a) - 1):
#     s += a[i + 1:].count(a[i])
# print(s)


# 11.6 Методы списков. Часть 2

# Метод insert() позволяет вставлять значение в список в заданной позиции. В него передается два аргумента:
#
# index: индекс, задающий место вставки значения;
# value: значение, которое требуется вставить.


# Метод index()
# Метод index() возвращает индекс первого элемента, значение которого равняется переданному в метод значению
# names = ['Gvido', 'Roman' , 'Timur']
# position = names.index('Timur')
# print(position)


# Метод remove() удаляет первый элемент, значение которого равняется переданному в метод значению.
# food = ['Рис', 'Курица', 'Рыба', 'Брокколи', 'Рис']
# print(food)
# food.remove('Рис')
# print(food)


# Метод pop() удаляет элемент по указанному индексу и возвращает его. В метод pop() передается
# один необязательный аргумент:
# index: индекс элемента, который требуется удалить.
# names = ['Gvido', 'Roman' , 'Timur']
# item = names.pop(1)
# print(item)
# print(names)
# >>>Roman
# >>>['Gvido', 'Timur']

# Метод count() возвращает количество элементов в списке, значения которых равны переданному в метод значению.
# names = ['Timur', 'Gvido', 'Roman', 'Timur', 'Anders', 'Timur']
# cnt1 = names.count('Timur')
# cnt2 = names.count('Gvido')
# cnt3 = names.count('Josef')
#
# print(cnt1)   ---> 3
# print(cnt2)   ---> 1
# print(cnt3)   ---> 0


# Метод reverse() инвертирует порядок следования значений в списке, то есть меняет его на противоположный.
# Метод clear() удаляет все элементы из списка.
# Метод copy() создает поверхностную копию списка.


# Все сразу 2 🌶️
# numbers = [8, 9, 10, 11]
# numbers[1] = 17  #Заменил второй элемент списка на 17;
# numbers.extend([4, 5, 6]) #Добавил числа 4, 5 и 6 в конец списка;
# del numbers[0]  #Удалил первый элемент списка;
# numbers *= 2  #Удвоил список;
# numbers.insert(3, 25)  #Вставил число 25 по индексу 3;
# print(numbers)


# Переставить min и max
# l = [int(i) for i in input().split()]
# x = l.index(min(l))
# y = l.index(max(l))
# l[x], l[y] = max(l), min(l)
# print(*l)


# Количество артиклей
# text = input().lower().split()
# counter = 0
# for i in text:
#     if i == 'a' or i == 'an' or i == 'the':
#         counter += 1
# print(f'Общее количество артиклей: {counter}')
#
# # text = input().lower().split()
# # print(f"Общее количество артиклей: {text.count('a') + text.count('an') + text.count('the')}")


# Взлом Братства Стали 🌶️
# n = input()
# for _ in range(int(n[1:])):
#     s = input()
#     if '#' in s:
#         s = s[:s.find('#')]
#     print(s.rstrip())

# Сортировка чисел
# n = list(map(int, input().split()))
# n.sort()
# print(*n)
# n.sort(reverse=True)
# print(*n)


# s = sorted(int(i) for i in input().split())
# print(*s)
# print(*s[::-1])

# 11.7 Списочные выражения
# Создание списков
# Примеры использования списочных выражений
# 1. Создать список, заполненный 10 нулями можно и при помощи списочного выражения:
#
# zeros = [0 for i in range(10)]
# 2. Создать список, заполненный квадратами целых чисел от 0 до 9 можно так:
#
# squares = [i ** 2 for i in range(10)]
# 3. Создать список, заполненный кубами целых чисел от 10 до 20 можно так:
#
# cubes = [i ** 3 for i in range(10, 21)]
# 4. Создать список, заполненный символами строки:
#
# chars = [c for c in 'abcdefg']
# print(chars)

# Например, если сначала вводится число n – количество строк, а затем сами строки, то создать список можно так:
#
# n = int(input())
# lines = [input() for _ in range(n)]
# Можно опустить описание переменной n:
#
# lines = [input() for _ in range(int(input()))]
# Если требуется считать список чисел, то необходимо добавить преобразование типов:
#
# numbers = [int(input()) for _ in range(int(input()))]

# Условия в списочном выражении
# список четных чисел от 0 до 20, то мы можем написать такой код:

# evens = [i for i in range(21) if i % 2 == 0]
# для того, чтобы получить список, состоящий из четных чисел, лучше использовать функцию range(0, 21, 2)


# Вложенные циклы
# numbers = [i * j for i in range(1, 5) for j in range(2)]
# print(numbers)  #--> [0, 1, 0, 2, 0, 3, 0, 4]


# Подводя итог
# Пусть word = 'Hello', numbers = [1, 14, 5, 9, 12], words = ['one', 'two', 'three', 'four', 'five', 'six'].
#
# Списочное выражение	                Результирующий список
# [0 for i in range(10)]          #-->	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [i ** 2 for i in range(1, 8)] #-->	[1, 4, 9, 16, 25, 36, 49]
# [i * 10 for i in numbers]        #-->	[10, 140, 50, 90, 120]
# [c * 2 for c in word]          #-->	['HH', 'ee', 'll', 'll', 'oo']
# [m[0] for m in words]            #-->	['o', 't', 't', 'f', 'f', 's']
# [i for i in numbers if i < 10] #-->	[1, 5, 9]
# [m[0] for m in words if len(m) == 3] #-->	['o', 't', 's']


# получить новый список, содержащий строки исходного списка с удаленным первым символом.
# keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']
# new_keywords = [i[1::] for i in keywords]
# print(new_keywords)

# длины строк исходного списка.
# keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']
# lengths = [len(i) for i in keywords]
# print(lengths)

# только слова длиной не менее пяти символов (включительно).
# keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']
# new_keywords = [i for i in keywords if len(i) >= 5]
# print(new_keywords)


# получить список всех чисел палиндромов от 100 до 1000
# palindromes = [i for i in range(100, 1001) if str(i) == str(i)[::-1]]
# print(palindromes)

# Списочное выражение 1
# print(*[i**2 for i in range(1, int(input())+1)], sep='\n')


# Списочное выражение 2
# print(*[int(i)**3 for i in (input().split())])

# В одну строку 1
# слова введенной строки в столбик.
# print(*[i for i in input().split()], sep='\n')

# В одну строку 2
# выводит все цифровые символы данной строки.
# print(*[i for i in input() if i.isdigit()], sep='')


# В одну строку 3
# выведет квадраты четных чисел, которые не оканчиваются на цифру 44.
# print(*[int(i) ** 2 for i in input().split() if int(i) ** 2 % 2 == 0 and int(i) ** 2 % 10 != 4])


# 11.8 Сортировка списков
# Сортировка пузырьком
# a = [1, 7, -3, 9, 0, -67, 34, 12, 45, 1000, 6,  8, -2, 99]
# n = len(a)
#
# for i in range(n - 1):
#     for j in range(n - i - 1):
#         if a[j] > a[j + 1]:                  # если порядок элементов пары неправильный
#             a[j], a[j + 1] = a[j + 1], a[j]  # меняем элементы пары местами
#
# print('Отсортированный список:', a)


# a = [17, 24, 91, 96, 67, -27, 79, -71, -71, 58, 48, 88, 88, -16, -78, 96, -76, 56, 92, 1, 32, -17, 36, 88, -61, -97, -37, -84, 50, 47, 94, -6, 52, -76, 93, 14, -32, 98, -65, -16, -9, -68, -20, -40, -71, 93, -91, 44, 25, 79, 97, 0, -94, 7, -47, -96, -55, -58, -78, -78, -79, 75, 44, -56, -41, 38, 16, 70, 17, -17, -24, -83, -74, -73, 11, -26, 63, -75, -19, -13, -51, -74, 21, -8, 21, -68, -66, -84, -95, 78, 69, -29, 39, 38, -55, 7, -11, -26, -62, -84]
#
# n = len(a)
# flag = False
# for i in range(n - 1):
#     for j in range(n - i - 1):
#         if a[j] > a[j + 1]:
#             flag = True
#             a[j], a[j + 1] = a[j + 1], a[j]
#     if flag == False:
#         break
#
#
# print(a)


# алгоритм сортировки выбором.
# a = [78, -32, 5, 39, 58, -5, -63, 57, 72, 9, 53, -1, 63, -97, -21, -94, -47, 57, -8, 60, -23, -72, -22, -79, 90, 96, -41, -71, -48, 84, 89, -96, 41, -16, 94, -60, -64, -39, 60, -14, -62, -19, -3, 32, 98, 14, 43, 3, -56, 71, -71, -67, 80, 27, 92, 92, -64, 0, -77, 2, -26, 41, 3, -31, 48, 39, 20, -30, 35, 32, -58, 2, 63, 64, 66, 62, 82, -62, 9, -52, 35, -61, 87, 78, 93, -42, 87, -72, -10, -36, 61, -16, 59, 59, 22, -24, -67, 76, -94, 59]
# b = []
# n = len(a)
# for i in range(n):
#     b.append(min(a))
#     a.remove(min(a))
# a = b
# print(a)
#
#
# n = len(a)
# for i in range(0, n):
#     m = i
#     for j in range(i + 1, n):
#         if a[j] < a[m]:
#             m = j
#     a[i], a[m] = a[m], a[i]
#
# print(a)


# Сортировка простыми вставками
# a = [1, 7, -3, 9, 0, -67, 34, 12, 45, 1000, 6,  8, -2, 99]
# n = len(a)
# for i in range(1, n):
#     elem = a[i]  # первый элемент из неотсортированной части списка
#     j = i
#     while j >= 1 and a[j - 1] > elem:
#         a[j] = a[j - 1]
#         j -= 1
#     a[j] = elem
# print('Отсортированный список:', a)


# a = [1, 7, -3, 9, 0, -67, 34, 12, 45, 1000, 6,  8, -2, 99]
# n = len(a)
# print('Начинаем цикл перебора всех элементов списка, начиная со второго (неотсортированный список)')
# for i in range(1, n):
#     print(a, i, 'итерация: a[i] =', a[i])
#     elem = a[i]  # первый элемент из неотсортированной части списка
#     print('Запоминаем проверяемый элемент списка в доп память - elem = a[i] =', a[i])
#     j = i
#     if a[j - 1] <= elem:
#         print(f'В while не заходим, тк проверяемое число ({a[i]}) больше предыдущего ({a[i - 1]})')
#     while j >= 1 and a[j - 1] > elem:
#         print(f'while: сравниваем индекс = {j}: на место a[j] = {a[j]} записываем число {a[j - 1]}, и получаем', end=' ')
#         a[j] = a[j - 1]
#         print(a)
#         j -= 1
#     print(f'Извлекаем из доп памяти elem = {elem} в индекс {j}')
#     a[j] = elem
#
# print(a)

# # выводит список четных чисел
# print([i for i in range(2,int(input())+1, 2)])

# Сумма двух списков
# l = [i for i in input().split()]
# m = [i for i in input().split()]
# t = []
# for j in range(len(l)):
#     t.append(int(l[j])+int(m[j]))
# print(*t)

# Сумма чисел
# x = [int(i) for i in input().split()]
# print(*x, sep='+',end='=')
# print(sum(x))

# Валидный номер 🌶️🌶️
# # 7-301-447-5820
# n = input().split("-")
# c = [len(i) for i in n]
# if c == [3, 3, 4] and ''.join(n).isdigit():
#     print("YES")
# elif c == [1, 3, 3, 4] and ''.join(n).isdigit() and n[0] == '7':
#     print("YES")
# else:
#     print("NO")

# Самый длинный
# print(max([len(a) for a in input().split()]))

# Молодежный жаргон
# print(*[i[1:] + i[0] + "ки" for i in input().split()])
# print(*[f"{s[1:]}{s[0]}ки" for s in input().split()])

# 13.1 Функции без параметров
# def название_функции():
#     блок кода

# def draw_box():
#     for _ in range(5):
#         print('*' * 7)
# draw_box()

# Звездный прямоугольник 1
# def draw_box():
#     print('*' * 10)
#     for _ in range(12):
#         print('*' + ' ' * 8 + '*')
#     print('*' * 10)
#
#
# draw_box()

# Звездный треугольник 1
# def draw_triangle():
#     for i in range(11):
#         print('*'*i)
#
#
# draw_triangle()

# 13.2 Функции с параметрами
# def название_функции(параметры):
#     блок кода

# def draw_box(height, width):    # функция принимает два параметра
#     for i in range(height):
#         print('*' * width)

# draw_box(5, 7)

# def draw_box(height, width):
#     height = 2
#     width = 10
#     for i in range(height):
#         print('*' * width)
#
# n = 5
# m = 7
# draw_box(n, m)
# print(n, m)

# def change_us(a, b):
#     a = 0
#     b = 0
#     print(a, b)
#
# x = 1
# y = 7
# print(x, y)
# change_us(x, y)
# print(x, y)

# Звездный треугольник
# def draw_triangle(fill, base):
#
#     # centr = base // 2 + 1  # находим середину
#     # count = 0  # кол-во звезд в строке
#     # for i in range(1, base + 1):
#     #     if i > centr:
#     #         count -= 1  # если перешли за середину то убавляем кол-во звезд
#     #     else:
#     #         count += 1  # иначе прибавляем кол-во звезд
#     #
#     #     for _ in range(count):  # выполняем цикл сколько нужно звезд
#     #         print(fill, end='')
#     #     print()
#     for i in range(1, base + 1):
#         print(fill * min(i, base - i + 1))
#
# fill = input()
# base = int(input())
#
# draw_triangle(fill, base)


# ФИО
# def print_fio(name, surname, patronymic):
#     print(f"{surname[0]}{name[0]}{patronymic[0]}".upper())
#     # print(surname[0].upper(),name[0].upper(),patronymic[0].upper(), sep='')
#
# name, surname, patronymic = input(), input(), input()
#
# print_fio(name, surname, patronymic)

# Сумма цифр
# def print_digit_sum(num):
#     print(sum([int(i) for i in str(n)]))
#
#
# # считываем данные
# n = int(input())
#
# # вызываем функцию
# print_digit_sum(n)

# 13.3 Локальные и глобальные переменные
# 13.4 Функции с возвратом значения. Часть 1

# функция перевода градусов Фаренгейта в градусы Цельсия
# def convert_to_celsius(temp):
#     result = (5 / 9) * (temp - 32)
#     return result
#
# # основная программа
# temp = float(input('Bвeдитe количество градусов по Фаренгейту: '))
# celsius = convert_to_celsius(temp)
# print(celsius)  # градусы Цельсия

# Использование нескольких return
# def convert_grade(grade):
#     if grade >= 90:
#         return 5
#     elif grade >= 80:
#         return 4
#     elif grade >= 70:
#         return 3
#     elif grade >= 60:
#         return 2
#     else:
#         return 1
#
# # основная программа
# grade = int(input('Введите вашу отметку по 100-балльной системе: '))
# print(convert_grade(grade))

# возвращает длину гипотенузы прямоугольного треугольника по известным значениям его катетов
# def compute_hypotenuse(a, b):
#     c = (a ** 2 + b ** 2) ** 0.5
#     return c
# x = int(input())
# y = int(input())
#
# hypotenuse = compute_hypotenuse(x, y)
# print(hypotenuse)

# Напишите функцию sum_digits(n), принимающую в качестве аргумента натуральное число и возвращающую сумму его цифр.
#
# Решение. Функция sum_digits(n) может иметь вид:
#
# def sum_digits(n):
#     result = 0
#     while n > 0:
#         result += n % 10
#         n //= 10
#     return result
# Основная программа имеет вид:
#
# n = int(input())
# print(sum_digits(n))      # вычисляем и выводим сумму цифр считанного числа

# ------------
# Для подсчета среднего значения элементов списка нужно вычислить сумму всех элементов и их количество
# def compute_average(numbers):
#     return sum(numbers) / len(numbers)
# numbers = [1, 3, 5, 1, 6, 8, 10, 2]
# print(compute_average(numbers))      # вычисляем и выводим среднее значение элементов списка
#
# def do_something(numbers):
#     result = 1
#     for i in numbers:
#         result *= i
#     return result
#
# print(do_something([2, 2, 2, 2]))


# def get_sum(x, y, z):
#     return x + y + z
#     print('Сумма равна', x + y + z)
#
#
# print(get_sum(1, 2, 3))

# Конвертер километров
# def convert_to_miles(km):
#     return km * 0.6214
#
# num = int(input())
# print(convert_to_miles(num))


# Количество дней
# def get_days(month):
#     m = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     return m[num-1]
# num = int(input())
# print(get_days(num))

# def get_days(month):
#     if month in (1, 3, 5, 7, 8, 10, 12): return 31
#     if month in (4, 6, 9, 11): return 30
#     if month == 2: return 28
# num = int(input())
# print(get_days(num))


# Делители 1
# def get_factors(num):
#     return [n for n in range(1, num + 1) if num % n == 0]
#     # sp = []
#     # for i in range(1, n + 1):
#     #     if n % i == 0:
#     #         sp.append(i)
#     # return sp
#
# n = int(input())
#
# print(get_factors(n))


# Делители 2
# def get_factors(num):
#     return [n for n in range(1, num + 1) if num % n == 0]
#
# def number_of_factors(num):
#     return len(get_factors(num))
#
# n = int(input())
# print(number_of_factors(n))


# Найти всех
# def find_all(target, symbol):
#     # return [x for x in range(len(target)) if target[x] == symbol]  # в 1 строку
#     a = []
#     for x in range(len(target)):
#         if target[x] == symbol:
#             a.append(x)
#     return a
#
# s = input()
# char = input()
#
# print(find_all(s, char))


# Merge lists 1
# def merge(list1, list2):
#     return sorted(list1 + list2)
#
#
# numbers1 = [int(c) for c in input().split()]
# numbers2 = [int(c) for c in input().split()]
#
# print(merge(numbers1, numbers2))


# Merge lists 2

# def quick_merge(list1, list2):
#     result = []
#     p1 = 0  # указатель на первый элемент списка list1
#     p2 = 0  # указатель на первый элемент списка list2
#     while p1 < len(list1) and p2 < len(list2):  # пока не закончился хотя бы один список
#         if list1[p1] <= list2[p2]:
#             result.append(list1[p1])
#             p1 += 1
#         else:
#             result.append(list2[p2])
#             p2 += 1
#     if p1 < len(list1):  # прицепление остатка
#         result += list1[p1:]
#     if p2 < len(list2):
#         result += list2[p2:]
#     return result

# n=int(input())
# def quick_merge(n):
#     return sorted([int(i) for i in range(n) for i in input().split()])
# print(*quick_merge(n))

# 13.5 Функции с возвратом значения. Часть 2
# Возвращение булевых значений
# если написать булеву функцию is_even(), которая принимает число в качестве аргумента
# и возвращает True, если оно четное, и False если нечетное.
# def is_even(number):
#     if number%2 == 0:
#         return True
#     else:
#         return False
#
# number = int(input())
# if is_even(number):
#     print('Это число четное. ')
# else:
#     print('Это число нечетное.')

# Использование булевых функций для валидации входных данных
# def is_valid(model):
#     if model == 100 or model == 200 or model == 300:
#         return True
#     else:
#         return False
#
#
# m = int(input())
#
# while not is_valid(m):
#     print('Допустимыми номерами моделей являются 100, 200 и 300.')
#     m = int(input())

# Is Valid Triangle?

# def is_valid_triangle(side1, side2, side3):
#     if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
#         return True
#     else:
#         return False
#
# a, b, c = int(input()), int(input()), int(input())
#
# print(is_valid_triangle(a, b, c))
#

# Is a Number Prime? 🌶️
# def is_prime(num):
#     return len([i for i in range(1, num+1) if num % i == 0]) == 2
#
# n = int(input())
# print(is_prime(n))

# Next Prime 🌶️🌶️
# def get_next_prime(num):
#     num += 1
#     for i in range(2, num):
#         if num % i == 0:
#             return get_next_prime(num)
#     return num
#
# # считываем данные
# n = int(input())
#
# # вызываем функцию
# print(get_next_prime(n))


# Good password 🌶️
# def is_password_good(password):
##     upp = [i for i in password if i.isupper()]
##     low = [i for i in password if i.islower()]
##     dig = [i for i in password if i.isdigit()]
##     return all([len(password) >= 8, upp, low, dig])
#
#     result = True
#
#         if len(password) < 8:
#             result = False
#         if password.lower() == password:
#             result = False
#         if password.upper() == password:
#             result = False
#         if password.isalpha():
#             result = False
#
#         return result
#
# txt = input()
# print(is_password_good(txt))


# Ровно в одном
# def is_one_away(word1, word2):
#     if len(word1) != len(word2):
#         return False
#     count = 0
#     for i in range(len(word1)):
#         if word1[i] != word2[i]:
#             count += 1
#     if count == 1:
#         return True
#     else:
#         return False
# txt1 = input()
# txt2 = input()
# print(is_one_away(txt1, txt2))


# Палиндром 🌶️
# объявление функции
# def is_palindrome(text):
#     text = [i.lower() for i in text if i not in (',.!?- ')]
#     return text == text[::-1]
#
# txt = input()
# print(is_palindrome(txt))

# BEEGEEK
# def is_prime(num):
#     return len([i for i in range(1, num+1) if num % i == 0]) == 2
#
# def is_palindrom(num):
#     num = str(num)
#     return(num == num[::-1])
#
# def is_even(num):
#     return(not num % 2)
#
# def is_valid_password(password):
#     try:
#         a, b, c = map(int, password.split(':'))
#         return is_palindrom(a) and is_prime(b) and is_even(c)
#     except: return (False)
#
#
#
#
# psw = input()
# print(is_valid_password(psw))

# Правильная скобочная последовательность 🌶️
# def is_correct_bracket(text):
#     while '()' in text:
#         text = text.replace('()', '')
#     return not text
#
# # считываем данные
# txt = input()
#
# # вызываем функцию
# print(is_correct_bracket(txt))


# Змеиный регистр
# def convert_to_python_case(text):
#     zm = ''
#     for i in text:
#         if i.isupper():
#             zm += '_'
#         zm += i.lower()
#     return zm[1:]
#
# txt = input()
# print(convert_to_python_case(txt))

# 13.6 Функции с возвратом значения. Часть 3
# объявление функции

# Середина отрезка
# def get_middle_point(x1, y1, x2, y2):
#     return (x1 + x2) / 2, (y1 + y2) / 2
#
# # считываем данные
# x_1, y_1 = int(input()), int(input())
# x_2, y_2 = int(input()), int(input())
#
# # вызываем функцию
# x, y = get_middle_point(x_1, y_1, x_2, y_2)
# print(x, y)

# Площадь и длина
# from math import pi
# # def get_circle(radius):
#     return 2 * pi * radius, pi * radius**2
# r = float(input())
# # length, square = get_circle(r)
# print(length, square)


# Корни уравнения 🌶️🌶️
# def solve(a, b, c):
#     d = (b ** 2) - 4 * a * c
#     x1 = ((-1 * b) - d ** 0.5) / (2 * a)
#     x2 = ((-1 * b) + d ** 0.5) / (2 * a)
#
#     return min(x1, x2), max(x1, x2)
#
#
# a, b, c = int(input()), int(input()), int(input())
#
# x1, x2 = solve(a, b, c)
# print(x1, x2)


# Звездный треугольник 🌶️
# def draw_triangle():
#     print('''       *
#       ***
#      *****
#     *******
#    *********
#   ***********
#  *************
# ***************''')
#
# draw_triangle()
#
#
# # объявление функции
# def draw_triangle():
#     m = 15
#     for i in range(1, m + 1, 2):
#         print(' ' * ((m - i) // 2) + '*' * i)
#
# # основная программа
# draw_triangle()
#
#
# Калькулятор доставки
# def get_shipping_cost(quantity):
#     return 1000 + 120 * (quantity-1)
#
#
# n = int(input())
# print(get_shipping_cost(n))

# Биномиальный коэффициент 🌶️

# from math import factorial
# def compute_binom(n, k):
#     return int(factorial(n)/(factorial(k) * factorial(n - k)))
#
#
# n = int(input())
# k = int(input())
# print(compute_binom(n, k))


# Число словами 🌶️
# def number_to_words(num):
#     zero_to_ninety_nine = ['ноль', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять',
#                            'десять', 'одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать',
#                            'шестнадцать', 'семнадцать', 'восемнадцать', 'девятнадцать', 'двадцать', 'двадцать один',
#                            'двадцать два', 'двадцать три', 'двадцать четыре', 'двадцать пять', 'двадцать шесть',
#                            'двадцать семь', 'двадцать восемь', 'двадцать девять', 'тридцать', 'тридцать один',
#                            'тридцать два', 'тридцать три', 'тридцать четыре', 'тридцать пять', 'тридцать шесть',
#                            'тридцать семь', 'тридцать восемь', 'тридцать девять', 'сорок', 'сорок один', 'сорок два',
#                            'сорок три', 'сорок четыре', 'сорок пять', 'сорок шесть', 'сорок семь', 'сорок восемь',
#                            'сорок девять', 'пятьдесят', 'пятьдесят один', 'пятьдесят два', 'пятьдесят три',
#                            'пятьдесят четыре', 'пятьдесят пять', 'пятьдесят шесть', 'пятьдесят семь',
#                            'пятьдесят восемь', 'пятьдесят девять', 'шестьдесят', 'шестьдесят один', 'шестьдесят два',
#                            'шестьдесят три', 'шестьдесят четыре', 'шестьдесят пять', 'шестьдесят шесть',
#                            'шестьдесят семь', 'шестьдесят восемь', 'шестьдесят девять', 'семьдесят', 'семьдесят один',
#                            'семьдесят два', 'семьдесят три', 'семьдесят четыре', 'семьдесят пять', 'семьдесят шесть',
#                            'семьдесят семь', 'семьдесят восемь', 'семьдесят девять', 'восемьдесят', 'восемьдесят один',
#                            'восемьдесят два', 'восемьдесят три', 'восемьдесят четыре', 'восемьдесят пять',
#                            'восемьдесят шесть', 'восемьдесят семь', 'восемьдесят восемь', 'восемьдесят девять',
#                            'девяносто', 'девяносто один', 'девяносто два', 'девяносто три', 'девяносто четыре',
#                            'девяносто пять', 'девяносто шесть', 'девяносто семь', 'девяносто восемь',
#                            'девяносто девять']
#     for i in zero_to_ninety_nine:
#         return zero_to_ninety_nine[num]
#
#
# n = int(input())
# print(number_to_words(n))


# Искомый месяц

# def get_month(language, number):
#     lng_ru = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь',
#               'декабрь']
#     lng_en = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october',
#               'november',
#               'december']
#
#     if language == 'ru':
#         return lng_ru[number-1]
#
#     elif language == 'en':
#         return lng_en[number-1]
#
#
#
# lan = input()
# num = int(input())
# print(get_month(lan, num))


# Магические даты

# def is_magic(date):
#     d = date.split('.')
#     return int(d[0]) * int(d[1]) == int(d[2][-2:])
#
# date = input()
# print(is_magic(date))


# # Панграммы
# def is_pangram(text):
#     t = text.lower()
#     s = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
#          'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#     for i in t:
#         if i in s:
#             s.remove(i)
#     return not s
#
# text = input()
# print(is_pangram(text))

# Модуль random
# import random
# num1 = random.randint(0, 17)
# num2 = random.randint(-5, 5)
# print(num1)
# print(num2)

# import random
# for _ in range(10):
#     print(random.randint(1, 100))

# import random
# num = random.randrange(10)
# print(num)

# import random
# num = random.random()
# print(num)   #--> 0.6913709822330527


# import random
# num = random.uniform(1.5, 17.3)
# print(num)

# import random
# random.seed(17)   # явно устанавливаем начальное значение для генератора случайных чисел
# for _ in range(10):
#     print(random.randint(1, 100))


# import random
# again = 'д'
# while again.lower() == 'д':
#     print('Бросаем кубики... ')l
#     print('Значения граней:')
#     print(random.randint(1, 6))
#     print(random.randint(1, 6))
#     again = input('Бросить кубики еще раз? (д = да, н = нет): ')

# import random

# for _ in range(10):
#     num = random.randint(0, 1)
#     if num == 0:
#         print('Орел')
#     else:
#         print('Решка')


# Функция shuffle() принимает список в качестве обязательного аргумента и перемешивает его случайным образом.
# import random
#
# numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# random.shuffle(numbers)
# print(numbers)   #->[4, 7, 8, 1, 2, 3, 6, 5]

# # Функция choice() принимает список (строку) в качестве обязательного аргумента и возвращает один случайный элемент
# import random
# print(random.choice('BEEGEEK')) #->E
# print(random.choice([1, 2, 3, 4]))  #->1
# print(random.choice(['a', 'b', 'c', 'd']))  #->d


# Функция sample() принимает два обязательных аргумента: список (строку) и количество случайных элементов,
# а возвращает список случайных элементов в указанном количестве.
# import random
# numbers = [2, 5, 8, 9, 12]
# print(random.sample(numbers, 1))  #->[9]
# print(random.sample(numbers, 2))  #->[5, 2]
# print(random.sample(numbers, 3))  #->[5, 2, 12]
# print(random.sample(numbers, 5))  #->[5, 9, 8, 12, 2]


# Угадайка чисел
# from time import *
# from random import randint
# print("Игра - 'Угадайка число!'")
# name = input('Привет, как тебя зовут? ')
# num = randint(1, 100)
# while True:
#     user_num = int(input(f'{name}, введи число от 1 до 100: '))
#     sleep(1)
#     if user_num > num:
#         print('Слишком много, давай еще разок')
#     elif user_num < num:
#         print('Слишком мало, давай еще разок')
#     else:
#         print('Опана, ничесе, ты угадал!')
#         sleep(2.5)
#         print(f'{name}, хочешь еще сыграть?')
#         sleep(0.5)
#         if input() == 'да':
#             sleep(1)
#             print('')
#             continue
#         else:
#             sleep(1.0)
#             print('')
#             print('Ясненько')
#             sleep(1.2)
#             print('Понятненько')
#             sleep(1.2)
#             print('Ну что ж, 'f'{name}, тогда удачи тебе. Береги себя. Пока! До встречи!')
#             break


# Тимур и его числа
# from random import randint
# from math import log2, ceil
#
# n = int(input())
# print(ceil(log2(n)))

# ---------------------------------
#
#
# import random
#
# def is_valid(n): # проверка на соответствие введенного значения условию
#     return n.isdigit() and float(n) - int(float(n)) == 0 and 1 <= int(n) <= 100
#
#
# def input_num(): # ввод данных
#     while True:
#         guess = input()
#         if is_valid(guess):
#             return int(guess)
#         else:
#             print('А может быть все-таки введем целое число от 1 до 100?')
#
#
# def compare_num(down_num, up_num): # Сравнение введенного значения с загаданным
#     num = random.randint(down_num, up_num)
#     total = 0
#     while True:
#         n = input_num()
#         total += 1
#         if n < num:
#             print('Не угадали, попробуйте число побольше')
#         elif n > num:
#             print('Мимо, назовите число поменьше')
#         else:
#             print('Победа!!! Вы угадали ответ за', total,  'попыток, поздравляем!' )
#             break
#
#
# def continue_game(): # Предложение продолжить игру
#     ans = input('Хотите продолжить ("д"/"н")?\n')
#     while True:
#         if ans not in ('y', 'д', 'n', 'н'):
#             ans = input('Вроде, взрослый человек, а на простой вопрос ответить не может...\nПродолжим ("д"/"н")?\n')
#         elif ans in ('n', 'н'):
#             print('До новых встреч!!!')
#             return False
#         else:
#             return True
#
#
# def game(): # Запуск игры
#     print('Добро пожаловать в числовую угадайку!')
#     while True:
#         print('Укажите, в каком диапазоне Вы готовы угадывать числа\n(В пределах от 1 до 100):\n')
#         x, y = input_num(), input_num()
#         if x > y:
#             x, y = y, x
#         print('Введите число от', x, 'до', y, '\n')
#         compare_num(x, y)
#         if continue_game():
#             continue
#         else:
#             break
#
#
# game() # Вызов игры

# ----------------------------------------
# # Magik Ball
#
# import random as rnd
# answers = ["Бесспорно", "Мне кажется - да", "Пока неясно, попробуй снова",
#            "Даже не думай",
#            "Предрешено", "Вероятнее всего", "Спроси позже", "Мой ответ - нет",
#            "Никаких сомнений", "Хорошие перспективы", "Лучше не рассказывать",
#            "По моим данным - нет",
#            "Можешь быть уверен в этом", "Да", "Сконцентрируйся и спроси опять",
#            "Весьма сомнительно"]
#
# print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.')
# name = input('Назови свое имя: ')
# print(f'Приветствую тебя, о {name}!')
# again = 'д'
# while again.lower() == 'д':
#     print('Ты можешь задать свой вопрос:')
#     _ = input()
#     print(f'На это я могу ответить: {rnd.choice(answers)}...')
#     again = input(f'Есть ли у тебя еще вопросы, о {name}? (д = да, н = нет): ')
#
# print(f'Возвращайся если возникнут вопросы, уважаемый {name}!')




# ## Генератор безопасных паролей
# def is_int(num):  # контроль числового ввода
#     if not num.isdigit():
#         return False
#     return True
#
# def is_correct_answer(answer):
#     if answer.lower() in ('y','n'):
#         return True
#     return False
#
# def on_off(answer):
#     if answer.lower() == 'y':
#         return True
#     else:
#         return False
#
# def generate_pwd(lenght, chars):
#     pwd = ''
#     for _ in range(lenght):
#         pwd += random.choice(chars)
#
#     return pwd
#
# import random
# import string
# digits = string.digits
# lowercases = string.ascii_lowercase
# uppercases = string.ascii_uppercase
# punctuations = '!#$%&*+-=?@^_'  #string.punctuation
# doubts = 'il1Lo0O'
# chars = ''
# pwd_list =[]
#
# pwd_quant = input('сколько паролей надо сгененрировать? ')
# while not is_int(pwd_quant):
#     pwd_quant = input('это не число. Еще раз: ')
# pwd_quant = int(pwd_quant)
#
# pwd_len = input('длина пароля: ')
# while not is_int(pwd_len):
#     pwd_len = input('это не число. Еще раз: ')
# pwd_len = int(pwd_len)
#
# upper_on_quest = input('использовать ПРОПИСНЫЕ буквы? Y / N: ')
# while not is_correct_answer(upper_on_quest):
#     upper_on_quest = input('Y or N: ')
#
# lower_on_quest = input('использовать строчные буквы? Y / N: ')
# while not is_correct_answer(lower_on_quest):
#     lower_on_quest = input('Y or N: ')
#
# digit_on_quest = input('использовать цифры? Y / N: ')
# while not is_correct_answer(digit_on_quest):
#     digit_on_quest = input('Y or N: ')
#
# punctuation_on_quest = input('использовать спецсимволы? Y / N: ')
# while not is_correct_answer(punctuation_on_quest):
#     punctuation_on_quest = input('Y or N: ')
#
# doubt_on_quest = input('Исключить неоднозначные символы? Y / N: ')
# while not is_correct_answer(doubt_on_quest):
#     doubt_on_quest = input('Y or N: ')
#
# upper_on = on_off(upper_on_quest)
# lower_on = on_off(lower_on_quest)
# digit_on = on_off(digit_on_quest)
# punctuation_on = on_off(punctuation_on_quest)
# doubt_on = on_off(digit_on_quest)
#
# if upper_on:
#     chars += uppercases
# if lower_on:
#     chars += lowercases
# if digit_on:
#     chars += digits
# if punctuation_on:
#     chars += punctuations
# if  doubt_on: # нужно убрать из строки сомнительные символы
#     chars = ''.join(i for i in chars if i not in doubts)
#
# for _ in range(pwd_quant):
#     pwd_list.append(generate_pwd(pwd_len, chars))
#
# print(*pwd_list, sep='\n')

# ------------------------------------

##Шифр Цезаря
# eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
# eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# rus_lower_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
# rus_upper_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
# symbol = [" ", ",", ".", "!", "?"]
#
# print("Выберите язык: aнгл=e, рус=r")
# lan = input()
# print("Выберите шифрование: шифрование - ch, дешифрование - def")
# chif = input()
# print("Введите ключ шифрования")
# n = int(input())
# print("Введите фразу")
# f = input()
#
# def chru(chifr, n, l, fraza):
#     if l == 'r':
#         moch = 32
#     if l == 'e':
#         moch = 26
#     if chifr== 'def':
#         n = -n
#     for i in range(len(fraza)):
#         if fraza[i].isalpha():
#             if fraza[i] == fraza[i].upper():
#                 for j in range (moch):
#                     if moch == 32:
#                         if fraza[i] == rus_upper_alphabet[j]:
#                             print(rus_upper_alphabet[(j+n)%moch], end = '')
#                             break
#                     if moch == 26:
#                         if fraza[i] == eng_upper_alphabet[j]:
#                             print(eng_upper_alphabet[(j+n)%moch], end = '')
#                             break
#             elif fraza[i] ==fraza[i].lower():
#                 for j in range (moch):
#                     if moch == 32:
#                         if fraza[i] == rus_lower_alphabet[j]:
#                            print(rus_lower_alphabet[(j+n)%moch], end='')
#                            break
#                     if moch == 26:
#                         if fraza[i] == eng_lower_alphabet[j]:
#                            print(eng_lower_alphabet[(j+n)%moch], end = '')
#                            break
#         else:
#             print(fraza[i], end='')
#
# chru(chif, n, lan, f)

# s = 'Hawnj pk swhg xabkna ukq nqj.'
# new_s = ''
# eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz' * 2
# eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' * 2
#
# for j in range(1, 26):
#     for i in range(len(s)):
#         if s[i].isupper():
#             ind = eng_upper_alphabet.rfind(s[i])
#             new_s += eng_upper_alphabet[ind - j]
#         elif s[i].islower():
#             ind = eng_lower_alphabet.rfind(s[i])
#             new_s += eng_lower_alphabet[ind - j]
#         else:
#             new_s += s[i]
#
#     print(new_s)
#     new_s = ''

# n = input()
# # ищем длину слов переводим в словарь в виде чисел
# s = n
# for j in n:
#     if j in '*,.!@"-':
#         s = s.replace(j, '')
# g = [len(i) for i in s.split()]
#
# # объявляем переменную счетчик, когда попадается пробел переходим на след ячейку в словаре
# count = 0
# word_new = ''
# for d in n:
#     number = ord(d)
#     if d == ' ':
#         count += 1
#         word_new += chr(number)
#     elif 65 <= number <= 90:
#         number += g[count]
#         if number > 90:
#             number = number - 26
#             word_new += chr(number)
#         else:
#             word_new += chr(number)
#     elif 97 <= number <= 122:
#         number += g[count]
#         if number > 122:
#             number = number - 26
#             word_new += chr(number)
#         else:
#             word_new += chr(number)
#     else:
#         word_new += chr(number)
#
# print(word_new)


# 15.6 Калькулятор систем счисления
# !!!! если в пайтоне написать: int("строка", основание счисления),
# то получите число, которое находится в строке в десятичном виде

# print(int('111111', 2))  ##->63
# print(int('1AF2', 16))   #->6898
#
#
# В саду 88n фруктовых деревьев, из них 32n яблони, 22n груши, 16n слив и 17n вишен.
# for n in range(8, 16):
#     if 8 * n + 8 == (3 * n + 2) + (2 * n + 2) + (n + 6) + (n + 7):
#         print(n)


# Переведите десятичное число 1000 в шестнадцатеричную систему счисления.
# print(hex(1000)[2:])   #->3E8


# # Переведите десятичное число 513 в двоичную систему счисления.
# print(bin(513))

# В Python встроены три функции bin(), oct(), hex(), которые возвращают строковые представления
# целого десятичного числа в соответствующей системе счисления (2,8,16)

# BOH

# a = int(input())
#
# bin_num = bin(a)
# oct_num = oct(a)
# hex_num = hex(a)
#
# print(bin_num[2:])
# print(oct_num[2:])
# print(hex_num[2:].upper())