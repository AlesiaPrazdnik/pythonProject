#Режимы доступа к файлам:
#r (read) - считываем
#w (write) - записываем, полностью всё стирается и записываеься новая инфо!!!
#a (append) - дозапись
# ЗАПИСЬ И ДОЗАПИСЬ ФАЙЛОВ
# f = open("test1.txt","w",encoding ="utf-8") #создание файла текстового
# s =input("enter string: ")         #ввод с клавиатуры
# f.write("Hello world \n")        #\n - перенос на новую строку
# f.write ("ned help")
# f.write(s+"\n")               #склеивание с пробелом
# for i in range(2):            #сдлали цикл на ввод информации  клавиатуры
#     s =input("enter string: ")
#     f.write("Hello world \n")
# lst = [2,4,5,1,51,2,1]
# for el in lst:
#     f.write(str(el) + "\n") #так как в файл можно только строки записывать
# d = {"Иванов Иван":[4,2,1,5,2], "Петров Пётр":[5,3,2,4,5], "Сидоров Сидор":[3,4,5,3,4]}
# for key,value in d.items():
#     f.write(key+":")
#     for el in value:
#         f.write(str(el)+" ")
#     f.write("\n")
#f.close() #закрытие файла! Обязательно!

#СЧИТЫВАНИЕ ФАЙЛОВ
# try:
#     f = open("test1.txt","r",encoding ="utf-8")  #r - read
#     s = f.read()
#     print(s)
#     #repr = позволяет увидить все скрытые символы
#     s = s.replace("\n"," ")      #поменяли скрытые символы на пробелы
#     s = s[:-1] #так можно избавится от последнего символа, если он скрытый
#     s = s.rstrip()    #убирает все вспомогательные символы в конце
#     print(repr(s)) #можно вывести все скрытые символы
#     lst = s.split()    #то же самое вывести как список
#     print(s)
#     print(lst)
#     f.close  ()
# except FileNotFoundError:
#     print("file not found")

#Чтение данных из файла. Конструкция with as
#with open("test1.txt","r",encoding='utf-8')   as f: #эта конструкция нужна, чтобы не использовать постоянно close file
   # s = f.read()
   # s = f.read(9) #выведет первых 9 символов
   #s = f.readline()   #выведет первую строку
   #s = f.readline().rstrip()      # выведет первую строку без пробела в конце
    #print(s)
# lst = []       #то же самое, но через  создать список
# with open("test1.txt","r",encoding='utf-8')   as f:
#     s = f.read()
#     lst.append(s)
#     s = f.read(9)
#     lst.append(s)
#     s = f.readline()
#     lst.append(s)
# print(lst)
# lst = []       #то же самое, но чтоб каждое слово было элементом списка
# with open("test1.txt","r",encoding='utf-8')   as f:
#     s = f.read()
#     lst.extend(s)
#     s = f.read()
#     lst.extend(s)
#     s = f.readline()
#     lst.extend(s)
# print(lst)

# lst = []       #то же самое, но короче, чтоб каждое слово было элементм списка
# with open("test1.txt","r",encoding='utf-8')   as f:
#     for line in f:
#         lst.extend(line.rstrip().split())
#     print(lst)

#d = {}   #создаём словарь
# with open("test1.txt","r",encoding="utf-8") as f:
#     for line in f: #считывание построчно!
#         # lst = line.rstrip().split(": ")    #разделяем по двоеточию и пробелу после него!!!!
#         # print(lst)
#         key = line.rstrip().split(": ")[0]      #вывели отдельно ключи
#         value = line.rstrip().split(": ")[1].split(" ") #вывели отдельно значения, чтоб каждое было отдельно - разделяем ковычками
#         # print(key)
#         # print(value)
#         value = list(map(int,value))   #получение списов чисел
#         print(value)
#         d[key]= value  #создаём словарь
#     print(d)

#Имеется текстовый файл. Переписать в другой файл все его строки
#с заменой в них символа 0 на символ 1 и наоборот
# lst = [] #создаём список для поэлементного считывания
# with open("test1.txt","r",encoding="utf-8") as f:
#      for line in f:                #идём построчно
#         lst.append(line.rstrip().split())
# print(lst)     #получили матрицу!!!
# #как перебирать поэлементно? в строках элементы неизменяемы
# for i in range(len(lst)):      #работаем как с матрицами
#     for j in range(len(lst[i])):
#         #print(lst[i][j],end = " ") #это вывод поэлементно
#          p = list(lst[i][j])#создаем список в списке списка)) и получаем доступ к каждому отдельному элементу списка
#          for k in range(len(p)):      #меняем нули на единицы и наоборот
#              if p[k] =="0":
#                  p[k] = "1"
#              elif p[k] =="1":
#                  p[k] = "0"
#          lst[i][j] = ''.join(p)
#
#          print(lst[i][j],end = " ")
#     print()
# #Если бы только поменять нули на единицы, то можно так:
# #lst[i][j] = lst[i][j].replace("0","1")   #меняем нули на единицы
# with open("test1.txt","w",encoding="utf-8") as f:  #теперь возвращаем всё в наш текстовый файл!!!
#    for el in lst:
#        s = " ".join(el)
#          f.write(s +" ")
#Как открыть текстовый файл, который тебе прислали? охранить на комп и
#указать весь путь, обязательно после диска поставить 2 слэша! энкодинг только если файл на русскомб если на
#английском - не надо энкодинг писать
# with open("C:\\Users\Denis\\test155.txt","r",encoding="utf-8") as f:
#     s = f.read()
#     print(s)