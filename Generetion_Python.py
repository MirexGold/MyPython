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




