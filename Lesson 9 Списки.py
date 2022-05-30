# #list cmprehension
import random
#
# lst = []
# n = int(input())
# for i in range(n):
#     x = int(input())
#     lst.append(x)
# print(lst)
#
# # [что хотите добавить for переменная-счётчик in range(диапозон)]
# n = int(input())
# lst = [ i for i in range(1,n)] #составит список от 1 до заданного чиcла n
# print(lst)
#
# print([random.randint(1,10) for i in range(1,n+1)]) #рандомно составить список
# print([str(random.randint(1,10))for i in range(1,n+1)]) #рандомно но преобразовано в строки
#
# s =  "hello"
# print([i for i in s]) #список  из букв в заанном слове
#
# print([int(i) for i in input().split])# для задания списка из ЧИСЕЛ выводимыз с клавиатуры


# n = int(input())
# print([i for i in range(1,n+1) if i % 2 == 0 and i % 3 ==0])# выводим сптском числа в диапозоне от 1 до n, если число чётное и кратное 3
# print ([i if i%2 ==0 else "hello" for i in range(1,n+1)])# если число чётное, то пишем это число, если нечётное, то заменяем его на hello
# print([i**5 if i %2 ==0 else i**0.5 for i in range(1, n+1)]) #если чётное, то возвести в 5ю степень, если нечётное, то извлечь корень

#СОРТИРОВКА

# lst = [int(i) for i in input().split()]
# lst.sort() #сортировка в возрастающем порядке
# print(lst)
# lst.sort(reverse = True)#сортировка в обратном порядке
# print(lst)
#
# lst = [int(i) for i in input().split()]
# lst.sort()
# print(lst)
# lst.sort(key=abs) #abs  - это модуль числа, abs в данном случае записываем без скобок
#
# #запишем как строки: Здесь сортировка будет идти по таблице индексов
# lst = [i for i in input().split()]
# lst.sort()
# print(lst)
#
# lst = [i for i in input().split()]
# lst.sort(key = len) #сортировка по длине строк
# print(lst)
# lst = [int(i) for i in input().split()]
# lst.sort(key = lambda  x: x%10) #сортировка списка будет по последней цифре числа
# print(lst)
# n = 10
# print([i**2 for i in range(random.randint (1,10))])

# count = 0
# while count <=10:
#      print([i**2 for i in range(random.randint (1,10))])
#      count +=1
# i = random
# count = 0
# while count <=10:
#     print([i ** 2 if count<10 else i == None for i in range(random.randint(1,10))])
#     count += 1