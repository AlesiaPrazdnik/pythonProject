"""s = "hello world hi Wowa"
print(s.split())
print(s.split(maxsplit=1)) #разбитие строки по разделитею и заданному количеству разделителей"""
#s.swapcase
#Выучи все функции строк !!!!!
#s.
#len() - длина итерируемого обекта
import random

"""print(len([4,2,1,4]))
print(len(kgkgkg))"""

#Решение можно сразу записать в функци принт, если задано 1 или 2 простых условий
"""a = int(input("enter number:"))
print('чётное' if a%2 == 0 else "нечётное")"""

#import random # подключение модуля
#print(random.random()) # вывод случайного числа от 0 до 1
#print(random.randint(1,100)) #выведет произвольное число, от 1 до 100, включая 1 и 100, границы можно задавать любые
#print(random.choice("hello world")) #выводит сулчайный символ из введённой строки, если ввести 1 число, то не работает,
# если ввести список чисел, то работает:
#print(random.choice([23,13,24,5]))
#\t - табуляция(4 пробела)
#\n - переход на новую строку
#\r - перенос курсора(каретки)
#\a - звуковой сигнал
"""i = 1
while i<=100:
    number = random.randint(1,7)
    print(number, end="\n ") #с переходом на новую строку(\n)
    i+=1"""
"""print('hello\t\tworld') #выведет с двойной табуляцией"""

# СЛОЖНЫЕ ЦИКЛЫ

"""for i in range(1,5): # внешний цикл
    print('i=',i)
    for j in range(1,5): #вложенный цикл
         #print(f'i={i} j={j}') #распечатывает подробно как работает цикл
         print(j,end= ' ')
    print()"""
#выведет по другому, табличкой квадратной
"""for i in range (1,4):
    for j in range(1,4):
        print(i,end=" ")
    print()"""

# выведет лесенкой
"""for i in range(1,4):
    for j in range(1, i+1): #когда i равно 1 - g будет 1 раз ( конец цикла не учитывется)б когда i = 2,j будет крутиться 2 раза и тд
        print(i, end=" ")
    print()"""
# выведет просто цифры от 1 до 3 в столбик
"""for i in range(1,4):
    for j in range(1, i+1): #когда i равно 1 - g будет 1 раз ( конец цикла не учитывется)б когда i = 2,j будет крутиться 2 раза и тд
        print(i, end=" ")
        break
    print()"""

#Проверить простое ли число (простое - значит делится только на себя и на 1, то есть имеет всего 2 делителя
"""number = int(input('enter number:'))
count = 0 # вводим переменную для подсчёта количества действий ( количества делителей)
for i in range (1,number + 1): # перебор всех чисел от 1 до нашего числа включительно
    if number%i==0: #если делится  на i без остатка
        count += 1 # увеличивается количество подсчётов
if count == 2: #делителя всего 2
    print('простое')
else: # в любом другом случае
    print("состовное")"""

#Можно ту же задачу упростиь. Любое число делится на 1 и на само себя. Поэтому берем меньший отрезок в цикле, исключая 1 и само число n
"""number = int(input('enter number:'))
count = 0  # вводим переменную для подсчёта количества действий ( количества делителей)
for i in range(2, number):  # перебор всех чисел от 1 до нашего числа включительно
        if number % i == 0:  # если делится  на i без остатка
            count += 1  # увеличивается количество подсчётов
            break
if count == 0:  # делителя всего 2
    print('простое')
else:  # в любом другом случае
    print("состовное")"""
#можно ещё упростить - если у числа до середины этого числа нет делителей, то и дальше их не будет,
# то есть можно сократить количество проверок(интераций) и задать for i in range(2, number//2+1)

#вывести все простые числа от 2 до 100

#Здесь нам не надо вводить number, у нас задан отрезок
"""for j in range (2,100):
    count = 0  # вводим переменную для подсчёта количества действий ( количества делителей)
    for i in range(2, j//2+1):  # перебор всех чисел от 1 до середины нашего числа включительно
        # (если до середины числа делителей нет, то и дальше их не будет)
        if j % i == 0:  # если делится  на i без остатка
            count += 1  # увеличивается количество подсчётов
            break
    if count == 0:  # делителя всего 2
        print(j,end=" ")"""


#Та же задача через while:
"""j = 2
while j <=100:
    count = 0
    for i in range(2, j // 2 + 1):  # перебор всех чисел от 1 до середины нашего числа включительно
        # (если до середины числа делителей нет, то и дальше их не будет)
        if j % i == 0:  # если делится  на i без остатка
            count += 1  # увеличивается количество подсчётов
            break
    if count == 0:  # делителя всего 2
        print(j, end=" ")
    j+=1 #ВАЖНО!!! Добавить шаг после выполнения цикла, иначе бесконечно выводится первое число"""

# повторяем вывод строк.
# Вывод по элементам, в столбик
"""s = "hello world"
for elem in s:
    print(elem)"""
# Вывод по индексам строки, используется когда нужно работать с отделными буквами например
"""s = "hello world"
for i in range(len(s)):
    print(s[i])"""
#То же самое через while:
"""s = "hello world"
i = 0
while i<len(s):
    print(s[i])
    i +=1"""



