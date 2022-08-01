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
a, b, c = int(input()), int(input()), int(input())
print(a if c<a<b else b if a<b<c else c)