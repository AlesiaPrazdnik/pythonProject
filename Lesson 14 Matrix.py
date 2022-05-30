#matrix
# raw (строка)
# column (столбец)
#       0       1       2  #ИНДЕКСЫ СПИСКОВ
#     0 1 2   0 1 2   0 1 2 #Индексы элементов
# A = [[1,2,4],[5,2,5],[1,5,2]]# - список с тремя вложенными списками,
# print(A)
# print(A[0][0])
# for i in range (len(A)):
#     for j in range (len(A[i])):
#         print(A[i][j], end = " ")
#         print(f"A[{i}][{j}]={A[i][j]}",end = " ")
#     print()
#Создаем матрицу 3 на 3. Для этого надо создать список с вложенными списками
# A = []
# for i in range (3):
#         lst = []
#         for j in range(3):
#             x = int(input())
#             lst.append(x)
#         A.append(lst)
# print(A)
# #То же самое, через генератор
# A = []
# for i in range (3):
#         lst = [int(input()) for j in range(3)]
#         A.append(lst)
# print(A)
# #ещё проще то же самое:
# A = []
# for i in range (3):
#     A.append([int(input()) for j in range(3)])
# print(A)
#Создание списка с вложенными списками с помощью генератора в генераторе

# A = [[int(input()) for i in range(3)] for j in range(3)] #найди ошибку, не работает
# print(A)
# B = [[0]*3 for i in range(3)] #список с вложенными списками из нулей
#
# print(B)
# for i in range(len(B)):
#     for j in range(len(B[i])):
#         if i ==j:
#             B[i][j] = i
#         elif i>j:
#             B[i][j] = 3
# print(B)
# Создать матрицу : 1234
#                   1234
#                   1234
#                   1234
# A = [[i+1 for i in range(4)] for j in range(4)] # чтоб без нуля выводилось i + 1
# print(A)
#
# B = [[i*j for i in range(4) if j<2] for j in range(4)]
# print (B)
#
# C = [[i*j for i in range(4)] if j<2 else [i+j for i in range(4)] for j in range(4)]
# print(C)
# #Найти сумму по строкам:
# for i in range(len(B)):
#     s = 0
#     for j in range(len(B[i])):
#         s += B[i][j] #сумма по строкам
#     print(s)
# # Найти сумму по столбцам:
# B = [[i*j for i in range(4) if j<2] for j in range(4)]
# b = [0,0,0,0]
# for i in range(len(B)):
#     for j in range(len(B[i])):
#         b[i] += B[j][i] #сумма по столбцам
# print(B)

#Найти максимальный и минималный эелемент в матрице и вывести на экран. Поменять эелементы местами. Матрица двухмерная
# print(max([[i for i in range(4)] for j in range(4)]))
# print(min([[i for i in range(4)] for j in range(4)]))
# import random
# A = [[random.randint(-100,100) for i in range(3)] for j in range(3)]
# print(A)
# min_el = max_el = A[0][0] #предпологаем, на случай если все элементы равны
# imin = jmin = imax = jmax = 0 #предпологаем что этот элемент и минимальный и максимальный,
# # если мы этого не сделаем, то дальше не с чем будет сравнивать
# for i in range(len(A)):
#     for j in range(len(A[i])):
#         print(A[i],[j], end =' ')
#         if min_el>A[i][j]: #если наш минимальный меньше проверяемого элемента
#             min_el = A[i][j] #то он становится минимальным
#             imin = i
#             jmin = j
#         if max_el<A[i][j]: #если наш минимальный меньше проверяемого элемента
#             max_el = A[i][j] #то он становится максимальным
#             imax = i
#             jmax = j
#         print()
# print(max_el,min_el)
# A[imin][imax] = A[imax][imin]
# for i in range(len(A)):
#     for j in range(len(A[i])):
#         print(A[i],[j], end =' ')
#     print()
#ИСКЛЮЧЕНИЯ Exception

#print(10+"hello")#невозможно, выдаст ошибку
#Чтоб не выдавало ошибку красным и продалжался код делаем методом исключения:
# try:
#     print(10+"hello")
# except TypeError:
#     print("type error :(")
# #Важно соблюдать очередность блоков
# try:
#     print(10+"hello")
# except Exception as e:
#     print(e)
#     print(type(e))
# except TypeError:
#     print("type error :(")
# #ещё вариант
# try:
#     print(10/0)
# except ZeroDivisionError:
#     print("zero div error")
#     print(type(e))
# except TypeError:
#     print("type error :(")
# else: # работает только если try блок отработал корректно, не вышло ошибки
#     print("all good")
# finally:  # это работат всегда
#     print("always work")
# print ("hello")

while True:
    try:
        name = input()
        if name.capitalize() == name:
            print("hello", name)
