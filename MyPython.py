# # Условия
# # x = int(input())
# # if ((x % 4 == 0) and not (x % 100 == 0)) or (x % 400 == 0):
# #    print("Високосный")
# # else:
# #   print("Обычный")
#
# # print("239" < "30" and 239 < 30)
# # print("239" < "30" and 239 > 30)
# # print("239" > "30" and 239 < 30)
# # print("239" > "30" and 239 > 30)
#
# # №a='string'
# # b='anozer string'
# # print(a + b)
#
# # Квадратный корень
# # a=int(input())
# # b=int(input())
# # c=int(input())
# # p=(a+b+c)/2
# # num=(p*(p-a)*(p-b)*(p-c))
# # s=num**(0.5) #вычисление кв корня
# # print(s)
#
# # a=int(input())
# # if (-15<a<=12)or(14<a<17)or(19<=a):
# #    print ("True")
# # else:
# #    print ("False")
#
# # Калькулятор
# # a=float(input()) #1 вещественное число
# # b=float(input()) #2 вещественное число
# # op=str(input()) #операция
# # if op=='+':
# #    print(a+b)
# # elif op=='-':
# #    print(a-b)
# # elif op=='/':
# #    if b==0:
# #        print("Деление на 0!")
# #    else:
# #        print(a/b)
# # elif op=='*':
# #    print(a*b)
# # elif op=='mod': #это взятие остатка от деления
# #    if b==0:
# #        print("Деление на 0!")
# #    else:
# #        print(a%b)
# # elif op=='pow': #возведение в степень
# #    print(a**b)
# # else:
# #    op=='div' #целочисленное деление
# #    if b==0:
# #        print("Деление на 0!")
# #    else:
# #        print(a//b)
#
# # Площадь фигуры
# # figura=str(input())
# # if figura=='треугольник':
# #    a=int(input())
# #    b=int(input())
# #    c=int(input())
# #    p=(a+b+c)/2
# #    num=(p*(p-a)*(p-b)*(p-c))
# #    s=num**(0.5) #вычисление кв корня
# #    print(s)
# # elif figura=='прямоугольник':
# #    a=int(input())
# #    b=int(input())
# #    print(a*b)
# # else:
# #    figura=='круг'
# #    r=int(input())
# #    print(3.14*r**2)
#
# # tp = int(input('Введите число: '))
# # if tp < 0:
# #    print('Ошибка, введите положительное число')
# # elif tp % 10 == 1 and tp % 100 != 11: # Формула 1
# #    print(tp, 'программист')
# # elif tp % 10 >= 2 and tp % 10 <= 4 and (tp % 100 < 10 or #tp % 100 > 20): # Формула 2
# #    print(tp, 'программиста')
# # else:
# #    print(tp, 'программистов')
#
# # Билетик
# # z=input()
# # a=int(z[0])+int(z[1])+int(z[2])
# # b=int(z[3])+int(z[4])+int(z[5])
# # if a==b:
# #    print('Счастливый')
# # else:
# #    print('Обычный')
#
# # a=5
# # while a<=55:
# #    print(a)
# #    a += 2
#
# # a=5
# # while a<=55:
# #    if a%2==1:
# #        print(a)
# #    a+=1
#
# # i = 0
# # while i < 5:
# #    print('*')
# #    if i % 2 == 0:
# #        print('**')
# #    if i > 2:
# #        print('***')
# #    i = i + 1
#
# # for i in range(1, 5):
# #    print(i)
# # else:
# #    print('Цикл for закончен')
#
# # number=15
# # running=True
# # while running:
# #    guess=int(input('Введите число ' ))
# #    if guess==number:
# #        print('Вы угадали')
# #        running = False
# #    elif guess<number:
# #        print('Число немного больше')
# #    else:
# #        print('Число немного меньше')
# # else:
# #    print('Цикл закончен')
# # print('Загаданное число было:', (number))
#
# # a=1
# # b=5
# # s=0
# # i=a
# # while i<=b:
# #    s+=i
# #    i+=1
# # print(s)
#
#
# # Сумма чисел
# # a=int(input())
# # sum=0
# # while a!=0:
# #    sum=sum+a
# #    a=int(input())
# # print(sum)
#
# '''"пока" остаток "d" деленного на "а" не равно нулю или "d" деленного на b не равно нулю, "d" будет плюс один.'''
# # a=int(input())
# # b=int(input())
# # d=1
# # while (d%a!=0) or (d%b!=0):
# #    d+=1
# # print(d)
#
#
# # breake, continue
# # i=0
# # while i<5:
# #    a, b = input().split()
# #    a=int(a)
# #    b=int(b)
# #    if (a==0) and (b==0):
# #        break
# #    if (a==0) or (b==0):
# #        continue
# #    print(a*b)
# #    i+-1
#
#
# # k = 0
# # i = 0
# # s = 0
# # while i < 10:
# #    k += 1
# #    i = i + 1
# #    s = s + i
# #    if s > 15:
# #        continue
# #    i = i + 1
# #    print('итерация №', k, '\ni=',i, 's=',s)
# # print('итерация №', k, '\ni=',i, 's=',s)
#
# '''10 < a < 100 '''
# # while True:
# # @    a = int(input())
# #    if a < 10:
# #        continue
# #    elif a > 100:
# #        break
# #    else:
# #        print(a)
#
# # a=0
# # while a<=100:
# #    a = int(input())
# #    if (10<=a<=100):
# #        print(a)
#
#
# # a=int(input())
# # b=int(input())
# # c=int(input())
# # d=int(input())
# # e=int(input())
# # f=int(input())
# # sec1=a*3600 + b*60 +c
# # sec2=d*3600 + e*60 +f
# # print(sec2-sec1)
#
#
# # Модуль
# # a = int(input())
# # b = int(input())
# # sum=abs(a)+abs(b)
# # print(sum)
#
# # Длинна отрезка
# # a, b = map(float,input().split())
# # l=abs(b-a)
# # print(l)
#
# # МАксимальное число
# # a,b,c,d,e = map(int,input().split())
# # p=max(a, b, c, d, e)
# # print(p)
#
# # Максимальное значени
# # a=int(input())
# # b=int(input())
# # c=int(input())
# # a0=a+b+c
# # a1=a+b*c
# # a2=a*b+c
# # a3=a*(b+c)
# # a4=(a+b)*c
# # a5=a*b*c
# # print(max(a0, a1, a2, a3, a4, a5))
#
# # округление
# # 2- до сотых, 3- до тысячных
# # a=float(input())
# # print(round(a,2), round(a,3))
#
# # Числа через ','   '<'
# # a,b,c = map(int,input().split())
# # print(a,b,c,sep=',')
#
# # a=int(input())
# # print((a-1),a,(a+1),sep='<')
#
# # a=input()
# # b=input()
# # c=input()
# # print(f'{a}---{b}---{c}')
#
# # print(input(), input(), input(), sep='---')
#
#
# # s=input()
# # print('1',s,'2',s,'3',s,'4',s,'5',sep='')
#
# # print(1, 2, 3, 4, 5, sep=input())
#
# # a = input()
# # print(1,2,3,4,5, sep = a)
#
# # print(input(), end=' - Сказала она!')
#
# # print('Гвидо', 'Ван', 'Россум', sep='*', end='-')
# # print('Основатель', 'Питона', sep='_', end='!')
#
#
# # print(int(input())//1000)
#
# # print((int(input()))%(int(input())))
#
# # вывести его последнюю цифру
# # print(int(input())%10)
#
# # вывести разряд сотен этого числа
# # print(int(input())%1000//100)
#
# # найти сумму разрядов числа
# # a=int(input())
# # print((a%1000//100)+(a%100//10)+(a%10))
#
# # print(sum(map(int,input())))
#
#
# # Количество купюр
# # n=int(input())
# # k=n//100
# # n=n%100
# # k=k+n//20
# # n=n%20
# # k=k+n//10
# # n=n%10
# # k=k+n//5
# # n=n%5
# # print(k+n)
#
#
# # n=int(input())
# # k=0
# # for i in (100, 20, 10, 5):
# #    k=k+n//i
# #    n=n%i
# # print(k+n)
#
# # n = int(input())
# # n1 = n // 100 # купюры по 100
# # n2 = n % 100 // 20 # купюры по 20, после выдачи купюр по 100
# # n3 = n % 20 // 10 # купюры по 10, после выдачи купюр по 20
# # n4 = n % 10 // 5 # купюры по 5, после выдачи купюр по 10
# # n5 = n % 5 // 1 # купюры по 1, после выдачи купюр по 5
# # print(n1 + n2 +n3 + n4 + n5) # скалдываем кол-во купюр
#
# # x = int(input())
# # print(x // 100 + x % 100 // 20 + x % 20 // 10 + x % 10 // 5 + x % 5 // 1)
#
# # число n.  следующее за ним четное число.
# # x=int(input())
# # p=x//2*2+2
# # print(p)
#
# # электронные часы
# # n=int(input())
# # hours = n % (60 * 24) // 60
# # minutes = n % 60
# # print(hours, minutes)
#
# # электронные часы
# # n = int(input())
# # h = n // 3600
# # m = n % 3600 // 60
# # s = n % 60
# # print(f'{h}:{m:02}:{s:02}')
#
# # Четное число
# # print(int(input())%2==0)
#
# # положительное число
# # print(int(input())>0)
#
# # Кратно 6
# # print(int(input())%6==0)
#
# # не делится на 9
# # print(int(input())%9!=0)
#
# # у введенного числа последняя цифра 2
# # print(int(input())%10==2)
#
# # оба делится на 7
# # a, b = map(int,input().split())
# # n=(a%7==0) and (b%7==0)
# # print(n)
#
# # a, b = map(int,input().split())
# # print((a%7==0) and (b%7==0))
#
# # a, b = map(int, input().split())
# # print(not a%7 and not b%7)
#
# # правильный треугольник
# # a, b, c = map(int, input().split())
# # print(a==b==c)
#
# # интервалу от 5 не включительно до 19 включительно
# # a=int(input())
# # print(a>5 and a<=19)
#
# # print(5<int(input())<=19)
#
# # хотя бы одно слово равно слову "awesome".
# # a=str(input())
# # b=str(input())
# # print((a=="awesome")or(b=="awesome"))
#
# # print(input() == 'awesome' or input() == 'awesome')
#
# # print('awesome' in {input(), input()})
#
# # равнобедренный треугольник
# # a, b, c = map(int, input().split())
# # print(a==b or b==c or a==c)
#
# # Прямоугольный треугольник
# # a, b, c = map(int, input().split())
# # print(a**2==b**2 + c**2 or b**2==a**2 + #c**2 or c**2==a**2 + b**2)
#
# # print(10<=int(input())<100)
#
#
# # trunc - удаление дробной части
# # import math
# # a=math.trunc(float(input()))
# # print(a)
#
# # аналог удаления дробной части
# # a=int(25.654)
# # print(a)
#
# # округление вниз
# # import math
# # a=math.floor(float(input()))
# # print(a)
#
# # округление вверх
# # import math
# # a=math.ceil(float(input()))
# # print(a)
#
# # Перевязь партоса
# # import math
# # a=math.ceil(int(input())/10)
# # print(a)
#
# # Такси
# # import math
# # a=math.ceil(int(input())/4)
# # print(a)
#
# # Парты
# # import math
# # a=int(input())
# # b=int(input())
# # c=int(input())
# # print(math.ceil(a/2)+math.ceil(b/2)+math.ceil(c/2))
#
# # площадь поверхности стены
# # необходимое количество банок
# # import math
# # a, b, c = map(int, input().split())
# # p=((a*c+b*c)*2)
# # print(math.ceil((p)/16))
#
# # нахождение длины строки len()
# # s=input()
# # print("Вы ввели", len(s), "символов")
#
# # print(len(input()))
#
#
# # Через пробел
# # a = input()
# # print((a + ' ') * 4)
#
# # a, b = input(), input()
# # print(b+a)
#
# # вывести код каждого символа при помощи функции ord
# # a,b,c = map(str,input().split())
# # print(f"Simvol code {a} is {ord(a)}.")
# # print(f"Simvol code {b} is {ord(b)}.")
# # print(f"Simvol code {c} is {ord(c)}.")
#
# # a,b,c=map(str,input().split())
# # print("Simvol code",a,"is",ord(a),end='.\n')
# # print("Simvol code",b,"is",ord(b),end='.\n')
# # print("Simvol code",c,"is",ord(c),end='.\n')
#
# # индекс символа
# # s='hello world'
# # print(s[2])
#
# # Номер последнего индекса меньше чем длина всей строки на 1.
# # s='hello world'
# # print(s[len(s)-1])
# ----------------------------
# # Срезы
# s = 'abcdefg'
# print(s[1])         # b
# print(s[-1])        # g
# print(s[1:3])       # bc
# print(s[1:-1])      # bcdef
# print(s[:3])        # abc
# print(s[2:])        # cdefg
# print(s[:-1])       # abcdef
# print(s[::2])       # aceg
# print(s[1::2])      # bdf
# print(s[::-1])      # gfedcba
#
# Делаем срезы
# s = 'Abrakadabra'
# print(s[2])
# print(s[-2])
# print(s[:5])
# print(s[:9])

# # s='hello world'
# # print(s[7:9])
#
#
# # каждый третий символ строки в обратном порядке
# # print(input()[::-3])
# # a=a[::3]
# # print(a)
#
# # a=input()[::-1]
# # a=a[::3]
# # print(a)
#
# # s=input()
# # print(s[-1]+s[1:-1]+s[0])
#
# # меняет первые буквы местами
# # s=input()
# # print(s[-1]+s[1:-1]+s[0])
#
# # со сдвигом
# # s=input()
# # print(s[-1]+s[:-1])
#
# # Заглавные
# # print(input().upper())
#
# # строчные
# # print(input().lower())
#
# # Сколько раз встречается буква
# # print(input().lower().count('e'))
#
# # удалить все символы "w" и "z".
# # print(input().replace('w','').replace('e',''))
#
# # индекс первой найденной латинской буквы "a"
# # print(input().find('a'))
#
# # индекс последней найденной латинской буквы "a"
# # print(input().rfind('a'))
#
# # из скольких слов состоит фраза
# # print(len(input().split()))
#
# # заменить все пробелы запятыми
# # print(input().replace(' ',','))
#
# ''' отформатировать строку так, чтобы первые 3 и последние 3 символа были заглавными, а оставшиеся строчные'''
#
# # a=input()
# # a=a.lower()
# # n=a[0:3]
# # k=a[-3::]
# # s=a[3:-3]
# # print(n.upper()+s+k.upper())
#
# # n = input().upper()
# # print(n[:3]+n[3:-3].lower()+n[-3:])
#
#
# # Удаление гласных и добавление точек
# # s=input().lower()
# # s=s.replace('a','')
# # s=s.replace('o','')
# # s=s.replace('y','')
# # s=s.replace('e','')
# # s=s.replace('u','')
# # s=s.replace('i','')
# # s='.'.join(s)
# # print('.'+s)
#
# # print('''/\_/\
# # >^,^<
# # / \
# # (|_|)_/''')
#
# # print('  /~~~\\\n //^ ^\\\\\n(/(_*_)\\)\n_/\'\'*\'\'\\_\n(/_)^(_\\)')
#
# # print(r'''
# #  /~~~\
# # //^ ^\\
# # (/(_*_)\)
# # _/''*''\_
# # (/_)^(_\)''')
#
# # форматирование строки
# # v=input()
# # print('''Что Вы сказали? {v}? Какое интересное слово.'''.format(v=v))
#
# # print('Что Вы сказали? {0}? Какое интересное слово'.format(input()))
#
# # print(f'Что Вы сказали? {input()}? Какое интересное слово')
#
# # i=input()
# # f=input()
# # print("Здравствуйте, {f} {i}!".format(i=i, f=f))
#
# # print("Здравствуйте, {1} {0}!".format(input(), input()))
#
# # print('Здравствуйте, {secondName} {firstName}!'.format(firstName=input(), secondName=input()))
#
# # n=int(input())
# # a=n-1
# # b=n+1
# # print('''
# # Для числа {n} предыдущим будет число {a}.
# # Для числа {n} следующим будет число {b}.'''.format(n=n, a=a, b=b))
#
# # n = int(input())
# # print('''Для числа {0} предыдущим будет число {1}.
# # Для числа {0} следующим будет число {2}.'''.format(n, n - 1, n + 1))
#
# # print(f"Мое имя {input()}!")
#
# # print(f"Hello {input().upper()}. You are {input()} years old.")
#
# # print(f'{input()}, вам исполнится 77 лет в {int(input())+77}')
#
# # Напишите программу для перевода натурального значения секунд в значение минут определенного формата.
# # t=int(input())
# # print(f'{t} сек - это {t//60} мин. {t%60} сек.')
#
# # x, y = map(int, input().split())
# # print(f'''Разрешение экрана: {x} x {y}.
# # Общее количество пикселей = {x*y}.''')
#
# # x, y = map(int, input().split())
# # print(f'''{x} / {y} = {x/y}\n{x} // {y} = {x//y}\n{x} % {y} = {x%y}''')
#
# # x=int(input())
# # y=int(input())
# # print(f'''{x} / {y} = {x/y}
# # {x} // {y} = {x//y}
# # {x} % {y} = {x%y}''')
#
# # a,b=int(input()),int(input())
# # print(f'{a} / {b} = {a/b}',f'{a} // {b} = {a//b}',f'{a} % {b} = {a%b}',sep='\n')
#
# # a,b,c=int(input()),int(input()),int(input())
# # print(f'Vector A({a}, {b}, {c})\nVector B({a+5}, {b+5}, {c+5})')
#
#
# # a,b=float(input()), int(input())
# # print(f'Current dollar rate is {a}. You want buy {b} dollars\nYou must pay {a*b}')
#
# #
# # a = [1, 2, 3]
# # b = [4, 5, 6]
# # print(a + b)
# # print(a + [4])
# # a = ['hi'] + a
# # print(a)
# # a = a + b
# # print(a)
#
# # сложение
# # a = [1, 2, 3]
# # b = [4, 5]
# # print(a+b)
#
# # Принадлежность списку
# # a = [2, 5, 8, 9]
# # print(5 in a)
# # print(15 in a)
#
# # Нахождение min и max
# # a = [2, 5, 8, 9]
# # print(max(a))  # Максимальное значение
# # print(min(a))  # Минимальное значение
# # print(sum(a))  # Сумма всех элементов
#
# # Сортировка
# # b = [6, 5, 2, 9]
# # print(sorted(b))
# # print(sorted(b, reverse=True))
# # сам список b не изменился
# # print(b)
# # теперь изменим b
# # b = sorted(b)
# # print(b)
#
# # Сравнение списков
# # a = [2, 5, 8, 99999]
# # b = [2, 5, 9]
# # print(a > b)
#
# # a = [2, 5, 9]
# # b = [2, 5, 9]
# # print(a == b)
#
# # среднее арифметическое списка
# # a = [2, 5, 9, 8]
# # print(sum(a) / len(a))
#
# # записывать в переменные списки
# # b = list(map(int, input('Введите значения: ').split()))
# # print(f'Вот наш список: {b}')
#
#
# my_list = [-214, 181, -139, 448, -664, -66, 213, 832, 717, -462, -924, -706, -85, -244, -222, -340, -482, -518, -781,
#            759, -593, 905, -354, -377, -141, -742, 383, -381, 109, -639, -480, -810, -686, 892, -612, 696, 993, 791,
#            631, -493, -218, -829, -275, 619, -628, -241, -565, -835, -69, 747, 711, -252, -811, -407, -153, 904, 933,
#            -254, 307, -493, -419, -109, -543, 155, -127, 613, -452, -459, 856, 562, 333, -66, -77, -598, -779, -278,
#            867, 321, -20, -415, -357, 735, -906, -14, -370, 453, -630, -736, -830, -917, 32, 422, -895, 198, 284, 472,
#            -986, -964, -989, 29]
# # print(min(my_list), max(my_list))
#
# # my_list = list(map(int, input().split()))
# # print(777 in my_list)
#
# # my_list = list(map(int, input().split()))
# # print(sum(my_list))
#
# # my_list = list(map(int, input().split()))
# # print(sum(my_list)/len(my_list))
#
# #      0   1   2   3  4   5
# # a = [34, 23, 12, 28, 9, 15]
# #     -6  -5  -4  -3 -2  -1
#
#
# # a=[2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# # a[::2] -> [2, 4, 6, 8, 10]
# # a[1::2] -> [3, 5, 7, 9, 11]
# # a[::-1] -> [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
# # a[::-2] -> [11, 9, 7, 5, 3]
# # b=a[:] - копирование списков с разрывом ссылок
#
#
# # a = [34, 23, 12, 28, 9, 15]
# # print(a[2:4])        [12, 28]
# # print(a[:4])         [34, 23, 12, 28]
# # print(a[2::2])       [12, 9]
# # print(a[::3])        [34, 28]
# # print(a[::-1])       [15, 9, 28, 12, 23, 34]
#
#
# # a = [34, 23, 12, 28, 9, 15]
# # a[2] = 123
# # print(a)  # => [34, 23, 123, 28, 9, 15]
#
# # a[3:5] = [23, 34]
# # print(a)  # => [34, 23, 123, 23, 34, 15]
#
# # a[1:5] = 23, 34
# # print(a)  # => [34, 23, 34, 15]
#
# # a = [34, 23, 12, 28, 9, 15]
# # del a[2]
# # print(a)  # => [34, 23, 28, 9, 15]
#
# # a = [34, 23, 12, 28, 9, 15]
# # b = a[:]
# # print(a)  # => [34, 23, 12, 28, 9, 15]
# # print(b)  # => [34, 23, 12, 28, 9, 15]
#
# # print('-' * 10)
#
# # b[0] = 999
# # print(a)  # => [34, 23, 12, 28, 9, 15]
# # print(b)  # => [999, 23, 12, 28, 9, 15]
#
# # print('-' * 10)
#
# # a[0] = 111
# # print(a)  # => [111, 23, 12, 28, 9, 15]
# # print(b)  # => [999, 23, 12, 28, 9, 15]
#
# # второй элемент списка
# # b = list(map(int, input().split()))
# # print(b[1])
#
# # print(list(map(int, input().split()))[1])
#
# # срез списка с третьего элемента по пятый включительно
# # print(list(map(int, input().split()))[2:5])
#
# # вывести последние три элемента этого списка через срез
# # print(list(map(int, input().split()))[-3:])
#
# # каждый третий элемент этого списка, начиная со второго
# # print(list(map(int, input().split()))[1::3])
#
# # список  в обратном порядке
# # print(list(map(int, input().split()))[::-1])
#
# # замена
# # top = ['Игра престолов', 'Шерлок', 'Друзья', 'Во все тяжкие', 'Доктор Хаус', 'Теория большого взрыва', 'Бригада']
# # top[6]='Сверхъестественное'
# # top[2]='Настоящий детектив'
# # print(top)
#
# # Метод append - элемент в конец списка
# # a = [34, 23, 12, 28, 9, 15]
# # print(a)  # [34, 23, 12, 28, 9, 15]
# # a.append(1)
# # print(a)  # [34, 23, 12, 28, 9, 15, 1]
#
# # a = a.append(1) - присвоение в переменную, то потеряете все значения, которые у вас были в списке.
#
# # Метод clear - удаляет все элементы из списка.
# # a.clear()
#
# # Метод copy - делает копию списка
# # a = [34, 23, 12, 28, 9, 15]
# # b = a.copy()
#
# # Метод count -  посчитать сколько раз встретилось какое-либо значение в списке.
# # a = [34, 23, 12, 28, 9, 15, 23, 2, 23]
# # print(f'23 встречается {a.count(23)} раз')
# # print(f'12 встречается {a.count(12)} раз')
# # rint(f'24 встречается {a.count(24)} раз')
#
# # Метод index - находит указанный элемент в списке и возвращает его индекс
# # a = [34, 23, 12, 28, 23, 2, 23]
# # print(a.index(23))
# # print(a.index(12))
# # print(a.index(23, 2))
#
# # Метод insert - Первое - это куда вставить, то есть какой индекс, и второе - что нужно ставить, то есть сам объект.
# # a = [34, 23, 12, 28, 23]
# # a.insert(1, 99)
# # print(a)  # ->[34, 99, 23, 12, 28, 23]
#
#
# # Метод pop -  удаляет значение с конца последовательности и при этом возвращает нам его.
# Результат мы можем сохранить в переменную или сразу распечатать на экран.'''
# # a = [34, 23, 12, 28, 23]
#
# # a.pop()
# # print(a)  # [34, 23, 12, 28]
#
# # b = a.pop()
# # print(b)  # 28
# # print(a)  # [34, 23, 12]
#
# # print(a.pop())  # 12
# # print(a)  # [34, 23]
#
# # print(a.pop(0))  # 34
# # print(a)  # [23]
#
# # Метод remove() переводится как удалить, но этот метод, в отличие от pop(), удаляет по значению.
# # a = [34, 23, 12, 28, 23, 34]
# # a.remove(34)
# # print(a)  # [23, 12, 28, 23, 34]
# # a.remove(34)
# # print(a)  # [23, 12, 28, 23]
#
# # Метод reverse() не требует никаких аргументов и данный метод просто переворачивает список
# # a = [34, 23, 12, 28, 23]
# # a.reverse()
# # print(a)  # [23, 28, 12, 23, 34]
# # a.reverse()
# # print(a)  # [34, 23, 12, 28, 23]
#
# # Метод sort - выполняет сортировку
# # a = [34, 23, 12, 28, 23]
# # a.sort()
# # print(a)  # [12, 23, 23, 28, 34]
# # a.reverse()
# # print(a)  # [34, 28, 23, 23, 12]
#
# # b = [34, 23, 12, 28, 23]
# # b.sort(reverse=True)
# # print(b)  # [34, 28, 23, 23, 12]
#
#
# # Реверс
# # mas = input().split()
# # mas.reverse()
# # print(*mas)
#
# # print(*(input().split()[::-1]))
#
# # Подсчитайте сколько раз в нем присутствует число 999
# # a = list(map(int, input().split()))
# # print(a.count(999))
#
# # print(input().split().count('999'))
# # print(list(map(int, input().split())).count(999))
#
#
# # Дефиснутая фраза
# # a=input().upper().split()
# # a1=list(a[0])
# # a2=list(a[1])
# # a1='-'.join(a[0])
# # a2='-'.join(a[1])
# # print(f'{a1} {a2}')
#
# # re = input().upper()
# # print('-'.join(re).replace('- -',' '))
#
# # print(*map('-'.join, input().upper().split()))
#
# # выводит слова введённой строки (части, разделённые символами пустого пространства) в столбик.
# # print('\n'.join(input().split()))
#
# # Инициалы
# # fio = input().split()
# # print(fio[2], fio[0][0] + "."+fio[1][0] + ".")
#
# # n, f, s = input().split()
# # print(s + " " + n[0] + "." + f[0] + ".")
#
# найти 13%
# a=int(input())
# if a>20000:
#     print(a-a*0.13)
# else:
#     print(a)
#
# # a=str(input())
# # if a == 'Python':
# #     print('ДА')
# # else:
# #     print('НЕТ')
#
# # print("ДА" if input() == "Python" else "НЕТ")
#
# # a, b = int(input()), int(input())
# # if a > b:
# #     print(a)
# # else:
# #     print(b)
#
# # a, b = int(input()), int(input())
# # print(a if a > b else b)
#
#
# # палиндром
# # s = input()
# # a = list(s[:2]) #первые 2 сивола
# # b = list(s[-2::]) #вторые 2 сивола
# # b = b[::-1] #переворачивыаем
# # if a == b:
# #     print('YES')
# # else:
# #     print('NO')
#
# # n = input()
# # if n == n[::-1]:
# #     print("YES")
# # else:
# #     print("NO")
#
# # a, b, c = map(int, input().split())
# # if a + b==c:
# #     print('YES')
# # else:
# #     print('NO')
#
# # a, b, c = map(int, input().split())
# # print('NO' if a+b-c else 'YES')
#
# # a, b = input(), input()
# # if a == b[::-1]:
# #     print("YES")
# # else:
# #     print("NO")
#
# # print('YES' if input() == input()[::-1] else 'NO')
#
# a, b, c = int(input()), int(input()), int(input())
# if a + b > c and b + c > a and c + a > b:
#     print('YES')
# else:
#     print('NO')


# Счастливый билетик
# b = input().rjust(6, '0')
# s1 = int(b[0]) + int(b[1]) + int(b[2])
# s2 = int(b[3]) + int(b[4]) + int(b[5])
# if s1 == s2:
#     print('YES')
# else:
#     print('NO')

# b = input().rjust(6, '0')
# print('YES' if int(b[0])+int(b[1])+int(b[2]) == int(b[3])+int(b[4])+int(b[5]) else 'NO')

# Шахматная доска
# s = '_abcdefgh'
# coord_1 = input()
# coord_2 = input()
# letter = coord_1[0]
# letter_2 = coord_2[0]
# column1 = s.find(letter)
# column2 = s.find(letter_2)
# row1 = int(coord_1[1])
# row2 = int(coord_2[1])
# # print(row1, column1)
# # print(row2, column2)
# if (row1 + column1) % 2 == 0 and (row2 + column2) % 2 == 0 or (row1 + column1) % 2 == 1 and (row2 + column2) % 2 == 1:
#     print('YES')
# else:
#     print('NO')

# print(('YES', 'NO')[sum(map(ord, input() + input())) % 2])


# (-1) = -1
# (-1 + 2) = 1
# (-1 + 2 - 3) = -2
# (-1 + 2 - 3 + 4) = 2
# (-1 + 2 - 3 + 4 - 5) = -3
# (-1 + 2 - 3 + 4 - 5 + 6) = 3
# (-1 + 2 - 3 + 4 - 5 + 6 - 7) = -4
# (-1 + 2 - 3 + 4 - 5 + 6 - 7 + 8) = 4
# (-1 + 2 - 3 + 4 - 5 + 6 - 7 + 8 - 9) = -5
# (-1 + 2 - 3 + 4 - 5 + 6 - 7 + 8 - 9 + 10) = 5

# a = int(input())
# if a % 2 == 0:
#     print(a // 2)
# else:
#     print(a // 2 - a)


# a = int(input())
# print((a // 2) if a % 2 == 0 else (a // 2 - a))

# a, b = int(input()), int(input())
# if a > b:
#     print('>')
# else:
#     if a < b:
#         print('<')
#     else:
#         print('=')

# a, b = int(input()), int(input())
# print('<' if a < b else '>' if a > b else '=')

# a, b, c  = int(input()), int(input()), int(input())
# print(a if a > b and a > c else b if b > a and b>c else c)

# a, b, c = int(input()), int(input()), int(input())
# if a > b:
#     #a -max
#     if a > c:
#         print(a)
#     else:
#         print(c)
# else:
#     if b > c:
#         print(b)
#     else:
#         print(c)


# Торт
# n = int(input())
# if n % 2 == 0:
#     print(n // 2)
# else:
#     if n ==1:
#         print(0)
#     else:
#         print(n)

# 3 Программиста
# a, b, c = map(int, input().split())
# if a<b and b<c:
#     print(c-a)
# else:
#     if c<b and b<a:
#         print(a-c)
#     else:
#         if b<a and a<c:
#             print(c-b)
#         else:
#             if c<a and a<b:
#                 print(b-c)
#             else:
#                 if a<c and c<b:
#                     print(b-a)
#                 else:
#                     if b<c and c<a:
#                         print(a-b)

# a, b, c = map(int, input().split())
# if a < b:
#     a, b = b, a
# if b < c:
#     b, c = c, b
# if a < b:
#     a, b = b, a
# print(a - c)

# a,b,c=sorted(map(int, input().split()))
# print(c-a)


# На вход поступает две СТРОКИ.
# Строки надо привести к одинаковому регистру.
# Сравните строки друг с другом (не длину строк, а прям сами строки) и:
# Если они равны выведите на экран 0.
# Если первая меньше второй выведите на экран  -1.
# Если вторая меньше первой выведите на экран 1.

# a, b = str(input()).upper(), str(input()).upper()
# if a==b:
#     print('0')
# else:
#     if a<b:
#         print('-1')
#     else:
#         print('1')
#
# a, b = input().lower(), input().lower()
# print(int(a > b) - int(b > a))
#

# Кнопочные гонки
# '''Многих сбивает с толку обозначение v - читаем внимательно: один символ за v1 миллисекунд,
# т.е. это не скорость набора текста, а время набора одного символа.
# Делаем вывод:  скорость набора будет :   w = 1/v
# Тогда время потраченное на набор текста из s символов будет равна :     t_text = s/w = sv
# Далее, пинг идет в два конца, соответственно общее время на пинга :     t_ping = 2t
# И того, для участника, его суммарное время:     t_all = t_text + t_ping = sv + 2t
# Для 1-го :
# T1 = s * v1 + 2 * t1
# Для 2-го:
# T2 = s * v2 + 2 * t2
# Далее  остаётся сравнить T1 с T2 и огласить победителя.'''

# s, v1, v2, t1, t2 = map(int, input().split())
# a = t1+(s*v1)+t1
# b = t2+(s*v2)+t2
# if a<b:
#     print('First')
# else:
#     if b<a:
#         print('Second')
#     else:
#         print('Friendship')

# s, v1, v2, t1, t2 =map(int,input().split())
# time1= t1*2+v1*s
# time2= t2*2+v2*s
# print('First' if time1<time2 else 'Second' if time1>time2  else 'Friendship')

# Города
# a, b = input().lower(), input().lower()
# if a[-1] == "ь":
#     if a[-2] == b[0]:
#         print("Good")
#     else:
#         print("Bad")
# else:
#     if a[-1] == b[0]:
#         print("Good")
#     else:
#         print("Bad")

# a,b=input().lower().replace('ь',''),input().lower() #в нижний регистр + убираем "ь" в конце в первом слове
# print('Good' if a[-1]==b[0] else 'Bad')

# a = input().lower()
# b = input().lower()
# if (a[-1] == 'ь' and a[-2] == b[0]) or a[-1] == b[0]:
#     print('Good')
# else:
#     print('Bad')

# a = int(input())
# if a%3==0 and a%5==0:
#     print('FizzBuzz')
# elif a%5==0:
#     print('Buzz')
# elif a%3==0:
#     print('Fizz')
# else:
#     print(a)

# a, b, c = int(input()), int(input()),int(input())
# s=[a,b,c]
# if a==b==c:
#     print(s.count(a))
# elif a==b!=c:
#     print(s.count(a))
# elif b==c!=a:
#     print(s.count(b))
# elif a == c != b:
#     print(s.count(a))
# else:
#     print('0')

# a = int(input())
# if a == 1:
#     print('Январь')
# elif a == 2:
#     print('Февраль')
# elif a == 3:
#     print('Март')
# elif a == 4:
#     print('Апрель')
# elif a == 5:
#     print('Май')
# elif a == 6:
#     print('Июнь')
# elif a == 7:
#     print('Июль')
# elif a == 8:
#     print('Август')
# elif a == 9:
#     print('Сентябрь')
# elif a == 10:
#     print('Октябрь')
# elif a == 11:
#     print('Ноябрь')
# elif a == 12:
#     print('Декабрь')

# n = int(input())
# month = ['Январь', 'Февраль', 'Март', 'Апрель',
#          'Май', 'Июнь', 'Июль', 'Август',
#          'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
# print(month[n-1])

# n = int(input())
# if n<2:
#     print("Младенец")
# elif n>=2 and n<4:
#     print("Малыш")
# elif n>=4 and n<12:
#     print("Ребенок")
# elif n>=12 and n<19:
#     print("Подросток")
# elif n>=19 and n<65:
#     print("Взрослый человек")
# elif n >= 65:
#     print("Пожилой человек")

# a = int(input())
# if a < 2: print('Младенец')
# elif a < 4: print('Малыш')
# elif a < 12: print('Ребенок')
# elif a < 19: print('Подросток')
# elif a < 65: print('Взрослый человек')
# else: print('Пожилой человек')


# Калькулятор
# a=float(input()) #1 вещественное число
# b=float(input()) #2 вещественное число
# op=str(input()) #операция
# if op=='+':
#     print(a+b)
# elif op=='-':
#     print(a-b)
# elif op=='*':
#     print(a*b)
# elif op=='/':
#     if b!=0:
#         print(a/b)
#     else:
#         print('Неизвестно')
# else:
#     print('Неизвестно')

# a=float(input())
# b=float(input())
# c=str(input())
# print(int(a+b) if c=='+'
#     else int(a-b) if c=='-'
#     else a*b if c=='*'
#     else a/b if c=='/' and b!=0
#     else 'Неизвестно')

# если пароль, который ввёл пользователь (в первый раз) короче 7 символов, программа выводит "Short"
# если пароль достаточно длинный, но введённый во второй раз пароль не совпадает с первым, программа
# выводит "Difference" если же и эта проверка пройдена успешно, программа выводит "OK" (латинскими буквами).
# a=input()
# b=input()
# if len(a)<7:
#     print('Short')
# elif a!=b:
#     print('Difference')
# elif a==b:
#     print('OK')

# ps = input()
# print('Short' if len(ps) < 7 else 'Difference' if ps != input() else 'OK')

# распечатывает посимвольно слово ‘privet’:
# a = 'privet'
# while len(a) > 0:
#     print(a[0])
#     a = a[1:]

# вводить пользователя пароль
# quess = input('Введите пароль: ')
# count = 0
# password = 'Abracadabra'
# while quess != password:
#   count += 1
#   print('Неправильный пароль')
#   quess = input('Введите пароль вновь: ')
# print('Вы угадали пароль')
# print(f'Количество неправильных попыток: {count}')

# от 1000 до 2000 включительно
# a = 1000
# while a < 2001:
#     print(a)
#     a += 1

# натуральные числа кратные 5 от 195 до 6785 включительно в порядке убывания
# a = 6785
# while a >= 195:
#     print(a)
#     a = a-5

# В первом примере изначально вес Лимака равен 4, а вес Боба — 7.
# Через год их веса равны 4·3=12 и 7·2=14 соответственно (один вес утроился, а второй удвоился).
# Лимак все еще не больше Боба. Через два года их веса равны 36 и 28, то есть вес Лимака больше, чем вес Боба.
# Лимак стал больше Боба через два года, поэтому вы должны вывести 2.
# Во втором примере веса Лимака и Боба в последующие года равны: 12 и 18,затем 36 и 36,
# и наконец 108 и 72 (через три года).
# Ответ равен 3. Помните, что Лимак хочет стать строго больше Боба, и его не устроят равные веса.
# В третьем примере Лимак станет больше Боба через один год, их веса будут равны 3 и 2 соответственно.

# a, b = map(int,input().split())
# years = 0
# while a <= b:
#     a = a * 3
#     b = b * 2
#     years += 1
# print(years)
#
# l, b = map(int, input().split())
# s = 0
# while b >= l:
#     l *= 3
#     b *= 2
#     s += 1
# print(s)

# удалить все цифры «4» в списке numbers
# numbers = [2, 3, 7, 9, 5, 0, 6, 3, 6, 0, 1, 7, 9, 4, 4, 4, 2, 2, 6, 9, 1, 7, 0, 3, 8, 1, 0, 3, 8, 0, 8, 4, 0, 2, 3, 6,
#            6, 1, 5, 8, 7, 2, 3, 8, 7, 7, 1, 2, 2, 8, 4, 3, 4, 8, 0, 7, 9, 8, 3, 7, 7, 7, 7, 5, 1, 7, 4, 5, 0, 8, 0, 9,
#            2, 4, 7, 6, 6, 5, 9, 7, 1, 7, 8, 8, 3, 4, 9, 7, 6, 4, 2, 0, 0, 0, 9, 4, 0, 9, 4, 4, 4, 5, 5, 4, 2, 5, 9, 4,
#            8, 1, 5, 7, 1, 0, 2, 6, 8, 7, 2, 7, 9, 3, 6, 4, 7, 5, 0, 7, 2, 0, 8, 2, 9, 8, 6, 4, 4, 7, 5, 5, 9, 4, 9, 5,
#            6, 9, 1, 1, 3, 1, 5, 2, 1, 7, 0, 0, 7, 8, 1, 3, 0, 0, 4, 4, 3, 3, 6, 7, 8, 6, 1, 2, 0, 2, 0, 9, 9, 0, 5, 2,
#            4, 1, 7, 4, 9, 9, 4, 9, 6, 9, 2, 7, 1, 2, 4, 5, 4, 0, 9, 0]
# while 4 in numbers:
#     numbers.remove(4)
# print(*numbers)

# будет пропадать первая и последняя буква
# s = input()
# print(s)
# while len(s)>1:
#     s = s[1:-1]
#     print(s)

# квадрат числа
# a = int(input())
# i = 1
# while i ** 2 <= a:
#     print(i ** 2)
#     i += 1

# В первый день спортсмен пробежал X километров.
# В каждый последующий день он увеличивал пробег на 15% от предыдущего дня.
# Вам необходимо определить номер дня, в который пробег спортсмена составил не менее Y километров.
# Само число Y будем поступать на вход программе.
# Входные данные
# Программа получает на вход два положительных вещественных числа X и Y (X,Y ≤ 1000).
# Выходные данные
# Выведите целое число – номер дня, в который спортсмен пробежал не менее Y километров.


# x, y = map(int, input().split())
# d=1
# while x<=y:
#     x=x+(x*0.15)
#     d += 1
# print(d)


# #Про носки
# socks,socksM=map(int,input().split()) # ввод данных в одной строке
#
# # Каждый день минус 1 носок, каждый M день 1 носок добавляется, на сколько дней хватит носков?
# days = 0
# # цикл работает пока кол-во носков больше нуля
# while socks > 0:
#     socks = socks - 1 # сколько носков осталось, отнимаем по одному каждый день.
#     days = days + 1 # увеличиваем счетчик дней
#     if days % socksM == 0: # проверка, что настал М день, т.е. надо добавлять +1 носок от мамы
#         socks = socks + 1 #увеличиваем кол-во носков на 1 (носок от мамы)
# print (days)

# Новогодние свечки
# time = 0
# a, b = map(int, input().split())
# while a > 0:
#     a -= 1
#     time += 1
#     if time % b == 0:
#         a += 1
# print(time)

# степень двойки
# a = int(input()) #Ввод
# x = 0 #Счётчик делений на 2
# b = a # Число ввода для проверки
# while int(a/2) != 0: #Пока а делиться на 2 и не равно 0
#     a = int(a/2) #Делим a на 2 (8/2 = 4)
#     x+=1 #Считаем кол-во операций, пока а не станет равно 0
# if (2**x)==b: #Возводим двойку в кол-во операций(степень) и если оно равно начальному числу
#     print(x) #Выводим само это кол-во операций
# else:
#     print('НЕТ') # Если не равно начальному числу, выводим НЕТ
#
#
# a = int(input())
# count = 0
# while a >= 1 and a % 2 == 0:
#     a //= 2
#     count += 1
# print(count if a == 1 else 'НЕТ')

# На данный момент изучено преобразование числа к строке str() и обратно int(), а так же сами строки и
# их индексы.
# Цикл продолжается пока первый элемент у строки n не равен "1" и само число n меньше или равно 10**9:
# в цикле число n меняется путем умножения самого числа n на его первую цифру (первый элемент).
# Выводим число n.


# Зимний вечер в Бурсе
# n = int(input())
# while str(n)[0] != '1' and n <= 1000000000:
#     n = n * int(str(n)[0])
# print(n)


# a=input()
# while int(a[0])!=1 and len(a)<10:
#     a=str(int(a[0])*int(a))
# print(a)

# кучу инпутов без доп перменных можно делать так:
# while True:
#     print('Something')

# Обход всех цифр числа
# n = 4782
# while n > 0:
#     print(n%10)
#     n = n//10

# Обход всех цифр числа в двоичной системе
# n = 14
# while n > 0:
#     print(n%2)
#     n = n//2

# сколько разрядов в числе:
# n = int(input('Введите число: '))
# count = 0
# while n > 0:
#     n = n//10
#     count = count + 1
# print(f"Количество цифр={count}")

# сколько всего четных цифр:
# n = int(input('Введите число: '))
# count_even = 0
# while n > 0:
#     last = n % 10
#     if last % 2 == 0:
#         count_even = count_even + 1
#     n = n//10
# print(f"Количество четных цифр = {count_even}")
#

# сумму всех цифр числа:
# n = int(input('Введите число: '))
# s = 0
# while n > 0:
#     s = s + n % 10
#     n = n//10
# print(f"Сумма всех цифр = {s}")
#

# произведение всех цифр числа:
# n = int(input('Введите число: '))
# product = 1
# while n > 0:
#     last = n % 10
#     product = product * last
#     n = n//10
# print(f"Произведение всех цифр = {product}")


# самую большую и самую маленькую цифру в числе:
# n = int(input('Введите число: '))
# maximum = 0
# minimum = 9
# while n > 0:
#     last = n % 10
#     if last > maximum :
#         maximum = last
#     if last < minimum :
#         minimum = last
#     n = n//10
# print(f"Самая большая цифра = {maximum}")
# print(f"Самая маленькая цифра = {minimum}")
#

# сколько цифр меньше 3х
# number = 1234567890
# count = 0
# while number > 0:
#     last_digit = number % 10
#     if last_digit < 3:
#         count = count + 1
#     number = number // 10
# print(count)

# натуральное число и выводит его цифры в столбик в обратном порядке.
# number = int(input())
# while number > 0:
#     print(number % 10)
#     number = number // 10
#
# print(*input()[::-1], sep='\n')


# сумму всех цифр числа:
# n = int(input())
# s = 0
# while n > 0:
#     s = s + n % 10
#     n = n//10
# print(s)
#
# print(sum(map(int, list(input()))))

# n = int(input())
# pr = 1
# while n > 0:
#     pr = pr * n % 10
#     n = n//10
# print(pr)

# произведение цифр данного числа
# n = int(input())
# product = 1
# while n > 0:
#     last = n % 10
#     product = product * last
#     n = n // 10
# print(product)

# n = int(input())        # вводим число
# k = 1                   # устанавливаем счетчик
# while n > 0:            # производим вычисления в блоке ниже пока n > 0
#     k *= n % 10         # берем остаток от введенного числа (последнюю цифру) и увеличиваем "K" на него
#     n = n // 10         # уменьшаем наше введенное число на один разряд (убираем последнюю цифру)
# print(k)                # выводим на печать


# самую большую и самую маленькую цифру в числе:
# n = int(input())
# maximum = 0
# minimum = 9
# while n > 0:
#     last = n % 10
#     if last > maximum :
#         maximum = last
#     if last < minimum :
#         minimum = last
#     n = n//10
# print(minimum)
# print(maximum)
#
# s = sorted(input())
# print(s[0], s[-1], sep = '\n')


# сколько раз встречается цифра 7
# n = int(input())
# count = 0
# while n > 0:
#     last = n % 10
#     if last/7==1:
#         count = count + 1
#     n = n // 10
# print(count)

# print(input().count('7'))

# цифры в двоичной системе в столбик в обратном порядке
# n = int(input())
# while n > 0:
#     print(n%2)
#     n = n//2
#
# print(*(f"{int(input()):b}"[::-1]), sep='\n')

# Нахождение всех делителей числа
# n = int(input())
# i = 1
# while i <= n:
#     if n % i == 0:
#         print(i, end=" ")
#     i += 1

# Нахождение суммы всех делителей числа
# n = int(input())
# a = []
# i = 1
# while i * i <= n:
#     if n % i == 0:
#         a.append(i)
#         if i != n // i:
#             a.append(n // i)
#     i += 1
# print(sum(a))


# натуральное число N. Определить, является ли оно простым
# n = int(input())
# a = []
# i = 1
# while i * i <= n:
#     if n % i == 0:
#         a.append(i)
#         if i != n // i:
#             a.append(n // i)
#     et = [a[0], a[-1]]
#     i += 1
# if a == et:
#     print('Yes')
# else:
#     print('No')

# a=int(input())
# i=2
# while a%i!=0 and i<a:
#     i+=1
# print('Yes' if i==a else 'No')


# найти сумму делителей.
# n = int(input())
# a = []
# i = 1
# while i * i <= n:
#     if n % i == 0:
#         a.append(i)
#         if i != n // i:
#             a.append(n // i)
#     i += 1
# print(sum(a))
#
# n = int(input())
# total = 0
# i = 1
# while i <= n:
#     if n % i == 0:
#         total += i
#     i += 1
# print(total)


# Алгоритм Евклида оптимизированный (путём деления) НОД
# a, b = map(int, (input().split()))
# while b > 0:
#     c = a % b
#     a = b
#     b = c
# print(a)


# Алгоритм Евклида НЕ оптимизированный (через вычитание) НОД
# a=int(input())
# b=int(input())
# while a!=b:
#     if a>b:
#         a=a-b
#     else:
#         b=b-a
# print(a)

# a, b = map(int, input().split())
# while a != b:
#     if a > b:
#         a = a - b
#     else:
#         b = b - a
# print(a)

# Наименьшее общее кратное (НОК)
# a = int(input())
# b = int(input())
# c = a
# d = b
# while b > 0:
#     a, b = b, a % b
# print((c * d) / a)

# наименьшее общее кратное(НОК).
# a,b = map(int, input().split())
# c = a
# d = b
# while b > 0:
#     a, b = b, a % b
# print(int((c * d) / a))
#
# a, b = map(int, input().split())
# c = a * b
# while b > 0:
#     a, b = b, a % b
# print(int(c / a))

# сумму всех членов данной последовательности.
# total = 0 # общая сумма
# while True: # бесконечный цикл
#     n = int(input()) # каждая строка содержит целое число
#     if n == 0: # нашли нуль
#         break  # выходим из цикла
#     total += n # суммируем
# print(total) # печатаем результат

# последний введенный валидный пароль
# n = input()
# list_of_passwords = []
# while (len(n) >= 5) and (len(n) <= 9):
#     n = input()
#     list_of_passwords.append(n)
#     if len(n) < 5 or len(n) > 9:
#         print(list_of_passwords[-2])

# a = input()
# while len(a) > 4 and len(a) < 10:
#     s = a
#     a = input()
# print(s)

# Собираемся в поход
# n = int(input())  # n - общий объем рюкзака
# a = 0             # a - объем который уже занят
# e = 0             # e - обьем следующей строки
# b = 0             # b - колличество
#
# while a <= n:
#     e = int(input())
#     b = b + 1
#     a += e
# print('Довольно!')
# print(a - e)
# print(b - 1)

# Новый год и спешка
# a, b = map(int, input().split())  # кол-во задач и время(мин) до вечеринки
# c = 0  # кол-во задач
# d = 240 - b  # время на задачи
# while d > 0:
#     c+=1
#     d-=c*5
#     if a == c: #если кол-во решеных задач равно максимальному то выходим из цикла
#         break
# #если время отрицательно значит нужно вычесть одну задачу что бы успеть ко времени
# if d<0:
#     c-=1
# print(c)


# Ваня и кубики
# num_cubs = int(input())    # кол-во всех кубиков
# i = 0                      # кол-во этажей с кубиками
# summa_cubs = 0             # сумма всех кубиков на этажах (считается в цикле)
# # пока еще есть возможность построить следующий этаж (хватит кубиков)
# while summa_cubs + i + 1 <= num_cubs:
#     i += 1                 # делаем следующий этаж с кубиками
#     summa_cubs += i        # находим сумму кубиков
#     num_cubs -= summa_cubs # и отнимаем эту сумму от оставшихся кубиков
#
# print(i)  # вывод кол-ва этажей


# новый отсортированный список
# n, m = (int, input().split())  # получаем из первой строки кол-во элементов 1 и 2 списка
# list1 = list(map(int, input().split()))  # получаем 1 список
# list2 = list(map(int, input().split()))  # получаем 2 список
# list = list1 + list2  # делаем из двух списков 1
#
# result = []  # пустой список для результата
#
# # проверяйте список, пока длина не станет 0
# while len(list) != 0:
#     a = min(list)      # найти минимальный элемент в списке
#     result.append(a)   # добавить элемент в новый список
#     list.remove(a)     # удалить элемент из старого списка
#
# print(*result) # распечатать новый отсортированный список


# boys_count = int(input())  # Количество мальчиков
# boys_list = list(map(int, input().split()))  # Список с показателями скиллов каждого мальчика
# boys_list.sort()  # Сортируем список мальчиков
# girls_count = int(input())  # Количество девочек
# girls_list = list(map(int, input().split()))  # Список с показателями скиллов каждой девочки
# girls_list.sort()  # Сортируем список девочек
# boys = 0  # Это первый мальчик индекс всегда равен 0 т.к. происходит удаление
# girls = 0  # Это первая девочка индекс всегда равен 0 т.к. происходит удаление
# count = 0  # Это количество пар, которое пока равно нулю
# Пока один из списков не станет пустым
# while boys_list != [] and girls_list != []:
#     if abs(boys_list[boys] - girls_list[girls]) <= 1:  # Если разность по модулю не больше единицы
#         count += 1  # Прибавляем пару
#         boys_list.pop(boys_list.index(boys_list[boys]))  # Удаляем из списка этого мальчика
#         girls_list.pop(girls_list.index(girls_list[girls]))  # Удаляем из списка эту девочку
#     else:  # Иначе
#         if boys_list[boys] > girls_list[
#             girls]:  # Если по скиллу мальчик лучше, чем девочка то этой девочке пару уже не найти
#             girls_list.pop(girls_list.index(girls_list[girls]))  # Поэтому удаляем её из списка
#
#         else:  # Если же девочка скилловее мальчика, то мы не сможем найти пару мальчику
#             boys_list.pop(boys_list.index(boys_list[boys]))  # Поэтому удаляем его
# print(count)  # Выводим количество пар

# Выведите минимальный делитель этого числа, отличный от единицы.
# n = int(input())
# d = 2 # создоем стартовый делитель, помня о том, что на ноль делить нельзя,
# # а также что делитель должен быть отличный от единицы.
# while True:
#     if n % d == 0:
#         print(d)
#         break
#     d += 1

# n, d = int(input()), 2
# while n % d: d += 1
# print(d)


# a=int(input())-1
# b=int(input())
# while a<b:
#     a+=1
#     if a%777==0:    # если встречаете число, кратное 777, необходимо принудительно закончить цикл
#         break
#     if a%2==0 or a%3==0: # пропускать (не выводить) числа, которые делятся на 2 или на 3
#         continue
#     print(a)

# a, b = int(input()), int(input()) + 1
# while a < b:
#     if a == 777:
#         break
#     if a % 2 and a % 3:
#         print(a)
#     a += 1


# Сиракузская последовательность
# n=int(input())
# count = 0 			#Создаем счетчик
# while True:			#Пока выражение True
#     if n==1:        #Если наше число равно 1
#         break       #то выходим из цикла
#     count+=1        #Добавляем к счетсику +1
#     if n%2==0:      #Проверяем на четное число
#         n=n/2
#     else:           #Иначе нечетное число
#         n=3*n+1
# print(count)

# i = 0
# while i < 5:
#     if i == 5:
#         break
#     print(i)
#     i += 1
# else:
#     print("Конец")

# a = input()
# while len(a) > 0:
#     if a[0] == 'a' or a[0] == 'e': #если a или b нашлись то выходим из цикла
#         print('Ага! Нашлась')
#         break
#     print(f'Текущая буква: {a[0]}')
#     a = a[1::]                     #убираем первый символ из строки
# else:
#     print('Распечатали все буквы') #если из цикла не вышили, а длина стала 0
#
#
# word = list(input())
# while word:
#     if word[0] in 'ae':
#         print('Ага! Нашлась')
#         break
#     print('Текущая буква:', word[0])
#     word.remove(word[0])
# else:
#     print('Распечатали все буквы')

# список, содержащий последовательность чисел 0,1,2,3,4,5,6,7,8,9 ?
# print(list(range(10)))

# последовательность чисел от 12 до 34 включительно
# print(list(range(12, 35)))

# сформировать последовательность 25, 33, 41, 49, 57 .... , 169
# print(list(range(25, 170, 8)))

# последовательность -11, -12, -13, -14 .... , -35
# print(list(range(-11, -36, -1)))

# последовательность 10, 9, 8, 7, ... , 0
# print(list(range(10, -1, -1)))
# print(list(reversed(range(11))))

# последовательность 1000, 950, 900, 850, ... , 500
# print(list(range(1000, 499, -50)))
# print(sorted(list(range(500, 1001, 50)), reverse=True))

# Рандомное число от 1 до 10 и их сумма
# from random import randint
# s=0
# n=int(input())
# for i in range(n):
#     a = randint(1, 10)
#     s+=a
#     print(a, end=' ')
# print()
# print(s)

# елка
# for i in range(1,11):
#     print('*'*i)

# # Степень
# for i in range(1,11):
#     print(2**i)

# n=int(input())
# s=0
# for i in range(n):
#     a=int(input())
#     s+=a
#     print('current s:', s)
# print('total s:', s)
# print('sred arefm =', s/n)

# вывести на экран все числа от 1 до N каждое число на отдельной строке.
# n = int(input())
# for i in range(1,n+1):
#     print(i)

# for i in range(int(input())):
#     print(i+1)

# вывести на экран все числа от N до 1 каждое число на отдельной строке.
# n = int(input())
# for i in range(n, 0, -1):
#     print(i)

# На вход ей будет поступать фраза и затем количество раз, которое эту фразу нужно повторить.\
# t=input()
# n=int(input())
# for i in range(n):
#      print(t)
#
# print(*[input()]*int(input()),sep='\n')


# a = int(input())
# b = int(input())
# for i in range(a, b+1):
#     if i % 3 == 0 and i % 5 == 0:
#         print('FizzBuzz')
#     elif i % 5 == 0:
#         print('Buzz')
#     elif i % 3 == 0:
#         print('Fizz')
#     else:
#         print(i)
#
# for n in range(int(input()), int(input()) + 1):
#     if not n % 3 and not n % 5:
#         print('FizzBuzz')
#     elif not n % 3:
#         print('Fizz')
#     elif not n % 5:
#         print('Buzz')
#     else:
#         print(n)

# for i in range(int(input()), int(input()) + 1):
#     print(f'Число {i}; его квадрат = {i**2}; его куб = {i**3}')


# n=int(input())
# m=0
# h=0
# for i in range(n):
#     pm, pc = map(int, input().split())
#     if pm > pc:
#         m = m + 1
#     elif pc > pm:
#         h = h + 1
#     i = i + 1
# if m>h:
#     print('Mishka')
# elif m==h:
#     print('Friendship is magic!^^')
# else:
#     print('Chris')
#
#
# Mishka_wins = 0
# Chris_wins = 0
# for i in range(int(input())):
#     m, c = map(int, input().split())
#     if m > c:
#         Mishka_wins += 1
#     elif m < c:
#         Chris_wins += 1
# if Mishka_wins > Chris_wins: print("Mishka")
# elif Mishka_wins < Chris_wins: print("Chris")
# else: print("Friendship is magic!^^")

# N=int(input())
# stroka=1
# z=0
# for i in range(N):
#     st=input().lower()
#     z=st.find('рок')
#     if z>=0:
#         print(stroka,st.find('рок')+1)
#     stroka+=1

# n = int(input())
# a = []
# for i in range(n):
#     s = input()
#     if 'соль' not in s:
#         a.append(s)
# print(', '.join(a))
#
# s = []
# for i in range(int(input())):
#     a = input()
#     if 'соль' not in a:
#         s. append(a)
# print(*s, sep=', ')


# n = int(input())  # Вводим число
# sum = 0  # Новая переменная, где мы будем записывать значение суммы
# for i in range(1, n):  # Цикл от 1го до нашего числа
#     if i % 3 == 0 or i % 5 == 0:  # Условие, если число кратно 3 или 5
#         sum += i  # Прибавляем к сумме, полная запись выглядит так "sum = sum + i"
# print(sum)

# n=int(input())
# sum=0
# for i in range(1,n):
#     if i%3==0 or i%5==0:
#         sum+=i
# print(sum)

# sum=0
# for i in range(50,101):
#     i=i**3
#     sum+=i
# print(sum)

# for i in range(int(input())):
#     a = input()
#     if len(a)>10:
#         print(a)
#     else:
#         print(f'{a[0]}{len(a)-2}{a[-1]}')

# Високосный год
# x = int(input())
# if x % 4 == 0 and x % 100 != 0 or x % 400 == 0:
#     print('YES')
# else:
#     print('NO')

# Даны три целых числа. Выведите значение наименьшего из них.
# a, b, c = int(input()), int(input()), int(input())
# if b >= a <= c:
#     print(a)
# elif a >= b <= c:
#     print(b)
# else:
#     print(c)

# Сколько совпадает чисел»
# a = int(input())
# b = int(input())
# c = int(input())
# if b == a == c:
#     print('3')
# elif a == b or b == c or a==c:
#     print('2')
# else:
#     print('0')

# Яша плавает в бассейне
# n, m, x, y = int(input()), int(input()), int(input()), int(input())
# if n > m:
#     n, m = m, n
# if x >= n / 2:
#     x = n - x
# if y >= m / 2:
#     y = m - y
# if x < y:
#     print(x)
# else:
#     print(y)

# число X. Выведите его дробную часть.
# x = float(input())
# print(x - int(x))

# Выведите его первую цифру после десятичной точки.
# x = float(input())
# print(int(x * 10) % 10)
#
# Конец уроков
# a = int(input())
# a = a*45 + (a//2)*5 + ((a+1)//2-1)*15
# print(a//60 + 9, a%60)
#

# Автопробег
# from math import ceil
# n = int(input())
# m = int(input())
# print(ceil(m / n))

# Стоимость покупки
# rub = int(input())
# kop = int(input())
# kol = int(input())
# cost = kol * (100 * rub + kop)
# print(cost // 100, cost % 100)

# Улитка
# h, d, n = int(input()), int(input()), int(input())
# print(int((h - d - 1) // (d - n) + 2))

# Число десятков
# n = int(input())
# print(n // 10 % 10)

# Сумма цифр
# a = int(input())
# print((a%1000//100)+(a%100//10)+(a%10))

# Гипотенуза
# import math
# a, b = int(input()), int(input())
# c = math.sqrt(b**2 + a**2)
# print(c)

# Проценты
# p = int(input())
# x = int(input())
# y = int(input())
# money_before = 100 * x + y
# money_after = int(money_before * (100 + p) / 100)
# print(money_after // 100, money_after % 100)

# Сумма десяти чисел
# sum = 0
# for i in range(10):
#     number = int(input())
#     sum += number
# print(sum)

# Сумма N чисел
# n = int(input())
# sum = 0
# for i in range(n):
#     sum += int(input())
# print(sum)

# Сумма кубов
# n = int(input())
# sum = 0
# for i in range(1, n + 1):
#     sum += i ** 3
# print(sum)

# # Факториал
# n = int(input())
# pr = 1
# for i in range(1, n + 1):
#     pr *= i
# print(pr)

# Сумма N чисел
# sum = 0
# for i in range(int(input())):
#     if (int(input())) == 0:
#         sum += 1
# print(sum)

# Задача «Лесенка»
# for i in range(1,int(input())+1):      # 1
#     for j in range(1,i+1):             # 12
#         print(j, end='')               # 123
#     print()                            # 1234

# Потерянная карточка
# n = int(input())
# sum = 0
# for i in range(1, n + 1):
#     sum += i
# # можно доказать формулу:
# # sum == n * (n + 1) // 2
# # но мы посчитаем это значение циклом
# for i in range(n - 1):
#     sum -= int(input())
# print(sum)


# таблица умножения
# i = 1
# j = 1
# while i < 10:
#     while j < 10:
#         print(i * j, end="\t")
#         j += 1
#     print("\n")
#     j = 1
#     i += 1

# Локальные функции
# def print_messages():
#     # определение локальных функций
#     def say_hello(): print("Hello")
#
#     def say_goodbye(): print("Good Bye")
#
#     # вызов локальных функций
#     say_hello()
#     say_goodbye()
#
#
# # Вызов функции print_messages
# print_messages()
#
# # say_hello() # вне функции print_messages функция say_hello не доступна


# Организация программы и функция main
# def main():
#     say_hello()
#     say_goodbye()
#
#
# def say_hello():
#     print("Hello")
#
#
# def say_goodbye():
#     print("Good Bye")
#
#
# # Вызов функции main
# main()

# def a1(*xx):
#     x = "Вася"
#     y = "Петя"
#     z = 2
#     k ="алкоголика"
#     return x, y, z, k
#
# a, b, c, d = a1()
# print("А вы знаете, что", a, "и", b,c,d,"?!")

# обход по значеням
# a = [23, 4, 5, 68, 56]
# for i in a:
#     print(i,a.index(i))


# обход по индексам
# a = [23, 4, 5, 68, 56]
# n=len(a)
# for i in range(n):
#     print(i, a[i])
#     a[i]+=5
# print(a)

# удаление дублей из списка
# a=[1,2,3,4,5,2,1,5]
# b=[]
# for i in a:
#     if not i in b:
#         b.append(i)
# print(b)


# четные, не четный
# a=[1,2,3,6,7,9,52,34,21]
# chet=[]
# nechet=[]
# n=len(a)
# for i in range(n):
#     if a[i]%2==0:
#         chet.append(i+1)
#     else:
#         nechet.append(i+1)
# print(chet)
# print(nechet)

# обход по строкам
# a = 'Hello World'
# for i in a:
#     if i >= 'a' and i <= 'z':
#         print(i, 'small')
#     elif "A" <= i <= "Z":
#         print(i, "big")
#     else:
#         print(i)

# v='aeiou'
# s='aertiooikjoaikl'
# n=len(s)
# for i in range(n-1):
#     if s[i] in v and s[i+1] in v:
#         print(s[i], s[i+1])

# Заполняем список
# a = int(input())
# sp=[]
# for i in range(a):
#     sl=input()
#     sp.append(sl)
# print(sp)
#
# n = int(input())
# a = [input() for _ in range(n)]
# print(a)

# вывести список слов, в которых присутствует введённая буква
# s = input()  # символ для поиска
# stroka = list(input().split())  # Предложение делим на слова
# g = len(stroka)  # Получаем длину списка
# for i in range(g):  # Цикл по списку
#     if s in stroka[i]:  # Если символ нашли в слове то выводим его
#         print(stroka[i])
#
# a=input()
# c=input().split()
# for i in c:
#     if a in i:
#         print(i)

# # Получаем список чисел в одну строку через пробел
# nums = list(map(int, input().split()))
# # Создаем пустой список для нужных чисел
# valid_nums = []
# # получаем числа больше 0 и кладем в новый список
# for i in nums:
#     if i > 0:
#         valid_nums.append(i)
# # Если новый список пустой выводим Empty
# if len(valid_nums) == 0:
#     print('Empty')
# else:
#     # Выводим на экран минимальное число
#     print(min(valid_nums))

# рекордное количество вхождений
# x=list(input().lower())  # делаем из слова список букв
# y=[]                     # пустой список для количества символов
# for i in x:              # цикл по списку букв в строке
#     y.append(x.count(i)) # считаем количество текущей буквы в списке
# print(max(y))            # находим и выводим максимальное число


# четные, не четный
# l = list(map(int, input()))  # преобразуем число в список
# chet = 0
# nechet = 0
#
# for i in range(len(l)):
#     if (i) % 2 == 0:
#         chet += l[i]  # cчитаем суммы четных
#     else:
#         nechet += l[i]  # и нечетных разрядов числа
#
# if (nechet - chet) % 11 == 0:  # условие по свойству делимости
#     print('YES')
# else:
#     print('NO')

# сколько символов в данной строке являются цифрами
# s = input()
# sum = 0  # сумма цифр
# cnt = 0  # кол-во цифр
# for i in (s):
#     if ("0" <= i <= "9"):
#         sum += int(i)  # Считаем сумму
#         cnt += 1  # Считаем кол-во
#
# print(cnt, sum)

# Правильная скобочная последовательность
# pairs = {'()', '[]', '{}'}  # список открывающихся и закрывающихся скобок
# str = input().replace(' ', '')  # получаем список и чистим его от пробелов
#
# for _ in range(len(str) // 2):  # полученную строку делим пополам т.к при нахождении удаляется сразу 2 символа
#     for i in pairs:  # в цикле бежим по заготовленному списку скобок
#         str = str.replace(i, '')  # если нашли пару удаляем ее из строки
#
# if len(str) == 0:
#     print('YES')
# else:
#     print('NO')
#
# pattern = input()
# for i in range(len(pattern) // 2):
#     pattern = pattern.replace('{}', '')
#     pattern = pattern.replace('()', '')
#     pattern = pattern.replace('[]', '')
# print('YES' if len(pattern) == 0 else 'NO')

# Сортировка подсчетом
# a = [0, 2, 3, 4, 4, 3, 1, 3, 1, 5, 4, 2, 1, 2, 3, 4]
# count = [0] * 6
# for i in a:
#     count[i] += 1
# print(count)
# for i in range(6):
#     if count[i]>0:
#         print(str(i) * count[i],end=' ')

# s='abczsdf fsdfw dddddd cv 3213 3 =-(07'
# letters=[0]*26
# for i in s.lower():
#     if i>= 'a' and i<='z':
#         nomer= ord(i)-97
#         letters[nomer]+=1
#
# for i in range(26):
#     if letters[i]>0:
#         print(chr(i+97), letters[i])

# a=[]
# import random
# for i in range(10):
#     a.append(random.randint(-10,10))
#
# count=[0]*21
# for i in a:
#     count[i+10]+=1
# print(a)
# for i in range(21):
#     if count[i]>0:
#         print(i-10, count[i])

# Переворот строки
# print(input()[::-1])


# a = list(map(int, str(input()))) # вводим строку и сразу преобразуем ее в список.
# count = [0]*10                   # создаем список из 10 нулей для подсчета чисел (от 0 до 9)
# for i in a:                      # Проходимся по нашему списку, считая какие цифры есть и сколько их.
#                                  # т.е.[i] это индекс нашего списка из 10 нулей.
#     count[i] += 1                # к каждому соответствующему индексу ставим +1
# for i in range(10):      # проходимся по заполненному списку (бывший из нулей)
#     if count[i] > 0:     # выводим только те значения что не являются 0
#         # печать i-ый индекс(цифра) и количество i-ых цифр в введеном числе
#         print(i, count[i])

# n = input()
# for i in range(10):
#     if str(i) in n:
#         print(i, n.count(str(i)))

# n = int(input())
# a = map(int, input().split())
# count = [0] * 201  # список count заполняется нулями
# for i in a:  # перебор всех элементов в а
#     count[i] += 1  # к элементу count с индексом i прибавляется 1, т.е. подсчет сколько данное число встречается в а
#
# for i in range(-100, 101):  # перебор в пределах от -100 до 100 включительно
#     for _ in range(count[i]):  # если по индексу i в count есть ненулевое значение, оно будет выведено
#         #например count[i] =0 то ни чего не выведет
#         #например count[i] =2 то цифру i выведет 2 раза
#         print(i, end=' ')


# Вложеные циклы
# for i in range(3):                 # *****
#     for j in range(5):             # *****
#         print('*', end='')         # *****
#     print()

# for i in range(3):                 # 00000
#     for j in range(5):             # 11111
#         print(i, end='')           # 22222
#     print()

# for i in range(3):                 # 01234
#     for j in range(5):             # 01234
#         print(j, end='')           # 01234
#     print()

# for i in range(3):                 #
#     for j in range(i):             # 0
#         print(j, end='')           # 01
#     print()

# for i in range(1,10):                  # 1
#     for j in range(1,i+1):             # 12
#         print(j, end='')               # 123
#     print()                            # 1234
#                                        # ....
#                                        # 123456789

# Длинна пароля 3
# from string import printable
#
# for b1 in printable:
#     for b2 in printable:
#         for b3 in printable:
#             print(b1, b2, b3)

# Таблица умножения
# for j in range(1, 10):
#     for i in range (1, 11):
#         print(i,'*',j,'=',i*j,end=' ')
#     print()

# k=0
# for b1 in 'tukva':
#     for b2 in 'tukva':
#         for b3 in 'tukva':
#             for b4 in 'tukva':
#                 for b5 in 'tukva':
#                     for b6 in 'tukva':
#                         rez=b1+b2+b3+b4+b5+b6
#                         if rez[0] in 'tkv' and rez[-1] in 'tkv':
#                             if rez.count('a')+rez.count('u')==2:
#                                 k+=1
# print(k)

# # сумма чисел
# for i in range(1, 100001):
#     x = i
#     s = 0
#     while x > 0:
#         s += x % 10
#         x //= 10
#     print(i, s)

# Найдите сумму всех четырехзначных чисел, сумма цифр каждого из которых равна 20.
# count=0
# for i_1 in range(1,10):
#     for i_2 in range(10):
#         for i_3 in range(10):
#             for i_4 in range(10):
#                 if i_1+i_2+i_3+i_4==20:
#                     a=str(i_1)+str(i_2)+str(i_3)+str(i_4)
#                     count+=int(a)
# print(count)

#
# s = 0
# for i in range(1000,10000):
#     x = 0
#     for j in str(i):
#         x += int(j)
#     if x == 20:
#         s+=i
# print(s)

# лесенку из чисел
# for i in range(1,int(input())+1):      # 1
#     for j in range(1,i+1):             # 12
#         print(j, end=' ')              # 123
#     print()                            # 1234
#

# Постулат Бертрана
# n = int(input())
# count=0
# for p in range(n + 1, n * 2):
#     if p % 2 == 0 and p != 2 or p==1:
#         continue
#     d=3
#     ip=True
#     while d*d<=p:
#         if p%d==0:
#             ip=False
#             break
#         d+=2
#     if ip:
#         count+=1
# print(count)
#
# n = int(input())
# a=0
# for i in range(n+1,n*2):
#     for j in range(2, int (i ** 0.5) + 1):
#         if i%j==0:
#             break
#     else:
#         a+=1
# print(a)


# Перебираем либо а либо б:
# Если перебираем (б):
# a = m - b**2  следовательно  из условия задачи a>=0:
# Если m - b**2 < 0 , то ставим break, далее корней не будет.
# Подставляем (m-b**2)**2+b-n == 0          ====>   k += 1
#
# a**2 + b = n и a + b**2 = n


# Система уравнений
# n, m = map(int, input().split())
# a = 0
# count=0
# while (a ** 2) <= n:
#     b = n - a ** 2
#     if b >= 0 and a + b ** 2 == m:
#         count+=1
#     a += 1
# print(count)

# n, m = map(int, input().split())
# count = 0
# for i in range(n+1):
#     for j in range(m+1):
#         if i**2 + j == n and i + j**2 == m:
#             count +=1
# print(count)

# построения горизонтальных столбчатых диаграмм с помощью символа звёздочки.
# a = list(map(int, input().split()))
# for i in range(len(a)):
#     for j in range(a[i]):
#         print('*', end='')
#     print()

# a = input().split()
# for i in a:
#     print('*' * int(i))


# Сортировка пузырьком
# n = int(input())
# mas = list(map(int, input().split()))
# count = 0
# for run in range(n - 1):
#     for i in range(n - 1 - run):
#         if mas[i] > mas[i + 1]:
#             count += 1
#             mas[i], mas[i + 1] = mas[i + 1], mas[i]
# for i in mas:
#     print(i, end=' ')  # этот цикл можно заменить на print(*mas)
# print()
# print(count)

# Сортировка вставками
# n = int(input())
# mas = list(map(int, input().split()))
# for i in range(1, n):
#     for j in range(i, 0, -1):
#         if mas[j] < mas[j - 1]:
#             mas[j], mas[j - 1] = mas[j - 1], mas[j]
#         else:
#             break
# print(*mas)

# Вложенные списки
# n = int(input())    # матрица размером n x n;
# b = []    # создаётся пустой список
# for i in range(n):    # просчитываются n строк
#     b.append((input().split()))    # считывается строка, через split разбивается на элементы списка (type : str),
#                                    #и одним списком присоединяются к b[] c индексом 0, 1, 2... до n
#     for j in range(n):
#         b[i][j] = int(b[i][j])    #   каждый элемент матрицы приводится к  int,  type: str --> int

# обход по спискам
# a = [
#     [0, 2, 4, 6],
#     [1, 5, 9, 13],
#     [3, 10, 17, 19]
# ]
# for i in a:
#     for j in (i):
#         о+=10  #Не можем менять список
#         print(j, end=' ')
#     print()
# print(a)

# обход по индексам
# a = [
#     [0, 2, 4, 6],
#     [1, 5, 9, 13],
#     [3, 10, 17, 19]
# ]
# for i in range(3):
#     for j in range(4):
#         #a[i][j]+=10 #можем менять список
#         print(a[i][j], end=" ")
#     print()
# print(a)

# обход по индексам в обратном порядке
# a = [
#     [0, 2, 4, 6],
#     [1, 5, 9, 13],
#     [3, 10, 17, 19]
# ]
#
# for j in range(3, -1, -1):
#     for i in range(2, -1, -1):  # если поменять циклы I на J --> местами поменяются строки столбцы
#         # a[i][j]+=10 #можем менять список +10
#         print(a[i][j], end=" ")
#     print()
# print(a)

# посчитать сумму строчек
# a = [
#     [0, 2, 4, 6],
#     [1, 5, 9, 13],
#     [3, 10, 17, 19]
# ]
#
# for i in range(3):
#     s=0
#     for j in range(4):
#        s+=a[i][j]
#     print(s)

# посчитать сумму столбцов
# a = [
#     [0, 2, 4, 6],
#     [1, 5, 9, 13],
#     [3, 10, 17, 19]
# ]
#
# for j in range(4):
#     s=0
#     for i in range(3):
#        s+=a[i][j]
#     print(s)

# заполнить список 0
# a=[]
# n=int(input()) #stroka
# m=int(input()) #stolb
#
# for i in range(n):
#     a.append([0]*m)
# for i in a:
#     print(i)

# заполнить список вручную
# a=[]
# n=int(input()) #stroka
# m=int(input()) #stolb
#
# for i in range(n):
#     b=[]
#     for i in range(m):
#         b.append(int(input()))
#     a.append(b)
# for i in a:
#     print(i)

# квадратные таблици N*N
# a = []
# n = int(input())  # stroka
# for i in range(n):
#     a.append([0] * n)           # заполняем нулями
# ## for i in a:
# ##     print(i)
# for i in range(n):
#     for j in range(n):
#         if i == j:
#             a[i][j] = 10        #обработка
#         elif i > j:
#             a[i][j] = 3
#         else:
#             a[i][j] = 5
# for i in a:                     #вывод таблицы
#     print(i)

# Матрица n * n,
# n = int(input())
# a = [[(int(input())) for j in range(n)] for i in range(n)]
# for i in a:
#     print(i)

# сумма диагонали в квадратной таблице N*N
# a = []
# s = 0
# n = int(input())    # количество строк и столбцов матрицы
# for i in range(n):
#     b = []    # создание пустого списка
#     b = list(map(int, input().split()))    # заполнение списка
#     a.append(b)    # добавление списка в строку матрицы
# for i in range(n):    # обход строк матрицы
#     for j in range(n):    # обход столбцов матрицы
#         if i == j:    # если текущий элемент находится на главной диагонале
#             s += a[i][j]    # суммирование элемента
# print(s)

# a = int(input())
# b = 0
# for i in range(a):
#     s = list(map(int, input().split()))
#     b+=s[i]
# print(b)

# Обход элементов матрицы 1 - с заменой строк на столбцы (транспонирование матрицы)
# n = int(input())  # количество строк и столбцов матрицы
# a = []
# for i in range(n):
#     b = []  # создание пустого списка
#     b = list(map(int, input().split()))  # заполнение списка
#     a.append(b)  # добавление списка в строку матрицы
# for j in range(n):  # обход столбцов матрицы
#     for i in range(n):  # обход строк матрицы
#         print(a[i][j], end=' ')  # вывод матрицы
#     print()

# n = int(input())
# a = []
# for i in range(n):
#     a.append(list(map(int, input().split())))
#
# for j in range(n):
#     for t in range(n):
#         print(a[t][j], end=' ')
#     print()

# Обход элементов матрицы 2 - с заменой строк на столбцы (транспонирование матрицы)
# n = int(input())
# a = []
# for i in range(n):
#     a.append(list(map(int, input().split())))
# for column in range(n-1, -1, -1): # обход столбцов(колонок) матрицы
#     for row in range(n-1, -1, -1): # обход строк(рядов) матрицы
#         print(a[row][column], end=' ')
#     print()
import pprint

'''Обход элементов матрицы - 3
Задана целочисленная матрица, состоящая из N строк и M столбцов. Необходимо обойти элементы этой матрицы
cправа налево сверху вниз и вывести элементы именно в таком порядке в виде таблицы. Программа принимает на вход
два натуральных числа N и M – количество строк и столбцов матрицы.
В каждой из последующих N строк записаны M целых чисел – элементы матрицы.'''

# cправа налево сверху вниз
# a = []  # matrix
# n, m = map(int, input().split())  # kol-vo strok i stolbcov
# for i in range(n):
#     a.append(list(map(int, input().split())))  # добавляем эелементы в матрицу
# for st in range(n):  # обход строк(рядов) матрицы
#     for sb in range(m - 1, -1, -1):  # обход столбцов(колонок) матрицы -->cправа налево сверху вниз
#         print(a[st][sb], end=' ')
#     print()

# cправа налево снизу вверх
# a = []  # matrix
# n, m = map(int, input().split())  # kol-vo strok i stolbcov
# for i in range(n):
#     a.append(list(map(int, input().split())))  # добавляем эелементы в матрицу
# for st in range(n-1, -1, -1):  # обход строк(рядов) матрицы
#     for sb in range(m - 1, -1, -1):  # обход столбцов(колонок) матрицы -->в строке с последнего символа к первому
#         print(a[st][sb], end=' ')
#     print()


# слева направо снизу вверх
# a = []  # matrix
# n, m = map(int, input().split())  # kol-vo strok i stolbcov
# for i in range(n):
#     a.append(list(map(int, input().split())))  # добавляем эелементы в матрицу
# for st in range(n-1, -1, -1):  # обход строк(рядов) матрицы
#     for sb in range(m):  # обход столбцов(колонок) матрицы -->в строке с последнего символа к первому
#         print(a[st][sb], end=' ')
#     print()

# Красивая матрица
# a = [list(map(int, input().split())) for i in range(5)]
# # for i in a:
# #     print(*i)
# for i in range(5):
#     for j in range(5):
#         if a[i][j] == 1:
#             row = i
#             column = j
# print(abs(2 - row) + abs(2 - column))

# a=[]
# for i in range(5):
#     a.append(list(map(int, input().split())))
# for i in a:
#     print(i)
# for j in range(n):
#     for t in range(n):
#         print(a[t][j], end=' ')
#     print()

# Сумма строк и столбцов двумерного массива
# a = []  # matrix
# n, m = map(int, input().split())  # kol-vo strok i stolbcov
# for i in range(n):
#     a.append(list(map(int, input().split())))  # добавляем эелементы в матрицу
#
# for i in range(n):
#     sumst = 0
#     for z in range(m):
#         sumst+=a[i][z]
#     print(sumst,end= ' ')
# print()
# for i in range(m):
#     sumstk = 0
#     for z in range(n):
#         sumstk+=a[z][i]
#     print(sumstk,end= ' ')


# Симметричная ли матрица?
# n = int(input())
# a = []
# s1 = s2 = 0
# for i in range(n):
#     a.append(list(map(int, input().split())))
# # for i in a:
# #     print(i)
# for j in range(n):
#     for t in range(n):
#         if j > t:
#             s1 += a[j][t]
#         elif j < t:
#             s2 += a[j][t]
#     #     print(a[j][t], end=' ')
#     # print()
# if s1==s2:
#     print('YES')
# else:
#     print('NO')

# Состязание 1
# a,b=map(int,input().split())
# s=[]
# q=[]
# for i in range(a):
#     s.append(list(map(int,input().split())))
# for i in range(a):
#         q.append(sum(s[i]))
# print(max(q))
# print(q.index(max(q)))

# Состязание 2
# n, m = map(int, input().split())
# matrix = []
# maxDig = []
#
# for i in range(n):
#     matrix.append(list(map(int, input().split())))
#     maxDig.append(max(matrix[i]))
#
# for i in range(n):
#     if max(maxDig) in matrix[i]:
#         print(max(maxDig))
#         print(i, matrix[i].index(max(maxDig)), sep = ' ')
#         break
# ----------
# n, m = map(int, input().split())
# a = [list(map(int, input().split())) for i in range(n)]
#
# b = [max(i) for i in a]
# print(max(b))
# print(b.index(max(b)), a[b.index(max(b))].index(max(b)))

# Состязание 3
# n, m = map(int, input().split())
# matrix = []
# maxDig = []
#
# for i in range(n):
#     matrix.append(list(map(int, input().split())))
#     maxDig.append(max(matrix[i]))
#
# if maxDig.count(max(maxDig)) == 1:
#     print(maxDig.index(max(maxDig)))
# else:
#     maxSum = []
#     for i in matrix:
#         if max(maxDig) in i:
#             maxSum.append(sum(i))
#         else:
#             maxSum.append(0)
#     print(maxSum.index(max(maxSum)))
# -------------
# a = []
# b = []
# n, m = map(int, input().split())
# for i in range(n):
#   a.append(list(map(int, input().split())))
# for i in range(n):
#   b.append([max(a[i]), sum(a[i])])
#
# print(b.index(max(b)))

# Состязание 4
# n, m = map(int, input().split())
# matrix = []
# maxDig = []
# for i in range(n):
#     matrix.append(list(map(int, input().split())))
#     maxDig.append(max(matrix[i]))
# print(maxDig.count(max(maxDig)))


# Симпатичный узор
# s = []
# yes = 0
# no = 0
# for i in range(4):
#     s.append(list(input()))
# for i in range(3):
#     if s[i] == s[i + 1] or s[i].count('B') >= 3 and s[i + 1].count('B') >= 3 or s[i].count('W') >= 3 and s[i + 1].count(
#             'W') >= 3:
#         print('No')
#         break
#     else:
#         print('Yes')
#         break
# ----------
# s=[[i for i in input()]for j in range(4)]
# q="Yes"
# for i in range(3):
#     for j in range(3):
#         if s[i][j]==s[i][j+1]==s[i+1][j]==s[i+1][j+1]:
#             q="No"
# print(q)
# ---------------
# n, m = 4, 4 #определяем размеры таблицы
# a = [] #создаем пустой список, в который запишем символы "B" и "W"
# answer = 0
# for i in range(n):
#     a.append(list(input())) #заполняем список вложенными списками
# for i in range(n):
#     for j in range(m): #проходим по всем элементам массива
#         if i+1 < n and j+1 < m: #проверяем, чтобы на следующей строчке не вышли за пределы таблицы
#             if a[i][j] == a[i][j+1] and a[i][j] == a[i+1][j] and a[i][j] == a[i+1][j+1]: #если условие выполняется, значит, что есть квадрат 2x2 одного цвета
#                 answer += 1
# if answer > 0:
#     print('No')
# else:
#     print('Yes')

# Миша и негатив
# n, m = map(int, input().split())
# start = [input() for _ in range(n)]
# _ = input()
# finish = [input() for _ in range(n)]
# count = 0
# for row in range(n):
#     for col in range(m):
#         if start[row][col] == finish[row][col]:
#             count += 1
# print(count)

# 10 5
# таблица n = 10*10   -# ( i, j )
# число x = 5

# n, x = map(int, input().split())
# count = 0
# for i in range(1, n+1):  #заполняем список (строки) от 1 до n+1
#     for j in range(1, n+1):   #заполняем список (столбцы) от 1 до n+1
#         if i * j == x:
#             # print(f'{i}*{j}={i*j}')
#             count+=1
# print(count)

# ---------------
# Матчи
# n = int(input())
# matrix = []
# count = 0
#
# for i in range(n):
#     matrix.append(list(map(int, input().split())))
#
# for i in range(n):
#     homeTeam = matrix[i][0]
#     for j in range(n):
#         if i == j:
#             continue
#         elif homeTeam == matrix[j][1]:
#             count += 1
# print(count)
#
# n=int(input())
# a = [list(map(int, input().split())) for i in range(n)]
# count=0
# for i in range(n):
#     for j in range(n):
#         if a[i][0]==a[j][1]:
#             count+=1
# print(count)

# -----------------------
# Морской бой - 2
# n,m=map(int,input().split())#размеры поля
# a,c,b=[],0,[]#a список исходного поля,c кол-во подходящих позиций,b расширенное поле на 1
# for i in range(n):#Ввод исходного поля
#     for j in range(1):
#         a.append(list(input()))
# for i in range(n+1):#Ввод расширенного поля,исходные размеры должны быть на 1 больше!
#     k = list('.' for x in range(m+1))#создается список с кол-вом точек большим на 1 чем у исходного поля
#     b.append(k)#добавляется в расширенное поле
# for i in range(n):#В этом цикле мы присваиваем значение из исходного поля в расширенное
#     for j in range(m):#Не забывайте вводить размеры именно исходного поля,т.е n и m,а не n+1 and m+1!
#         b[i][j] = a[i][j]#Можем присваивать значения,поскольку мы создали список b с уникальными элементами,нельзя просто скопировать их!
# for i in range(n):
#     for j in range(m):
#         if b[i][j] == '.' and b[i+1][j]=='.' and b[i-1][j]=='.' and b[i][j-1]=='.' and b[i][j+1]=='.' :#Наше условие
#             c+=1#Подсчет подходящих позиций
# print(c)

# n, m = map(int, input().split())
# count = 0
#
# a = [input() for i in range(n)]
#
# for i in range(n):
#     for j in range(m):
#         if a[i][j] == '.':
#             if (i - 1 > -1 and a[i - 1][j] == '*') \
#                     or (j - 1 > -1 and a[i][j - 1] == '*') \
#                     or (j + 1 < m and a[i][j + 1] == '*') \
#                     or (i + 1 < n and a[i + 1][j] == '*'):
#                 continue
#             else:
#                 count += 1
#
# print(count)

# ---------------------------------------

# Заполнение змейкой
# n, m = map(int, input().split())
#
# for i in range(n):
#     if i % 2 == 0:
#         print(*list(range(i * m, i * m + m)))
#     else:
#         print(*list(range(i * m, i * m + m))[::-1])
#
# n, m=map(int, input().split())
# for i in range(n):
#     a=[j for j in range(m*i, m+m*i)]
#     if i%2 !=0:
#         a.reverse()
#     print(*a)
#
#
# n, m = map(int, input().split())
#
# a = [[0]*m]*n
# x = 0
# y = 0
#
# for i in range(n):
#     for j in range(m):
#         if i%2 == 0:
#             if i == 0 and j == 0:
#                 print(0, end=' ')
#             elif i != 0 and j == 0:
#                 print(x, end=' ')
#             else:
#                 a[i][j] = x + 1
#                 print(a[i][j], end=' ')
#                 x = a[i][j]
#         else:
#             if j == 0:
#                 print(x+m, end=' ')
#                 y = x + m
#                 x += 2
#             else:
#                 a[i][j] = y - 1
#                 print(a[i][j], end=' ')
#                 y -= 1
#                 x = a[i][j] + m
#     print()
#
#
#
# # a = []
# # count = 0
# # n, m = map(int, input().split())
# # for i in range(n):
# #     tmp = []  # создаем пустой временный список, очищаемый на каждой итерации
# #     if i % 2 == 0:  # если строка имеет чётный номер, то …
# #         for j in range(m):
# #             tmp.append(count)  # …добавляем последовательность во временный список
# #             count += 1
# #             a.append(tmp)  # и ‘’цепляем’’ временный к основному
# #         else:  # если строка имеет нечётный номер, то …
# #             for j in range(m):
# #                 tmp.append(count)  # … добавляем последовательность во временный список
# #             count += 1
# #             a.append(tmp[::-1])  # ‘’разворачиваем’’ список tmp и ‘’цепляем’’ к основному
# #     for i in a:
# #         print(*i)

# --------------------
# Фотографии Брейна
# n, m = map(int, input().split())
# matrix = [input() for i in range(n)]
#
# #print(matrix)
# for row in range(n):
#     if 'C' in matrix[row] or 'M' in matrix[row] or 'Y' in matrix[row]:
#         print('#Color')
#         exit()
# else:
#     print('#Black&White')

# n, m = map(int, input().split())
# a = [input() for i in range(n)]
# c = '#Black&White'
# for i in range(n):
#     for j in range(m):
#         if a[i][j] == 'C' or a[i][j] == 'M' or a[i][j] =='Y':
#             c = '#Color'
# print(c)
# -------------------
# Спираль
# n = int(input())
# mas = [[0] * n for i in range(n)]
# i = 1
# x = 0
# y = -1
# d_row = 0  # -1 0 1
# d_column = 1  # -1 0 1
# lenght = len(str(n**2))
# while i <= n ** 2:
#     if 0 <= x + d_row < n and 0 <= y + d_column < n and mas[x + d_row][y + d_column] == 0:
#         x += d_row
#         y += d_column
#         mas[x][y] = i
#         i += 1
#     else:
#         if d_column == 1:
#             d_column = 0
#             d_row = 1
#         elif d_row == 1:
#             d_row = 0
#             d_column = -1
#         elif d_column == -1:
#             d_column=0
#             d_row=-1
#         elif d_row == -1:
#             d_row=0
#             d_column=1
# for row in mas:
#     for elem in row:
#         print(str(elem).rjust(lenght), end=' ')
#     print()
# ---------------------------------------
# r, c = map(int, input().split())
#     a = []
#     b = []
#     d = []
#     count = 0
#     x = 0
#     y = 0
#     # Ввод таблицы
#     for i in range(r):
#         a.append([0] * c)
#         a[i] = input()
#     # Создаем таблицу в котором строки состоят из столбцов вводной таблицы
#     for j in range(c):
#         b = []
#         for i in range(r):
#             b.append(a[i][j])
#         d.append(b)
#     # Считаем количество строк в которых нет клубник("S")
#     for i in range(r):
#         if "S" not in a[i]:
#             x += 1
#     # Считаем количество столбцов в которых нет клубник("S")
#     # Используем таблицу которую создали чуть раньше
#     for i in range(c):
#         if "S" not in d[i]:
#             y += 1
#     # Считаем и выводим сумму всех седенных частей
#     count = x * c + y * (r - x)
#     print(count)
#
# n, m=map(int, input().split())
# b=0
# s=[]
# for _ in range(n):
#     a=input()
#     if 'S' in a:
#         s.append(a)
#     else:
#         b+=len(a)
#         n-=1
# for j in range(m):
#     c=''
#     for i in range(n):
#         c+=s[i][j]
#     if 'S' not in c:
#         b+=len(c)
# print(b)

# --------------------------
# Треугольник Паскаля
# n = int(input())
# triangle = []
# for i in range(n + 1):
#     triangle.append([1] + [0] * n)
# for i in range(1, i + 1):
#     for j in range(1, n + 1):
#         triangle[i][j] = triangle[i - 1][j] + triangle[i - 1][j - 1]
# for i in range(0, n + 1):
#     for j in range(0, i + 1):
#         print(triangle[i][j], end=' ')
#     print()

# -----------------------------
# Генераторы списков
# [выражение for val in коллекция]
# a = [i for i in range(7)] # число от 0 до 7
# print(a)

# a = [i for i in ('hello')]  #текст
# print(a)

# import  random
# a = [random.randint(-10,10) for i in range(10)] #рандомное число от -10 до 10
# print(a)

# import  random
# a = [random.randint(-10,10) for i in range(10)] #рандомное число от -10 до 10
# print(a)
# a = [elem+1 for elem in a] #увеличим все числа списка (а) на 1
# print(a)

# условные конструкции в генераторах списков
# [выражение for val in коллекция if условие]
# import  random
# a = [random.randint(-10,10) for i in range(10)] #рандомное число от -10 до 10
# print(a)
# b = [elem for elem in a if elem % 2 == 0 and elem % 3 == 0] #четные элементы списка (а) и делящиеся на 3
# print(b)

# несколько чисел через пробел в 1 строку
# a = input().split()
# a = [int(i) for i in a]
# print(a)

# проинициализировать двухмерные списки значением n * m (двухменрная матрица)
# n = 5
# m = 4
# a = [[0] * m for i in range(n)]
# print(a)
# for i in a:
#     print(i)

# двойиные циклы в генераторах
# a = [i*j for i in [2,3,4,5] for j in [1,2,3] if i*j >= 10]
# print(a)
# ____________

# zeroes = [0 for i in range(100)]  #вывести 100 нолей
# print(zeroes)


# a = [i+1 for i in range(int(input()))]   # создайте список [1, 2, 3, ..., n],
# print(a)

# оздайте список, состоящий из делителей введенного числа.
# n = int(input())
# a = [i for i in range(1, n // 2 + 1) if n % i == 0] + [n]
# print(a)
#
# n = int(input())
# l = [i for i in range(1,n+1) if n%i ==0]
# print(l)
#
# [print([i for i in range(1, n + 1) if not n % i]) for n in [int(input())]]


# создайте список, состоящий из нечетных натуральных чисел в интервале [n; n**2]
# n = int(input())
# l = [i for i in range(n, (n ** 2)+1) if i % 2 != 0]
# print(l)

'''Если a<=b необходимо сформировать список квадратов целых чисел на интервале от а до b включительно
и вывести его на экран.
Если же a>b, необходимо сформировать список кубов целых чисел на интервале от a до b включительно,
двигаясь в порядке убывания, и затем вывести его.'''
# a, b = map(int, input().split())
# if a <= b:
#     s1 = [i ** 2 for i in range(a, b + 1)]
#     print(s1)
# elif a > b:
#     s2 = [i**3 for i in range(a, b -1,-1)]
#     print(s2)

# a, b = map(int, input().split())
# if a <= b:
#     print([x ** 2 for x in range(a, b + 1)])
# else:
#     print([x ** 3 for x in range(a, b - 1, -1)])

# a, b = map(int, input().split())
# print([i**2 for i in range(a, b+1)] if a <= b else [i**3 for i in range(a, b-1, -1)])

'''Создайте список первых букв каждого слова из строки st'''
# st = 'Create a list of the first letters of every word in this string'
# print([i[0] for i in st.split()])

# вывести список из первых n заглавных букв английского алфавита
# from string import ascii_uppercase
# print(ascii_uppercase) # выведет строку ABCDEFGHIJKLMNOPQRSTUVWXYZ
# from string import ascii_uppercase
# n = int(input())
# s=[ascii_uppercase[i] for i in range(n)]
# print(s)
#
# from string import ascii_uppercase
# print([ascii_uppercase[i] for i in range(int(input()))])


# список букв:['A', 'BB', 'CCC', 'DDDD', 'EEEEE', 'FFFFFF', ...]
# from string import ascii_uppercase
# print([ascii_uppercase[i]*(i+1) for i in range(int(input()))])

# список, состоящий из слов,  начинающихся с буквы 't' или 'T'
# phrase = 'Take only the words that start with t in this sentence'
# print([i for i in phrase.split() if i[0]== 't' or i[0]== 'T'])

# a = [                       #только фамилии
#     ('Sidorov', 1995),
#     ('Lukov', 2002),
#     ('Petrov', 1991),
#     ('Gorbachev', 1984),
#     ('Kostin', 2000),
#     ('Isaev', 2005),
#     ('Eliseev', 1999),
#     ('Kozlov', 2004),
#     ('Bukov', 1995),
#     ('Gavrilov', 1980),
#     ('Efremov', 2006),
# ]
# #b = [elem[0] for elem in a if elem[0].startswith('E')]  #только фамилии на 'E'
# b = [elem[0] for elem in a if elem[1]>2000]  #только фамилии на год которых больше 2000
# print(b)

# a ='sv6s8cv76sd85s8zxc7v5s8d58sd7f5s6df57sd6f54'
# # b= [i for i in a if i.isdigit()] #только числа из списка
# b= [int(i) for i in a if i.isdigit()] #только целые числа из списка
# # b= [i for i in a if i.isalpha()] #только буквы из списка
# print(b)

# import random
# n = 5
# m = 3
# a = [[random.randint(1, 6) for j in range(m)] for i in range(n)]  #заполнение массива рандомными числами
# for i in a:
#     print(i)

# import random
#
# n = 5
# m = 5
# a = [[random.randint(1, 6) for j in range(m)] for i in range(n)]  # заполнение массива рандомными числами
# for i in a:
#     print(i)
# b = [a[i][j] for i in range(n) for j in range(m) if i == j]  # вывод главной диагонали
# c = [a[2][j] for j in range(m)]   # вывод второй строки
# d = [a[i][3] for i in range(n)]   # вывод третьего солбца
# print('main diagonal', b)
# print('2 stroka', c)
# print('3 stolbec', d)

# Таблица умножения
# n = 5
# m = 5
# a = [[i * j for i in range(1, m + 1)] for j in range(1, n + 1)]  # заполнение массива рандомными числами
# for i in a:
#     print(i)


# на основании vector линейный(одномерный ) список и вывести его
# vector = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]]
# print([j for i in vector for j in i])

# Словари


# a=['moskva', 'piter', 'penza']
#     d={
#     #key:value              #создание словоря 1
#     'moskva': 495,
#     'piter': 812,
#     'penza': 8412
# }
# print(d)

# r = dict(moskva=495, piter=812, penza=8412)  #создание словоря 2
# print(r)
#
# a = [['moskva', 495], ['piter', 812], ['penza', 8412]]   #создание словоря 3
# t= dict(a)
# print(t)

# a = [['moskva', 495], ['piter', 812], ['penza', 8412]]   #создание словоря 4
# t= dict(a)
# q = dict.fromkeys(['a','b','c'],100) #создание словоря 5
# w={}  #создание пустого словоря 6
# e=dict()  #создание пустого словоря 7
# print(e, type(w))
#

# d={
#     1: 'one',
#     2: 'two',
#     3: 'three'
# }
# d[4]='four'   #добавление ключа в словарь
# d[5]='five'
# print(d)
# d[3]='три' #изменение ключа в словарь
# print(d)

# Словарь из строки
# person = {}
# s = 'IVANOV IVAN Samara SGU  5 4 5 5 4 3 5'
# s=s.split()
# person['last_name'] = s[0]
# person['ferst_name'] = s[1]
# person['siti'] = s[2]
# person['universaty'] = s[3]
# person['marks'] = []
# for i in s[4:]:                 #обходим оценки с 4 элемента
#     person['marks'].append(int(i)) #добавляем оценки
# print(person)

# удаление элемента из словаря
# d = {
#     1: 'one',
#     2: 'two',
#     3: 'three'
# }
# print(d)
# del d[1] #удаление
# print(len(d)) #длинна словоря
# print(1 in d, 7 not in d) #есть ли 1 в словаре, нет ли 7 в словаре
# if 4 in d:
#     print(d[4])
# else:
#     d[4]='four'
# print(d)

# обход в цикле for
# d = {
#     1: 'one',
#     2: 'two',
#     3: 'three'
# }
# for key in d:
#     print(key, d[key])  #в key присваивается значение ключа, затем выводится элемент ключа


# Методы у словарей
# d = {
#     1: 'one',
#     2: 'two',
#     3: 'three'
# }
# print(d)
# d.clear() #очищение словаря
# print(d.get(5, 'no such key')) #пытается обратится по ключу к словарю и если не находит выводит "no such key", если найдет выведет на экран ключи значение
# print(d.setdefault(5)) #пытается обратится по ключу к словарю и если не находит создает новый ключ со значением 'None' или которое укажем, если найдет выведет на экран значение ключа
# print(d.pop(2)) #обратится по ключу к словарю, если находит - выводит значение и удаляет ключ из словаря
# print(d.popitem()) #выводит  ПОСЛЕДНИЙ ДОБАВЛЕННЫЙ ключ и значение и удаляет эту пару из словаря
# print(d.keys())     #значение всех ключей словаря
# print(d.values())     #всех значений словаря без ключей
# print(d.items())     #всех пары значений и ключей словаря
# for key, value in d.items():
#     print(key, value)  #вывод через пробел

# оздать словарь, c ключzvb от 1 до n, а значениями соответствующего ключа будет значение ключа в квадрате.
# d = dict()
# for x in range(1,int(input())+1):
#     d[x]=x**2
# print(d)
#
#
# a = int(input())
# rez = {}
# for i in range(1, a+1):
#     rez.setdefault(i, i**2)
# print(rez)

# словарь, где ключи  - строчные английские символы, а значения - порядковые номера букв в алфавите
# from string import ascii_lowercase
# alphabet = {}
# for i in range(len(ascii_lowercase)):
#     alphabet[ascii_lowercase[i]] = i + 1
#
# for k, v in alphabet.items():
#     print(k, v)

# не проходит проверку
# from string import ascii_lowercase
# alphabet={}
# for i in range (26):
#     alphabet[i+1]=ascii_lowercase[i]
# for i in range (26):
#     print(alphabet[i+1],i+1)


# Есть два словаря, нужно их объединить в новый словарь rez и вывести его на экран
# d1 = {'a': 100, 'b': 200, 'c': 333}
# d2 = {'x': 300, 'y': 200, 'z': 777}
# rez = dict()
# rez.update(d1)
# rez.update(d2)
# print(rez)
# -----------------------------------
# Система регистрации
# Создалать пустой словарь.
# Цикл по n:
# принимаем на ввод name
# Если name не в словаре:
# печатаем ОК
# добавляем name:0 в словарь
# иначе:
# изменяем значение ключа: на значение+1
# печатаем (ключ+str(значение))

# logins = {}
# n = int(input())
# for i in range(n):
#     name = input()
#     if name not in logins:
#         logins[name]=0
#         print ('OK')
#     else:
#         logins[name]+=1
#         print(name+str(logins[name]))

#
#
# def fun(names, match_name):
#     j = 1
#     while True:
#         new_name = match_name + str(j)
#         if names.get(new_name):
#             j += 1
#         else:
#             names[new_name] = new_name
#             break
#     return True
#
#
# number = int(input())
# d = {}
# for i in range(number):
#     a = input()
#     if d.get(a):
#         fun(d, a)
#     else:
#         d[a] = 'OK'
# for i in d:
#     print(d.get(i))


'''Программе на вход будет поступать название города в переменную city.
Задача найти какой стране принадлежит введенный город'''

# countries = {
#     "Sweden": ["Stockholm", "Göteborg", "Malmö"],
#     "Norway": ["Oslo", "Bergen", "Trondheim"],
#     "England": ["London", "Birmingham", "Manchester"],
#     "Germany": ["Berlin", "Hamburg", "Munich"],
#     "France": ["Paris", "Marseille", "Toulouse"]
# }
# city = input()
# for para in countries.items():
#     if city in para[1]:
#         print(f'INFO: {city} is a city in {para[0]}')
#         break
# if city not in para[1]:
#     print(f'ERROR: Country for {city} not found')
#
# countries = {
#     "Sweden": ["Stockholm", "Göteborg", "Malmö"],
#     "Norway": ["Oslo", "Bergen", "Trondheim"],
#     "England": ["London", "Birmingham", "Manchester"],
#     "Germany": ["Berlin", "Hamburg", "Munich"],
#     "France": ["Paris", "Marseille", "Toulouse"]
# }
# city = input()
# text = f"ERROR: Country for {city} not found"
#
# for i in countries:
#     if city in countries[i]:
#         text = f"INFO: {city} is a city in {i}"
#
# print(text)


# ИСПОЛЬЗОВАНИЕ СЛОВАРЕЙ

# Подсчет количества объектов
# При таком использовании в словаре ключи будут являться объектами, а значение ключа - количество появления этих объектов.
# s=input()
# d={}
# for i in s:
#     if i.isalpha(): #если i буква
#         # if i in d:
#         #     d[i] += 1             #этот блок можно заменить 1 строкой
#         # else:
#         #     d[i] = 1
#         d[i] = d.get(i,0) +1
# # print(d)  #словарь
# # for i in d:   #вывод ключей
# #     print(i)
# # for i in d:   #вывод ключей и значений через пробел
# #     print(i, d[i])
#
# for i in sorted(d):   #вывод ключей и значений через пробел отсортированный
#     print(i, d[i])

# Замена разряженного списка
# Вместо списка(массива) из большого количества элементов, в котором предполагается, что не все элементы будут использоваться.
# s=input()
# d={}
# for i in s:
#     if i.isalpha(): #если i буква
#         d[i] = d.get(i,0) +1
# print(d)

# Установить соответствие между объектами.
#  - Словарь, как он есть, в общем понимании.
# worlds = {}
# while True:
#     s = input()
#     if s in worlds:
#         print('Слово', s, 'переводится как', worlds[s])
#     else:
#         # translate = input()
#         # worlds[s] += translate
#         print('Введите перевод слова ', s)
#         worlds[s] = input()


#  Хранение данных об объекте.
#  - Вложенные словари.
# contacts = {
#     'John Kenedy': {
#         'berthday': '29 may 1917', "city": 'Brooklin',
#         'phone': None, 'children': 3
#     },
#     'Arnold Shvarc': {
#         'berthday': '30 july 1947', "city": 'Gradec',
#         'phone': '555-55-555', 'children': 5
#     },
#     'Donald Tramp': {
#         'berthday': '14 july 1946', "city": 'New Yerk',
#         'phone': '777-777-77', 'children': 4
#     }
# }
# persons = ['John Kenedy', 'Arnold Shvarc', 'Donald Tramp']

# for person in persons:
#     berthday = contacts[person]['berthday']            #1 способ получить все значения внутри вложенного словаря
#     city = contacts[person]['city']
#     phone = contacts[person]['phone']
#     children = contacts[person]['children']
#     print(person, berthday, city, phone, children)

# persons = ['John Kenedy', 'Arnold Shvarc', 'Donald Tramp']
# for person in persons:                                  #2 способ получить все значения внутри вложенного словаря
#     print(person)
#     for data in contacts[person]:
#         print(data, contacts[person][data])
#
# -----------------------------------
# сколько раз встретилась каждая буква в строке
# s=input().lower()
# d={}
# for i in s:
#     if i.isalpha(): #если i буква
#         d[i] = d.get(i,0) +1
# print(d)  #словарь

# получить значения ключа first_name у всех элементов и вывести их в алфавитном порядке
# data = {'my_friends': {'count': 10,
#                        'items': [{'first_name': 'Kurt', 'id': 621547005, 'last_name': 'Cobain', 'bdate': '31.8.2005'},
#                                  {'first_name': 'Виолетта', 'id': 484200150, 'last_name': 'Кастилио'},
#                                  {'first_name': 'Иринка', 'id': 21886133, 'last_name': 'Бушуева', 'bdate': '28.8.1942'},
#                                  {'first_name': 'Данил', 'id': 282456573, 'last_name': 'Греков', 'bdate': '4.7.2002'},
#                                  {'first_name': 'Валентин', 'id': 184902932, 'last_name': 'Долматов', 'bdate': '25.5'},
#                                  {'first_name': 'Евгений', 'id': 620469646, 'last_name': 'Шапорин',
#                                   'bdate': '6.12.1982'},
#                                  {'first_name': 'Ангелина', 'id': 622328862, 'last_name': 'Краснова',
#                                   'bdate': '4.11.1995'},
#                                  {'first_name': 'Иван', 'id': 576015198, 'last_name': 'Вирин', 'bdate': '2.2.1915'},
#                                  {'first_name': 'Паша', 'id': 386922406, 'last_name': 'Воронов', 'bdate': '27.9'},
#                                  {'first_name': 'Ольга', 'id': 622170942, 'last_name': 'Савченкова',
#                                   'bdate': '20.12'}]}}
#
# a = []
# for i in data['my_friends']['items']:
#     a.append(i['first_name'])
# a.sort()
# print(*a, sep='\n')
#
# first_names = []
# for i in data['my_friends']['items']:
#     first_names.append(i['first_name'])
# for i in sorted(first_names):
#     print(i)

# Анаграмма
# print('YES' if sorted(input()) == sorted(input()) else 'NO')


# Азбука Морзе
# В первом - принимаем на вход строку в нижнем регистре и разбиваем методом split на слова.
# Второй цикл проходит по буквам слова, и если буква есть, то печатает значение:
# (обращается к словарю morze[буква], где буква - это переменная цикла)
# С выводом (print)нужно применить разделение символов sep=' ')
# morze = {'a': '•—', 'b': '—•••', 'c': '—•—•', 'd': '—••',
#          'e': '•', 'f': '••—•', 'g': '——•', 'h': '••••',
#          'i': '••', 'j': '•———', 'k': '—•—', 'l': '•—••',
#          'm': '——', 'n': '—•', 'o': '———', 'p': '•——•',
#          'q': '——•—', 'r': '•—•', 's': '•••', 't': '—',
#          'u': '••—', 'v': '•••—', 'w': '•——', 'x': '—••—',
#          'y': '—•——', 'z': '——••', ' ': ' '}
# s = input()
# for i in s.lower():
#     if morze[i] != ' ':
#         print(morze[i], end=" ")
#     else:
#         print()
# -------------------------
# morze = {'a': '•—', 'b': '—•••', 'c': '—•—•', 'd': '—••',
#          'e': '•', 'f': '••—•', 'g': '——•', 'h': '••••',
#          'i': '••', 'j': '•———', 'k': '—•—', 'l': '•—••',
#          'm': '——', 'n': '—•', 'o': '———', 'p': '•——•',
#          'q': '——•—', 'r': '•—•', 's': '•••', 't': '—',
#          'u': '••—', 'v': '•••—', 'w': '•——', 'x': '—••—',
#          'y': '—•——', 'z': '——••'}
# for i in input().lower().split():
#     for j in i:
#         print(morze[j], end=' ')
#     print()
#


# создать словарь, где ключами будут имена, а значениями словарь из трех ключей: salary, gender и passport
# persons = [
#     ('Allison Hill', 334053, 'M', '1635644202'),
#     ('Megan Mcclain', 191161, 'F', '2101101595'),
#     ('Brandon Hall', 731262, 'M', '6054749119'),
#     ('Michelle Miles', 539898, 'M', '1355368461'),
#     ('Donald Booth', 895667, 'M', '7736670978'),
#     ('Gina Moore', 900581, 'F', '7018476624'),
#     ('James Howard', 460663, 'F', '5461900982'),
#     ('Monica Herrera', 496922, 'M', '2955495768'),
#     ('Sandra Montgomery', 479201, 'M', '5111859731'),
#     ('Amber Perez', 403445, 'M', '0602870126')
# ]
# data = {i[0]: {'salary': i[1], 'gender': i[2], 'passport': i[3]} for i in persons}
# # print(data)
# print(data)
# ---------------------------------------
# person = {}
# person["name"] = 'Neo'
# person["age"] = 42
# person["car"] = 'lada'
# print(person)
# for key, value in person.items():  #перебор по ключу и значению
#     print(key, value)  #вывод ключ и значение
# for key in person: #перебор по ключу
#     print(key) #вывод ключа
# for value in person.values(): #перебор по значению
#     print(value) #вывод значения

# person={
#     'name': 'Neo',
#     'ves': 105,
#     'age': 42,
#     'bludo': ["Pelmeni", "plov", "kolbasa"],
#     'car': 'lada'
# }
# for value in person['bludo']:
#     print(value)
# persons = {
#     'Neo': {
#         'ves': 105,
#         'age': 42,
#         'bludo': ["Pelmeni", "plov", "kolbasa"],
#         'car': 'lada'
#     },
#     'Trinity': {
#         'ves': 75,
#         'age': 40,
#         'bludo': ["Pelmeni", "samsa", "kolbasa"],
#         'car': 'moskvich'
#     },
# }
# for user_name, user_info in persons.items():
#     print(f'Имя пользователя: {user_name}')
#     age = user_info['age']
#     car = user_info["car"]
#     print(f'Возраст {user_name}: {age}')
#     print(f'Машина {user_name}: {car}\n')


# Генераторы словарей
# a = [i for i in range(1, 11)]   #Генераторы списка
# print(a)

# key:value
# a = {i:i**2 for i in range(1, 11)}   # Генераторы словарей
# print(a)

# a = {}
# for i in range(1, 11):
#     a[i] = i**2   # Генераторы словарей
#
# print(a)

# a = {word: len(word) for word in ['hello', 'hi', 'www']}  # Генераторы словарей текст
# print(a)


# обход словаря
# data = {
#     'Джеф Бозес': '177',
#     'Илон МаСк': '126',
#     'бернар АрнО': "150",
#     "Билл ГеитС": "124"
# }
# new_data = {key.title(): int(value) for key, value in data.items()} #быстрый способ

# new_data={}
# for key, value in data.items():                   #ручной способ
#     new_data[key.title()] = int(value)
#
#
# print(data)
# print(new_data)

# users = [
#     [0, 'Bob', "passwoord"],
#     [1, 'code', 'python'],
#     [2, 'Stack', 'overflow'],
#     [3, 'username', '1234'],
#     [51, 'qwerty', '1234'],
# ]
# new_users = {user[0]: user for user in users}
# print(new_users[51])


# при помощи генератора словарей, в котором в качестве ключей будут хранится номера телефонов,
# а значениями будут имена владельцев
# people = [
#     ['Amy Smith', '694.322.8133x22426'],
#     ['Brian Shaw', '593.662.5217x338'],
#     ['Christian Sharp', '118.197.8810'],
#     ['Sean Schmidt', '9722527521'],
#     ['Thomas Long', '163.814.9938'],
#     ['Joshua Willis', '+1-978-530-6971x601'],
#     ['Ann Hoffman', '434.104.4302'],
#     ['John Leonard', '(956)182-8435'],
#     ['Daniel Ross', '870-365-8303x416'],
#     ['Jacqueline Moon', '+1-757-865-4488x652'],
#     ['Gregory Baker', '705-576-1122'],
#     ['Michael Spencer', '(922)816-0599x7007'],
#     ['Austin Vazquez', '399-813-8599'],
#     ['Chad Delgado', '979.908.8506x886'],
#     ['Jonathan Gilbert', '9577853541']
# ]
#
# phone_book = {value: key for key, value in people}
# print(phone_book)

# Кортежи (tuple)  не изменяемый объект
# Создание кортежей
# a = (1, 2, 3, 4, 5)
# a = 1, 2, 3, 4, 5
# a = 1,

# b = tuple(range(5))
# print(b, type(b))
# c = ()
# c = tuple

# a = (1, 2, 3)
# b = (4, 5)
# # print(a + b, b + a)  #сцепление кортежей
# # print(a*2)  #дублирование кортежей
# # print(min(a), max(a))  #min max кортежей
# print(sum(a))  #sum кортежей

# a = (1, 'hello', [5,3,4,2], False, 3)  #внутри кортежа может быть список [5,3,4,2]
# a[2].append(100)   #добавляем в  список новое значение 100
# print(a[2]) #выводим значение списка [5, 3, 4, 2, 100]

# Кортеж нужен - если нам необходима не изменяемость объекта, занимает меньше места в памяти
# a = [1, 'hello', [5, 3, 4, 2], False, 3]
# b = tuple([1, 'hello', [5, 3, 4, 2], False, 3])
# print(a.__sizeof__())  #сколько места в памяти  - 80 bate
# print(b.__sizeof__())  #сколько места в памяти  - 64 bate

# Кортеж может быть ключем словаря
# a = (1, 2, 3)
# b = {}
# b[a] = 'hello'
# print(b)


# a = (1, 2, 3)
# a = list(a)    # Кортеж можно преобразовать в список
# a.append(100)
# a.reverse()
# a = tuple(a)
# print(a, type(a))


# Переверните кортеж my_tuple и распечатайте на экран
# my_tuple = (32, 45, 32, 60, 43, 19, 39, 75, 50, 12, 53, 13, 28, 70, 68, 5, 64, 55, 30, 47, 23, 20, 17, 36, 45, 31, 46, 50, 33, 45, 9, 41, 12, 57, 40, 43, 47, 51, 56, 54, 40, 30, 37, 23, 43, 66, 64, 27, 44, 75, 51, 2, 19, 72, 30, 8, 29, 43, 7, 73, 34, 65, 54, 50, 43, 6, 50, 45, 49, 30, 39, 50, 41, 70, 38, 16, 31, 51, 72, 45, 58, 39, 50, 56, 24, 30, 9, 53, 27, 31, 68, 56, 26, 39, 34, 50, 10, 12, 3, 27)
# my_tuple = list(my_tuple)
# my_tuple.reverse()
# my_tuple = tuple(my_tuple)
# print(my_tuple)
#
# print(my_tuple[::-1]) #еще вариант

# Сохраните в переменной lonely кортеж из одного элемента: 777
# Распечатайте на экран lonely
# lonely = (777,)
# print(lonely)

# my_tuple = (
# 32, 45, 32, 60, 43, 19, 39, 75, 50, 12, 53, 13, 28, 70, 68, 5, 64, 55, 30, 47, 23, 20, 17, 36, 45, 31, 46, 50, 33, 45,
# 9, 41, 12, 57, 40, 43, 47, 51, 56, 54, 40, 30, 37, 23, 43, 66, 64, 27, 44, 75, 51, 2, 19, 72, 30, 8, 29, 43, 7, 73, 34,
# 65, 54, 50, 43, 6, 50, 45, 49, 30, 39, 50, 41, 70, 38, 16, 31, 51, 72, 45, 58, 39, 50, 56, 24, 30, 9, 53, 27, 31, 68,
# 56, 26, 39, 34, 50, 10, 12, 3, 27)
# schetchik = 0
# my_tuple = list(my_tuple)
# for i in my_tuple:
#     if i == 50:
#         schetchik += 1
# print(schetchik)
#
# print(my_tuple.count(50)) #еще вариант
# print(len([i for i in my_tuple if i == 50]))


# вывела через пробел в одной строке значения самого маленького и самого большого элементов кортежа my_tuple.
# my_tuple = (
# -214, 181, -139, 448, -664, -66, 213, 832, 717, -462, -924, -706, -85, -244, -222, -340, -482, -518, -781, 759, -593,
# 905, -354, -377, -141, -742, 383, -381, 109, -639, -480, -810, -686, 892, -612, 696, 993, 791, 631, -493, -218, -829,
# -275, 619, -628, -241, -565, -835, -69, 747, 711, -252, -811, -407, -153, 904, 933, -254, 307, -493, -419, -109, -543,
# 155, -127, 613, -452, -459, 856, 562, 333, -66, -77, -598, -779, -278, 867, 321, -20, -415, -357, 735, -906, -14, -370,
# 453, -630, -736, -830, -917, 32, 422, -895, 198, 284, 472, -986, -964, -73, 29)
# print(min(my_tuple), max(my_tuple))
#
# a = sorted(my_tuple)
# print(a[0], a[-1])  #еще вариант


# среднее арифметическое всех нечетных элементов кортежа my_tuple
# my_tuple = (
#     -214, 181, -139, 448, -664, -66, 213, 832, 717, -462, -924, -706, -85, -244, -222, -340, -482, -518, -781, 759,
#     -593,
#     905, -354, -377, -141, -742, 383, -381, 109, -639, -480, -810, -686, 892, -612, 696, 993, 791, 631, -493, -218,
#     -829,
#     -275, 619, -628, -241, -565, -835, -69, 747, 711, -252, -811, -407, -153, 904, 933, -254, 307, -493, -419, -109,
#     -543,
#     155, -127, 613, -452, -459, 856, 562, 333, -66, -77, -598, -779, -278, 867, 321, -20, -415, -357, 735, -906, -14,
#     -370,
#     453, -630, -736, -830, -917, 32, 422, -895, 198, 284, 472, -986, -964, -73, 29)
# a = []
# my_tuple = list(my_tuple)
# for i in my_tuple:
#     if i % 2 != 0:
#         a.append(i)
# print(sum(a)/len(a))
#
#
# n = [i for i in my_tuple if i % 2 != 0]
# print(sum(n) / len(n))


# Сформировать кортеж, содержащий натуральные числа в интервале [a; b] и вывести его на экран.
# a, b = int(input()), int(input())
# t = tuple(range(a, b + 1))
# print(t)
#
# print(tuple(range(int(input()), int(input()) + 1)))

# Сформировать кортеж, содержащий нечетные натуральные числа в интервале [ n; n**2] и вывести его на экран.
# n = int(input())
# t = list(range(n, (n ** 2) + 1))
# # print(t)
# a = []
# for i in t:
#     if i % 2 != 0:
#         a.append(i)
# a = tuple(a)
# print(a)
#
# n=int(input())
# print(tuple(i for i in range(n, n**2+1) if i%2!=0 ))

# shoplist = ['яблоки', 'манго', 'морковь', 'бананы']
# name = 'swaroop'
## Операция индексирования
# print('Элемент 0 -', shoplist[0])
# print('Элемент 1 -', shoplist[1])
# print('Элемент 2 -', shoplist[2])
# print('Элемент 3 -', shoplist[3])
# print('Элемент -1 -', shoplist[-1])
# print('Элемент -2 -', shoplist[-2])
# print('Символ 0 -', name[0])
## Вырезка из списка
# print('Элементы с 1 по 3:', shoplist[1:3])
# print('Элементы с 2 до конца:', shoplist[2:])
# print('Элементы с 1 по -1:', shoplist[1:-1])
# print('Элементы от начала до конца:', shoplist[:])
### Вырезка из строки
# print('Символы с 1 по 3:', name[1:3])
# print('Символы с 2 до конца:', name[2:])
# print('Символы с 1 до -1:', name[1:-1])
# print('Символы от начала до конца:', name[:])


# 6.5 Множества в Python

# Создание
# a = {1, 2, 3, 1, 2, 3, 1, 2, 3, 4}
# b = {'ha', 'ha', 'ho', 'ha', 'hj', 'ha'}
# c = set('abracadabra')
# d = set([1, 2, 3, 4, 5, 2, 4, 6])
# f = set()
# e = set(range(5))
# print(e)

# a = [1, 2, 3, 1, 2, 3, 1, 2, 3, 4]
# a = list(set(a)) #убираем дубли
# print(a)

# Добавление
# a = {54, 3, 54, 9, 84, 3}
# a.add(112)    #добавление элемента в множество
# a.update([1,2,3])
# a.update('hello')
# a.update(range(118, 125))
# a.update({12,13,15})
# print(a)

# Удаление
# a = {54, 3, 54, 9, 84, 3}
# a.discard(3)
# a.remove(84)
# a.pop()
# a.clear()
# print(a)

# Операции над множествами
# a = {54, 3, 54, 9, 84, 3}
# print(len(a))
# print(4 in a, 7 in a, 23 not in a)
# a = {4, 3, 2, 1}
# b = {3, 4, 5, 6, 7}
# print(a & b)           # нахождение пересечения a и b
# print(a.intersection(b))         # нахождение пересечения a и b
# a &= b            #заменяет значения a пересечением a и b
# a.intersection_update(b)          #заменяет значения a пересечением a и b
# print(a, b)
# print(a | b)         #объединяет значения a и b в 1 множество
# print(a.union(b))          #объединяет значения a и b в 1 множество
# a = a.union(b)        #заменяет значение a объединением a и b
# a|=b            #заменяет значение a объединением a и b
# print(a - b)  # вычитание элементов
# print(b - a)  # вычитание элементов
# b -= a      #вычитаем b - a и присваеваем это значение b
# print(a ^ b)   #симметричяная разность
# for i in a:         #обход множества по значению
#     print(i)

# text = input()
# a = set()
# while text != '':   #вводим текст пока не введем пустую строку
#     slova=text.split()    #разбиваем слова на список
#     a.update(slova)     #добавляем слова в множество а
#     text = input()
# print(len(a))

# Выведите все числа, которые входят как в первый, так и во второй список в порядке возрастания.
# a = set(map(int, input().split()))
# b = set(map(int, input().split()))
# print(*(sorted(a & b)))
#
# print(*sorted(set(input().split()) & set(input().split()), key=int))

# Выведите все числа в порядке возрастания, которые входят в первый список, но при этом отсутствуют во втором.
# print(*sorted(set(input().split()) - set(input().split()), key=int))
#
# a,b = set(input().split()), set(input().split())
# print(*sorted(a - b))


'''Ввод данных
Создание пустого множества
Цикл по символам Если коунт переменной цикла > 1 и переменная цикла цифра (метод исдиджит),
то Переменную цикла добавляем в пустое множество(метод add)
Далее сортируем множество (метод сортед) Если длина множества равна нулю: Печатаем NO Иначе: Печатает множество
(не просто печатаем, а распаковываем его)'''

# Напишите программу, которая выводит все цифры, встречающиеся в символьной строке больше одного раза.
# a = input()
# b = set()
# for i in a:
#     if a.count(i) > 1 and i.isdigit():
#         b.add(i)
# if len(b)>0:
#     print(*sorted(list(map(lambda x: int(x), b))), sep=' ')
# else:
#     print('NO')
#
#
# a = [i for i in input() if i in '0123456789']
# b = set(a)
# for i in b:
#     a.remove(i)
# if a:
#     print(*sorted(set(a)))
# else:
#     print('NO')
#
# a = [i for i in input() if i.isdigit()]
# a = sorted(set([i for i in a if a.count(i) > 1]))
# print(*a + ['NO'][len(a):])

# Удаляет из строки все повторяющиеся символы
# Алгоритм:
# 1.  Ввод строки
# 2. Создаем пустое множество
# 3. Циклом обходим элементы строки
# 4. Если элемента (i) еще не было в пустом множестве - добавляем и выводим, end'ом убираем пустую строку после вывода


# old_list = input()
# new_list = []
# for item in old_list:
#     if item not in new_list:
#         new_list.append(item)
# for i in new_list:
#     print(i,end="")
#
# a = input()
# b = set(a)
# for i in a:
#     if i in b:
#         print(i, end='')
#         b.remove(i)


# Дили Вили Били завели себе аккаунты в одной известной соцсети
# names = ['Дили', 'Вили', 'Били']
# d = {name: set() for name in names}
# for s in iter(input, 'конец'):
#     name, comment = s.split(': ')
#     d[name].add(comment)
# d = {k: len(v) for k, v in d.items()}
# for k, v in sorted(d.items(), key=lambda x: x[1], reverse=True):
#     print(f'Количество уникальных комментаторов у {k} - {v}')
#

# Девушка или Юноша
# a = set(input())
# if len(a) % 2 == 0:
#     print('CHAT WITH HER!')
# else:
#     print('IGNORE HIM!')

# print('CHAT WITH HER!' if len(set(input())) % 2 == 0 else 'IGNORE HIM!')


# Не смешите мои подковы
# Просто 4 минус длина множества от списка от инпут.
# print(5 - len(set(input())))
# print(4 - len(set(input().split())))


# Красивый год
# y = input()
# def checkfun(string):
#     for i in range(len(string) - 1):
#         for j in range(i+1, len(string)):
#             if y[i] == y[j]:
#                 return False
#     return True
# while True:
#     y = int(y)
#     y += 1
#     y = str(y)
#     if not checkfun(y):
#         continue
#     else:
#         print(y)
#         break
#
# y = int(input()) + 1
# while len(set(str(y))) != 4:
#     y += 1
# print(y)


# Антон и буквы
# Выводим принтом (длину(множества(в котором каждая буква из строки(введенной) если буква.islower())))
# print(len({i for i in input() if i.isalpha()}))
#
# a = input()
# b = list()
# if len(a) == 0:
#     print('0')
# else:
#     for i in a:
#         if i.isalpha():
#             b.append(i)
# b = set(b)
# print(len(b))
#
# print(len(set(input()) - set('{ },')))

# Панграмма
# print(['NO','YES',input()][len(set(input().lower()))==26])
#
# z=input()
# text = input()
# s = set(text.lower())
#
# if sum(1 for c in s if 96 < ord(c) < 123) == 26:
#     print ('YES')
# else:
#     print ('NO')
#
# F-строки
# x, y = int(input()), int(input())
# print(f'Точка(x = {x}, y = {y})')

# выводилось только шесть знаков после запятой
# number_pi = 3.141592653589793
# print(f'{number_pi:.6f}')

# выводилось только 2 знака после запятой
# x = float(input())
# print(f'{x:.2f}')

# Запись n:7d говорит, что  переменную n нужно представить в виде целого числа (это знак  d ) и на отображение всего числа выделить 7 знаков
# n = 12345
# print(f'{n:08d}')     #00012345


# n = 12345678912345
# print(f'{n:,d}')        #12,345,678,912,345
# print(f'{n:_d}')        #12_345_678_912_345
# sep = '_'
# print(f'{n:{sep}d}') # вложенная f-строка      #12_345_678_912_345

# print(f'Число\t\tКвадрат\t\tКуб')
# for x in range(1, 11):
#    print(f'{x:2d}\t\t\t{x*x:3d}\t\t\t{x*x*x:4d}')

# Выравнивание
# number = 12345.6789
# print(f"Число {number = }")
# print(f"|{number:=<25}|")
# print(f"|{number:=>25}|")
# print(f"|{number:=^25}|")
# print('-'*25)
# text = "Python 3.10"
# print(f"Строка {text = }")
# print(f"|{text:-<25}|")
# print(f"|{text:!>25}|")
# print(f"|{text:?^25}|")


# пример выравнивания
# APPLES = .50
# BREAD = 1.50
# CHEESE = 2.25
# num_apples = 3
# num_bread = 10
# num_cheese = 6
# price_apples = num_apples * APPLES
# price_bread = num_bread * BREAD
# price_cheese = num_cheese * CHEESE
# str_apples = 'Яблоки'
# str_bread = 'Хлеб'
# str_сheese = 'Сыр'
# total = price_bread + price_cheese + price_apples
# print(f'{"Список покупок":^30s}')
# print(f'{"=" * 30}')
# print(f'{str_apples:10s}{num_apples:10d}\t${price_apples:>5.2f}')
# print(f'{str_bread:10s}{num_bread:10d}\t${price_bread:>5.2f}')
# print(f'{str_сheese:10s}{num_cheese:10d}\t${price_cheese:>5.2f}')
# print(f'{"Total:":>20s}\t${total:>5.2f}')

# Определение и вызов функции. Инструкция def
# def seyHello():
#     print('Hello')
#     print('world')
#     print('and evrybody')
# def square(x):
#     print('Квадрат числа ', x, '=', x**2)
# # seyHello() #главная программа (в ней вызываем функцию)
# # for i in range(1,11):
# #     square(i)
# def multiplay(a,b):
#     print(a*b)
# def even (a):
#     if a % 2 == 0:
#         print(a, 'chetnoe')
#     else:
#         print(a, 'ne chetnoe')
# # multiplay(3, 5) #главная программа (в ней вызываем функцию)
# # multiplay(10, 100)
# for i in range(20, 30):
#     even(i)

# def even(a):
#     if a % 2 == 0:
#         print(a, 'chetnoe')
#     else:
#         print(a, 'ne chetnoe')
# for i in range(20, 30):
#     even(i)


# def factorial(n):
#     pr = 1
#     for i in range(2, n + 1):
#         pr = pr * i
#     print(pr)
# factorial(3)

# if 0.5>1:
#     def primer():
#         print('hello')
# else:
#     def primer():
#         print('HELLO')
# primer()
#
# def primer():
#     print('hello')
# def primer():
#     print('HELLO')
# primer()


# def keanu_reeves():
#     print(f"YOU'RE BREATHTAKING")
# keanu_reeves()

# def say_hello_world(name):
#     print(f'{name} говорит hello world!')

# t= int(input())
# def summa_n():
#     sum = 0
#     for i in range(1, t + 1):
#         sum += i
#     print(f'Я знаю, что сумма чисел от 1 до {t} равна {sum}')
# summa_n()

# def summa_n(t):
#     S = sum(range(1, t + 1))
#     print(f"Я знаю, что сумма чисел от 1 до {t} равна {S}")

'''Напишите функцию check_password, которая проверяет переданный ей пароль на сложность и печатает на экран результат проверки.
Сложным паролем будет считаться комбинация символов, в которой :
Есть хотя бы 3 цифры
Есть хотя бы одна заглавная буква 
Есть хотя бы один символ из следующего набора "!@#$%*"
Общая длина не менее 10 символов'''

# def check_password(password):
#     count_digit = 0
#     count_upper = 0
#     count_spec = 0
#     for i in password:
#         if i.isdigit():
#             count_digit += 1
#         # for i in password:        #можно оходить в 1 цикле
#         if i.isupper():
#             count_upper += 1
#         if i in "!@#$%*":
#             count_spec += 1
#     if count_digit >= 3 and count_upper > 0 and count_spec > 0 and len(password) >= 10:
#         print("Perfect password")
#     else:
#         print("Easy peasy")
#
# check_password("1234asdSA5!%")
# check_password("asdAV@()")
# check_password("asd123A ")
#
#
# def  check_password(p):
#     numbers = [i for i in p if i.isdigit()]
#     char = [i for i in p if i.isupper()]
#     symb = [i for i in p if i in  "!@#$%*"  ]
#
#     print("Pefrect password" if len(numbers) >= 3 and len(char) >= 1 and len(symb) >= 1 and len(p) >= 10 else "Easy peasy")

# def count_letters(fr):
#     k = 0       # strochnye
#     n = 0       # zaglavnye
#     for i in fr:
#         if i.isupper():
#             n+=1
#         if i.islower():
#             k+=1
#     print(f'Количество заглавных символов: {n}')
#     print(f'Количество строчных символов: {k}')
#
# count_letters('Oleg')

# def count_letters(string):
#     upper = [i for i in string if i.isupper()]
#     lower = [i for i in string if i.islower()]
#     print("Количество заглавных символов:", len(upper))
#     print("Количество строчных символов:", len(lower))

# IMPORT TURTLE
# import turtle as t
# from random import *
# t.Screen().colormode(255)
# t.speed(0)
# t.bgcolor((0, 0, 0))
# for i in range(333):
#     t.color(randint(0, 255), randint(0, 255), randint(0, 255))
#     t.left(70)
#     t.forward(i)
# t.done()

# import turtle
# x=100
# def storona1():
#     turtle.forward(x * 2)
#     turtle.left(90)
# def storona2():
#     turtle.forward(x)
#     turtle.left(90)
# def move(x):
#     for i in range(2):
#         storona1()
#         for y in range(1):
#             storona2()
# turtle.speed(1)
# move(x)

# import turtle
#
# turtle.speed(1)
#
#
# def triangle():
#     for i in range(3):
#         turtle.forward(100)
#         turtle.left(120)
#
#
# triangle()

# import turtle
#
#
# def move(x):
#     turtle.forward(x)
#     turtle.left(90)
#
#
# def draw_square(x, y):
#     for _ in range(2):
#         move(x)
#         move(y)
#
#
# def draw_square_color(x, y, color):
#     turtle.color(color)
#     turtle.begin_fill()
#     draw_square(x, y)
#     turtle.end_fill()
#
#
# turtle.speed(1)
# draw_square_color(60, 80, 'red')
# turtle.goto(150, 150)
# draw_square_color(120, 140, 'blue')

# Рисование квадрата
# import turtle
#
# turtle.speed(1)
# turtle.forward(100)
# turtle.left(90)
# turtle.forward(100)
# turtle.left(90)
# turtle.forward(100)
# turtle.left(90)
# turtle.forward(100)
# turtle.left(90)
#
# turtle.goto(150,150)
# turtle.forward(100)
# turtle.left(90)
# turtle.forward(100)
# turtle.left(90)
# turtle.forward(100)
# turtle.left(90)
# turtle.forward(100)
# turtle.left(90)

# # Рисование квадрата
# import turtle
#
#
# def drawSquear():
#     turtle.forward(100)
#     turtle.left(90)
#     turtle.forward(100)
#     turtle.left(90)
#     turtle.forward(100)
#     turtle.left(90)
#     turtle.forward(100)
#     turtle.left(90)
#
#
# turtle.speed(1)
# drawSquear()
# turtle.goto(150, 150)
# drawSquear()

# Рисование квадрата
# import turtle
#
#
# def move():   #движение в перед и поваорот на 90 градусов
#     turtle.forward(100)
#     turtle.left(90)
#
#
# def drawSquear():  #рисование 4 сторон квадрата
#     for i in range(4):
#         move()
#
#
# turtle.speed(1)
# drawSquear()
# turtle.goto(150, 150)
# drawSquear()

#
# # Рисование разных квадратов и цветов
# import turtle
#
#
# def move(a):   #движение в перед и поваорот на 90 градусов
#     turtle.forward(a)
#     turtle.left(90)
#
#
# def drawSquear(a):  #рисование 4 сторон квадрата
#     for i in range(4):
#         move(a)
#
# def drawSquearColor(a, color):  #рисование 4 сторон квадрата с цветом
#     turtle.color(color)
#     turtle.begin_fill()
#     drawSquear(a)
#     turtle.end_fill()
#
# turtle.speed(1)
# drawSquearColor(60, 'red')
# turtle.goto(150, 150)
# drawSquearColor(120, 'blue')


# Рисование прямоугольников разных цветов
# import turtle
# x=100
# def storona1():
#     turtle.forward(x * 2)
#     turtle.left(90)
# def storona2():
#     turtle.forward(x)
#     turtle.left(90)
# def move(x):
#     for i in range(2):
#         storona1()
#         for y in range(1):
#             storona2()
# turtle.speed(1)
# move(x)

# должна n раз распечатать фразу "Just do it" в отдельной строчке
# def repeat_please_n_times(n):
#     for i in range(n):
#         print('Just do it')
# repeat_please_n_times(5)
#

# Инициалы
# объявление функции
# def print_initials(name, surname, middlename):
#     pass
# # считываем данные
# name = input()
# surname = input()
# middlename = input()
# # вызываем функцию
# def print_initials(name, surname, middlename):
#     print(f'{surname.capitalize()} {name[0].capitalize()}.{middlename[0].capitalize()}.')
# print_initials(name, surname, middlename)

# объявление функции
# def print_initials(name, surname, middlename):
#     pass
#
#
# # считываем данные
# name = input()
# surname = input()
# middlename = input()
#
#
# # вызываем функцию
# def print_initials(name, surname, middlename):
#     print(
#         f'{surname.title()} {name[0].title()}.{middlename[0].title()}.')  # переводим 1 буквы слова в верхний регистр, остльные в нижний
#
#
# print_initials(name, surname, middlename)


# Возвращаемое значение функции. Оператор return----------------------------------
# def squear(x):
#     print(x**2)
#
# a = squear(6)  #возвращает 36
# print(a)       #возвращает none


# def squear(x):
#     return (x**2)
#
# a = squear(squear(3)) #квадрат от квадрата X
# print(a)       #просто возвращает x без none

# def squear(x):
#     return (x**2)
#
# def example():
#     print(1)
#     print(2)
#     return 'hello'
#     print(3)
#     print(4)
#
# # example() #выводит принт1 и принт2 до ретерна
# print(example()) #выводит принт1 и принт2 и ретерн

# def example():
#     return 1
#     return 2
#     return 3
# print(example()) #выводит только 1 ретерн

# четное число или нет
# def even(x):
#     if x % 2 == 0:
#         return True
#     # else:
#     #     return False
#     return False    #можно убрать else
# for i in range(1,11):
#     print(i, even(i))

# можно вообще сделать проще
# def even(x):
#     return x % 2 == 0
# for i in range(1, 11):
#     print(i, even(i))

# Число сочетаний Н по К
# def factorial(x):
#     pr=1
#     for i in range(2, x+1):
#         pr=pr*i
#     return pr
#
# def sochetanie(n,k):
#     return factorial(n)/(factorial(k)*factorial(n-k))
#
# print(sochetanie(5,3))

# Площадь и периметр
# def sqAndPer(a,b):
#     return a*b, 2*(a+b)
# square, perimetr = sqAndPer(2,5)
# print(square, perimetr)

# def sqAndPer(a,b):
#     mas=[]
#     mas.append(a*b)
#     mas.append(2*(a+b))
#     return mas
# print(sqAndPer(2,6))


# Функция is_person_teenager принимает на вход возраст человека и возвращает True или False
# def is_person_teenager(x):
#     return 12<= x <= 17

# значение факториала данного числа
# def factorial(x):
#     pr = 1
#     for i in range(1, x + 1):
#         pr = pr * i
#     return pr
#
#
# print(factorial(4))


# Снова НОД
# n = int(input())
# s = [int(input()) for i in range(n)]
# def gcd(a, b):
#     while b > 0:
#         a, b = b, a % b
#     return a
# b = set()
# for j in range(n - 1):
#     b.add(gcd(s[0], s[j + 1]))
# print(min(b))
#
# --------------------
# Сначала определяем НОД для первых двух чисел,  далее ищем НОД для третьего числа и получившегося НОД, и т.д.
# def gcd(a, b):
#     while b > 0:
#         a, b = b, a%b
#     return a
#
# n=int(input())
# a=int(input())
# for i in range(n-1):
#     b=int(input())
#     a=gcd(a, b)
# print(a)
# --------------------
# from functools import reduce
#
# def gcd(a, b):
#     while b > 0:
#         a, b = b, a % b
#     return a
#
#
# nums = [int(input()) for _  in range(int(input()))]
# print(reduce(gcd, nums))

# --------------------

# должна возвращать список из дублей, каждый дубль нужно брать только один раз в том порядке, в котором они встречаются в исходном списке
# def find_duplicate(x):
#     y = []
#     for i in range(len(x)):
#         if x.count(x[i]) >= 2 and y.count(x[i]) < 1:
#             y.append(x[i])
#     return y
# ------------
# def find_duplicate(d):
#     duplicate = []
#     for _ in d:
#         if d.count(_) > 1 and _ not in duplicate:
#             duplicate.append(_)
#     return duplicate


# --------------
# принимает строку символов и возвращает позицию первого уникального символа в строке
# def first_unique_char(x):
#     a = 0
#     for i in x:
#         if x.count(i) == 1:
#             a = x.index(i)
#             break
#         else:
#             a = -1
#     return a

# def first_unique_char(array):
#     for i, num in enumerate(array):
#         if array.count(num) == 1:
#             return i
#     return -1

# def first_unique_char(s):
#     for i in s:
#         if s.count(i) == 1:
#             return s.index(i)
#     return -1


# def format_namelist(slovar):
#     for i in slovar[0]:
#         return  i, i 'и' i


# def format_namelist(dct):
#     lst = []
#     for key in dct:
#         lst.append(key["name"])
#     if len(lst) > 1:
#         lst.insert(-1, "и")
#         return lst[::]
#     if len(lst) == 1:
#         return lst[::]
#     if len(lst) == 0:
#         return ""
#
# print(format_namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ]))

# def format_namelist(names):
#     if len(names) > 1:
#         return '{} и {}'.format(', '.join(name['name'] for name in names[:-1]), names[-1]['name'])
#     elif names:
#         return names[0]['name']
#     else:
#         return ''
#
#
# print(format_namelist([ {'name': 'Bart'}, {'name': 'Lisa'} ]))

# def format_namelist(lst):
#     a = []
#     for i in range(len(lst)):
#         a.append(lst[i]['name'])
#     if len(a) > 1:
#         a.append(a.pop(-2) + " и " + a.pop())
#     return ', '.join(a)
# print(format_namelist([ {'name': 'Bart'}, {'name': 'Lisa'} ]))
#
# def format_namelist(name_list: list='') -> str:
#     """Принимает список словарей, у каждого словаря в списке есть
#     только ключ name.
#     Возвращает отформатированную строку, в которой все имена из списка
#     разделяются запятой кроме последних двух имен, они разделены
#     союзом "и".
#     """
#     return ' и '.join(dict['name'] for dict in name_list).replace(' и', ',', len(name_list) - 2)

# -----------------------------
# r'(?:https?\://)?(?:www\.)?([^\.]+)(?:.+)'
# def domain_name(url):
#     ur=""
#     url = url.replace("https://", "").replace("http://", "").replace("www.", '').replace("https://www.", "").replace("http://www.", "")
#     for i in url:
#         if i.isalpha():
#             ur=ur+i
#         elif i==".":
#             break
#     return (ur)
#
#
# print(domain_name("https://www.asos.com,sdf s"))

# Write a function that when given a URL as a string, parses out just the domain name and returns it as a string.
# #For example: domain_name("https://github.com/AlvisonHunterArnuero") == "github"
# Made with ❤️ in Python 3 by Alvison Hunter - October 22th, 2020
# def domain_name(url:str) -> str:
#     pass
#     #list with the most common protocols to start cleaning the url
#     lst_protocols =['http://','www.','https://','ftp','http://www.']
#     #This is the part that we will extract, typically goes between the
#     # protocol and domain, for example alvisonhunter in www.alvisonhunter.com
#     subdomain = ''
#     #the initial prefix of any Uniform Resource Locator we know of.
#     protocol_type = url
#     #the second or top level domain or this URL, example .com, .org, .edu, .net
#     domain_suffix = ''
#     #First, let's iterate the list to find any of its element on the current URL
#     for el in lst_protocols:
#         #If found, let us extract that part from this string
#         if(url.find(el) != -1):
#             protocol_type = url[len(el):]
#
#         #now that we remove the protocol, let's find the domain
#         domain_suffix = protocol_type.find('.')
#         #if domain is found, let's remove it from the string and add it to subdomain
#         if(domain_suffix != -1):
#             subdomain = protocol_type[:domain_suffix]
#         #If there is no dot, then let's simply return the string that was passed as URL
#         else:
#             subdomain = url
#
#     #Having all the elements ready, the time has come for us to return it to the user
#     print(subdomain)
#     return subdomain
#
# #Time to test these URLs out, my dear Pythonistas and pythoneers!
# domain_name('http://google.com')
# domain_name('http://google.co.jp')
# domain_name('www.xakep.ru')
# domain_name('https://youtube.com')
# domain_name('cornisland')
# domain_name('icann.org')
# domain_name('https://github.com/AlvisonHunterArnuero')

# # ------------
# import re
#
# def domain_name(url):
#     return url.split("www.")[-1].split("//")[-1].split(".")[0]
#
# print(domain_name("http://google.com")) # возвращает "google"
# # -------------------

# def domain_name(url:str) -> str:
#     url = url.replace("http://", "").replace("https://", "").replace("www.", "")
#     return url.split('.')[0]
# print(domain_name('https://github.com/AlvisonHunterArnuero'))

# a = "https://www.ya.ru"
# print(a.strip('https://www.'))  # ----->  ya.ru
# ----------------------------
# def squar(x):
#     print(x,x**2)
# for i in range(1,11):
#     squar(i)


# def function1(a, b):
#     result1 = a + b
#     return result1
#
#
# print(function1(a=2, b=3))


# def name_function2(result1, c):
#     result2 = result1 - c
#     return result2


# print(name_function2(c=1))


# -------------------------------
# def factorial(n: int):
#     pr = 1
#     for i in range(1, n + 1):
#         pr = pr * i
#     return pr
#
# def trailing_zeros(n: int) -> int:
#     count = 0
#     stroka = factorial(n)
#     while stroka > 0:
#         s = stroka % 10
#         if s == 0:
#             count += 1
#         elif s != 0:
#             break
#         stroka //= 10
#     return count

'''# Вычисляем факториал. Переводим результат в str.
Переворачиваем его и переводим в int. Нули теперь находятся спереди и отбрасываются сами.
Переводим обратно в str и сравниваем длины'''

# def factorial(n: int):
#     pr=1
#     for i in range(1,n+1):
#         pr=pr*i
#     return pr
#
# def trailing_zeros(n: int) -> int:
#     x=str(factorial(n))
#     return len(x)-len(x.strip('0'))
# ----------------------------------------
# def trailing_zeros(n: int) -> int:
#     t = str(factorial(n))
#     return len(t)-len(str(int(t[::-1])))
# ----------------------------------
# Docstring
# def add_binary(a, b):
#     '''Возвращает сумму чисел a и b в двоичном виде'''
#     binary_sum = bin(a + b)[2:]
#     return binary_sum

# ------------------------------------
# 7.5 Аннотации
# from typing import List, Dict, Tuple, Optional, Any, Union
#
#
# def add_numpers(a: int, b: Optional[int] = None) -> int:
#     return a + b
#
#
# def list_upper(lst: List[str]):
#     for elem in lst:
#         print(elem.upper())
#
#
# t: Optional[list] = [1, 12]
# d: dict[str, int] = {'a': 100, 'b': 200}
# ferst: int = 100
# second: int = 200
# print(add_numpers(ferst, second))
# print(add_numpers('hello', 'world'))
# print(add_numpers([1, 3, 4], [2, 3, 5]))
# print(add_numpers.__annotations__)
# -------------------------------------------
# '''Функция shift_letter  сдвигает символ letter вперед или назад на заданное значение shift.
# Сдвиг может быть цикличным в пределах от a до z.'''
# def shift_letter(letter: str, shift:int):
#     '''Функция сдвигает символ letter на shift позиций'''
#     # alfavit = 'abcdefghijklmnopqrstuvwxyz'
#     # for i in alfavit:
#     count = ((ord(letter) - 97 + shift) % 26) + 97
#     return chr(count)
#
#
# print(shift_letter('d', 26))
#
# def shift_letter(letter: str, shift: int) -> str:
#     """Функция сдвигает символ letter на shift позиций"""
#     letters ='abcdefghijklmnopqrstuvwxyz'
#     return letters[(letters.index(letter) + shift)%26]
#

# Шифр цезаря

# def cipher(s,n):
# 	if s>26:
# 		s=s%26
# 	caesar=''
# 	for i in n:
# 		if ord(i)>=ord('a') and ord(i)<=ord('z'):
# 			if ord(i)+s>ord('z'):
# 				caesar=caesar+chr((ord(i)+s)-26)
# 			else:
# 				caesar=caesar+chr(ord(i)+s)
# 		elif ord(i)>=ord('A') and ord(i)<=ord('Z'):
# 			if ord(i)+s>ord('Z'):
# 				caesar=caesar+chr((ord(i)+s)-26)
# 			else:
# 				caesar=caesar+chr(ord(i)+s)
# 		else:
# 			caesar=caesar+i
# 	return caesar
#
# def dec(n,s):
# 	if s>26:
# 		s=s%26
# 	caesar=''
# 	for i in n:
# 		if ord(i)>=ord('a') and ord(i)<=ord('z'):
# 			if ord(i)-s<ord('a'):
# 				caesar=caesar+chr((ord(i)-s)+26)
# 			else:
# 				caesar=caesar+chr(ord(i)-s)
# 		elif ord(i)>=ord('A') and ord(i)<=ord('Z'):
# 			if ord(i)-s<ord('A'):
# 				caesar=caesar+chr((ord(i)-s)+26)
# 			else:
# 				caesar=caesar+chr(ord(i)-s)
# 		else:
# 			caesar=caesar+i
# 	return caesar
#
# s=input("Введите ключ - ")
# n=input("Введите текст - ")
#
# #print (dec(int(s),n))
# print (cipher(int(s),n))

# alphabet = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
# key, string = int(input('Введите ключ шифрования\t'))%33, input('Введите строку для шифрования\t')
# [print(chr(ord(i)+key), end='') if (i.isalpha() and ord(i)+key<=ord('z')) else print(chr( ord('a') - 1 + (key - (ord('z') - ord(i)))), end='') if i.isalpha() else print(i, end = '') for i in string]

# def shift_letter(letter: str, shift: int) -> str:
#     """Функция сдвигает символ letter на shift позиций"""
#     letters ='abcdefghijklmnopqrstuvwxyz'
#     return letters[(letters.index(letter) + shift)%26]
#
# llst = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
#         'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
#         's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# def caesar_cipher(letter, shift):
#     '''Шифр цезаря'''
#     ret = ""
#     for x in letter:
#         if x in llst:
#             ind = llst.index(x)
#             ret += llst[ind + shift]
#         else:
#             ret += x
#     return ret#
#
# def shift_letter(letter: str, step: int) -> str:
#     """Функция сдвигает символ letter на shift позиций"""
#     return chr(97 + (ord(letter) + step - 97) % 26)
#
# def caesar_cipher(text: str, step: int) -> str:
#     """Шифр цезаря"""
#     return ''.join(shift_letter(i, step) if i.isalpha() else i for i in text)


# 7.6 Область видимости: локальная, глобальная и встроенная

# def s():
#     # local
#     a, b, c = 1, 2, 4
#     print(a,b,c,)
#
# def q():
#     r,t = 1,5
#     print(r,t)
# s()
# q()

# def s():
#     # local
#     w = 'HELLO'
#     a, b, c = 1, 2, 4
#     print(id(w))
#     print(a, b, c, w)
#
#
# # global
# w = 'hello'
# print(id(w))
# s()
# print(w)

# def s():
#     # local
#     a = 11
#     b = 22
#     c = 33
#     print(a, b, c, 'local')
#
#
# # global
# a=100
# b=200
# c=300
# s()
# print(a,b,c, 'global')

# def s():
#     # local
#     # global a
#     a = 30
# def q():
#     s()
# # global
# a=[1,2,3,4]
#
# s()
# def w(x):
#     return x**2
# abc = w
# print(abc(-7))

# def s():
#     # local
#     abc = 200
#     def q():
#         abs = 'hello'
#         print(abs, 'q')
#     q()
#     print(abc,'s')
# # global
# abc = [1,2,3]
# s()

# MIN_DRIVING_AGE = 18
# def allowed_driving(name, age):
#     if age >= MIN_DRIVING_AGE:
#         print (f'{name} может водить')
#     else:
#         print (f'{name} еще рано садиться за руль')
# allowed_driving('tim', 17)
#
#
# MIN_DRIVING_AGE = 18
#
#
# def allowed_driving(name: str, age: int) -> str:
#     """It decides can you drive."""
#     print(f"{name} может водить" if age >= MIN_DRIVING_AGE else f"{name} еще рано садиться за руль")


# 7.7 Передача аргументов. Сопоставление аргументов по имени и позиции

# def f(a, b):
#     print(id(a), id(b), 'lokal')
#     a = 100
#     b = 200
#     print(id(a), id(b), 'lokal after')
#     # print(a, b, 'local')
#
#
# c = 20
# d = 50
# print(id(c), id(d), 'global')
# f(c, d)
# # print(c, d, 'global')


# def f(a, b, c):
#     print(a, b, c)


# f(1, 2, 3) # позиционный

# f(b=20, c=5, a=10) # по имени

# f(2, c=10, b=20) # #комбинированный вариант


# def f(a='hi', b='hello', c='Неизвестно'):  # значение по умолчанию
#     print(a, b, c)
#
#
# f()  # ->   hi hello Неизвестно
# f(1)  # ->   1 hello Неизвестно
# f(2, 3)  # ->   2 3 Неизвестно
# f(2, 3, 4)  # ->   2 3 4
# f(b=111)  # ->   hi 111 Неизвестно

# def append_to_list(value, my_list):
#     my_list.append(value)
#     print(my_list)
#
# a = [1, 2, 3, 4]
# append_to_list(10, a)
# append_to_list(15, a)

# def append_to_dict(key, value, my_dict=None):
#     if my_dict is None:
#         my_dict = {}
#     my_dict[key] = value
#     print(my_dict)
#
# append_to_dict(10, 100)
# append_to_dict(20, 200)
# append_to_dict(20, 200, {'a':111})

# --------------------------------


# 7.8 *args и **kwargs Python. Передача аргументов в функцию

# a,*b,c = True, 12,3,124,2,45,'sdf',23,'43',2
# print(a,b,c)   #-> True [12, 3, 124, 2, 45, 'sdf', 23, '43'] 2

# s = [4, 10]
# print(list(range(1,5)))  #-> [1, 2, 3, 4]
# print(list(range(*s)))  #-> [4, 5, 6, 7, 8, 9]


# def f(a, b, c, d):
#     print(a, b, c, d)
#
#
# f(1, 2, 3, 4)  #-> 1 2 3 4
# a = ('hello', True, 78, [3, 4, 5])
# f(*a)  #-> hello True 78 [3, 4, 5]

# *args

# def f(*args):
#     print(args, type(args))
#
#
# f(1, 2, 3, 4, 5, 6)  #-> (1, 2, 3, 4, 5, 6) <class 'tuple'>
# f(1, 2)  #-> (1, 2) <class 'tuple'>
# f()  #->() <class 'tuple'>


# def f(*args):
#     s = 0
#     for i in args:
#         s += i
#     return s
#
#
# print(f(1, 2, 3, 4, 5, 6))  # -> 21


# # **kwargs
# def f(**kwargs):
#     print(kwargs)
#
# f(a=1,b=2,c=3)  # -> {'a': 1, 'b': 2, 'c': 3}

# def f(**kwargs):
#     for k,v in kwargs.items():
#         print(k,v)
#
#
# f(a=1,b=2,c=3, name=9)  # ->    a 1
#                                #b 2
#                                #c 3
#                                #name 9


# *args + **kwargs
# def f(*args, **kwargs):
#     print(args, kwargs)
#
#
# f(5,4,3,5,7,7,a=5,b=8, d='hello')        # ->   (5, 4, 3, 5, 7, 7) {'a': 5, 'b': 8, 'd': 'hello'}

# def outPrint(*args, sep='#', end='@'):
#     print(args, sep, end)
#
#
# outPrint(1, 2, 3, 4, 5, sep=90)   # ->  (1, 2, 3, 4, 5) 90 @
# outPrint(1, 2, end=111)   # ->  (1, 2) # 111
# outPrint(1, 2)   # ->  (1, 2) # @


# a = [1, 2, 3, 4, 5]
# print(*a)  # -> 1 2 3 4 5


# принимает произвольное количество аргументов. возвращать количество переданных ей на вход аргументов
# def count_args(*args):
#     return len(args)
#
# print(count_args(1,'2',3,4,[2,3]))
#
#
# def only_one_positive(*args):
#     s=0
#     for i in args:
#         if i > 0: s+=1
#     return s == 1
#
#
# print(only_one_positive(-1, 0, -3, 5, -3))

# функцию print_goods, которая печатает список покупок
# def print_goods(*args):
#     count = 1
#     for i in args:
#         if type(i) == str and len(i)>0:
#             print(f'{count}. {i}')
#             count+=1
#     if count == 1:
#         print('Нет товаров')
#
#
# print_goods(1, True, 'Грушечка', '', 'Pineapple')


# Функция info_kwargs должна распечатать именованные аргументы в каждой новой строке в виде пары <Ключ> = <Значения>
# причем ключи должны следовать в алфавитном порядке.
# def info_kwargs(**kwargs):
#     for i, j in sorted(kwargs.items()):
#         print (f'{i} = {j}')
#
# print(info_kwargs(first_name="John", last_name="Doe", age=33))
#
# def info_kwargs(**kwargs):
#     for key in sorted(kwargs):
#         print(f'{key} = {kwargs[key]}')


# 7.9 Рекурсия в Python. Рекурсивная функция Часть 1

# def rec(x):
#     if x<4:
#         print(x)
#         rec(x+1)
#         print(x)
# rec(1)

# Factorial
# def fact(x):
#     if x ==1:
#         return 1
#     return fact(x-1)*x
# print(fact(4))
# print(fact(10))

# Fibonacci
# def fib(n):
#     if n==1:
#         return 0
#     if n ==2:
#         return 1
#     return fib(n-1) + fib(n-2)
# print(fib(5))
# print(fib(6))
# print(fib(7))

# #Палиндром
# шалаш
# asdffdsa
# '' 'a'
# def palindrom(s):
#     if len(s)<=1:
#         return True
#     if s[0] != s[-1]:
#         return False
#     return palindrom(s[1:-1])
#
# print(palindrom('шалаш'))
#


# a = int(input())
# b = list(map(int, input().split()))
#
# def rec(a):
#     if a > 0:
#         rec(a - 1)
#         print(b[-a], end=" ")
#
# rec(a)


# n=int(input())
# def fib(n):
#     if n==0:
#         return 0
#     if n ==1:
#         return 1
#     return fib(n-1) + fib(n-2)
#
# print(fib(n))
#
#
# def fibonacci(n):
#     if n < 2:
#         return n
#     return fibonacci(n - 1) + fibonacci(n - 2)
#
# print(fibonacci(int(input())))

# def list_sum_recursive(x):
#     if len(x) == 0:
#         return 0
#     if len(x) == 1:
#         return x[0]
#     return x[0] + list_sum_recursive(x[1:])

# Преобразование списка
# def resorted_list(list):
#     new_list = []
#     for i in list:
#         if type(i) is int:
#             new_list.append(i)
#         else:
#             new_list += resorted_list(i)
#     return new_list
# print(resorted_list([1, [2, 3], [4, 5, [6, 7]], [8, [9]], 10]))

# Преобразование списка
# base_list = [1, [2, 3], [4, 5, [6, 7]], [8, [9]], 10]
#
#
# def get_element(base_list, result_list=None):
#     if result_list is None:
#         result_list = []
#     for element in base_list:
#         if type(element) == list:
#             get_element(element, result_list)
#         else:
#             result_list.append(element)
#     return result_list
#
#
# result_list = get_element(base_list)
# print(result_list)


# Добавляет скобки
# def rec(s):
#     if len(s) == 1 or len(s) == 2:
#         return s
#     return s[0] + '(' + rec(s[1:-1]) + ')' + s[-1]
#
#
# s = input()
# print(rec(s))


# функция возведения в степень
# def power(x, n):
#     if n == 0:
#         return 1
#     if n < 0:
#         return 1/power(x,-n)
#     if n % 2 == 0:
#         return power(x, n // 2) * power(x, n // 2)
#     else:
#         return power(x, n - 1) * x
#
#
# x = int(input())
# n = int(input())
# print(power(x, n))

# обход списка и указание вложенности
# a = [1, [3, [2, 3, [4]]], 2, [2, 3, 4, [3, 4, [2, 3], 5]]]
#
#
# def rec(spisok, level=1):
#     print(*spisok, 'level = ', level)
#     for i in spisok:
#         if type(i) == list:
#             rec(i, level + 1)
#
#
# rec(a)

# ----------------------------------------

# Сортировка слиянием (merge sort)
# # функция merge_two_list должна объединить два списка
# def merge_two_list(a, b):
#     c = []
#     i = j = 0
#     while i < len(a) and j < len(b):
#         if a[i] < b[j]:
#             c.append(a[i])
#             i += 1
#         else:
#             c.append(b[j])
#             j += 1
#     if i < len(a):
#         c += (a[i:])
#     if j < len(b):
#         c += (b[j:])
#
#     return c
#
#
# # функция merge_sort должна выполнить сортировку
# def merge_sort(s):
#     if len(s) == 1:
#         return s
#     middle = len(s) // 2
#     left = merge_sort(s[:middle])
#     right = merge_sort(s[middle:])
#     return merge_two_list(left, right)


# print(merge_sort([7, 5, 2, 3, 9, 8, 6]))

# -----------------------------------

# def mergeSort(alist):
#     print("Splitting ",alist)
#     if len(alist)>1:
#         mid = len(alist)//2
#         lefthalf = alist[:mid]
#         righthalf = alist[mid:]
#
#         mergeSort(lefthalf)
#         mergeSort(righthalf)
#
#         i=0
#         j=0
#         k=0
#         while i<len(lefthalf) and j<len(righthalf):
#             if lefthalf[i]<righthalf[j]:
#                 alist[k]=lefthalf[i]
#                 i=i+1
#             else:
#                 alist[k]=righthalf[j]
#                 j=j+1
#             k=k+1
#
#         while i<len(lefthalf):
#             alist[k]=lefthalf[i]
#             i=i+1
#             k=k+1
#
#         while j<len(righthalf):
#             alist[k]=righthalf[j]
#             j=j+1
#             k=k+1
#     print("Merging ",alist)
#
# # alist = [54,26,93,17,77,31,44,55,20]
# mergeSort(alist)
# print(alist)

# Быстрая сортировка (quick sort)
# import random
# def quick_sort(A):
#     if len(A) <= 1:
#         return A
#     else:
#         q = random.choice(A)
#         L = []
#         M = []
#         R = []
#         for elem in A:
#             if elem < q:
#                 L.append(elem)
#             elif elem > q:
#                 R.append(elem)
#             else:
#                 M.append(elem)
#         return quick_sort(L) + M + quick_sort(R)
#
# print(quick_sort([19, 4, 5, 17, 1]))


# def quick_sort(s):
#     if len(s)<=1:
#         return s
#     median=sum(s)//len(s)
#     left=[i for i in s if i<median]
#     center=[i for i in s if i==median]
#     right=[i for i in s if i>median]
#     return quick_sort(left)+center+quick_sort(right)


# 7.11 Рекурсивный обход файлов
# import os
# path = 'C:\\Soft'
#
# print(os.listdir(path))
# for i in os.listdir(path):
#     print(i, type(i), path + '\\'+i, os.path.isdir(path + '\\'+i))
#     # print(i, type(i), path + '\\' + i, os.path.isfile(path + '\\' + i))

# import os
#
# path = 'C:\\Test'
#
#
# def obhod_file(path, level=1):
#     print('level=', level, 'Content:', os.listdir(path))
#     for i in os.listdir(path):
#         if os.path.isdir(path + '\\' + i):
#             print('Спускаемся', path + '\\' + i)
#             obhod_file(path + '\\' + i, level + 1)
#             print('Возвращаемся', path)
# obhod_file(path)

# import os
#
#
# def recursive_search(path, file_name):
#     for i in os.listdir(path):
#         if i == file_name:
#             print('Путь к файлу:', path + '/' + i)
#         elif os.path.isdir(path + '/' + i):
#             recursive_search(path + '/' + i, file_name)
#
#
# path = input()
# file_name = input()
# recursive_search(path, file_name)

# ----------------------------------------
# 7.12 Анонимная функция Lambda
# def s(x):
#     return x**2   # х в степени 2
# print(s(2))

# lambda аргумент_1, аргумент_2: выражение

# r=lambda x: x**2  # х в степени 2
# print(r(4))

# def perimetr(a, b, c):
#     return a + b + c
#
#
# per = lambda a, b, c: a + b + c
# text= lambda : "Hello"
# print(perimetr(2, 3, 4))
# print(per(2, 3, 4))
# print(text())

# Цикл for нельзя обходить lambda, if можно
# def s(x):
#     if x > 0:
#         return "Positive"
#     else:
#         return "Negative"
#
#
# print(s(-1))
#
# t = lambda x: "Positive" if x > 0 else "Negative"
# print(t(-1))
# ----------------

# def f(x):
#     return x % 10


# a = [78, 86, 35, 5, 48, 1253, 868, 31681, 1231, 5000]
# # a.sort(key=f)
# a.sort(key=lambda x: x % 10)
# print(a)

# ----------------------------

# def linear(k,b):
#     return lambda x: x*k+b
#
# graf1 = linear(2,5)
# print(graf1(3))
#
# graf2 = linear(-4,1)
# print(graf2(5))
# -------------------------------

# adding_10 = lambda x: x + 10
# print(adding_10(x))

#
# starts_with = lambda x: x[0] =='W'
# print(starts_with('Winner'))


# 7.13 Вложенные функции в Python

# g = 'grey'
#
#
# def colors(param='r'):
#     y = 'yello'
#     g = 'green'
#
#     def print_red():
#         nonlocal y
#         r = 'red'
#         print(r)
#
#     def print_blue():
#         b = 'blue'
#         print(b)
#
#     if param == 'r':
#         print_red()
#     elif param == 'b':
#         print_blue()
#     else:
#         print('I don know this colors')
#
#
# colors('1')

# 7.14 Замыкания в Python. Closure Python

# def main_func(name):
#     def inner_func():
#         print('Hello my frend', name)
#
#     return inner_func

# -------------------

# def adder(value):
#
#     def inner(a):
#         return value + a
#
#     return inner

# --------------------
# def counter():
#     count = 0
#
#     def inner():
#         nonlocal count
#         count+=1
#         return count
#     return inner

# -----------------------------

# def multiply(value):
#
#     def inner(a):
#         return value * a
#
#     return inner
#
# f_2 = multiply(2)
# print("Умножение 2 на 5 =", f_2(5)) #10
# print("Умножение 2 на 15 =", f_2(15)) #30
# f_3 = multiply(3)
# print("Умножение 3 на 5 =", f_3(5)) #15
# print("Умножение 3 на 15 =", f_3(15)) #45
#
# def multiply(m):
#     _ = lambda x: x * m
#     return _

# 7.15 Замыкания в Python Часть 2

# Задача про таймер:
# def timer(a = perf_counter()):
#
#     def inner():
#         nonlocal a
#         b = perf_counter()
#         c = b - a
#         a = b
#         return c
#     return inner
# -----------------------------
# def averedge_numbers():
#     numbers = []
#
#     def inner(number):
#         numbers.append(number)
#         print(numbers)
#         return sum(numbers) / len(numbers)
#
#     return inner

# ----------------------
# from datetime import datetime
# from time import perf_counter
#
# def timer():
#     # start = datetime.now()
#     start = perf_counter()
#
#     def inner():
#         # return datetime.now() - start
#         return perf_counter() - start
#
#     return inner
# --------------------
# def add (a,b):
#     return a+b
#
# def counter (func):
#     count = 0
#     def inner (*args, **kwargs):
#         nonlocal count
#         count+=1
#         print(f'функция {func.__name__} вызывалаось {count} раз')
#         return func(*args, **kwargs)
#     return inner
# ----------------------------

# 7.16 Декораторы в Python Часть 1

# def decorator(func):
#
#     def inner():
#         print('start decorator...')
#         func()
#         print('end decorator...')
#
#     return inner
#
# def say():
#     print('Hello world')
# def buy():
#     print('Buy world')
#
# say=decorator(say)
# say()
# buy=decorator(buy)
# buy()
# ----------------------------
# def decorator(func):
#     def inner(*args, **kwargs):
#         print('start decorator...')
#         func(*args, **kwargs)
#         print('end decorator...')
#
#     return inner
#
#
# def say(name, surname, age):
#     print('Hello', name, surname, age)
#
#
# say = decorator(say)
# say('Vasya', 'Petrov', 30)

# ------------------------

# def header(func):
#     def inner(*args, **kwargs):
#         print('<h1>')
#         func(*args, **kwargs)
#         print('</h1>')
#
#     return inner
#
# def table(func):
#     def inner(*args, **kwargs):
#         print('<table>')
#         func(*args, **kwargs)
#         print('</table>')
#
#     return inner
#
#
# @header  #   --> say = header(say)
# @table   #   --> say = header(table(say))
# def say(name, surname, age):
#     print('Hello', name, surname, age)
#
#
# # say = table(header(say))
# say('Vasya', 'Petrov', 30)

# ----------------------------------
'''Декоратор text_decor, который оборачивает вызов декорированной функции
фразами «Hello» и «Goodbye!»: фраза «Hello» печатается до вызова,
фраза «Goodbye!» - после'''

# def text_decor(func):
#     def inner(*args, **kwargs):
#         print('Hello')
#         func(*args, **kwargs)
#         print('Goodbye!')
#
#     return inner
# ---------------------------------
'''Напишите декоратор repeater, который дважды вызывает декорированную функцию'''

# def repeater(func):
#     def inner(*args, **kwargs):
#         func(*args, **kwargs)
#         func(*args, **kwargs)
#     return inner
# -------------------------------------

"""Напишите декоратор double_it, который возвращает удвоенный результат вызова декорированной функции"""

# def double_it(func):
#     def inner(*args, **kwargs):
#         return (func(*args, **kwargs)+func(*args, **kwargs))
#
#     return inner
#
# # def double_it(func):
# #     inner = lambda *args: func(*args) *2
# #     return inner
#
###def double_it(func):
###    def _wrapper(*args, **kwargs):
###        return func(*args, **kwargs) * 2
###   return _wrapper
#
#
# @double_it
# def multiply(num1, num2):
#     return num1 * num2
#
#
# res = multiply(9, 4)  # произведение 9*4=36, но декоратор double_it удваивает это значение
# print(res)
# --------------------------------

# 7.17 Декораторы в Python Часть 2

# 8.1 Установка модулей в Python
# import math
# import pprint
# pprint.pprint(math.pi)

# import calendar
# import math
# from math import pi, e, factorial
#
# pprint.pprint(pi)
# pprint.pprint(e)
# pprint.pprint(factorial(5))
# c = calendar.TextCalendar()
# print(c.formatyear(2022))

# ---------------------------------------------------

# 9.1 Чтение и запись данных. Функция open

# file = open(r'C:\Users\Polomoshnov\PycharmProjects\MyPython\111.txt', encoding='utf-8')
# file = open('111.txt', encoding='utf-8')

# print(file.read()) #считать и вывести
# print(file.read(3)) #считать и вывести только 2 первых символа
# print(file.read(3)) #считать и вывести следующие  3 первых символа
# file.seek(0) #возвращение в начало текста
# print(file.read(3)) #считать и вывести опять 3 первых символа

# print(file.readline()) #считать и вывести строку
# print(file.readline()) #считать и вывести следующую строку

# for row in file:    #обход текста по строкам
#     print(row)

# for row in file:
#     for letter in row:    #обход текста по буквам
#         print(letter, end=' ')

# s = file.readlines()  #создать список элементами которого будет строки
# print(s)
#
# file = open('111.txt', 'a+', encoding='utf-8')
# # file.write('Hello World\n')  #не забыть указать 'w' - write(запись)
# # file.write('Hello World\n')
# file.write('Poka World\n')  # указать 'a' - дописать в конец
# file.read()  # указать 'a+' - считать и дописать в конец
#
# file.close()  #закрыть файл
# --------------------------------------------
# Напишите функцию file_read, которая принимает имя файла, и печатает его содержимое.
# def file_read(file_name):
#     file = open(file_name, encoding='utf-8')
#     print(file.read())
#
# def file_read(file_name):
#     print(open(file_name, 'r', encoding='utf-8').read())
#
#
# file_read('111.txt')

# ----------------------------------------------

# Напишите функцию create_file_with_numbers, которая принимает на вход одно целое положительное число - n.
# def create_file_with_numbers(n):
#     file = open(f'range_{n}.txt', 'a+', encoding='utf-8')
#     for i in range(1, n + 1):
#         file.write(str(i) + '\n')
#     file.close()
# create_file_with_numbers(5)

# ----------------------------------------------------
# функция longest_word_in_file, принимает имя файла и внутри его содержимого находит самое
# длинное слово и возвращает его в качестве ответа

# def longest_word_in_file(file_name):
#     file = open(file_name, 'r', encoding='utf-8')
#     max_word=''
#     for line in file:
#         words = line.split()
#         for word in words:
#             word_wihtout_punk = remote_punktuation(word)
#             if len(word_wihtout_punk) >= len(max_word):
#                 max_word = word_wihtout_punk
#
#     return max_word
#
# def remote_punktuation(word):
#     from string import punctuation
#     for punk in punctuation:
#         if punk in word:
#             word = word.replace(punk, '')
#     return word
#
# print(longest_word_in_file('test.txt'))


# from string import punctuation
#
# def longest_word_in_file(file_name):
#     a = open(file_name, encoding='utf-8')
#     x = ''
#     for i in a.read().split():
#         i = i.strip(punctuation)
#         if len(i) >= len(x):
#             x = i
#     return x

# -------------------------------------
# скачать файл, в котором записаны натуральные числа. Ваша задача найти
# количество трехзначных чисел;
# сумму двухзначных чисел;
# def number(file_name):
#     file = open(file_name)
#     count = 0
#     summa = 0
#     for i in file:
#         if 99 < int(i) < 1000:
#             count += 1
#         if 9 < int(i) < 100:
#             summa += int(i)
#     return count, summa
#
#
# print(number(r'C:\Users\Олег\PycharmProjects\MyPython_work\numbers.txt'))

# ----------------------------------------
# 9.2 Контекстный менеджер

# file = open('test.txt', 'w')
# file.write([1,3,3])
# file.close()

# lst = []
# for i in range(10000):
#     # file = open('test.txt', 'w')
#     # lst.append(file)
#     with open('test.txt', 'w') as f:    #менеджер контекста
#         lst.append(f)
#     # file.close()


# менеджер контекста
# with open('test.txt', 'w') as f:
#     f.write('1,3,4')
#     f.write('hello')
# print('end')


# вывод размера папки. (если '.' - текущий каталог где лежит файл,
# '..' - на уровень выше)
# import os
#
# with os.scandir('..') as entries:
#     for entry in entries:
#         print(entry.name, '->', entry.stat().st_size, 'bytes')

# ----------------------------------------
# 9.3 Работаем с JSON в Python. Парсинг JSON, сохраняем JSON в файл

# JSON - JavaScript Object Notation
#
# import json
# from random import randint
# from datetime import datetime
# str_json = """
# {
#     "response": {
#         "count": 5961878,
#         "items": [{
#             "first_name": "Елизавета",
#             "id": 620471795,
#             "last_name": "Сопова",
#             "can_access_closed": true
#         }, {
#             "first_name": "Роман",
#             "id": 614752515,
#             "last_name": "Малышев",
#             "can_access_closed": true
#         }]
#     }
# }"""
# # print(type(str_json))
# data = json.loads(str_json)
# print(type(data))
# print(data["response"]) #получить из словаря "response"
# print(data["response"]['count']) #получить из словаря "count"
# print(data["response"]['items']) #получить из словаря "items"
# for item in data["response"]['items']:
#     print(item['first_name'], item['last_name']) #получить из словаря 'first_name' и 'last_name'
# for item in data["response"]['items']:
#     del item['id']    #удаляем ключ 'id'
#     item['likes'] = randint(100, 200)  #добавляем ключ 'likes' с рандом значением от 100 до 200
#     item['a'] = None  #добавляем пустой ключ 'а' с значением None
#     item['time'] = datetime.now().strftime('%d/%m/%y') #добавляем ключ 'time' с текушим временем
# print(data["response"]['items'])
#
# # new_json = json.dumps(data, indent=2)  #создаем новый файл json с отступами 2
# # print(new_json)
# with open('my_json.json', 'w') as file:  #сохраняем новый файл json
#     json.dump(data.json', 'w') as file:  #сохраняем новый файл json

# with open('my_json.json', 'r') as file:  #открываем файл json
#     data = json.load(file) #сохраняняем json  в  data
# print(data)

# -----------------------------------------------

# # Работаем с JSON в Python. Парсинг JSON, сохраняем JSON в файл
# # JSON - это текстовый формат обменна данными
# # преобразуем в пеновский объект при помощи
# # функция load когда мы считываем файлик json
# # loads когда мы считываем строку в формате json
# # метод damp создаёт файлик
# # метод damps создаёт строку в виде json
# import json
# from random import randint
# from datetime import datetime
# str_json = """
# {
#     "response": {
#         "count": 5961878,
#         "items": [{
#             "first_name": "Елизавета",
#             "id": 620471795,
#             "last_name": "Сопова",
#             "can_access_closed": true
#         }, {
#             "first_name": "Роман",
#             "id": 614752515,
#             "last_name": "Малышев",
#             "can_access_closed": true
#         }]
#     }
# }"""
# print(type(str_json))
#
# data = json.loads(str_json)
# print(type(data))  # проверяем какой тип объекта
# # так как items список можно его обойти циклом for
# for item in data["response"]["items"]:
#     print(item["first_name"], item["last_name"])
#     # этим мы распарсили эту джейсонину
#
# # создаём собственную джейсонину
# for item in data["response"]["items"]:
#     del item['id']  # удаляем один ключ
#     item['a'] = None  # добавляем None в джесоне это будет null
#     item['likes'] = randint(100, 200)  # добавляем словарь лайков
#     item['now'] = datetime.now().strftime('%d/%m/%y')  # нужно преобразовать в одному из пазовых типов который поддерживает джесон
# print(data["response"]["items"])
# # создаём новую джейсонину из нового словарика
# new_json = json.dumps(data, indent=2)  # функция dumps к которой мы передаём объект который хотим превратить в джесон
# print(new_json)
# # очень часто джесон нужно будет сохранять в виде файла
# with open('my.json', 'w') as file:  # создаём файл
#     json.dump(data, file, indent=3) # indent для красоты вывода
#
# with open("my_json", 'r') as file:  # загружаем наши данные из файлика в переменную data
#     date = json.load(file)
# print(data)
#
# --------------------------------------

# import json
# with open('manager_sales.json','r') as file:
#     data = json.load(file)
# total_price=0
# for item in data:
#     summa=sum([i['price'] for i in item['cars']])
#     if summa > total_price:
#         total_price=summa
#         name_manager= item['manager']['first_name']
#         last_name_manager = item['manager']['last_name']
# print(name_manager,last_name_manager,total_price)
# ----------------------------------------------
# import json
#
# with open('group_people.json', 'r') as file:
#     data = json.load(file)
#     maximum = 0
#     max_group = None
#     for group in data:
#         id_group = group['id_group']
#         count = 0
#         for person in group['people']:
#             if person['gender'] == 'Female' and person['year'] > 1977:
#                 count+=1
#         if count > maximum:
#             maximum = count
#             max_group = id_group
#         # print(id_group, count)
#     print(max_group, maximum)

# --------------------------------------------
# import json
#
# with open("Alphabet.json") as f:
#     key = json.load(f)
# with open("Abracadabra.txt", encoding="utf-8") as f:
#     txt = f.read()
# print(txt.translate(txt.maketrans(key)))
# # --------------------
# import json
#
# with open('Alphabet.json') as dict:
#     d = json.load(dict)
#
# with open('Abracadabra.txt') as text:
#     t = text.read()
#
# for i in t:
#     if i in d:
#         print(d[i], end='')
#     else:
#         print(i, end='')

# --------------------------------------
# import json
#
# people = '[{"name": "Haley Whitney", "country": "British Indian Ocean Territory (Chagos Archipelago)", "age": 54}, {"name": "Matthew King", "country": "Colombia", "age": 34}, {"name": "Sean Sullivan", "country": "Mayotte", "age": 40}, {"name": "Christian Crawford", "country": "Russian Federation", "age": 29}, {"name": "Sarah Contreras", "country": "Honduras", "age": 82}, {"name": "Danielle Williams", "country": "Togo", "age": 91}, {"name": "Jonathan Wilson", "country": "Tunisia", "age": 49}, {"name": "Patricia Wilkerson", "country": "Georgia", "age": 22}, {"name": "Zachary Scott", "country": "Brunei Darussalam", "age": 55}, {"name": "Elizabeth Sanchez", "country": "Nauru", "age": 23}, {"name": "Christina Fernandez", "country": "Burundi", "age": 71}, {"name": "Allen Norton", "country": "Montserrat", "age": 79}, {"name": "Scott Arroyo", "country": "Montenegro", "age": 72}, {"name": "Brooke Boyd", "country": "Latvia", "age": 74}, {"name": "Jerry Morrow", "country": "San Marino", "age": 23}, {"name": "Danielle Bradshaw", "country": "Vietnam", "age": 64}, {"name": "Jerry Thompson", "country": "Belgium", "age": 30}, {"name": "Mark Jordan", "country": "Comoros", "age": 89}, {"name": "Joseph Berger", "country": "Cook Islands", "age": 94}, {"name": "Gina Brooks", "country": "Samoa", "age": 51}, {"name": "Walter Duran", "country": "Chad", "age": 67}, {"name": "John Martinez", "country": "Wallis and Futuna", "age": 65}, {"name": "Johnny Glover", "country": "Eritrea", "age": 72}, {"name": "Lindsay Moore", "country": "Liberia", "age": 53}, {"name": "Kimberly Burton", "country": "Nicaragua", "age": 92}, {"name": "Jacqueline Ballard", "country": "Nigeria", "age": 78}, {"name": "Charles Thompson", "country": "Saudi Arabia", "age": 50}, {"name": "Suzanne Roberts", "country": "Serbia", "age": 43}, {"name": "David Decker", "country": "South Africa", "age": 71}, {"name": "Christopher Perez", "country": "Cayman Islands", "age": 49}, {"name": "Debra Hall", "country": "Greece", "age": 13}, {"name": "John King", "country": "Bahamas", "age": 40}, {"name": "Justin Galvan", "country": "Namibia", "age": 19}, {"name": "Jacqueline Berger", "country": "Yemen", "age": 59}, {"name": "Shawn Robinson", "country": "Saint Pierre and Miquelon", "age": 32}, {"name": "Kristen Garcia", "country": "Portugal", "age": 48}, {"name": "Christopher Barry", "country": "French Polynesia", "age": 23}, {"name": "Alejandra Cook", "country": "Egypt", "age": 16}, {"name": "Jill Harrell", "country": "Comoros", "age": 49}, {"name": "Sara Zimmerman", "country": "Brazil", "age": 26}, {"name": "Mrs. Charlene Flores", "country": "New Caledonia", "age": 75}, {"name": "Melissa Crawford", "country": "Lebanon", "age": 17}, {"name": "Larry Wong", "country": "New Caledonia", "age": 6}, {"name": "Brenda Acosta", "country": "Grenada", "age": 48}, {"name": "Latoya Terry", "country": "Saint Martin", "age": 41}, {"name": "Seth Luna", "country": "Sao Tome and Principe", "age": 59}, {"name": "Micheal Adams", "country": "Barbados", "age": 53}, {"name": "Susan Carroll", "country": "Somalia", "age": 64}, {"name": "Douglas Morris", "country": "Thailand", "age": 24}, {"name": "Dennis Wagner", "country": "Zimbabwe", "age": 66}, {"name": "Kristin Johnson", "country": "Niue", "age": 71}, {"name": "Steven Krause", "country": "Turkmenistan", "age": 84}, {"name": "Jared Smith", "country": "Colombia", "age": 46}, {"name": "Lauren Anderson", "country": "Christmas Island", "age": 46}, {"name": "Joshua Spencer", "country": "Russian Federation", "age": 38}, {"name": "Maria Edwards", "country": "Hungary", "age": 78}, {"name": "Anne Lee", "country": "United States of America", "age": 10}, {"name": "James Mckenzie", "country": "Uganda", "age": 43}, {"name": "Joshua Gallegos", "country": "United States Minor Outlying Islands", "age": 27}, {"name": "Paul Herrera", "country": "Kiribati", "age": 17}, {"name": "Veronica White", "country": "Gabon", "age": 88}, {"name": "Michael Hall", "country": "China", "age": 43}, {"name": "Sabrina Thompson", "country": "Chad", "age": 27}, {"name": "Jennifer Archer", "country": "Korea", "age": 45}, {"name": "Christina Simmons", "country": "Israel", "age": 80}, {"name": "Travis White", "country": "Central African Republic", "age": 31}, {"name": "Dennis Hernandez", "country": "Slovenia", "age": 66}, {"name": "Matthew Richards", "country": "Svalbard & Jan Mayen Islands", "age": 34}, {"name": "Stephen Curry", "country": "Finland", "age": 92}, {"name": "Margaret Williamson", "country": "Hong Kong", "age": 86}, {"name": "Mary Estes", "country": "Montenegro", "age": 19}, {"name": "Alex Scott", "country": "Christmas Island", "age": 67}, {"name": "John Andrews", "country": "Bahamas", "age": 68}, {"name": "Jonathan Willis", "country": "Saint Martin", "age": 23}, {"name": "Olivia Campos", "country": "Armenia", "age": 72}, {"name": "Diana Davis", "country": "Azerbaijan", "age": 54}, {"name": "Jack Cummings", "country": "Martinique", "age": 94}, {"name": "Kaitlyn Mcdonald", "country": "Austria", "age": 12}, {"name": "Maria Blake", "country": "Pitcairn Islands", "age": 91}, {"name": "Kelly Thomas", "country": "Ethiopia", "age": 74}, {"name": "John Terrell Jr.", "country": "India", "age": 50}, {"name": "Lindsay Wood", "country": "United Arab Emirates", "age": 72}, {"name": "Matthew Gilbert", "country": "Madagascar", "age": 86}, {"name": "Tanner Johnson", "country": "Congo", "age": 11}, {"name": "Michael Garcia", "country": "Liberia", "age": 45}, {"name": "Nicole Johnson", "country": "Barbados", "age": 54}, {"name": "William Lee", "country": "Lithuania", "age": 59}, {"name": "Jeffrey Coffey", "country": "Faroe Islands", "age": 88}, {"name": "Sandra Freeman", "country": "Philippines", "age": 35}, {"name": "Latoya Maxwell", "country": "Sweden", "age": 12}, {"name": "Darius Blevins", "country": "Thailand", "age": 29}, {"name": "Teresa Newman", "country": "Jersey", "age": 6}, {"name": "Larry Bray", "country": "Brunei Darussalam", "age": 21}, {"name": "Adam Roberson", "country": "Jordan", "age": 71}, {"name": "Michael Gomez", "country": "Tajikistan", "age": 37}, {"name": "Abigail Mccarthy", "country": "Kiribati", "age": 85}, {"name": "Tom Morris", "country": "Cayman Islands", "age": 27}, {"name": "Kevin Wagner", "country": "Suriname", "age": 55}, {"name": "Peggy Bryant", "country": "Korea", "age": 36}, {"name": "Erik Mclaughlin", "country": "Austria", "age": 24}]'
# lst = json.loads(people)
# lst = sorted(lst, key=lambda x: (x['age'], x['name']))
# for i in lst:
#     print(f'{i["name"]}, {i["country"]}, {i["age"]}')
# -------------------
# [print(f'{i["name"]}, {i["country"]}, {i["age"]}') for i in
#  sorted(json.loads(people), key=lambda x: (x["age"], x["name"]))]


# # 10.1 Выражения-генераторы
#
# Выражение генератор это почти тоже самое что и генератор списков, отличия лишь в скобках
# Выражение генератор это – итератор обьекты которого можно обойти только один раз.
# Итератор это обьект который поддерживает функцию next()
# a = (i for i in range(1, 6))
# print(next(a)) – выведется 1, данное выражение мы можем написать только 5 раз после чего уже не получится так как элементы генератора можно обойти только один раз.
# Можно генератор обойти циклом for:
# for i in a:
#      print(i) -  Второй раз обойти уже не получится.
# Можно найти сумму элементов генератора: print(sum(a))
# Почему нельзя обойти второй раз? Потому-что элементы генератора попросту не хранятся в памяти.
# Где это может пригодиться? Например если нужно сделать итератор с очень большой цифрой например 100000000
# Такое большое число запихнуть в список через range() – не получится ибо выйдет ошибка memoryError
# Но решение проблемы есть! – Генератор.
# a = (i for i in range(1000000000)) – и никаких ошибок.
# a = (i for i in range(10)) – его можно преобразовать в список:
# print(list(a)) – [0,1,2,3,4,5,6,7,8,9] – список из генератора.
# a = [(i for i in range(10))] – из этого список не выйдет.

# 10.2 Функция генератор. Создание генератора при помощи yield

# Давайте вспомним как работает обычная функция
#
# def generator():
#      return [1,3,4,5]
#
# при вызове функции generator() – нам разом вернется список [1,3,4,5], но функция генератор
# представляет из себя функцию которая запоминаем на каком обьекте происходила итерация и возвращает
# элементы по одному.
# Чтобы написать такую функцию смотрите ниже:
#
# def generator():
#      for i in range(1,6):
#            yield i – yield это ключевое слово для генератора
#
# давайте сохраним функцию в переменную а:
# a = generator()
# Теперь мы можем обращаться к нашей переменной а (которая хранит функцию генератор) через функцию next
#
# print(next(a)) – такой вызов будет возвращать по одному элементу из указанных в функции range(1,6)
#
# Так как эта функция – генератор. Элементы ее можно обойти только один раз!
# Еще раз о ключевом слове yield – Она в буквально смысле замораживает функцию на том месте где она вызывалась и если у вас после нее есть код то он выполнится только при следующем вызове функции:
#
# def sayGenerator():
#     a = 'like'
#         for i in range(5):
#              yield i
#                  print(a)
#
# a = sayGenerator() – сохраняем функцию в переменную а
# print(next(a)) – при первом вызове мы выполним итерацию цикла for и выведется цифра 0
# print(next(a)) – это второй вызов и так как в первом вызове мы вывели число с цикла for а после него шло ключевое слово yield – оно заморозило фунцию и при втором вызове фунцию продолжит выполнять код уже после выполнения первой итерации цикла – тоесть выведется like
# Где такая функция генератор может понадобится?
# Например мы делаем функцию factorial которая находит факториал числа от 2 до n – n укажет пользователь.
# Факториалы мы будем записывать в список и вернем их сразу.
#
# def factorial(x): – факториал с аргументом х – от 0 до x+1
#          pr = 1 – переменная в которой будут считаться факториалы.
#          a = [] – список в котором будут храниться факториалы
#          for i in range(2, i+1): почему с двух? Умножать 1 на 1 нет смысла.
#              pr = pr * i – записываем в пр факториал.
#              a.append(pr) – записываем факториал в список
#          return a – возвращаем все факториалы числа x
#
# Теперь фунция вернет список в котором хранятся факториалы числа x.
# Но этот список будет занимать место в памяти. И это можно решить функцией генератором
#
# def factorialGenerator(x): – функция генератор факториал.
#     Pr = 1 – переменная в которую записывается факториал
#        for i in range(2, x+1): обходим все цифры от 2 до х + 1
#           pr = pr * i – записываем факториал в pr
#              yield pr – возвращаем факториал i числа.
#
# Теперь наша функция будет возвращать факториал от 2 до x и она итерабельна, тоесть можно к ней вызывать функцию next.
# И самое главное она не занимает места в памяти.

# -------------------------------------

# 10.3 Функция map Python
# class map(object)
#   map(fuc, *iterables) --> map object
# map object - представляет собой итератор который вычисляет результат работы функции которую вы передали
# на каждый аргумент из этой последовательности

# a = [-1, 2, -3, 4, 5]
# b = list(map(abs, a))  # вворачиваем в вызов функции list
# print(b)  # <map object at 0x7f431d2a5fa0>
# # другой способ написания этой программы
# c = [abs(i) for i in a]
# print(c)  # [1, 2, 3, 4, 5]


# так же мы можем передавать функции которые сами создали

# def f(x):
#     return x ** 2
#
#
# t = [-1, 2, -3, 4, 5]
# e = list(map(f, t))  # передали нашу созданную функцию f
# print(e)  # [1, 4, 9, 16, 25]
# # пример со строками
# s = ['hello', 'hi', 'helloworld']
# n = list(map(len, s))
# print(n)  # [5, 2, 10]
# # в качестве функции мы можем передавать не только встроенные и самописные функции но и методы этих объектов
# s = ['hello', 'hi', 'helloworld']
# n = list(map(str.upper, s))
# print(n)  # ['HELLO', 'HI', 'HELLOWORLD']
# # так же в функцию мап можно передавать анонимную функцию
# s = ['hello', 'hi', 'helloworld']
# n = list(map(lambda x: x[::-1], s))
# print(n)  # ['olleh', 'ih', 'dlrowolleh']
# o = list(map(lambda x: x + '!', s))
# print(o)  # ['hello!', 'hi!', 'helloworld!']
# # так же можно строку переобразовать в список
# p = list(map(list, s))
# print(p)  # [['h', 'e', 'l', 'l', 'o'], ['h', 'i'], ['h', 'e', 'l', 'l', 'o', 'w', 'o', 'r', 'l', 'd']]
# m = list(map(sorted, p))  # сортируем список p
# print(m)
#
# k = map(int, input().split())  # что вводить неопределённое количества чисел через пробел
# print(k)

# ----------------------------------------------------
# программа, которая возводит в квадрат и в куб каждое число из списка numbers
# пользуясь при этом функциями map и lambda.
#
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list(map(lambda x: x**2, numbers)))
# print(list(map(lambda x: x**3, numbers)))

# -----------------------------------------

# 10.4 Функция filter

# Функция filter похожа на функцию map, она также первым аргументом принимаент функцию а вторым итерабельную последовательность – результатом будет являться обьект filter
# Будем работать со списком а:
#
# a = [14, 0, 5, 79, 645, 7952, 18, 0, 192, 471]
#
# Также создадим функцию в аргумент которого по очереди будут поступать элементы списка а:
# def f(x):
#     if x > 10: - если x больше 10ти, возвращаем Тру
#            return True
#     else: - В противном случае возвращаем фолс
#          return False
#
# b = filter(f, a) – в переменную суем функцию filter первым аргументом которому передаем нашу функцию f, вторым список
#
# Сейчас переменная b представляет из себя обьект filter, посмотреть это можно так:
#
# print(type(b)), Вывод = <class 'filter'>
#
# Чтобы вывести то что вернула нам функция filter нужно ее обернуть в список.
#
# b = list(filter(f, a)), print(b)
#
# Вывод: [14, 79, 645, 7952, 18, 192, 471] – вернулись все цифры больше 10ти.
#
# Напишем функцию которая возвращает элемент если он делится без остатка на два, тоесть четный.
#
# def f(x):
#    return x % 2 == 0
# b = list(filter(f, a)), print(b)
#
# Вывод: [14, 0, 7952, 18, 0, 192] – Вернулись все четные цифры.
#
# Функция которая возвращает только 1-разрядные числа.
#
# def f(x):
#    return x >= 0 and x <= 9
#
# Тоесть числа от 0 до 9 являются 1-разрядными(числа с длиной 1)
#
# b = print(list(filter(f, a))), print(b)
#
# Вывод: [0, 5, 0] – вернулись все 1-разрядные числа.
#
# Можно эту функцию заменить генератором списков:
#
# b = [i for i in a if i >= 0 and i <= 9]
# print(b) - Вывод такойже
#
# В filter можно передавать не только самописные функции но и уже имеющиеся, но важно чтобы функция возвращала либо True либо False – одна из таких является функция bool() которая возвращает Тру если число не является пустым множеством(0)
#
# b = list(filter(bool, a)), print(b)
#
# Вывод:  [14, 5, 79, 645, 7952, 18, 192, 471] – все числа не являющиеся нулем
#
# В функицю filter также можно передавать анонимные функции(lambda), Функция должна возвращать True or False
#
# b = list(filter(lambda x: x % 3 == 0, a)) – функция lambda в которую аргументом x поступают по очереди элементы списка а и если элемент делиться на 3 без остатка, возвращается элемент.
#
# Вывод: [0, 645, 18, 0, 192, 471] – делятся на 3 без остатка
#
# Также первым аргументом в функцию filter можно передавать методы:
# Создадим переменную а со строкой внутри которой элементы(числа и буквы.)
#
# a = '13opj13i4h[1o'
# b = list(filter(str.isdigit, a)) – передаем аргументом строку которая проверяется методом isdigit() – тоесть isdigit возвращает тру если элемент является числом.
#
# Вывод: ['1', '3', '1', '3', '4', '1'] – все числовые элементы.
#
# Тоже самое можно проделать с isalpha() – который возвращает True если элемент является буквой.

# ----------------------------------------

# отфильтрует список numbers так, чтобы в нем остались только четные значения

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list(filter(lambda x: x % 2 == 0, numbers)))

# --------------------------------------
# При помощи функций filter и len определить сколько в этом списке отрицательных значений,
# сколько нулей и сколько положительных

# numbers = [54, 71, 65, 51, 36, -82, -32, 61, -61, 92, 17, -68, -62, 40, 16, -49, -51, -38, 60, -24, -61, 3, -26, -46,
#            -97, -28, 36, 7, 52, 56, -96, -69, 67, 76, 16, 36, 38, 74, 11, -87, 69, 69, -69, -61, 92, 67, -45, -26, 94,
#            38, 27, -26, 10, 55, 28, -81, 53, -75, -32, -83, 38, 83, -40, -51, 88, 28, 76, 25, 84, -79, -69, -65, 6, 12,
#            81, -58, -92, 44, -41, 60, -14, -65, 7, 64, -40, -25, -91, -23, -19, -40, -4, 36, 38, 28, -27, -28, 72, 47,
#            -95, 47, 10, 31, 62, -75, 22, -34, 44, -62, -30, -41, 19, -13, 30, -11, -54, -46, -80, -57, -60, 72, -49, 84,
#            5, 66, 62, -35, 69, 23, 41, -15, 75, -53, 94, -76, -28, -41, -17, 71, 67, -50, 18, 65, -16, -27, -88, 21,
#            -42, 58, 85, 36, 9, -72, -26, -73, -1, 41, -87, 85, 5, -92, -60, -33, 33, -74, 17, 47, -38, -95, -39, 64, 85,
#            -27, -42, -91, -39, -15, -75, 78, -54, 26, -10, -3, 89, -11, -71, -85, 63, 9, -59, 72, 27, 40, 99, -9, 77,
#            64, -39, -28, 73, -50, -80, -74, 52, 26, 53, -18, 22, 70, 85, 1, -90, 53, -19, -80, -14, -29, -64, -21, 23,
#            99, 15, -52, 66, 30, 82, -81, -30, -68, 30, -25, -63, 33, 1, 0, 84, 18, -35, 31, -34, 10, 48, -37, -41, -94,
#            -1, -14, -87, -37, -6, 48, 38, 33, -13, 71, -81, 45, -63, 52, -35, 34, -88, -82, -7, -92, -22, 96, -28, 0,
#            21, 74, -28, 81, 81, 44, -16, 17, -95, 18, -73, 15, -61, 6, -43, -67, -31, -61, -72, -66, 60, 67, -13, 47,
#            29, 44, -93, 55, -13, -23, 74, 79, 32, -20, 33, 17, -48, 7, 24, 19, 89, -60, 34, 81, 18, -39, 56, 10, -32,
#            46, -33, -75, -99, -37, -23, 59, -33, -1, 75, -65, 92, 80, 51, -59, -28, -22, -47, -1, 28, -85, 1, 23, -15,
#            -66, -97, -25, 7, 17, -87, -60, 14, -70, 88, 20, 40, -89, 38, -41, -97, 76, 80, 43, 22, -72, -38, 47, -2, 12,
#            58, -91, 82, -98, 50, 15, -33, -56, 69, -27, 94, -90, 92, -71, -73, -71, -78, 22, -86, -48, 10, 46, 19, 68,
#            -23, 52, -42, 74, 44, 89, -71, 93, 43, -86, 79, 3, -56, 14, 41, 15, -37, 77, -9, 36, 51, -89, 1, 37, 82, 27,
#            72, -92, 91, 94, 71, -81, -49, -42, 26, 57, -30, -40, 86, -77, -85, 1, 71, 16, 73, -82, 26, -90, 72, 14, -65,
#            -55, 34, 45, 66, -64, -40, 92, 42, -78, -22, 53, -18, -41, -75, 10, -59, -55, 8, -90, -3, -65, 43, -49, -86,
#            -96, 69, 48, 27, -48, -42, -34, -6, 7, 50, -55, -65, 79, 30, 16, -21, -98, -73, -25, -20, -51, 20, 17, -91,
#            34, 96, 12, 13, -58, -73, -82, 19, -48, -61, 57, 96, 74, 34, -63, 38, -27, -12, -24, 94, -25, -10, -41, 53,
#            -13, 16, -21, 24, 96, 95, 58, 83, 10, 42, -11, -33, 10, 38, -6, -66, -40, -36, -99, -55, 37, -81, -93, 67,
#            -77, -3, 77, 25, 38, -16, 21, -82, 77, 95, 73, 9, 94, -27, -21, -33, -90, 31, 98, 28, -63, 75, 53, -17, -1,
#            6, 51, 11, -92, 30, -24, 12, 47, -75, -15, -63, 57, 3, 37, -82, -28, -26, -3, -30, -90, -45, 20, -41, 72,
#            -42, 15, -3, 92, 57, -1, 40, -65, 88, 28, -76, 52, -63, -51, 59, 69, -39, -47, -1, -18, -57, 68, 77, 66, 62,
#            -71, 31, -50, 61, 88, 98, 5, 98, -57, -46, 2, 90, 43, 67, 76, -81, -57, 77, 25, -66, -81, -92, -76, 72, 14,
#            59, 52, 36, 20, -2, 92, 58, 36, -34, 94, -74, 42, -56, 96, -81, 69, -83, 71, -13, -13, 56, 86, -29, 58, -17,
#            65, 70, 74, 28, 8, 91, 51, 79, -57, -86, 5, -37, -67, -28, 56, 65, -90, 97, -20, 81, -85, -45, 46, -74, 76,
#            -75, -7, 74, 82, 56, 14, -43, 20, -48, -99, 19, -39, -66, 44, -75, 24, -5, -70, 85, -12, 20, -85, -69, -26,
#            -57, 28, -96, 42, -56, 13, 80, -48, 59, 11, -30, 4, -96, 58, 41, -2, -84, -51, 52, -69, 37, 60, -12, 48, -5,
#            -48, 29, -62, 42, 15, 16, 65, 60, 43, -53, 4, 50, -21, 1, -21, -42, -57, -21, -50, -67, 77, -22, -5, 59, -67,
#            86, -77, 39, -67, 41, 83, -21, 33, 73, 55, 80, 93, 44, -71, 38, -93, 4, 83, -52, 75, -51, 1, -11, -45, 56,
#            81, 84, 70, 23, -36, -63, 69, 1, 86, -21, 53, -85, 70, -89, -31, -10, -94, -76, -17, -21, -60, 49, -22, -48,
#            67, 21, 18, 89, 20, 73, -43, -17, -52, 36, -21, 6, -37, -98, 94, 56, 31, 99, 86, 65, -19, -67, 46, 20, -29,
#            -88, -54, 88, -12, -69, 17, 83, -94, 21, 59, -99, 70, -54, -35, 2, 58, 93, 1, -35, -44, 47, 40, 55, 10, -15,
#            -96, -42, 10, -83, -82, -26, 48, 78, -72, 56, -99, -36, 25, 76, -3, -95, -38, -24, 96, 82, 7, 84, 46, 8, 93,
#            -52, -86, 87, -85, -81, 52, -67, 52, -45, -93, -69, 60, -83, -20, -14, 80, -36, 62, -78, 3, -61, 51, 48, 73,
#            92, -65, 71, -86, 8, -14, 82, 58, -58, -21, 62, -38, 16, 20, -80, -78, 19, 19, 93, -83, 2, 71, 85, 71, -4,
#            81, 4, 90, 73, 21, -3, -55, 49, 66, -4, -6, 42, 76, -3, -94, 49, 55, -53, 12, 1, -25, 56, 93, -68, -21, 15,
#            -13, 35, 71, -68, 34, -44, 48, 97, 51, 32, 87, 27, -85, -41, -27, 54, -91, -99, 83, -44, 70, -87, -76, 49,
#            99, 38, 15, 75, -54, -59, 22, 80, 49, -63, 8, -46, 97, -4, -92, -47, -20]
# print((len(list(filter(lambda x: x < 0, numbers)))), (len(list(filter(lambda x: x == 0, numbers)))),
#       (len(list(filter(lambda x: x > 0, numbers)))))
#
# print(*[len([*filter(eval(f'lambda x: x {a} 0'), numbers)]) for a in ['<', '==', '>']])
# print(*[len(list(filter(fnc, numbers))) for fnc in [lambda x: x < 0, lambda x: x == 0, lambda x: x > 0]])


# ---------------------------------------------------------

# программа, которая отфильтрует список days так, чтобы в нем остались только дни,
# названия которых состоят из четырех символов или начинаются с буквы S. Используйте при этом lambda функцию.
# Распечатайте получившийся список в алфавитном порядке, каждый элемент на новой строчке

# days = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve']
# print(*sorted(list(filter(lambda x: len(x) == 4 or x[0] =="S", days))), sep='\n')

# --------------------------------------------

# 10.5 Функция zip python
# Вот у нас есть два списка:
#
# a = [1, 2, 3, 4, 5]
# b = [100, 200, 300, 400, 500]
#
# Нам нужно вывести в одну строчку пару с двух списков которые стоят на одинаковы индексах, тоесть индекс начинается с 0.
# В списке а под нулевым индексом стоит -  1, а в списке б – 100
# Нам нужно так вывести все пары каждую на отдельной строчке и это можно сделать циклов for
#
# for i in range(len(a)): – указываем в range() длину списка а(можно и b но нет разницы у них одинаковая длина)
#     print(a[i], b[i]) – range(len(a)) – выдаст 5 элементов – 0,1,2,3,4 а эти числа совпадают с индексами элементов двух списков и если указать переменную i В которой по очередно будут поступать числа от 0 до 4 то мы можем вывести в обоих списках по одному элементу начания с нулевого индекса
#
# Вывод:
#     1 100
#     2 200
#     3 300
#     4 400
#     5 500
#
# Мы получили то что нам нужно но этот код можно заменить одной функцией zip:
#
# zip() принимает аргументами несколько итерабельных последовательностей(tuple, list) и выводит их элементы стоящие на одном индексе парно каждую в отдельной строке:
# print(zip(a, b)) – первым аргументом мы передали список а, вторым передали список б.
#
# Данное выражение вернет нам zip Обьект: <zip object at 0x02C0A488>
# Zip обьект является итератором а как мы знаем итератор можно превратить в итерабельную последовательность например кортеж(tuple):
#
# print(tuple(zip(a, b))) – данный код выведет нам пары в одну строчку но так как на нужно вывести их каждую в отдельной строке сделаем так:
#
# print(*tuple(zip(a, b)), sep='\n') – тут мы передаем парамет sep=’\n’
#
# который является параметров функции print() в параметре sep`а мы указали \n тоесть переходи на следующую строку, и так после каждого вывода новой пары мы будем переходить на следующую строку, а ‘*’в начален принта убирает запятые.
# Вывод:
#
# (1, 100)
# (2, 200)
# (3, 300)
# (4, 400)
# (5, 500)
#
# Как видите все работает.
#
# Также можно добавить третий аргумент.
#
# c = ‘abcde’ – переменная ‘c’ с строкой
#
# Далее делаем все тоже самое:
#
# print(*tuple(zip(a, b, c)), sep='\n') – просто добавляем переменную с как третий аргумент.
#
# Вывод:
#
# (1, 100, 'a')
# (2, 200, 'b')
# (3, 300, 'c')
# (4, 400, 'd')
# (5, 500, 'e')
#
# Если вас не устраивают скобки, можете делать так:
#
# for i in zip(a, b, c): - обходим все элементы трех переменных
#     print(*i) – выводим их с приставкой ‘*’ чтобы не было скобок
#
# Чтобы из zip обьекта снова вернуть наши былые списки или кортежи делаем так:
#
# result = zip(a,b,c) -  записываем в оператор result zip обьект
# a1, b1, c1 = zip(*rezult) – записываем в три переменные элементы оператора result в котором хранится Zip object, * там берет элементы стоящие под первым индексом и кладет их по одному в три оператора и так делает до последнего индекса.
# print(a1, b1, c1) -  в трех переменных готовые списки которые соответствуют спискам изначальным.


# -------------------------------------------
# 10.6 Сортировка коллекций в Python. Метод sort и функция sorted

# sort - метод списков
# # sorted() - встроенная функция
# a = [1, 4, 56, 3, 2, 4, 5]
# b = 'hello world'
# c = ('hi', 'kniga', 'alfa', 'poka')
# a.sort()   #отсортирует список через метод .sort
# print(a)
# print(sorted(a))  # -> [1, 2, 3, 4, 4, 5, 56]   #функция сортировки, не меняет изначальные данные
# print(sorted(b))  # -> [' ', 'd', 'e', 'h', 'l', 'l', 'l', 'o', 'o', 'r', 'w']
# print(sorted(c))  # -> ['alfa', 'hi', 'kniga', 'poka']
# # c = sorted(c, reverse=False/True)   возрастание/убывание и возвращает список (list)

# Бывает, что надо отсортировать словарь по убыванию значений, а если значения одинаковые, то по возрастанию ключей
# (или наоборот... главное - что направление сортировки разное)
#
# sorted(sorted(my_dict.items(), key=lambda x: x[0]), key=lambda x: x[1], reverse=True)
# или
# sorted(my_dict.items(), key=lambda x:(-x[1], x[0])) # только если значение - число
# на выходе получаем отсортированный список кортежей
# my_dict = {'foo': 400, 'baz': 200, 'zar': 200, 'aab': 200, 'aaa': 100}
# >>>[('foo', 400), ('aab', 200), ('baz', 200), ('zar', 200), ('aaa', 100)]

# ----------------------------------------------

# 10.7 Сортировка по ключу Python. Аргумент key

# https://tproger.ru/translations/python-sorting/

# 1) встроенная функция
# a = [4, -10, 43, -300, 54, 289, -34, -8, 749]
# print(sorted(a, key = abs))

# 2) собственная функция
# def f(x):
#     return x % 10, x // 10 % 10
# a = [4, 10, 43, 300, 54, 289, 34, 8, 749]
# print(sorted(a, key=f))

# 3) встроенные методы обьектов
# a = ['ZZZ', 'aaa', 'eee', 'DDD', 'BBB', 'www']
# print(sorted(a, key=str.lower))

# 4) анонинмные функции lambda
# a = ['ZZZ 800', 'aaa 45', 'eee 43', 'DDD 800', 'AaA 43', 'aaa 14']
# print(sorted(a, key=lambda x: (x.split()[0].lower(), int(x.split()[1]))))

# ------------------------------------
# subject_marks = [('English', 88), ('Science', 90), ('Maths', 97), ('Physics', 93),('History', 82)]
# a = sorted(subject_marks, key=lambda x: x[1])
# for i in a:
#     print(*i)
#
# [print(*_) for _ in sorted(subject_marks, key=lambda x: x[1])]

# [print(*i) for i in sorted(subject_marks, key = lambda x: x[1])]
# ----------------------------------------------
#
# subject_marks = [('English', 88), ('Science', 90), ('Maths', 97),
#                  ('Physics', 93), ('History', 82), ('French', 78),
#                  ('Art', 58), ('Chemistry', 76), ('Programming', 91)]
#
# [print(*i) for i in sorted(subject_marks, key = lambda x: -x[1])]

# -------------------------------------
#
# Отсортирует список subject_marks по убыванию оценок.
# Предметы, имеющих одинаковые оценки, должны быть отсортированы в алфавитном порядке
#
# subject_marks = [('English', 88), ('Science', 90), ('Maths', 88),
#                  ('Physics', 93), ('History', 78), ('French', 78),
#                  ('Art', 78), ('Chemistry', 88), ('Programming', 91)]
#
# [print(*i) for i in sorted(subject_marks, key = lambda x: (-x[1], x[0]))]

# -------------------------------------
# Как отсортировать словарь Python. Сортировка словаря по значениям
# конспект урока:
#
# heroes = {
#     'spider-man':80,
#     'batman': 65,
#     'superman': 85,
#     'wonder woman': 70,
#     'flash': 70,
#     'iron man': 65,
#     'thor': 90,
#     'aquaman': 65,
#     'captain america': 65,
#     'hulk': 87
# }
#
# # 1 сортировка по значениям
# for i in sorted(heroes.items(), key=lambda para: para[1]):
#     print(*i)
#
# # 2 сортировка по значениям + по ключам при одинаковых значениях
# for i in sorted(heroes.items(), key=lambda para: (para[1], para[0])):
#     print(*i)


# # ------------------------------------------
# models = [{'make': 'Nokia', 'model': 216, 'color': 'Black'},
#           {'make': 'Mi Max', 'model': 2, 'color': 'Gold'},
#           {'make': 'Samsung', 'model': 7, 'color': 'Blue'},
#           {'make': 'Apple', 'model': 10, 'color': 'Silver'},
#           {'make': 'Oppo', 'model': 9, 'color': 'Red'},
#           {'make': 'Huawei', 'model': 4, 'color': 'Grey'},
#           {'make': 'Honor', 'model': 3, 'color': 'Black'}]
#
# for i in sorted(models, key=lambda x: x['color']):
#     print(f"Производитель: {i['make']}, модель: {i['model']}, цвет: {i['color']}")
# # ----
# [print('Производитель: ' + i['make'] +', модель: ' + str(i['model']) +', цвет: ' + i['color']) for i in sorted(models, key = lambda x: x['color'])]

# ---------------------------------------
# Вверху хотим видеть самые дорогие товары, внизу самые дешевые
# Программа будет принимать строки, в которых сперва указывается название товара,
# а затем через двоеточие с пробелом его цена - целое положительное число.
# Вывести список товаров по уменьшению цены

# sp = [i.split(':') for i in iter(input, 'конец')]
# for i in sorted(sp, key=lambda x: int(x[1]), reverse=True):
#     print(i[0])

# -------------------------------------

# my_dict = dict()
# for _ in range(int(input())):
#     name = input()
#     if name in my_dict.keys():
#         my_dict[name] += 1
#     else:
#         my_dict[name] = 1
# res = sorted(my_dict.items(), key=lambda x: x[1], reverse=True)
# [print(f'{i}, {j}') for i, j in (res[0], res[-1])]

# -------------------------------
# phone_book = {}
#
# for _ in range(int(input())):
#     phone, name = input().split()
#     phone_book.setdefault(name, []).append(phone)
#
# for _ in range(int(input())):
#     name = input()
#     print(*phone_book.get(name, ['Неизвестный номер']))

# ------------------------------

# dr = {}
#
# for _ in range(int(input())):
#     name, _, month = input().split()
#     dr.setdefault(month, []).append(name)
#
# for _ in range(int(input())):
#     print(*sorted(dr.get(input(), ['Нет данных'])))

# ------------------------------------
# Рейтинг таксистов

# lst = [i.split(', ') for i in iter(input, 'конец')]
# d = {}
# for i in lst:
#     d.setdefault(i[0], []).append(int(i[1]))
# d = {key: sum(value) / len(value) for key, value in d.items()}
# for i in sorted(d.items(), key=lambda x: (-x[1], x[0])):
#     print(*i)


# taxi_drivers = {}
# a = str
# while a != 'конец':
#     a = list(input().split(', '))
#     if a[0] == 'конец':
#         break
#     if a[0] in taxi_drivers:
#         taxi_drivers[a[0]].append(int(a[1]))
#     else:
#         taxi_drivers[a[0]] = [int(a[1])]
# for key, value in taxi_drivers.items():
#     x = sum(value) / len(value)
#     taxi_drivers[key] = x
# for i in sorted(taxi_drivers.items(), key=lambda para: (-para[1],para[0])):
#     print(*i)
#
#
# d = {}
# while True:
#     driver = input().split(', ')
#     if driver == ['конец']:
#         break
#     d[driver[0]] = d.get(driver[0], []) + [int(driver[1])]
# for key, val in sorted(d.items(), key=lambda x: (-(sum(x[1]) / len(x[1])), x[0])):
#     print(key, sum(val) / len(val))

# -----------------------------------
# 10.8 Встроенная функция isinstance

# Функция isinstance является встроенной функцией python
# И для того что-бы показать что она может делать давайте создадим список а:
#
# a = [1, 2, '3', '4', [5, '6'], (7,'8'), 9.0] – в этом списке есть типы данных: int, str, list, tuple, float.
#
# Чтобы убедиться в этом можно сделать такое выражение:
#
# for  i in a:
#     print(i, type(i))
#
# Вывод:
# 1 <class 'int'> - число
# 2 <class 'int'> - число
# 3 <class 'str'> - строка
# 4 <class 'str'> - строка
# [5, '6'] <class 'list'> - список
# (7, '8') <class 'tuple'> - кортеж
# 9.0 <class 'float'> - вещественное число
#
# Теперь давайте заведем перебенную b в которой будем считать сумму всех чисел:
#
# b = 0
# for i in a:
#     b += i
# print(b)
#
# Вывод: TypeError: unsupported operand type(s) for +=: 'int' and 'str' – эта ошибка гласит что нельзя к числу прибавлять строку, этой строкой был элемент ‘3’
# И чтобы решить данную проблему, на помощь приходит функцию isinstance()
#
# Функция isinstance принимает на вход два аргумента, первый аргумент это какой либо обьект, второй аргумент это тип обекта.
# Тоесть эта функция проверяет является ли первый аргуемент инстанцией второго аргумента:
# Isinstance возвращает bool:
#
# print(isinstance(1, int)) – здесь мы первым аргументом передали цифру 1, а вторым аргументом тип обьекта int, и так как цифра 1 является типом обьекта Int, функция isinstance Вернут True
#
# И это очень полезно, например будем использовать эту функцию для проверки обьекта i в цикле for
#
# a = [1, 2, '3', '4', [5, '6'], (7,'8'), 9.0]
# b = 0 – сюда будем складывать все цифры обьекта Int
# for i in a:
#     if isinstance(i, int) – тоесть проверяется является ли элемент i Обьектом типа int, и если функция isinstance вернет True То выполнится код в блоке условия.
#         b += i прибавляем к b проверенный элемент i
#
# Вывод: 3, первые два элемента это 1, 2 их сумма равняется 3, дальше 3 и 4 это строки (str) – они проверку не проходят, дальше список с элементами 5(int), 6(str) они не будут складываться так как они внутри вложенного списка и в функцию isinstance попадают не они а сам список и так как список не Int а лист, проверку не проходит, с tuple тоже самое а 9.0 это float (вещественное число)
# В функцию isinstance() вторым аргументом можно передавать все существующие типы обьектов в python:
# Int, str, list, tuple, dict, file, float, set, bool.

# a = [1, [2], 'Hello', 3, '4', [5, 6], ' ', (7, 8), 'world', 9.0]
# s_strok = ''
# s_list = []
# s_numbers = 0
# for i in a:
#     if isinstance(i, str):
#         s_strok = s_strok + i
#     elif isinstance(i, list):
#         s_list = s_list + i
#     elif isinstance(i, (int, float)):
#         s_numbers = s_numbers + i
# print(s_strok)
# print(s_list)
# print(s_numbers)

# ----------------------------

# 10.9 Функции all и any
# Функция all это встроенная функция в которую можно передать аргументом обьект.
# Давайте вспомним про логический тип обьекта(bool)
# В функцию bool можно передать обьект, и она вернет True если обьект не является пустым либо нулем.
#
# Например bool(1, 2, 3, 4,’6’) –вернет True ибо эти обьекты являются не пустыми, а bool(0) или bool([]), bool({})
# вернут False ибо они являются пустыми.
#
# Функция all также принимает в себя последовательность элементов и возвращает True в случае если все обьекты переданные
# в эту функцию не являются пустыми либо нулем:
# Давайте создадим список a:
# a = ['56', 7, 8.8]
# print(all(a))
#
# Вывод: True ибо все элементы внутри списка a являются не пустыми множествами.
# Теперь добавим один пустой элемент:
# a = ['56', 7, 8.8, 0]
# print(all(a))
#
# Вывод: False, ибо 0 является пустым множеством, как и пустой список либо кортеж.
# Как мы поняли функция all вернет True если переданный в переданном ей аргументе все элементы являются не пустыми, если
# хотябы один элемент пустой, то вернет False.
#
# Функция any принимает также только один аргумент, но вот только any возвращает True если хотябы один элемент в
# переданном аргументе является не пустым множеством:
# a = [‘’, 0, [], (), 1]
# print(any(a))
#
# Вывод: True, так как число 1 является не пустым множеством.
# Если убрать его:
# a = [‘’, 0, [], ()]
# print(any(a))
#
# Вывод: False ибо все элементы пустые. Также в эти функции можно передавать свои условные выражения: \
#
# a = 13
# first = a % 2 == 0 – в
# данном выражении проверяется четность числа а.
# second = a > 11 = проверяем большели а чем 11
# thirth = isinstance(a, int) – является ли а инстанцие Int
# Теперь можем передавать по одному эти переменные в функции.
#
# Print(all([first])) – выведется False ибо 13 нечетное число
# Print(all([second])) – True ибо 13 больше чем 11
# Также обратите внимание что мы передаем нашу переменную внутри коллекции, ибо наша переменная вернет булевый
# тип обьекта а функции all и any такое принять не могут, а вот внутри списка либо кортежа могут.
#
# print(all([first, second, thirth])) – False ибо первое условие не выполняется
# print(any([first, second, thirth])) – True ибо выполнются два условия

# ------------------------------------------
# 10.10 7 видов вызываемых (callable) объектов
# Вызываем обьект это обьект который поодерживает оператор вызоыва, оператор вызова обозначаетсякруглыми скобочками.
# Всего есть 7 видов Вызываемых обьектов в python:
# 1)Встроенные функции.
# Например len() внутрь которого поступает аргумент которому нужно найти длину Проверить является ли обьект вызываемым
# можно функцией callable:
# print(callable(len)) = True
# 2)Встроенные методы.
# Например lower() – который делает все буквы в переданном обьекте строчными.
# a = 'AbCd', print(a.lower()) – abcd
# print(callable(a.lower)) – True
# 3)Самописные функции.
# Тоесть функции которые вы написали сами:
# def sqr(x):
#     return x ** 2
# Простая функция принимающая аргументом число и возвращает его квадрат.
# print(callable(sqr)) – True
# (Анонимные lambda функции также вызываемые)
# 4)Классы.
# Создадим пустой класс
# class dog():
#     pass
# print(callable(dog)) – True
# 5) Экземпляры классов.
# Наш класс dog можно присвоить в переменную которая и станет экземпляром класса:
# class dog():
#    pass
# a = dog()
# Но в таком с нашим классом это не сработает ибо онабсолютно пуст:
# print(callable(a)) – False
# Чтобы он наш экземпляр стал вызываевым используем магический метод __call__
# class dog():
#     def __call__(self, *args, **kwargs):
#         print('gav')
# a = dog()
# print(callable(a)) = True
# Вот вызовем нашу переменнуюа:
# a() – ‘gav’
#
# 6)Методы класса.
# class dog():
#     def sayhello(self):
#         print('hello')
# Вот наш метод sayhello который принимает self(Экземпляр) и выводит hello
# a = dog()
# print(callable(a.sayhello)) = True
# print(a.sayhello()) = ‘hello’
#
# 7)Функции генераторы.
# Вспомним функции генераторы которые внутри себя имеют ключевое слово yield
# def gen():
#     a = [1, 2, 3, 4, 5, 6]
#     for i in a:
#         yield i
# print(callable(gen)) = True
#
# Это и есть все вызываемые обьекты, к остальным обратиться через скобочки нельзя:
# print(callable(1)) = False – обьект int
# print(callable('2')) = False – обьект str
# print(callable(3.0)) = False - обьект float
# print(callable([])) = False – обьект list
# print(callable({})) = False – обьект dict
# print(callable(())) = False – обьект tuple

# -------------------------------------------
# 11.1 Модуль collections: объект Counter
from collections import Counter

# s = 'abracadabra'
# words = ['Donald', 'Mickey', 'Donald', 'Mickey', 'Mickey']
# inners1 = Counter(s) #создание словаря, ключ - символ, цифра - количество
# inners = Counter(words)
#
# print(inners.most_common())  #т.к. словарь- можем применять разные методы
# print(inners1.most_common())
#
# r = Counter()
# for i in (1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3):  # создаст счетчик с подсчетом колько раз встречалась цифра
#     r[i] += 1
# print(r)  # ----> Counter({3: 8, 2: 4, 1: 3})
#
# d = Counter([2, 2, 2, 3, 3, 4, 4, 4, 4])
# print(d)
# f = r + d    #можно складывать счетчики
# print(f)

# collections.Counter - вид словаря, который позволяет нам считать количество неизменяемых объектов
# (в большинстве случаев, строк). Пример:
#
# >>> import collections
# >>> c = collections.Counter()
# >>> for word in ['spam', 'egg', 'spam', 'counter', 'counter', 'counter']:
# ...     c[word] += 1
# ...
# >>> print(c)
# Counter({'counter': 3, 'spam': 2, 'egg': 1})
# >>> print(c['counter'])
# 3
# >>> print(c['collections'])
# 0
# Но возможности Counter на этом не заканчиваются. У него есть несколько специальных методов:
#
# elements() - возвращает список элементов в лексикографическом порядке.
#
# >>> c = Counter(a=4, b=2, c=0, d=-2)
# >>> list(c.elements())
# ['a', 'a', 'a', 'a', 'b', 'b']
# most_common([n]) - возвращает n наиболее часто встречающихся элементов,
# в порядке убывания встречаемости. Если n не указано, возвращаются все элементы.
#
# ---------------------------------------------------------

# 11.2 Модуль collections: объект defaultdict
# defaultdict
#
# Стандартный словарь включает метод setdefault() для извлечения значения и установления значения по умолчанию,
# если значение не существует. Напротив, defaultdict позволяет вызывающему объекту указать
# значение по умолчанию (возвращаемое значение) заранее при инициализации контейнера.
#
# как определено Дугом Хеллманом в стандартной библиотеке Python на примере
#
# Как использовать defaultdict?
# Импорт defaultdict
#
# >>> from collections import defaultdict
# Инициализировать defaultdict
# Инициализируйте его, передав тип элемента по умолчанию
# defaultdict является Callable
#
# >>> d_int = defaultdict(int)
# >>> d_list = defaultdict(list)
# >>> def foo():
# ...     return 'default value'
# ...
# >>> d_foo = defaultdict(foo)
# >>> d_int
# defaultdict(<type 'int'>, {})
# >>> d_list
# defaultdict(<type 'list'>, {})
# >>> d_foo
# defaultdict(<function foo at 0x7f34a0a69578>, {})
# можно было передать **kwargs
#
# >>> d_int = defaultdict(int, a=10, b=12, c=13)
# >>> d_int
# defaultdict(<type 'int'>, {'a': 10, 'c': 13, 'b': 12})
# или
#
# >>> kwargs = {'a':10,'b':12,'c':13}
# >>> d_int = defaultdict(int, **kwargs)
# >>> d_int
# defaultdict(<type 'int'>, {'a': 10, 'c': 13, 'b': 12})
# Как это работает?
#
# Как и дочерний класс стандартного словаря, он может выполнять все те же функции.
# Но в случае передачи неизвестного ключа он возвращает значение по умолчанию вместо ошибки.
#
# >>> d_int['a']
# 10
# >>> d_int['d']
# 0
# >>> d_int
# defaultdict(<type 'int'>, {'a': 10, 'c': 13, 'b': 12, 'd': 0})
# В случае, если вы хотите изменить значение по умолчанию, перезапишите default_factory:
#
# >>> d_int.default_factory = lambda: 1
# >>> d_int['e']
# 1
# >>> d_int
# defaultdict(<function <lambda> at 0x7f34a0a91578>, {'a': 10, 'c': 13, 'b': 12, 'e': 1, 'd': 0})
# или
#
# >>> def foo():
# ...     return 2
# >>> d_int.default_factory = foo
# >>> d_int['f']
# 2
# >>> d_int
# defaultdict(<function foo at 0x7f34a0a0a140>, {'a': 10, 'c': 13, 'b': 12, 'e': 1, 'd': 0, 'f': 2})
# Примеры:
#
# Пример 1
#
# int передается как default_factory --> значение по умолчанию будет 0
# Теперь, когда строка передается в цикле, она увеличит количество конкретных встречаемых букв в d.
#
# >>> s = 'mississippi'
# >>> d = defaultdict(int)
# >>> d.default_factory
# <type 'int'>
# >>> for k in s:
# ...     d[k] += 1
# >>> d.items()
# [('i', 4), ('p', 2), ('s', 4), ('m', 1)]
# >>> d
# defaultdict(<type 'int'>, {'i': 4, 'p': 2, 's': 4, 'm': 1})
# Пример 2
#
# Поскольку list был передан как default_factory, любой неизвестный (несуществующий) ключ вернет [] (т. е. список) по умолчанию. Теперь, когда список кортежей передается в цикле, он добавит значение в d[color]
#
# >>> s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
# >>> d = defaultdict(list)
# >>> d.default_factory
# <type 'list'>
# >>> for k, v in s:
# ...     d[k].append(v)
# >>> d.items()
# [('blue', [2, 4]), ('red', [1]), ('yellow', [1, 3])]
# >>> d
# defaultdict(<type 'list'>, {'blue': [2, 4], 'red': [1], 'yellow': [1, 3]})
# Пример 3
# from collections import defaultdict
# data = [
#     ('ivanov', 2),
#     ('petrov', 1),
#     ('sidorov', 5),
#     ('petrov', 3),
#     ('ivanov', 2),
#     ('ivanov', 4),
# ]
# marks = defaultdict(int)
# marks_list = defaultdict(list)
# marks_unio = defaultdict(set)
# for surname, mark in data:
#     marks[surname]+=mark
#     marks_list[surname].append(mark)
#     marks_unio[surname].add(mark)
#
# print(marks)
# print(marks_list)
# print(marks_unio)
# # #

# -----------------------------------------------

# # 11.3 Модуль collections: объект namedtuple
# Класс collections.namedtuple позволяет создать тип данных, ведущий себя как кортеж, с тем дополнением,
# что каждому элементу присваивается имя, по которому можно в дальнейшем получать доступ:
#
# Point = namedtuple('Point', ['x', 'y'])
# p = Point(x=1, y=2)
# p
# Point(x=1, y=2)
# >>> p.x
# 1
# >>> p[0]
# 1
# -------------------------------
# from collections import namedtuple

# point = (3, 5)
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
# PointV2 = namedtuple('PointV2', 'x y')
#
# a = Point(4, 5)
# b = PointV2(7, 9)
# c = PointV2(x= 10, y = 12)
#
# print(a.x, a.y)
# print(b.x, b.y)
# print(c.x, c.y)

# ------------------------------

# from collections import namedtuple
# from datetime import datetime
# class Person(namedtuple):
#     name:str
#     surname:str
#     date:datetime
#     country:str
# Person('Megan', 'Fox', '12-05-20', 'USA')
#
# --------------------------------------------------------

# 12 Модули работы со временем и датой

# Модуль datetime
# Название	Цель использования
# date	    для работы только с датой (день, месяц, год)
# time	    для работы только со временем (часы, минуты , секунды, милисекунды)
# datetime	для работы одновременно и с датой и со временем (день, месяц, год, часы, минуты, секунды, милисекунды)
# timedelta	для измерения продолжительности периода времени, или иными словами для нахождения разницы между двумя отрезками времени
# tzinfo	    для работы с часовыми поясами

from datetime import date  # -> импорт datetime

# >>> help(date)
# Help on class date in module datetime:
# class date(builtins.object)
# |  date(year, month, day) --> date object


#
# d1 = date(2020, 12, 31)
# print(d1)
#
# #именованная передача аргументов
# d2 = date(day=12, year=2010, month=9)
# print(d2)
#
# #комбинированная передача аргументов
# d3 = date(70, day=1, month=10)
# print(d3)
# --------------------------------
# from datetime import date
# date_7_08_1996 = date(1996, 8, 7)
# date_31_12_1981 = date(1981, 12, 31)
# print(date_7_08_1996)
# print(date_31_12_1981)
# -------------------------
# from datetime import date
# a, b, c = int(input()), int(input()), int(input()),
# print(date(c, b, a))
# ------------------------------------

# from datetime import date
# a = date(2015, 8, 21)
# print(a.year, type(a.year))
# print(a.month, type(a.month))
# print(a.day, type(a.day))
#
# b = date(888, 3, 11)
# print(f'{b.month}/{b.day}/{b.year}')
# -----------------------------------------
# вывести номер месяца и номер года
# from datetime import date
#
# my_date = date(2013, 6, 21)
# print(my_date.month, my_date.year)
# -------------------


# from datetime import date
#
# d = int(input())
# m = int(input())
# y = int(input())
# user_date.da = date(y, m, d)
# print(user_date.da)
# print(user_date.da.strftime("%d.%m.%Y"))
# ----------------------------
# ----------------------
# a = [int(y) for y in input().split()]
# N = len(a)
# b = [1]*N
#
# if N == 0:
#     b = [0]
# elif N == 1:
#     b = a
# else:
#     for i in range(0,N-1):
#         b[i] = a[i-1] + a[i+1]
#     b[N-1] = a[N-2] + a[0]
#
# for j in b:
#     print(j, end=' ')
# --------------------------------
# lst= [int(i) for i in input().split()]
# if len(lst) == 1:
#         print(lst[0])
# else:
#     for i in range(len(lst)):
#         print(lst[i-1] + lst[i+1-len(lst)], end=' ')
# --------------------------------
# Напишите программу, которая принимает на вход список чисел в одной строке и выводит на экран
# в одну строку значения, которые встречаются в нём более одного раза.
# a = [int(i) for i in input().split()]
# b = set()
# for i in a:
#     if a.count(i) > 1:
#         b.add(i)
# if len(b)>0:
#     print(*sorted(list(map(lambda x: int(x), b))), sep=' ')
# else:
#     print()
# ---------------------------
# a = [int(i) for i in input().split()]
# m = a[0]
# for i in a:
#     if m>=i:
#         m=i
# print(m)

# -------------------------------------

# Игра Сапер

# n, m, k = (int(i) for i in input().split())  # чтение размеров поля и числа мин
# a = [[0 for j in range(m)] for i in range(n)]  # заполнение поля нулями
# for i in range(k):
#     row, col = (int(i) - 1 for i in input().split())
#     a[row][col] = -1  # расставляем мины
# for i in range(n):
#     for j in range(m):
#         if a[i][j] == 0:  # в этой клетке мины нет, поэтому считаем число мин вокруг
#             for di in range(-1, 2):
#                 for dj in range(-1, 2):
#                     ai = i + di
#                     aj = j + dj
#                     # (ai, aj)
#                     if 0 <= ai < n and 0 <= aj < m and a[ai][aj] == -1:
#                         a[i][j] += 1
# # вывод результата
# for i in range(n):
#     for j in range(m):
#         if a[i][j] == -1:
#             print('*', end='')
#         elif a[i][j] == 0:
#             print('.', end='')
#         else:
#             print(a[i][j], end='')
#     print()

# -----------------------------------

# Программа, считывает числа (по одному в строке), пока сумма введённых чисел не будет равна 0
# и сразу после этого выводит сумму квадратов всех считанных чисел

# Заводим две переменные total - для подсчета += чисел
# вторая с квадратами (+= x**2) Делаем  условие: while True: а дальше вводим число...
# ищем total и одновременно считаем квадраты,
# делаем условие, если total == 0: печатаем переменную,
# считавшую квадраты и квадраты и break)))
# a = int(input())
# if a == 0:
#     print(a)
# else:
#     count = a
#     sq = a ** 2
#     while True:
#         a = int(input())
#         sq += a ** 2
#         count += a
#         if count == 0:
#             break
#     sq = float(sq.real)
#     print(int(sq))
# # -------------------------------------
# # -------------------------------------
# # -------------------------------------
# suma, sqd = 0, 0
# while True:
#     a = int(input())
#     suma += a
#     sqd += a**2
#     if suma == 0:
#         break
# print(sqd)

# --------------------------------
# sp = [int(i) for i in input().split()]   #   2 3 5 9 8 2 ->  [2, 3, 5, 9, 8, 2]
# sp = [i for i in range(int(input())+1)]    #   5   ->  [0, 1, 2, 3, 4, 5]

# ------------------------------------------------------
# Программа, выводит часть последовательности 1 2 2 3 3 3 4 4 4 4 5 5 5 5 5 ...
# (число повторяется столько раз, чему равно)

# sp = []
# n = int(input())
# for i in range(1, n+1):
#     sp += [i] * i
# print(*sp[0:n])

# ----------------------------------------

# Программа, считывает список чисел lstlst из первой строки и число x из второй строки,
# выводит все позиции, на которых встречается число x в переданном списке lstlst.
# 5 8 2 7 8 8 2 4
# 8
# 1 4 5

# sp = list(map(int, input().split()))
# n = int(input())
# for i in range(len(sp)):
#     if sp[i] == n:
#         print(i, end=' ')
# if n not in sp:
#     print('Отсутствует')

# -------------------------------
# Вывести матрицу того же размера, у которой каждый элемент в позиции i, j равен сумме
# элементов первой матрицы на позициях (i-1, j), (i+1, j), (i, j-1), (i, j+1)


# i =    [0, 1, 2],  [0, 1,  2], [ 0, 1, 2]
# lst = [[9, 5, 3,], [0, 7, -1], [-5, 2, 9]]
# j =    [    0,          1,           2    ]
#
# j0i0 = j0i2(i0-1) + j0i1(i0+1) + j2(j0-1)i0 + j1(j0+1)i0 = 3 + 5 - 5 + 0 = 3
# j0i1 = j0i0(i1-1) + j0i2(i1+1) + j2(j0-1)i1 + j1(j0+1)i1 = 9 + 3 + 2 + 7 = 21
# j0i2 = j0i1(i2-1) + j0i0(i2+1) + j2(j0-1)i2 + j1(j0+1)i2 = 5 + 9 + 9 -1 = 22

# m = []
# while True:
#     n = input().split()
#     if n[0] == 'end':
#         break
#     else:
#         m.append(n)
# for i in range(len(m)):
#     x = ''
#     for j in range(len(m[i])):
#         a = int(m[i - 1][j])
#         if i == len(m) - 1:
#             b = int(m[0][j])
#         else:
#             b = int(m[i + 1][j])
#         c = int(m[i][j - 1])
#         if j == len(m[i]) - 1:
#             d = int(m[i][0])
#         else:
#             d = int(m[i][j + 1])
#         s = a + b + c + d
#         x += str(s) + ' '
#     print(x.rstrip())
# ----------------------------------------------

# Выведите таблицу размером n×n, заполненную числами от 1 до n**2
# по спирали, выходящей из левого верхнего угла и закрученной по часовой стрелке

# a=int(input())
# nul=[[0]*a for i in range(a)]
# x,y=0,0
# for i in range(1,a**2+1):
#     nul[x][y]=i
#     if x<=y+1 and x+y<a-1: y+=1
#     elif x<y: x+=1
#     elif x+y>=a : y-=1
#     elif x>=y : x-=1
# for i in range(a):
#     print(*nul[i])

# -------------------------------------------
# 3.1 Функции
