# Контрольная работа
# 1. С клавиатуры вводится 7 значное число. Если четных цифр в нем больше, чем
# нечетных, то найти сумму всех его цифр, если нечетных больше, то найти
# произведение 1й 3й и 6й цифры.
"""s = input("Введите семизначное число") #вводим не как цифру, а как строку, работать будем о строкой
print (len(s))
if len(s) != 7:
    print ("это не семизначное число")
a = 0 #счетчик чётных цифр
b = 0 # счетчик нечётны цифр
summa = 0 #сумма четных цифр

for i in s:
    if int(i)%2 ==0:
        a +=1
        print (i, "чётное")
        summa +=int(i)

    if int(i)%2 !=0:
       b +=1
       print (i, "нечётное")
if a>b: #если чётных больше чем нечётных
    print (summa) #вывести сумму чётных
else: # если иначе - вывести произведение определённых символов(снова переводим стрчные символы в цифровые)
    print(int(s[0])*int(s[2])*int(s[5]))"""

#Та же задача, с решением через индекс:
"""s = input("Введите семизначное число") #вводим не как цифру, а как строку, работать будем о строкой
print (len(s))
if len(s) != 7:
    print ("это не семизначное число")
count1 = 0 #счетчик чётных цифр
count2 = 0 # счетчик нечётны цифр
summa = 0 #сумма четных цифр
mult = 1 #счётчик для произведения

for i in range(len(number)):
    
    
    if int(number[i]%2 ==0
        count1 +=1
    else:
        count2 +=1
    
    s +=int(number[i]) #переводим инекс в число!!!!!
    
    if i ==0 or i ==2 or i ==5:
        mult*=int(number[i])
if count1>count 2
    print(s)
else:
    print(mult)  """

# 2. С клавиатуры вводится текст, определить, сколько в нём гласных, а сколько
# согласных. В случае равенства вывести на экран все гласные буквы.
#обратить внимание на пробелы
# завести список из 6 английских гласных букв
#проверить на гласность
import random

"""s = input("введите текст:")
count1 = 0 # переменная для подсчёта гласных
count2 = 0 # переменная для подсчёта согласных

n = ""# строчная переменная для вывода самих гласных
for i in s:
    if i != "a" and i != "o" and i != "u" and i != "i" and i != "e" and i != "y" and i !=" ":
        count1 += 1 #считаем согласные, увеличиваем счётчик
        print(i,'это согласная',count1)
       
    elif i == " ":
        continue #игнорируем
    
    else:
        count2 += 1 #считаем гласные, увеличиваем счётчик гласных
        print(i, 'это гласная', count2)
        n += i #увеличиваем нашу строчную переменнную если это гласная
        

if count1 == count2: # уже вне цикла, когда весь цикл выполнен, сравниваем наши два счётчмка
    print(n) # выводим все наши гласные(это уже как строчная сумма наших гласных)"""


# 3. Вводится 2 числа с клавиатуры (от 1 до 20). Так же генерируется 2 числа рандомно в этм же диапазоне
# Посчитать, сколько раз пара введенных чисел с клавиатуры окажется больше
# рандомной пары. Проверку выполнить 7 раз.
# В случае равенства (количества, когда пара больше и всех остальных случаев)
# вывести случайные числа, полученные в 4й итерации.
"""a=int(input("введите число1:"))
b = int(input("введите число 2:"))
c = a+b
print (c)
count1 = 0 # переменная для подсчёта количества проверок
count2 = 0 # переменная для подсчёте случаев, когда первая пара больше второй пары
count3 = 0 # переменная для подсчта всех других случаев(когда первая пара меньше или равна второй паре)
while count1<7:# чтобы сделать 7 проверок, ограничиваем нашу переменную для подсчёта проверок
    d = random.randint(1,20)# рандомные переменные выводим уже в цикле
    e = random.randint(1,20)
    count1 +=1#прикждом рандомном выводе пары увеличивам наш счётчик выводов на 1
    print (d)
    print (e)
    f = d+e
    print(f,count1) #для контроля печатаем сумму и номер проверки
    if c>f: #всё ещё в цикле while вводим условие - если первая пара больше рандомной пары,
        count2 +=1#то увеличивам сётчик, который считает именно эти случаи
        print(c,">",f) #для контроля печатаем
    else:
        count3 +=1
print("введённая пара больше рандомной пары", count2, "раз") #уже вне цикла печатаем окончательный подсчёт
if count1 ==4 and count2 == count3:
    print(d,"число из 4й интерации")
    print(e,"число из 4й интерации")"""

# 4. Посчитать, сколько раз встречается определенная цифра в числах. Количество
# введенных чисел и искомая цифра задаются с клавиатуры. Числа выбираются
# рандомно ( от 1 до 100)

"""n = int(input("Enter number:")) #цифра
q = int (input("Enter number2:")) #количество вводов
f = random.randint(1,100) #число
s = 0 #счётчик выводов
count = 0 #счётчик совпадений
while s<q: # пока количество выводов меньше заданного
    f = random.randint(1,100) #число
    print (f)
    for i in str(f):#для каждой цифры в числе f
        if i == str(n): #если цифра в числе равна заданной нами цифре
            count +=1 # увеличиваем счётчик совпадений
    s +=1
print(n, "встречается", count, "раз" )"""

# 5. Вводится строка, содержащая буквы, целые неотрицательные числа и иные символы.
# Требуется все числа, которые встречаются в строке отдельно вывести на экран. Строка
# может содержать пробелы. (если три цифры подряд, то это число)
"""s = "45 22 sa 12da"
s +=" "
s1 = "" # пустая строка, вводим, чтобы было к чему прибалять, или с чем сравнивать
for elem in s:
    if elem.isdigit():
        print(elem)
        #s+=elem
        s1 += elem
        #print(s1)
        if elem.isalpha() or elem != " ":
            s += elem

    elif s1:
            print(s1)
            s1 = "" """

#Решение от Дениса ( выводит только числа
"""s = input()
s +=" "
s1 = " "
for i in s:
    if i != " ":
        s1 += i
    elif s1: #если существует s1, то его выводим и зануляем ( чтобы избежать множества пробелов
        if s1.isdigit(): #проверяем числовая ли это строка
            print(s1) # если строка числовая, то мы ее выводим
        s1="" #занулили множество пробелов!!!! если она нечисловая выводим пустоту"""


#Это решение выводит не числа, а цифры. То есть если 2 цифры стоит вместе, то она распознаёт их как отдельные цифры, а не как совместное число
# s = input("stroka:")
# for i in s:
#     if i.isdigit():
#         print(i)

# 6. Посчитать, сколько пар (стоят рядом) верхнего и нижнего регистра находится в
# веденном с клавиатуры слове. (Пример HjkLM- 1 пара нижнего, 1 пара верхнего), а
# также сколько всего букв в слове, сколько гласных и согласных.

"""s = "HjkLM"
count1 = 0  # переменная для подсчёта гласных
count2 = 0  # переменная для подсчёта согласных

count5 = 0 # переменная для подсчета пар заглавных букв
count6 = 0 # переменная для подсчета пар прописных букв
for i in s:
    if i != "a" and i != "o" and i != "u" and i != "i" and i != "e" and i != "y" and i != " ":
        count1 += 1  # считаем согласные, увеличиваем счётчик
        print(i, 'это согласная', count1)

    elif i == " ":
        continue  # игнорируем

    else:
        count2 += 1  # считаем гласные, увеличиваем счётчик гласных
        print(i, 'это гласная', count2)


print(count1,"согласных в слове")
print(count2,"гласных в слове")
print(len(s),"всего букв в слове")

print (s.isupper()) #проверяет, что всё в верхнем регистре
print (s.islower()) #проверяет, что всё в нижнем регистре
for i in range(1,len(s)):#важно брать именно от 1, а не от нуля, тогда будет сравниваться предыдущий символ с последующим
    print(s[i-1],s[i])
    if s[i-1].islower() and s[i].islower():
        count6 =+1
    if s[i-1].isupper() and s[i].isupper():
        count5 =+1
print(count6,"пар прописных букв")
print(count5,"пар заглавных букв")"""

