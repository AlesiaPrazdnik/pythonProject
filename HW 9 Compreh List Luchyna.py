# 1. Сгенерировать список нечётных двузначных чисел.
#print([i for i in range(10,100) if i % 2 != 0])
# 2. Сгенерировать список из 10 чисел степени 2. Отрезок От 1 до  10.
from random import random
"""print([i**2 for i in range (1,11)])"""

# 3. Сгенерировать список всех трёхзначных чисел кратных 5 и 3.
#print([i for i in range(100,1000) if i % 5 == 0 and i % 3 ==0])

# 4. Дан список, упорядоченный по не убыванию элементов в нем.
# Определите, сколько в нем различных элементов. Set не  использовать.
#
"""lst = [2,2,3,4,5,5,5,6,7]
c = []
for i in lst:
    if i not in c:
        c.append(i)
print(c)
print(len(c))"""
#То же самое одной строкой
#print(len({elem:elem for elem in input('Enter numbers:').split()}))
#     count += 1
# print(count)


# 5. Программа  получает на вход три числа через пробел — начало и конец
# диапазона, а также степень, в которую нужно возвести каждое число из
# диапазона.Выведите числа получившегося списка через пробел.
#
# Sample Input:
# 5 12 3
# Sample Output:
# 125 216 343 512 729 1000 1331 1728
"""a,b,c = map(int,input("enter numbers:").split())
print([i**c for i in range(a,b+1)])"""
# 6. Напишите программу, на вход которой подаётся список чисел одной строкой.Программа
# должна для каждого элемента этого списка вывести сумму двух его соседей.Для
# элементов списка, являющихся крайними, одним из соседей считается элемент, находящий
# на противоположном конце этого списка.Например, если на вход подаётся список
# "1 3 5 6 10", то на выход ожидается список "13 6 9 15 7"(без кавычек).Если на
# вход пришло только одно число, надо вывести его же.Вывод должен содержать одну
# строку с числами нового списка, разделёнными пробелом.
# Sample Input 1:  1 3 5 6 10
# Sample Output 1:  13 6 9 15 7
# Sample Input 2:  10
# Sample Output 2:  10
# Sample Input 3:  10 2
# Sample Output 3:  4 20
#a,b,c = map(int,input("enter numbers:").split())
#Решение от Дениса
"""lst = [int(i) for i in input().split()]
lst2 = []
if len(lst) ==1:
    lst2 = lst[::1]
else:
    for i in range(len(lst)-1):
        lst2.append(lst[i-1]+lst[i+1])
    lst2.append(lst[-2] +lst[0]) #ВОТ ЭТО Я НЕ ДОДУМАЛАСЬ СДЕЛАТЬ
print(lst2)"""

#А ЭТО МОЁ РЕШЕНИЕ
"""lst = [1,3,5,6,10]
#lst = [20]
#i = 0
c = []
for i in range(len(lst)-1):
        s = str(lst[i - 1])
        #print(int(s))
        n = str(lst[i + 1])
        #print(int(n))
        i = int(s)+int(n)
        print(i)
        c.append(i)
        i += 1
c.append(lst[-2] +lst[0]) #ВОТ ЭТО Я НЕ ДОДУМАЛАСЬ СДЕЛАТЬ!!!!
# ОСТАЛЬНОЕ ВЕРНО

print(c)

# s = [1,2,3]
# print(s[-1])

# lst = [1,3,5,6,10]
# #lst = [20]
# #i = 0
# c = []
# for i in range(len(lst)-1):
#         # s = str(lst[i - 1])
#         # #print(int(s))
#         # n = str(lst[i + 1])
#         # #print(int(n))
#         # i = int(s) + int(n)
#         # print(i)
#         # c.append(i)
#         # i += 1
#         if i == str(lst[-1]):
#                 s = str(lst[i - 1])
#                 n = str(lst[0])
#                 i = int(s) + int(n)
#         print(i)
#         c.append(i)
#         i += 1
#
# print(c)
"""
# 7. Числа вводятся в список в одной строке. Отсортировать их по убыванию их абсолютных значений.
# c = ((sorted([elem for elem in input('Enter numbers:').split()])))
# print(c[::-1])
#В одну строку то же самое
#print((sorted([elem for elem in input('Enter numbers:').split()])[::-1]))

# 8. Дан список, состоящий из строк. Отсортировать его по длине слов. Сначала должны идти длинные слова затем короткие.
"""lst = [i for i in input().split()]
lst.sort(key = len) #сортировка по длине строк
print(lst)"""
# 9. Дан список состоящий из слов. Отсортировать его по количеству вхождений буквы 'a'
# lst = [i for i in input().split()]
# lst.sort(key = lambda  x:x.count("a")) #указываем x.count, а не list.count, так как идём по каждому элементу без range
# print(lst)

# Дополнительные задачи:
#
# 10. Напишите программу, которая принимает на вход список чисел в одной строке и выводит на экран в одну строку
# значения, которые повторяются в нём более одного раза.
# Выводимые числа не должны повторяться, порядок их вывода может быть произвольным.
# Sample Input 1:
# 4 8 0 3 4 2 0 3
# Sample Output 1:
# 0 3 4
# Sample Input 2:
# 10
# Sample Output 2:
# Sample Input 3:
# 1 1 2 2 3 3
# Sample Output 3:
# 1 2 3


"""lst = [int(i) for i in input().split()]
for i in range (0,len(lst)):
    if i == lst.index(lst[i]) and lst.count(lst[i])>1:
        print(lst[i], end = "")"""


# 11. *Сгенерировать список всех простых чисел до  100 с помощью генератора.
"""a = ([i for i in range (2,8) if i % 2 ==1 or i//2 == 1])
b = ([i for i in range (7,100) if i % 2 != 0 and i % 3 !=0 and i % 5 !=0 and i % 7 !=0])
c = a+b
print(c)"""
#Решение от Дениса
# print([int(x) for x in range(2,100) if x == 2 or x == 3 or x ==5 or x == 7 or x>9
#        and x%2 !=0 and x % 3 !=0 and x % 5 !=0 and x % 7 !=0])
#Более простое решение с фуекнкцией ALL
#print([int(x) for x in range(2,100) if all(x%y != 0 for y in range(2,x))]) #ФУНКЦИЯ ALL проверка верности утверждения,
# что наше число не делится без остатка на любое число от 2 до нашего числа

# 12. Дан список , преобразуйте исходный список, вставив 0 между числами. Дополнительный список не создавать!
# Sample Input:
# 7 4 1
# Sample Output:
# 7 0 4 0 1
# lst = [i for i in input().split()]
"""lst = [7,4,1,5]
for ind,el in enumerate(lst): #выводим и индекс и число, чтобы можно было ссылаться на индекс
    #print(ind,el)
    if ind%2 !=0: #если индекс нечётный, вставляем рядом ноль Так как эта вставка со сдвигом - индекс опять будет нечётным, каждый раз
        lst.insert(ind,0)
print(lst)"""

#Решение от Дениса
# lst = [5,2,6,1]
# i = 0
# while i<len(lst):
#     if i%2 ==1:
#         lst.insert(i,0)
#         i +=1
#     i +=1
# print(lst)
#Ещё проще
# lst = [5,2,6,1]
# i = 0
# while i<len(lst):
#         lst.insert(i,0)
#         i +=2
# print(lst)
# 13. Напишите программу, которая выводит часть последовательности 1 2 2 3 3 3 4 4 4 4 5 5 5 5 5 ...
# (число повторяется столько раз, чему равно). На вход программе передаётся неотрицательное целое число
# n — столько элементов последовательности должна отобразить программа.
# На выходе ожидается последовательность чисел, записанных через пробел в одну строку.
#
# Sample Input:
# 7
# Sample Output:
# 1 2 2 3 3 3 4
# Sample Input 2:
# 10
# Sample Output 2:
# 1 2 2 3 3 3 4 4 4 4
lst = []
n = int(input("enter n: "))
for i in range(1,100):
    for j in range(1, i+1):
        if len(lst) == n:
            break
        print(i, end = " ")
        lst.append(i)
#Решение проще

lst = []
n = int(input("enter n: "))
count = 0
for i in range(1, 100):
    for j in range(1, i + 1):
        if count == n:
            break
        print(i, end=" ")
        count +=1
