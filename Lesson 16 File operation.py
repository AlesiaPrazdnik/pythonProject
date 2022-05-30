# 1.Список товаров, имеющихся на складе, включает в себя наименование товара,
# количество единиц товара, цену единицы и дату поступления товара на склад.
# Вывести список товаров, хранящихся больше месяца и стоимость которых превышает 1 000 000 р.
#
#Данное решение подходит, когда всё надо вводить с клавиатуры,
# если же список дан заранее: смотри следующее решение (ниже)
#lst =[]
# n = int(input("Введите количество наименований товаров: ")) #количество ввода товаров
# for i in range(n):
#     a = input("Введите наименование  товара: ")
#     b = int(input("Введите количество единиц товара: "))
#     с = int(input("Введите цену единицы товара: "))
#     d = int(input("Введите номер месяца поступления товара на склад: "))
#     e = int(input("Введите номер текущего месяца: "))
#     stoim = b*с
#     srok = e - d
#     if stoim >= 1000000 and srok >1 or srok<0:
#         lst.append(a)
# print(lst)

#  РЕШЕНИЕ С ТЕКСТОВЫМ ФАЙЛОМ:
# Данные для текстового файла:
# Бумага : 1000000, 10, 01
# Стол : 10, 1000, 03
# Вилки : 1000, 13000, 07
# Ложки : 15, 3, 08
# Ножи : 12, 12, 12
# d = {}
# p = int(input("Введите номер текущего месяца: "))
# e = 1
# with open ('input.txt','r',encoding='utf-8') as f:
#     for line in f:  # считывание построчно!
#         lst = line.rstrip().split(":")  # разделяем по двоеточию
#         #print(lst)
#         key = line.rstrip().split(":")[0]  # вывели отдельно ключи
#         value = line.rstrip().split(": ")[1].split(" ") #вывели отдельно значения, чтоб каждое было отдельно - разделяем ковычками  # вывели отдельно значения
#         # print(key)
#         # print(value)
#         d[key] = value  # создаём словарь
#     print(d)
#     for n in d.keys():
#         if (p-(int(d[n][2])))<0 or (p-(int(d[n][2])))>1:
#             print((p-(int(d[n][2]))))
#             print ("Срок хранения больше месяца у товара", n)


#2. На АТС информация о разговорах содержит номер телефона абонента, время разговора и тариф.
# Вывести для заданного абонента сумму, которую ему следует оплатить за разговоры.
#Данные для текстового файла:
# 1111, 3.15, 10
# 2222, 0.25, 12
# 3333, 4.44, 100
# 4444, 6.00, 14
#
# d={}
# #s=''
# with open ('input.txt','r',encoding='utf-8') as f:
#     for line in f:
#         key=line.rstrip().split(":")[0]
#         #print(key, end =" ")
#         value = line.rstrip().split(": ")[1].split(",")
#         #str(f'Ученик {line.split()[0][0::]} {line.split()[1][0::]}  ')
#         #print(value, end =" ")
#         d[key]=value
# print(d)
# """e = 1
# h = 1
# n = input("Введите номер абонента: ") #ВАЖНО!!! СТРОЧНОЕ ЗАЧЕНИЕ!!! не int input, a input
# for key,value in d.items():
#     if n in d.keys():
#          e = e*(d[n])
#          h = h * (d[n][1])
#
#          print(e)
# else:
#     print("no number")"""

# 3. Вам дается текстовый файл, содержащий некоторое количество непустых строк.
# На основе него сгенерируйте новый текстовый файл, содержащий те же строки в обратном порядке.
# Для решение вам необходимо открыть файл для чтения 3.txt .
# Sample Input:
# ab
# c
# dde
# ff
# Sample Output:
# ff
# dde
# c
# ab
#Это решение для перевёрнутых слов
# with open("test3.txt","r",encoding="utf-8") as f:
#     s = f.read()
#     lst = s.split()
#     lst2 = []
#     #print(lst)
#     for el in lst:
#         d = el[::-1]
#         #print(d)
#         lst2.append(d)
#     #print(lst2)
#     p = open("test5.txt", "w", encoding="utf-8")
#     for el in lst2:
#      p.write(str(el) + "\n")

# Это решение для выдачи слов в обратном порядке:
# with open("test3.txt","r",encoding="utf-8") as f:
#     s = f.read()
#     lst = s.split()
#     #print(lst)
#     lst2 = lst[::-1]
#     #print(lst2)
#     p = open("test5.txt", "w", encoding="utf-8")
#     for el in lst2:
#      p.write(str(el) + "\n")

# 4.Написать программу “Викторина”. У вас есть 2 файла содержащих вопросы и ответы
# на данные вопросы.
# Пользователь отвечает на имеющиеся вопросы и затем программа показывает
# сколько правильных ответов было сделано.
# Файл 1:
# 1.Вопрос
# 2.Вопрос
# 3.Вопрос
# 4.Вопрос
# Файл 2:
# 1.Ответ
# 2.Ответ
# 3.Ответ
# 4.Ответ

# d1 ={}
# d2 = {}
# #n = int(input("how many questions you are going to answer: "))
# count = 0
# with open("test5.txt","r",encoding="utf-8") as f:
#         for line in f:  # считывание построчно!
#             lst = line.rstrip().split(".")    #разделяем по точке
#                  #print(lst)
#             key = lst[0]  # вывели отдельно ключи
#             value = lst[1] #вывели отдельно значения
#             d1[key]= value  #создаём словарь
# print(d1)
# with open("test3.txt", "r", encoding="utf-8") as p:
#         for line in p:  # считывание построчно!
#              lst2 = line.rstrip().split(".")    #разделяем по точке
#              key = lst2[0]  # вывели отдельно ключи
#              value = lst2[1]  # вывели отдельно значения
#              d2[key] = value  # создаём словарь
# print(d2)
# print("You will answer", max(d1), "questions")
# #так как ключи одинаковые, перебираем 1 словарь
# for key,value in d1.items():
#     print(value)
#     quest = input("enter your answer: ")
#     if quest==d2[key]:
#         print("Bingo!")
#         count +=1
#     print("Number of correct answers = ",count)

#РЕШЕНИЕ ОТ ДЕНИСА:

# ans = []
# count = 0
# with open("test5.txt", 'r', encoding='utf-8') as f:
#     for line in f:
#         print(line.rstrip())
#         a = input("Ваш ответ: ")
#         ans.append(a)
#     print(ans)
# with open("test3.txt", "r", encoding="utf-8") as p:
#     for line in p:  # считывание построчно!
#         lst2 = line.rstrip()  # разделяем по точке
#         #print(lst2)
# for el in lst2:
#     if el in ans:
#         count += 1
# print("Правильных ответов:", count)

# 5.Дан кортеж. Найти наибольшее из чисел, которые встречаются ровно 2 раза.

# tup = (1,3,3,1,4,4,5,6,7,8,1)
# lst = []
# for i in range (0,len(tup)):
#     if i == tup.index(tup[i]) and tup.count(tup[i])==2: #Это решение находит элемены, которые встречаются ровно 2 раза
#         #print(tup[i], end = "")
#         lst.append(tup[i]) #Создаём список из повторяющихся в кортеже элементов
# print(lst)
# print(max(lst))

#
# 6. Напишите программу, которая считывает текст из файла (в файле может быть больше одной строки)
# и выводит самое частое слово в этом тексте и через пробел то, сколько раз оно встретилось.
# Если таких слов несколько, вывести лексикографически первое.
# Для решение вам необходимо открыть файл для чтения 6.txt .Слова, написанные в разных регистрах,
# считаются одинаковыми.
# Sample Input:
# abc a bCd bC AbC BC BCD bcd ABC
# Sample Output:
# abc 3
# count = 0
# lst = []
# lst1 = []
# lst2 = []
# with open("test4.txt", "r", encoding="utf-8") as f:
#     for line in f:  # считывание построчно!
#         lst = line.rstrip().split(" ")  # разделяем по пробелу
#         #print(lst)
#         for i in lst:
#             d = i.lower()
#             lst1.append(d)
#         print(lst1)
# d = {}
# for i in range (len(lst1)):
#     if i == lst1.index(lst1[i]) and lst1.count(lst1[i])>1:
#          key = lst1.count(lst1[i])
#          value = lst1[i]
#          if key not in d.keys():
#             d[key] = value
#          else:
#             d[key] = d[key] + value
#             #print(max(d))
# # print(d)
# # print(max(d))
# for key in d.keys():
#     if key == (max(d)):
#         a = (d[key])
# print(max(d), "раза повторяется сочетание букв",a)

# 7. Сгенерировать список из 30 чисел, заполнив его случайными значениями от 1 до 100.
# Вывести на экран числа которые являются полными квадратами.
# Числа кратные 5 записать в текстовый файл, остальные сложить.
# И вывести результат сложения на экран.
import math
import random
# lst = ([random.randint(1,100) for i in range(1,31)])
# #lst = [87, 42, 13, 12, 78, 90, 45, 38, 7, 72, 5, 47, 20, 43, 82, 12, 62, 84, 21, 72, 52, 64, 96, 53, 59, 74, 85, 18, 87, 65]
# # print(len(lst))
# print(lst)
# count = 0
# for i in lst:
#     d = math.sqrt(i)
#     #print(d, "это корень из",i)
#     if d %2==0:
#         print(i, "это полный квадрат")
#
# with open ('test1.txt','w',encoding='utf-8') as f:
#         for i in lst:
#             if i%5==0:
#                  print(i, "кратно пяти")
#                  f.write(str(i))
#                  f.write("\n")
#             if i%5 != 0:
#                  count+=i
# print("Сумма чисел, не кратных пяти = ",count)

# 8. Определить, является ли квадратная числовая
# матрица симметричной (относительно главной или побочной диагонали).
# Найти максимальный элемент среди стоящих на главной и побочной диагонали и поменять его местами с элементом,
# стоящим на пересечении этих диагоналей. Матрица нечётная. Генерируем матрицу через генератор в  одну строку.

#НЕ СДЕЛАНО


#9. Компоненты файла f – целые числа, причём десять идущих подряд положительных чисел чередуются с
# десятью отрицательными числами и т. д. Получить файл g из чисел исходного файла,
# в котором записано сначала пять положительных чисел, затем пять отрицательных и т.д.

# lst1 = ([random.randint(1, 100) for i in range(1, 11)])
# lst2 = ([(random.randint(1,100)*(-1)) for i in range(1, 11)])
# lst3 = (lst1 +lst2)
# print(lst3)
# lst4 = []
# with open ('test1.txt','w',encoding='utf-8') as f:
#         for i in lst3:
#                 f.write(str(i))
#                 f.write("\n")
# with open ('test1.txt','r',encoding='utf-8') as f:
#      for line in f:
#         lst4.extend(line.split())
#      #print(lst4)
# lst5 = (lst4[0:5])
# lst6 = (lst4[5:10])
# lst7 = (lst4[10:15])
# lst8 = (lst4[15:20])
# with open('test3.txt', 'w', encoding='utf-8') as p:
#     for i in lst5:
#       p.write(str(i))
#       p.write("\n")
#     for i in lst7:
#       p.write(str(i))
#       p.write("\n")
#     for i in lst6:
#         p.write(str(i))
#         p.write("\n")
#     for i in lst8:
#         p.write(str(i))
#         p.write("\n")
#

#10. Жаркий аукцион.
# Перед началом торгов организаторы аукциона объявляют все предметы, участвующие в аукционе,
# а также начальную цену, с которой начинаются продажи всех предметов.
# Также перед началом аукциона все участники обязаны заявить об участии, указав свое имя.
# Когда начинаются торги, каждый участник имеет право объявить предмет, который он желает приобрести, и новую ставку.
# Если новая ставка больше предыдущей, она принимается организаторами.
# Незарегистрированные участники не могут предлагать ставку.
# Торги заканчиваются фразой организаторов "Аукцион закончен!".
# После этого необходимо вывести результаты аукциона: в каждой строчке необходимо указать предмет,
# имя покупателя, а также итоговую стоимость. Если предмет остался без покупателя,
# вместо этого выведите "Предложений не было".
# Формат ввода: в первой строке – список предметов через запятую;
# во второй – начальная стоимость всех предметов;
# в третьей – список имен участников через запятую;
# в последующих строках до строки "Аукцион закончен!" указываются название предмета,
# имя участника и новая ставка через пробел.
#
# Формат вывода: в каждой строчке находится название предмета,
# имя покупателя и итоговая стоимость, разделенные пробелом.
#
# Sample Input:
# Apple II, компьютерная мышь Lisa, Sony PS1, YIS-805, IBM 5150, Macintosh LC520, Эльбрус 801-PC
# 1500
# Michael, Jake, John, Alex, Jane, Steve
# John YIS-805 2400
# Jane Macintosh LC520 5000
# Jake Macintosh LC520 4000
# Michael IBM 5150 10000
# Alex Apple II 1501
# Steve Apple II 15000
# Sergey Apple II 17000
# Lisa компьютерная мышь 2000
# Jake Sony PS1 4200
# Аукцион закончен!
#
# Sample Output:
# Apple II Steve 15000
#компьютерная мышь Lisa 2000
#Sony PS1 Jake 4200
#YIS-805 John 2400
#IBM 5150 Michael 10000
#Macintosh LC520 Jane 5000
#Эльбрус 801-PC Предложений не было
# d ={}
# lst = []
# h = int(input("Сколько человек будет участвовать в аукционе:"))
# with open('test3.txt', 'r', encoding='utf-8') as f:
#         for line in f:
#             lst.extend(line.rstrip().split(","))
#         print("Список предметов, выставленных в аукцион: ",lst)
# n = int(input("Введте начальную цену: "))
# with open('test3.txt', 'r', encoding='utf-8') as f:
#         for line in f:
#             key=line.rstrip().split(",")[0]
#         #print(key, end =" ")
#             value = n
#         #print(value, end =" ")
#             d[key]=value
# print(d)
# count = 0
# lst1 = []
# while count !=h:
#     name = input("Введите ваше имя: ")
#     if name in lst1:
#         print("Человек с таким именем уже зарегистрирован")
#     if name not in lst1:
#         lst1.append(name)
#         count +=1
#
# print("Список участников аукциона: ", lst1)
# b = len(lst1)
# count1 = 0
# d2 = {}
# while count1 !=b:
#     v = input("Введите ваше имя: ")
#     if v not in lst1:
#             print("Вы не зарегистрированы, пройдите регистрацию")
#     else:
#             for key, value in d.items():
#                 print(key)
#                 g = int(input("Вы хотите сделать ставку на этот предмет? Нажмите 1, ели ДА. Нажмите 0, если нет: "))
#                 if g == 1:
#                     s = int(input("Введите вашу ставку для предмета:"))
#                     if s>d[key]:
#                         d[key] = s
#                         print(v,key,s)
#
#     count1 +=1
# print("Результаты аукциона: ")
# for key, value in d.items():
#     if value>n:
#         print(key,value)
# print("Аукцион закончен!")

bnbnbn