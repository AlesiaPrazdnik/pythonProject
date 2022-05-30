# 1. Дан список. Выведите те его элементы, которые встречаются в списке только один
# раз. Элементы нужно выводить в том порядке, в котором они встречаются в
# списке.
# lst = [1,2,1,3,3,4,5,4,5,6] #ответ нужен 2 и 6
# print(lst)
# tup = tuple(lst)
# print (tup)
# lst1 = []
# for i in range (0,len(tup)):
#     #print(tup.index(tup[i]))
#     #print (i,tup.count(tup[i]))
#     if tup.count(tup[i])==1:
#
#          lst1.append(tup[i])
# print("Элементы, которые не повторяются: ", lst1)

# 2. Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
# Считается, что любые два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать.
#Решение, которое работает, если предположить, что цифры повторяются максимум 2 раза
# lst = [1,2,1,3,3,4,5,4,5,6]
# lst1 = []
# set =set(lst)
# print(len(lst))
# print(len(set))
# pars = (len(lst) - len(set))//2
# print("Всего",pars,"пар")

#ПОЛНОЕ РЕШЕНИЕ
"""lst = (1,1,1,1,1)
lst1 = []
lst2 = []
tup = tuple(lst)
print(tup)
summa1 = 0
summa = 0
for i in range (0,len(tup)):
    #print(tup.index(tup[i]))
    #print (i,tup.count(tup[i]))
    if tup.count(tup[i])>1:
        #print(tup.count(tup[i])%2)
        if tup.count(tup[i])%2 ==0:#если количество повторений чётное
            lst1.append(tup[i]) #Создаём список из повторяющихся в кортеже элементов
            summa1=len(lst1)
        #print(tup[i], "встречается", tup.count(tup[i]), "раз")
        # print(lst1)
        # print("всего",summa//2,"пар")
        if tup.count(tup[i])%2 !=0: #если количество повторений нечётное
            lst2.append(tup[i])  # Создаём список из повторяющихся в кортеже элементов
            summa = len(lst2)
   
summa_all = (summa1+summa)//2
print("всего",summa_all,"пар")
"""
# 3. Даны два кортежа:
# C1 = (35, 78,21,37, 2,98, 6, 100, 231)
# C2 = (45, 21,124,76,5,23,91,234)
# Необходимо определить:
# 1) Сумма элементов какого из кортежей больше и вывести соответствующее
# сообщение на экран (Сумма больше в кортеже - ..)
# 2) Вывести на экран порядковые номера минимальных и максимальных элементов
# этих кортежей
# print(sum(C1))
# print(sum(C2))
# if (sum(C1))>(sum(C2)):
#     print("Сумма больше в кортеже C1")
# else:
#     print("Сумма больше в кортеже C2")
# # print("максимальное и минимальное значение первого кортежа",max(C1), min(C1))
# # print("максимальное и минимальное значение второго кортежа",max(C2), min(C1))
# lst1 = list(C1)
# lst2 = list(C2)
#
# print(lst1.index(max(lst1)),"индекс максимального значения в первом кортеже")
# print(lst1.index(min(lst1)),"индекс минимального значения в первом кортеже")
# print(lst2.index(max(lst2)),"индекс максимального значения во втором кортеже")
# print(lst2.index(min(lst2)),"индекс минимального значения во втором кортеже")

# 4. Создайте словарь из строки ' An apple a day keeps the doctor away' следующим
# образом: в качестве ключей возьмите символы строки, а значениями пусть будут
# числа, соответствующие количеству вхождений данной буквы в строку.
# s = ' An apple a day keeps the doctor away'
# # lst = list[s]
# # print(lst)
# tup = tuple(s)
# tup1 = ()
# tup2 = ()
# lst1 = []
# lst2 = []
# d = dict()
# print(tup)
# summa = 0
# for i in range (0,len(tup)):
#           print(tup[i], "встречается", tup.count(tup[i]), "раз")
#           key = tup[i]
#           value = tup.count(tup[i])
#           d[key] = value  # присваеваем значение ключу
# print(d)

# 5. Клиент приходит в кондитерскую. Он хочет приобрести один или несколько видов
# продукции, а также узнать её состав.
# Реализуйте кондитерскую.
# У вас есть словарь, где ключ – название продукции (торт, пирожное, маффин и
# т.д.). Значение – список, который содержит состав, цену (за 100гр) и кол-во (в
# граммах).
# Предложите выбор:
# 1. Если человек хочет посмотреть описание: название – описание
# 2. Если человек хочет посмотреть цену: название – цена.
# 3. Если человек хочет посмотреть количество: название – количество.
# 4. Всю информацию.
# 5. Приступить к покупке:
# С клавиатуры вводите название торта и его кол-во. n – выход из программы.
# Посчитать цену выбранных товаров и сколько товаров осталось в изначальном
# списке
# 6. До свидания
# d = {"торт":["состав1","500","500"], "маффин":["состав2","100","300"], "пирожное":["состав3","900","1000"]}
# # for key in d:
# #     print(key)
# n=input('введите название торта: ')
# if n not in d.keys():
#    print("к сожалению такого товара у нас еще нет, но мы обязательно приготовим его для вас в следующий раз")
# if n in d.keys():
#    c = int(input(" Если вы хотите прочитать состав торта - нажмите 1\n "
#                  "Если вы хотите узнать цену - нажмите 2\n "
#                  "Если вы хотите узнать количество торта - нажмите 3\n "
#                  "Если вы хотите узнать всю информацию - нажмите 4\n"
#                  "Если вы хотите перейти к покупке - нажмите 5\n"
#                  "Если вы хотите закончить - нажмите 6\n"))
#    if c ==1:
#         print(n,d[n][0])
#    if c ==2:
#        print(n,d[n][1])
#    if c ==3:
#        print(n, d[n][2])
#    if c ==4:
#        print(n, d[n])
#    if c ==6:
#        print("До свидания!")
#    if c ==5:
#        n = input("Введите название торта, который вы хотите купить: ")
#        b = int(input("введите сколько грамм торта вы хотите купить: "))
#        if b >int(d[n][1]):
#          print("сейчас в наличии только: ",d[n][1],"грамм")
#
#        else:
#        # print(d[n][1])
#             summa = (int(d[n][1]))*b
#             print(n, summa,"рублей ваша сумма за", b,"грамм")
#
#             d[n][1] = int(d[n][1]) - b
#        print(d)
# 6. Даны два списка чисел. Посчитайте, сколько чисел содержится одновременно как в
# первом списке, так и во втором.
# lst1 = [1,2,3,4,5,6]
# lst2 = [4,5,6,7,8]
# lst3 = []
#
# for i in lst1:
#     if i in lst1 and i in lst2:
#         lst3.append(i)
# print(len(lst3))

#Решение через множества:
# lst1 = [4,5,10]
# lst2 = [1,2,3,4,5,6,7]
# set1 = set(lst1)
# set2 = set(lst2)
# print(set1)
# len1 = print(len(set1))
# print(set2)
# len2 = print(len(set2))
# if len(set1)>len(set2):
#     set1.update(lst2)
#     print(set1)
#     lst3 = list(set1)
#     print(len(lst3))
#     b = print(len(set1)+(len(set2))-len(lst3)-1,"повторяющихся символа")
# if len(set1)<=len(set2):
#     set2.update(lst1)
#     print(set2)
#     lst3 = list(set2)
#     print(len(lst3))
#     b = print(len(set1)+(len(set2))-len(lst3)-1,"повторяющихся символа")

# 7. Напишите программу, демонстрирующую работу try\except\finally
# d = {1:1,2:2,3:3}
# try:
#     value = d[5]
# except KeyError:
#     print("Произошла ошибка KeyError!")
# finally:
#     print("Оператор finally выполнен!")


# 8. В текстовый файл построчно записаны фамилия и имя учащихся класса и его
# оценка за контрольную. Вывести на экран всех учащихся, чья оценка меньше 3
# баллов и посчитать средний балл по классу
# input.txt:
# Иванов Пётр : 5
# Петров Иван : 4
# Сидоров Вася : 3
# Васин Петя : 5
# Серый Женя : 2
# Женина Катя : 5
# Васина Маша : 2

# d={}
# s=''
# with open ('input.txt','r',encoding='utf-8') as f:
#     for line in f:
#         key=line.rstrip().split()[3]
#         #print(key, end =" ")
#         value = str(f'Ученик {line.split()[0][0::]} {line.split()[1][0::]}  ')
#         #print(value, end =" ")
#         if key not in d.keys():
#              d[key]=value
#         else:
#              d[key] = d[key]+value #чтоб по одной оценке сразу в словаре шло перечисление всех ученико в с это фамилией
#     print(d)
# for key in d:
#     if key <= "3":
#         print(key,d[key])
# n=input('введите оценку: ')
# if n in d.keys():
#     print(d[n])
