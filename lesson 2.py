"""print(8>3)
print(8>3 and 3<1)
print(8>3 or 3<1)
print (24 % 2 == 0 and 24 % 3 == 0)"""

"""number = int(input())
if number > 0: #неполный уловный оператор
    print("чило положительное")
elif number == 0:
    print("это число ноль")
else:
    print("число отрицательное")

    a = True
    b = True
    c = a and not b
    print (c)

    a = True
    b = True
    c = a or not b
    print (c)"""

"""Напишите программу, которая проверяет последнюю цифру числа.
Если последняя цифра числа 3, то вывести True иначе вывести False

number = int(input())
print(number%10 == 3)"""


"""Напишите программу, которая выводит True, если хотя бы одно из чисел А, В, С отрицательно. Если нет вывести False.
 Числа вводятся с клавиатуры в одной строке.
a,b,c = map(int,input("Введите три чсла:").split())
print ((0-a)>0 or(0-b)>0 or (0-c)>0)"""


"""Верно ли что, целые n и k имеют одинаковую четность.
n,k = map(int,input("Введите два числа:").split())
print ((n%2==0 and k%2==0) or(n%2!=0 and k%2!=0))"""


"""Напишите программу, которая выводит True если число Х кратно 3 и заканчивается на 5. Число х вводится с клавиатуры.
x = int(input())
print(x % 3 ==0 and x % 10 ==5)"""

"""Найти количество четных чисел среди заданных трех целых чисел.
В ответе вывести количество четных чисел.
a,b,c = map(int,input("Введите три целых числа:").split())
if ((a%2==0 and b%2!=0 and c%2!=0) or (b % 2 == 0 and a % 2 != 0 and c % 2 != 0) or (c%2==0 and b%2!=0 and a%2!=0)):
    print ("одно чётное число")
if ((a%2==0 and b%2==0 and c%2!=0) or (a % 2 == 0 and b % 2 != 0 and c % 2 == 0) or (a%2!=0 and b%2!=0 and c%2==0)):
    print("два чётных числа")
if (a%2==0 and b%2==0 and c%2==0):
    print ("три чётных числа")"""


"""Дано двузначное число. Определить является ли сумма его цифр двузначным числом. (Ответ: Да/Нет)

a = int(input("Введите двузначное число:"))
if a < 10:
  print("это не двузначное число")
b = a//10 #деление без остатка
c = a%10 #деление с остатком
if((b+c)<10):
    print ("НЕТ")
else:
    print("ДА")"""

"""Дано четырёхзначное число. Проверить одинаковы ли все цифры в нем.

a = int(input("Четырёхзначное число:"))
b = a//1000
c = a//100- b*10
d = a//10 - b*100 - c*10
e = a%10
print (b,c,d,e)
if(b==c==d==e):
    print("все цифры равны")
else:
    print("цифры не равны")"""
#можно решить в 1 действие, поделив число на 1111, если нет остатака, зачит все цифры одинаовые print(a % 1111 ==0)

"""Напишите программу, принимающую на вход год и выводящую "Високосный", если в этом году действительно 366 дней, и "Не високосный" иначе. 
Год считается високосным, если его номер делится на 4, но не делится на 100 или же делится на 400.

a = int(input("Введите какой сейчас год:"))
if(a%4 == 0 and a%100 !=0 or a%400 ==0):
   print("год високосный")
else:
    print("год невисокосный")"""

"""Объяснить результат и вывести на экран результат логического выражения  
T = S для заданных значений логических переменных a, b, c.
+   логическое сложение   (логическое «или») or 
·    логическое умножение (логическое «и») and
 ¯  логическое отрицание (логическое «не») not
a = bool(input("введите True/False:"))
b = bool(input("введите True/False:"))
c = bool(input("введите True/False:"))
T = a and not (b and not c)
print(T)
S = a and not b or a and c
print(S)
print(T==S)"""
#Я списала решение в группе и вообще ничего не поняла, ни в задании, ни в решении!!!




   
"""9) Поле  шахматной доски определяется парой натуральных чисел, каждое из которых не превосходит 8:   
первое – номер вертикали, второе – номер горизонтали. Заданы натуральные числа x1, y1, x2, y2. 
Определить, являются ли поля (x1, y1) и (x2, y2) одного  цвета?
На поле (x1, y1) расположен ферзь. Угрожает ли он полю (x2, y2)?
На поле (x1, y1) стоит ладья, на поле (x2, y2) – пешка. Определить, бьет ли ладья пешку, 
пешка – ладью или фигуры не угрожают друг другу.
На поле (x1, y1) стоит слон, на поле (x2, y2) – конь. 
Определить, бьет ли слон коня, конь – слона или фигуры не угрожают друг другу."""

#x1,x2,y1,y2 = map(int,input("Введите 4 числа:").split()) - не сработало, считывает числа не по порядку8

x1 = int(input("Введите число от 1 до 8"))
x2 = int(input("Введите число от 1 до 8"))
y1 = int(input("Введите число от 1 до 8"))
y2 = int(input("Введите число от 1 до 8"))
if (0<x1<9 and 0<y1<9 and 0<x2<9 and 0<y2<9):
 print("данные введены верно")
else:
 print("неверно введены данные")
if x1 == x2 ==y1 == y2:
    print("не существует решения")
if((((x1+y1)%2) ==0 )and (((x2+y2)%2) == 0)):
  print("поля одного цвета")
else:
     print("поля не одного цвета")
if((x2-x1)!=0 or (y2-y1)!=0):
    print("ферзь угрожает полю x2,y2")
else:
    print('ферзь не угрожает')
if (x1 == x2 and y1 != y2) or (y1 == y2 and x1 != x2):
    print("ладья угражает пешке")
else:
    print("ладья не угрожает пешке")

#РЕШЕНИЕ ПРО КОНЯ




