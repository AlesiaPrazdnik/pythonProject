# 1.Создать текстовый файл и записать в него 6 строк.
# Записываемые строки вводятся с клавиатуры.
# f = open("test1.txt","w",encoding ="utf-8")
# for i in range(6):
#     s =input("enter string: ")
#     f.write(s)
#     f.write("\n")
# 2.В конец существующего текстового файла записать три новые строки текста.
# Записываемые строки вводятся с клавиатуры.
# f = open("test1.txt","a",encoding ="utf-8")
# for i in range(3):
#     s =input("enter string: ")
#     f.write(s)
#     f.write("\n")
# 3. Дан текстовый файл. Подсчитать количество символов в нем. Без \n
# lst = []
# with open("test1.txt","r",encoding='utf-8')   as f:
#     for line in f:
#         lst.extend(line.rstrip().split())
# with open("test1.txt","w",encoding="utf-8") as f:
#    for el in lst:
#        s = "".join(el) #вывод в одну строкуБесли между ковычками поставить пробел, то выведет каждую букву с новой строки и тогда длина будет 1
#        f.write(s)
#        print(s)
#        print(len(s))

# 4. Имеется текстовый файл, содержащий 5 строк.
# Переписать каждую из его строк в список в том же порядке.
# lst = []
# with open("test1.txt","r",encoding='utf-8')   as f:
#     for line in f:
#         lst.extend(line.rstrip().split())
#     print(lst)
# 5. Имеется текстовый файл. Получить текст, в котором в конце
# каждой строки из заданного файла добавлен восклицательный знак.
# f = open("test1.txt","r",encoding ="utf-8")
# s = f.read()
# print(s)
# s = s.replace("\n","!\n")
# print(s,end = " ")

# 6. Имеется текстовый файл.
# -Найти длину самой длинной строки.
# -Найти номер самой длинной строки. Если таких строк несколько,
# то найти номер одной из них.
# -Напечатать самую длинную строку.
# Если таких строк несколько, то напечатать первую из них.
# lst = []
# with open("test1.txt","r",encoding='utf-8') as f:
#     for line in f:
#         lst.extend(line.rstrip().split())
#     print(lst)
# lst2 = []
# for el in lst:
#         d = (len(el))
#         print(d)
#         lst2.append(d)
# print(lst2)
# print("максимальное количество символов: ", max(lst2))
# print("номер строки с максимальным количеством символов: ",lst2.index(max(lst2))+1)
# p = lst2.index(max(lst2))+1
#
# for i in range(len(lst)):
#     if len(lst[i-1])> len(lst[i]):
#         print(lst[i-1])

#  7. Создать файл input.txt и записать в него 10 чисел через пробел.
#  Считать из него эти числа. Затем записать их произведение в файл output.txt.
# i = 0
# lst = []
# count = 0
# while i<10:
#      number = int(input("Enter number: ")) #вводим 10 чисел
#      lst = lst+[number]
#      i +=1
# print(lst)
# f = open("input.txt","w",encoding ="utf-8")#эту часть делаем для записи в файл
# s = str(len(lst))
# # f.write(s)
# # f.write("\n")
# for i in lst:
#      s = str(i)
#      f.write(s +' ')
# f = open("input.txt","r",encoding ="utf-8") #эту часть делаем для читывания с файла
# s = f.read()
# print(s)
# lst1 = []
# import functools
# summa = (functools.reduce(lambda a,b:a*b,lst))
# print(functools.reduce(lambda a,b:a*b,lst)) #нашла решение на форуме, ищет произведение чисел списка
# lst1.append(summa)
# print(lst1)
# f = open("output.txt","w",encoding ="utf-8") #создание файла текстов
# with open("output.txt","w",encoding="utf-8") as f:
#     f.write(str(summa)) #записывает файл только строчные значения


# 8. Имеется текстовый файл. Все четные строки этого файла записать
# во второй файл, а нечетные — в третий файл.
# Порядок следования строк сохраняется.
# count = 0
# lst1 = []
# lst2 = []
# with open("test1.txt", "r", encoding="utf-8") as f:
#     for line in f:  # считывание построчно!
#         count += 1
#         if count %2 ==0:
#             print(line)
#             lst1.append(line)
#         else:
#             lst2.append(line)
#     print(lst1)
#     print(lst2)
# f = open("test3.txt", "w", encoding="utf-8")  # создание файла текстов
# with open("test3.txt", "w", encoding="utf-8") as f:
#         for el in lst1:
#             s = " ".join(el)
#             f.write(s + " ")
# f = open("test4.txt", "w", encoding="utf-8")  # создание файла текстов
# with open("test4.txt", "w", encoding="utf-8") as f:
#         for el in lst2:
#             s = " ".join(el)
#             f.write(s + " ")

# 9. Имеются два текстовых файла с одинаковым числом строк.
# Выяснить, совпадают ли их строки. Если нет, то получить номер первой строки,
# в которой эти файлы отличаются друг от друга.

# count=0 # вводим счётчик чтоб считать строки
# with open ('test3.txt','r',encoding='utf-8') as f:#делаем списки из наших файлов
#     lst4 = f.read().rstrip().split()
# with open('test4.txt', 'r', encoding='utf-8') as d:
#     lst5 = d.read().rstrip().split()
# print(lst4, lst5)
# for i in range(len(lst4)):
#     if i<len(lst5):
#         if not lst4[i]==lst5[i] or i==len(lst4):
#             print(f'файлы отличаются друг от друга с {i+1} строки')
#             break
#         count+=1
#     else:
#         print(f'файлы отличаются друг от друга с {i + 1} строки, '
#               f'во втором файле лишь {i} строк')
# if len(lst4)==len(lst5)==count:
#     print('текст в файлах одинаковый')
# if len(lst4)<len(lst5) and count==len(lst4):
#     print(f'файлы отличаются друг от друга с {count + 1} строки, '
#           f'в первом файле лишь {count} строк')
# #
# 10. В справочной аэропорта хранится расписание вылета самолетов
# на следующие сутки. Для каждого рейса указаны номер рейса,
# пункт назначения, время вылета. Вывести все номера рейсов и время
# вылета самолета для заданного пункта назначения.
#Решение:
#Это мой пример записи, но при нём в словаре остётя только 1 рейс в каждый город
# Минск, рейс 16: время вылета 14.00
# Минск, рейс 18: время вылета 15.15
# Москва, рейс 10: время вылета 20.00
# Москва, рейс 1: время вылета 12.10
#
# d = {}   #создаём словарь
# with open("test1.txt","r",encoding="utf-8") as f:
#     for line in f: #считывание построчно!
#         lst = line.rstrip().split(", ")    #разделяем по двоеточию и пробелу после него!!!!
#         #print(lst)
#         key = line.rstrip().split(", ")[0]      #вывели отдельно ключи
#         value = line.rstrip().split(", ")[1].split(" ") #вывели отдельно значения
#         # print(key)
#         # print(value)
#         #d[key]= value  #создаём словарь
#     print(d)
#     # print(d.keys())
#     # print(d.values())
#     lst1 = []
#     n = input('введите направление: ')
#     if n in d.keys():
#         print(d[n])

#РЕШЕНИЕ ВЕРНОЕ:
# B8500: Москва 08.10
# B9600: Екатеринбург 10.10
# B1085: Саратов 12.40
# А6900: Киев 14.30
# B6900: Севастополь 17.10
# B8506: Сыктывкар 19.20
# B5200: Санкт-Петербург 20.50
# B8500: Москва 22.10
# d={}
# s=''
# with open ('test1.txt','r',encoding='utf-8') as f:
#     for line in f:
#         key=line.rstrip().split()[1]
#         value = str(f'рейс {line.split()[0][0:5]}, время вылета: {line.rstrip().split()[2]}. \n')
#         if key not in d.keys():
#             d[key]=value
#         else:
#             d[key] = d[key]+value
#     print(d)
#
# n=input('введите направление: ')
# if n in d.keys():
#     print(d[n])
# Дополнительные задачи:
# 11. Ведомость студентов, сдававших сессию, содержит ФИО и
# оценки по четырем предметам. Вывести список студентов,
# сдавших сессию со средним баллом больше 7.
#
# 12. В файле записаны в столбик целые числа. Отсортировать их по
# возрастанию суммы цифр и записать в другой файл.
#
# 13. Вашей задачей будет восстановление исходной строки обратно. Напишите
# программу, которая считывает из файла строку, соответствующую тексту,
# сжатому с помощью кодирования повторов, и производит обратную операцию,
# получая исходный текст. Для решение вам необходимо открыть файл для чтения 13.txt
# Sample Input:
# a3b4c2e10b1
# Sample Output:
# aaabbbbcceeeeeeeeeeb