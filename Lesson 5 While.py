#Цикл While
# вывести  все трёхзначные числа, сумма цифр которых равна 10
"""number = 100 #начало
while number <= 999: #вводим условие, пока число меньше 1000
    s = number //100 + number%10 + number // 10 % 10 # вводим s
    if s == 10:#и при этом сумма цифр равна s
        print (number, end=" ") # тогда выводим нашу цифру

    number += 1 #далее переходим к следующему числу увеличивая number на 1"""

#найти сумму пяти чисел, введённых с клавиатуры, с помощью while
"""count = 1 #вводим переменную, которая обозначает количество чисел от которой будем считать
s = 0 # переменная для подсчёта суммы
while count <= 5: # проверка истинности условий
    number = int(input("enter number:")) # ввод числа с клавиатуры (пока не будет 5 введений, будет выводить эту надпись)
    s += number # прибавление к сумме ( к нулю) числа number
    count += 1 # увеличение счётчика для дальнейшего завершения условия
print(s)   """

#посчитать сумму чисел пока не введём 0
"""number = int(input("enter number:"))
s = 0
while number != 0: #пока число не равно нулю
    s = number + s
    number = int(input("enter number:"))
print("s = ",s)"""
#Решить эту же задачу, только используя бесконечный цикл
"""s = 0
while True: #это конструкция бесконечного цикал, пока верно: выполняем
      number = int(input("enter number:"))
      s = number + s
      if number == 0: # проверка для выхода из цикла
          break #прервать бесконечный цикл, как только будет введён ноль
print(s)"""

#  та же задача с бесконечным циклом но плюс условие - мы не хотм прибавлять все цифры, кратные пять
"""s = 0
while True: #это конструкция бесконечного цикла, пока верно: выполняем
      number = int(input("enter number:"))
      if number % 5 ==0 and number != 0: #проверка кратности 5
          continue # если кратно 5 то не прибавляем, пропускаем и продолжаем проверку
      if number == 0: # проверка для выхода из цикла
          print('s =',s)
          break #прервать бесконечный цикл, как только будет введён ноль
      s += number
#print(s)"""

#посчитать сумму чисел пока не введём 0 без бесконечного цикла, но с break  на цифре 5 и else
"""number = int(input("enter number:"))
s = 0
while number != 0: #пока число не равно нулю
    s += number
    number = int(input("enter number:"))
    if number == 5:
         break
else: #else относится к break. Если цикл завершается по невыполнению условия, то выводится команда else
    # если же цикл был прерван ( сработал break, то есть была введена 5), то срабатывает блок else
    print("цикл не был прерван")
print("s = ",s)"""

# Сложить все цифры n-значного числа
# для решения этой задачи мы должны число разложить на цифры, делать это будем через деление на 10 с
#остатком. то есть поделили например 234 на 10 с остатком и получили в остатке 4, отсекли этот остаток,потом поделили
# 23 на 10, получили остаток 3, тоже его отсекли и так до нуля. Потом все остатки нужно сложить.
"""number = int(input("enter number:"))
s = 0 #вводим переменную для просчёта нашей суммы
while number !=0:
    s += number %10 # делим наше число на 10 c остатком, то есть находим последнюю цифру и прибавляем к s
    number = number // 10 # отсекаем последнюю цифру, делим без остатка
    print(number) #это для понимания что происходит вывоим, можно не выводить, тогда сразу ответ будет
print(s)"""

#Найти количество пятёрок в n - значном числе
"""number = int(input("enter number:"))
count = 0 #вводим переменную для просчёта нашей суммы
while number !=0:
    if number % 10 == 5:
      count += 1
    number = number // 10
print(count)"""

# вывести все делители числа
# Например для числа 12 это ответ 1 2 3 4 6 12
"""number = int(input("enter number:"))
i = 1 # это переменная, которая будет отвечать за наш делитель, то есть это число от 1 до числа number
count = 0 #это переменна, которая будет отвечать за количество делителей
while i<=number:
    if number % i ==0: # проверка делимости number на i
        count += 1
        print(i,end = " ") #выводит число с пробелом
    i+=1
print ("count =", count)
if count == 2: # проверка на простое число(делится на себя и на 1 только)
    print(" число простое")"""

# Дано два числа, вывести общие делители этих двух чисел
"""number1, number2 = map(int,input().split())
i = 1 # это переменная, которая будет отвечать за наш делитель, то есть это число от 1 до числа number
while i <=number1 and i <=number2: #делитель должен быть меньше обоих чисел, начинаем проверку с делителя = 1
    if number1 % 1 == 0 and number2 % i == 0: #если оба числа делятся на делитель без остатка то выводим этот делитель
        print(i,end =" ")
    i += 1 #переходим к следующему делителю, проверяем делитель 2, затем делитель 3 и т д, пока делитель меньше обоих чисел"""

#Найти общий НАИБОЛЬШИЙ делитель у двух чисел Алгоритм Евклида
"""n1, n2 = map(int,input().split())
while n1 != 0 and n2 != 0:
    if n1>n2:
        n1 = n1 - n2 #можно делить с остатком n1 = n1 % n2 #новое n1 получаем
    else:
        n2 = n2 - n1 #можно делить с остатком n2 = n2 % n1 # новое n2 получаем
nod = n1 + n2
print ("nod =", nod)"""

