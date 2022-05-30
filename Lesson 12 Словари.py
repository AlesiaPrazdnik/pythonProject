# d = {1:24,5:52, 25:10}
# #keys 1 5 25
# #values: 24 52 10
# print(d[5]) #выведет 52
# # по ключам можно менять значения
# # ключи в словаре уникальны и не могут повтрояться
# d[1] = 65 #заменит 24 на 65
# d[23] = 40 #добавит ключ и значение в наш словарь

# d = {2:21,6:24, 7:34}
# print(d.keys()) #выводит кортеж ключей списком
# lst = list(d.keys()) #создаём список из словаря по ключам
#lst2 = list(d.values()) #создаём список из словаря по значениям
# print(lst)
# print(d.values())#выведет все значения
# d.update({8:14}) #добавляем в наш словарь ещё один словарь
# t = d.pop(2) #удалили по ключу, ео можно вывести как переменную
# print(t)
# print(d)
#print(sum(d.values())) # вывести сумму значений
#print(sum(d.keys()))# вывести сумму ключей

#d = {2: 21, 6: 24, 7: 34}
# for key in d:
#     print(key,d[key])
# for key, value in d.items():
#     print(key,value)
# for el in d.items():
#     print (el) #выведет как кортеж
#     print(el[0],el[1])#как элементы кортежа


# key = int(input())
# if key in d:
#     print("yo") #пишем yo и удаляем!
#     del d[key]
# else:
#     print("not yo")
# print(d)

#Как добавить ключа и значеня в пустой словарь
# d = dict()
# n = int(input())
# for i in range(n):
#     key = input() #ключи у нас строки
#     value = int(input()) #а значения = цифры
#     if key not in d:
#         d[key] =value #если такого ключа у нас нет, о присваиваем ему значение
# print(d)

#объеинение двух списков в словарь
# d = dict(zip([1,2,3],['one','two','three']))
# print(d)

#Перемножить все значения словаря
# d = {2: 21, 6: 24, 7: 34}
# res = 1
# for value in d.values():
#     res *= value
# print(res)

# #Вывести словарь по элементам, словарь состоит из разнотипных элементов
# d = {2: [2, 41], "hello": 24, 7: ("11","23")} #словарь с разныеи данныеми, список, слова, кортеж
# print(d)
# for key in d:
#     if type(key) ==list ==list or type(d[key]) == tuple:
#         print(key, ":", end = ' ')
#         for el in d[key]:
#            print(el,end = ' ')
#         print()
#     else:
#         print(key,":", d[key])

#Словарь, в котором значения = вложенный словарь. отдельно вывести каждый элемент
# d = {
#         'key1': {"key11":1,"key12":2},
#         'key2': {"key21":1,"key22":2},
#         'key3': {"key31":1,"key32":2}
# }
# for key in d:
#     print(key,":", end =" ")
#     for key_wrapper in d[key]:
#         print(key_wrapper, d[key][key_wrapper], ",", end = " ")
#     print()
