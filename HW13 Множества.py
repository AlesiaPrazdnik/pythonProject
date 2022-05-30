# 1. Дан список чисел. Определите, сколько в нем встречается различных чисел.
"""lst =[1,2,3,1,2,3,4,5,6]
print(len(lst))
s = set(lst)
print(len(s))
dif = len(lst) - len(s)
print (dif)"""

# 2. Даны два списка чисел. Посчитайте, сколько чисел содержится одновременно как в первом списке, так и во втором.
import random

"""lst =[1,2,3,1,2,3,4,5,6]
lst1 = [1,5,7,3,6,5,2,10]
s = set(lst)
s1 = set(lst1)
print(s1.intersection(s)) # выводит все числа, которые пересекаются 
print(len(s1.intersection(s)))"""

# 3. Даны два списка чисел. Найдите все числа, которые не содержатся одновременно в этих двух списках.
"""lst =[1,2,3,1,2,3,4,5,6]
lst1 = [1,5,7,3,6,5,2,10]
s = set(lst)
s1 = set(lst1)
print(s1.symmetric_difference(s))
print(len((s1.symmetric_difference(s))))"""

# 4.Во входной строке записана последовательность чисел через пробел.
# Для каждого числа выведите слово YES (в отдельной строке),
# если это число ранее встречалось в последовательности или NO, если не встречалось.

# Решение через список
"""c = []
lst = [1,1,5,7,3,6,6,5,2,10,1]
for i in lst:
    if i not in c:
        print(i,"NO")
        c.append(i)
    else:
        print (i,"YES")
print("повторяющиеся числа", c)
#То же самое, через множество
lst = [1,1,5,7,3,6,6,5,2,10,1]
set = set(lst)
for i in lst:
    if i in set:
        print (i, "Yes")
    else:
        print(i, "no")
"""

# 5. В ходе исследований ученые делают некие замеры, результаты которых заносят в базу данных.
# Однако для анализа результатов нет необходимости держать в базе "лишние", повторяющиеся данные.
# Напишите программу, которая выводит максимальное количество записей,
# после удаления которых анализ результатов будет произведен верно. Список элементов вводится через пробел.
# проще говоря - ищем количество повторений,которые будут удалены
# Sample Input:
# 6311 9423 142 142 8654 909 Error 6311 142 909 404 502 828 404 9423

# Sample Output:
# 6
"""n = int(input())
c = []
c1 = []
c2 = []
for i in range(n):
    # i = map(int, input().split())
    i = input("Введите результат замера:")
    c.append(i)
#Если решать через списки
# print(c)
# for el in c:
#     if el not in c1:
#         c1.append(el)
#
#     else:
#         c2.append(el)
# print(c1)
# print(c2)
# print(len(c2))
#Если решать через множество
print(c)
print(len(c))
set = set(c)
print(set)
print(len(set))
dif = len(c) - len(set)
print(dif)"""


# 6. Август и Беатриса играют в игру. Август загадал натуральное число от 1 до n.
# Беатриса пытается угадать это число, для этого она называет некоторые множества натуральных чисел.
# Август отвечает Беатрисе YES, если среди названных ей чисел есть задуманное или NO в противном случае.
# После нескольких заданных вопросов Беатриса запуталась в том, какие вопросы она задавала
# и какие ответы получила и просит вас помочь ей определить, какие числа мог задумать Август.
# В первой строке задано n - максимальное число, которое мог загадать Август.
# Далее каждая строка содержит вопрос Беатрисы (множество чисел, разделенных пробелом) и ответ
# Августа на этот вопрос .Вы должны вывести через пробел, в порядке возрастания, все числа, которые мог задумать Август.
#
# Sample Input:
# 20
# Enter guess: 1 2 3 4
# Enter guess: 5 9 20 11
# Enter guess: 12 15 10 17 13
# Enter guess: 10 17
# Enter guess: 13
# Sample Output:
# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
# NO: 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
# NO: 6 7 8 10 12 13 14 15 16 17 18 19
# YES: 10 12 13 15 17
# NO: 12 13 15
# YES: 13 is correct. You answered on the 5th try.

# n = 20
# lst = []
# m = random.randint(0,n) #до какого числа выводим последовательность
# numb = random.randint(0,m) #загаданное число
# print(numb)
# set0 = set()
# set0.add(numb)
# print(set0)
#
# for i in range(1,m+1):
#     print(i," ",end = "")
#     lst.append(i)
# print(lst)
# set_main =set(lst)
# #while len(set_main) !=0:
#     n1 = random.randint(0,m)
#     n2 = random.randint(0,m)
#     n3 = random.randint(0,m)
#     print("Enter guess:",n1 ,n2 ,n3 )
#     lst1 = [n1, n2, n3]
#     set1 = set(lst1)
#     for el in range (len(lst1)):
#         if set0.issubset(set1):
#
#             if el == numb:
#                 print("yes")
#             print(numb)
#         else:
#             set1.symmetric_difference(set_main)
#     print(set1.symmetric_difference(set_main))
# #Решение от Дениса
n = int(input())
count = 0
numb = random.randint(1,n)
main_set = {i for i in range(1,n+1)}
print(numb)
while True:
    count +=1
    print(main_set)
    print("Enter gues:", end = " " )
    set1 ={int(i) for i in input().split()}
    if numb in set1:
        print("Yes", end = " ")
        main_set = set1 #о есть наше начальное множество становится этим множеством
    else:
            print("NO:", end = " ")
            main_set = main_set-set1
    if (len(set1)==1 and numb in set1) or len(main_set) ==1:
        print("yes, it's correct answer, try = ",(count))
        break