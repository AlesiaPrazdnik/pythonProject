# 1. Сгенерировать двумерный список. Среди строк заданной матрицы, содержащих только нечетные элементы,
# найти строку с максимальной по модулю суммой элементов.
import random
#Нашла и вывела сумму строки, у кооторой самая большая сумма
# A = [[random.randint(-100,100) for i in range(3)] for j in range(3)]
# print(A)
# B =([sum(A[i]) for i in range(len(A))])
# print(B)
# print(max(B))
#Решение. попытка 2
#A = [[random.randint(-100,100) for i in range(3)] for j in range(3)]
# A = [[3,5,3],[3,5,7],[2,3,6]]
# lst = []
# lst2 = []
# print(A)
# for i in range(len(A)):
#     s = 0
#     count = 0
#     for j in range(len(A[i])):
#         if A[i][j]% 2 != 0:
#             s += A[i][j] #сумма по строкам
#             count+=1
#     if count == 3:
#         # print(s)
#         lst.append(s)
#         p = A.index(A[i])
#         print(p)
#         lst2.append(p)
# print(lst)
# print(lst2)
# d = dict(zip(lst,lst2))
# print(d)
# print (max(d))
# for key,value in d.items():
#     if key == (max(d)):
#         print("сумма максимальная = ",key,"номер строки с максимальной суммой = ", value)

# 2 Дано нечетное число n. Создайте двумерный список из n×n элементов, заполнив его символами "."
# (каждый элемент списка является строкой из одного символа).
# Затем заполните символами "*" среднюю строку списка, средний столбец массива, главную диагональ и побочную диагональ.
# В результате  в списке должна получиться снежинка. Выведите полученный список на экран, разделяя элементы списка пробелами.

# n = 5
# A = [["."]*n for i in range(n)]
# #print(A)
# m = n//2
# A[m] = ["*"for i in range(n)]
# print (A)
# for i in range(len(A)):
#     A[i][m] = "*"
#     for j in range(len(A[i])):
#         if i == j:
#             A[i][j] = "*"
#         if i+j == n-1:
#             A[i][j] = "*"
# for i in range(len(A)):
#     for j in range(len(A[i])):
#         print(A[i][j],end = " ") #чтоб каждая строка выводилась с отдельной строки
#     print('\n')

# 3. Даны два числа n и m. Создайте двумерный список размером n×m и заполните его символами "."
# и "*" в шахматном порядке. В левом верхнем углу должна стоять точка.
# n = int(input("Введите первое число :"))
# m = int(input("Введите второе число :"))
# A = []
# for i in range (n):
#     A.append(["." for j in range(m)])
# # for i in range(len(A)):
# #     for j in range(len(A[i])):
# #         print(A[i][j],end = " ") #чтоб каждая строка выводилась с отдельной строки
# #     print('\n')
# for i in range(len(A)):
#     # if i%2 == 0:
#     #     A[i][j] = "*"
#     for j in range(len(A[i])):
#         if j%2 != 0 and i%2 ==0:
#             A[i][j] = "*"
#         if j % 2 == 0 and i % 2 != 0:
#             A[i][j] = "*"
# for i in range(len(A)):
#     for j in range(len(A[i])):
#         print(A[i][j],end = " ") #чтоб каждая строка выводилась с отдельной строки
#     print('\n')
# 4. Сгенерируйте список как показано ниже. Делаем в одну строку:
#
# 1    1    1    1     1    1
# 1    2    3    4     5    6
# 1    3    6   10  15    21
# 1   4   10   20  35    56
# 1   5    15   35  70   126
# 1   6   21   56  126  252
#Не решила
"""A = [[(i+1)**j for i in range(6)] for j in range(6)]
for i in range(len(A)):
    for j in range(len(A[i])):
        print(A[i][j],end = " ") #чтоб каждая строка выводилась с отдельной строки
    print('\n')"""
"""A = [[(i+1)**j for i in range(6)] for j in range(6)]
print(A)
for i in range(len(A)):
    for j in range(len(A[i])):
        A[i][j] =A[i-1][j] + A[i][j-1]
        print(A[i][j], end=" ")  # чтоб каждая строка выводилась с отдельной строки
    print('\n')"""


# 5. Сгенерируйте список как показано ниже. Делаем в одну строку:
#
#  1    2    3    4     5
#  1    4    9    16   25
#  1    8    27  64   125
#  1    16   81  256  625
# A = [[(i+1)**j for i in range(5)] for j in range(5)]
# for i in range(len(A)):
#     for j in range(len(A[i])):
#         print(A[i][j],end = " ") #чтоб каждая строка выводилась с отдельной строки
#     print('\n')

# 6. Дано число n, и массив размером n × n. Проверьте, является ли палиндромом хоть одно число состоящее
# из цифр стоящих в  строке массива. Выведите слово “YES”, если есть такое число и слово “NO” в противном случае.
#
# Sample Input:
# 4
# 2 1 2 1
# 1 3 3 1
# 2 3 4 5
# 4 5 1 2
# Sample Output:
# YES
# Sample Input:
# 3
# 2 1 1
# 1 2 3
# 2 3 4
# Sample Output:
# NO
# lst = []
# n = int(input("Enter number: "))
# A = [[random.randint(0,2) for i in range(n)] for j in range(n)]
# for i in range(len(A)):
#     for j in range(len(A[i])):
#          print(A[i][j],end = " ") #чтоб каждая строка выводилась с отдельной строки
#     print('\n')
# for raw in A: #для каждого ряда
#     if raw == raw[::-1]: #переворачиваем ряд
#      print(raw)
#     else:
#         print("NO")

# Exeption:
#
# 1. Опишите конструкцию отлова ошибок, так чтобы выводило, какую ошибку вы сделали. Код представлен ниже:
#
# x = (1, 2, 5, 7)
# try:
#  x = x  / 2
# except:
#     TypeError
# print(x)
#
# x = (1, 2, 5, 7)
# try:
#  x = x  / 2
# except TypeError:
#     print("Недопустимый тип")
#
# 2. Напишите программу которые будет ловить IndexError, когда вы пытаетесь взять индекс элемента, которого нет в списке.
# lst =[1,2,3]
# try:
#     print(lst[4])
# except IndexError:
#     print("этого индекса нет в списке")

"""lst = [i for i in input("Enter number: ").split()]
print(lst)
#while True:
d = input("Укажите индекс переменной: ")

for i in range (len(lst)):
    try:
        if d == lst[i]:
             print(lst[i])
    except IndexError:
         print("этого индекса нет в списке")"""
# 3. Напишите программу которые будет ловить TypeError, когда вы пытаетесь скаткатенировать строку и число.
#
# 4. Напишите программу которая вычисляет площадь треугольника по формуле Герона,
# однако если пользователь введёт длину хоть одной стороны треугольника равную 0,
# то программа должна бросить исключение ArithmeticError.
#
# 5. Дан список. Пользователь не знает его размер. Программа должна бросить исключение TypeError,
# когда пользователь пытается удалить элемент которого нет в списке.
#
# 6..Дана строка. Пользователь ищет в ней подстроку. Если подстрока не найдена то бросьте ValueError.
#
# 7. Дана строка. Проверьте есть ли в ней цифры, иначе бросьте ValueError.
# s = "23hello"
# for i in s:
#     if i.isalpha():
#         print("ValueError")
"""s = "23hello"
try:
    raise Exception ("ValueError")
except Exception as e:
    for i in s:
        if i.isalpha():
            print(str(e))"""

# 8. Дан словарь, который содержит некоторые ключи и значения по этим ключам, пользователь не знает этих ключей.
# Бросьте ошибку KeyError в том случае когда пользователь пытается просмотреть значение по ключу, которого нет в словаре
# d = {2: 21, 6: 24, 7: 34}
# try:
#     n = int(input("enter number: "))
#     raise Exception ("KeyError")
# except Exception as e:
#     if n not in d.keys():
#         print(str(e))

