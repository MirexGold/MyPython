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