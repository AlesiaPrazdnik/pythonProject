#Дано число n. Вывести все числа от 1 до n.
"""n = int(input("enter number: ")) #вводим число n
s = 1 #водим переменную от которой будем считать, ессли бы в условии было от нуля, то s = 0
while s<=n:#пока наша провеяремая переменная меньше заданного числа n
    print (s) #выводим эту переменную
    s += 1 #и переходим к проверке этих же условий к следующей переменной"""

#Дано число n. Посчитать сумму всех чётных чисел от 0 до n.
"""n = int(input("enter number: ")) #вводим число n
s = 0 #вводим переменную по условию задачи задаём ее равной нулю.
while s<=n: # пока введенная переменная меньше вводимой цифоры
    if s%2 == 0: #и если при этом переменная делится на 2 без остатка
      print(s) #выводим эту переменную
    s += 1 #и переходим к проверке условий для следующей переменной"""

#Дано натуральное число. Определить произведение цифр в нем. учитывать только цифры которые кратны 2.

# для решения этой задачи мы должны число разложить на цифры, делать это будем через деление на 10 с
#остатком. то есть поделили например 234 на 10 с остатком и получили в остатке 4, отсекли этот остаток,потом поделили
# 23 на 10, получили остаток 3, тоже его отсекли и так до нуля. Потом все остатки нужно перемножить, при условии, что они кратны 2.
"""n = int(input("enter number: ")) #вводим число n
s = 1 #вводим переменную для просчёта нашей суммы ( она не может быть равна 0 так как умножение на ноль будет давать ноль)
while n !=0:
     s = s * (n % 10) #s *= n %10 # делим наше число на 10 c остатком, то есть находим последнюю цифру и прибавляем к s
     n = n // 10 # отсекаем последнюю цифру (то, что получилось в остатке)
     print(n) #это для понимания что происходит выводим, можно не выводить, тогда сразу ответ будет
print(s)
s += 1"""
# выше сделано решение, которое даёт произведение всех цифр числа, а как добавить условие четности цифр????

"""n = int(input("enter number: ")) #вводим число n c клавиатуры
s = 1 #вводим переменную для просчёта нашей суммы ( она не может быть равна 0 так как умножение на ноль будет давать ноль)
while n != 0: #пока n не равно нулю
    if n % 2 == 0: # и если проверяемое n изначально чётное
        s *= n % 10 #тогда считаем новое s
    n = n // 10  #и тогда считаем новое n
print(s)
s += 1"""

"""Дано число n. Вывести на экран числа 1, 4, 9, 16, 25, ... которые меньше n.
Sample Input :15
Sample Output :1 4 9"""
"""n = int(input("enter number:"))
#s = 0
while 1<n<26:
     if 1<n<=4:
          print('1')
     if 4<n<=9:
          print("1","4")
     if 9<n<=16:
          print("1", "4", "9")
     if 16<n<=25:
          print("1", "4", "9", "16")
     break #проверить эти условия и прервать цикл"""
#В этом решении не учтена закономерность приведённых чисел, это то, что все эти числа от 1 до бескончености в квадрате
"""n = int(input("enter number:"))
s = 1
while s**2 <= n: #ПОка s в квадрате меньше введённого числа
     print(s**2,end=" ") #выводим это s в квадрате
     s += 1 # и задаём новое s  = старое s плюс 1"""


"""Дано число n. Среди чисел 1, 4, 9, 16, 25, ... найти первое, которые больше n.
Sample Input : 5   Sample Output : 9 """
#Это решение не учитывает, что дана закономерность:
"""n = int(input("enter number:"))
while 1<=n<26:
     if 1 <= n < 4:
          print('4')
     if 4 <= n < 9:
          print("9")
     if 9 <= n < 16:
          print("16")
     if 16 <= n < 25:
          print("25")
     break  # проверить эти условия и прервать цикл"""
#Это решение УЖЕ УЧИТЫВАЕТ, что дана закономерность:
"""Дано число n. Среди чисел 1, 4, 9, 16, 25, ... найти первое, которые больше n.
Sample Input : 5   Sample Output : 9 """
"""n = int(input("enter number:"))
s = 1
while n>0:#пока n > 0 (логичное условие, но подобран методом тыка)
     s += 1 #ничего не выводим, просто ситаем, увеличивая s на 1
     if n < s**2: # как только n оказываетс меньше квадрата s
          print(s**2, end ="") #выводим квадрат s
          break #и прерываемся"""



"""Дано число n. Определить первую цифру этого числа."""
"""n = int(input("enter number:"))
s = 0
while n != 0:
        if n < 10: #если n меньше 10 (первая цифра в любом случае меньше 10
             s+= n % 10 #тогда считаем новое s, оно равно старое s (0) плюс остаток, полученный при делении на 10
             print (s) #и тогда выводим это новое s
        n = n // 10  #и тогда считаем новое n !!!ВАЖНО ГДЕ ПРОБЕЛ ЭТО ЧЕТКО ПОД IF"""
#Возьми число 234. идем по циклу : пока 234 не равно нулю ( не равно), если 234 меньше 10 ( не меньше), значит переходим
# к делению без остатка, остается 23, оно не равно нулю, но оно опять не меньше 10, поэтому опять делим без остатка на 10, получаем 2,
# оно не равно 0 и оно меньше 10, поэтому выводим s, коорое равно 0 ( старая s) + остаток, полученный при делении 2 на 10, то есть 2 и выводим 2


"""Дано число n. Найти сумму цифр в этом числе."""
# для решения этой задачи мы должны число разложить на цифры, делать это будем через деление на 10 с
#остатком. то есть поделили например 234 на 10 с остатком и получили в остатке 4, отсекли этот остаток,потом поделили
# 23 на 10, получили остаток 3, тоже его отсекли и так до нуля. Потом все остатки нужно сложить.
"""n = int(input("enter number:"))
s = 0 #вводим переменную для просчёта нашей суммы
while n !=0:
    s += n %10 # делим наше число на 10 c остатком, то есть находим последнюю цифру и прибавляем к s
    n = n // 10 # отсекаем последнюю цифру, делим без остатка
    print(n) #это для понимания что происходит выводим, можно не выводить, тогда сразу ответ будет
print(s)"""

"""Дано натуральное число n. Найти значение минимальной цифры в данном числе."""
#Если бы число было двузначное, то подошло бы и это решение:
"""n = int(input("enter number:"))
b = n%10
while n !=0:
     n = n//10
     if b > n:
        print (n)
     if b < n:
          print(b)"""
"""Дано натуральное число n. Найти значение минимальной цифры в данном числе."""
#Это верное решение:
"""n = int(input("enter number"))
i = n%10 #это неизменная переменная  и она будет равна последней цифре вводимого числа 
#и именно с этой цифрой мы будем сравнивать все последуюие цифры
n = n//10 #это новая переменная n, так как всё число нам уже не надо, 
#мы отделяем крайнюю цифру ( знаем, что она раван i) и работаем с оставшимся числом
while n!= 0:
     a =n%10 # теперь уже у нового n мы отделяем крайнюю цифру 
     if i>a: #сравниваем эту новую отделённую цифру с  нашим зафикисрованным i  и если a меньше i, 
          i=a #то назначаем a на место i
     n = n//10 #переходим к следующей переменной, оставшейся целой части и снова идём по циклу
print(i) #в итоге выводим то i  которое оказалось самым маленьким"""




#Дополнительные задачи:

"""Дана непустая последовательность натуральных чисел(вводим с клавиатуры в цикле while через int(input())), 
оканчивающаяся отрицательным числом. Найти максимальное число в данной последовательности"""
#Решить эту же задачу, только используя бесконечный цикл
"""s = 0 #вводим переменную, от которой будем считать
while True: #это конструкция бесконечного цикла, пока верно: выполняем
      number = int(input("enter number:")) #вводим любую цифру, это и есть последовательность, так как она зациклина на бесконечность
      s = max(number,s)  #выбирать будем максимальную цифру ключ  s (не понимаю эту запись, нашла методом тыка)
      if number < 0: # проверка для выхода из цикла, то есть пока мы не ввели отрицательное исло, программ будет
           # писать нам "enter number^"как только мы введем отрицательное число,
          print (s)# программа выведет нам максимальное число из всех, которые мы вводили
          break #прервать бесконечный цикл, как только будет введёно отрицательное число"""

"""Дана непустая последовательность натуральных чисел(вводим с клавиатуры в цикле while через int(input())), 
оканчивающаяся отрицательным числом. Верно ли, что все элементы последовательности равны между собой."""

"""s = 1 #вводим переменную, от которой будем считать
number = int(input("enter number:"))
while True: #это конструкция бесконечного цикла, пока верно: выполняем
      number1 = int(input("enter number:"))
      if number1 == number:
        print("True")
      if number1 != number:
        print ("False")
        break"""

"""В Институте биоинформатики между информатиками и биологами устраивается соревнование. 
Победителям соревнования достанется большой и вкусный пирог. 
В команде биологов a человек, а в команде информатиков — b человек. Нужно заранее разрезать пирог таким образом, 
чтобы можно было раздать кусочки пирога любой команде,
выигравшей соревнование, при этом каждому участнику этой команды должно достаться одинаковое число кусочков пирога.
  И так как не хочется резать пирог на слишком мелкие кусочки, нужно найти минимальное подходящее число.
Напишите программу, которая помогает найти это число. Программа должна считывать размеры команд 
(два положительных целых числа a и b, каждое число вводится на отдельной строке) 
и выводить наименьшее число d, которое делится на оба этих числа без остатка."""
"""a = int(input("enter number > 0:"))
b = int(input("enter number > 0:"))
d = 1
if a <= 0 or b <= 0:
     print("неверно введены данные")

while a != 0 and b != 0:
     if d%a == 0 and d%b == 0:
          print (d)
          break
     d += 1"""


