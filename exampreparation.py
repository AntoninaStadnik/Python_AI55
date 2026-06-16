# Добуток двох чисел
# Введіть два числа з клавіатури та виведіть результат їхнього множення.
# Підказка: Використайте input() та перетворення на int або float.

# ask1 = int(input("Type num1: "))
# ask2 = int(input("Type num2: "))
# print(ask1 + ask2)

# Середнє арифметичне
# Введіть три числа. Обчисліть та виведіть їх середнє арифметичне.
# Підказка: Середнє = сума / кількість чисел.
# ask1 = int(input("Type num1: "))
# ask2 = int(input("Type num2: "))
# ask3 = int(input("Type num3: "))
# result = (ask1 + ask2+ ask3) / 3
# print(result)

# Площа прямокутника
# Введіть довжину та ширину прямокутника. Виведіть його площу.
# Підказка: Площа = довжина * ширина.
# lenght = int(input("Input length: "))
# width = int(input("Input width: "))
# result = lenght*width
# print(f"Площа прямокутника {result}")

# Остача від ділення
# Введіть два числа. Виведіть остачу від ділення першого на друге.
# Підказка: Оператор % повертає остачу.
# a = int(input("Type num1: "))
# b = int(input("Type num2: "))
# result = a % b
# print(result)

# Перевірка парності
# Введіть ціле число. Визначте та виведіть,
# чи є воно парним чи непарним.
# Підказка: Число парне, якщо n % 2 == 0.

# num = int(input("Type num: "))
# if num % 2 == 0:
#     print("Even")
# else:
#     print("Odd")


# Більше з двох чисел
# Введіть два числа. Визначте і виведіть,
# яке з них більше, або повідомте, що вони рівні.
# Підказка: Використайте if / elif / else.
# num1 = int(input("Input num1: "))
# num2 = int(input("Input num2: "))
#
# if num1 > num2:
#     print(num1)
# elif num1 < num2:
#     print(num2)
# else:
#     num1 = num2
#     print("equal")


# 21. Числа від 1 до 20
# Використовуючи цикл while,
# виведіть усі числа від 1 до 20 через пробіл або кожне на
# новому рядку.
# Підказка: Ініціалізуйте лічильник i = 1, збільшуйте на 1 поки i <= 20.
# num = 1
#
# while True:
#     if num > 20:
#         break
#
#     print(num)
#     num += 1

# 22. Числа від 20 до 1
# Використовуючи цикл while,
# виведіть усі числа від 20 до 1 у зворотному порядку.
# Підказка: Ініціалізуйте i = 20, зменшуйте на 1 поки i >= 1.
# num = 20
#
# while True:
#     if num < 1:
#         break
#
#     print(num)
#     num -= 1

# 31. Числа від 1 до 100
# За допомогою циклу for виведіть усі числа від 1 до 100.
# Підказка: Використайте range(1, 101).
# for i in range(1, 102):
#     print(i)

# 32. Парні числа до 100
# За допомогою for виведіть усі парні числа від 1 до 100.
# Підказка: Використайте range(2, 101, 2) або перевірку n % 2 == 0.
# for i in range(2, 101, 2):
#     print(i)

# for i in range(1, 100):
#     if i % 2 == 0:
#      print(i)

# 41. Трикутник зі зірочок
# Виведіть прямокутний трикутник із символів *:
# перший рядок — 1 зірочка, другий — 2,
# і так далі до N.
# Підказка: for i in range(1, N+1): print("*" * i).
# N = 5
#
# for i in range(1, N + 1):
#     print("*" * i)

# 42. Перевернутий трикутник
# Введіть N. Виведіть трикутник у зворотному порядку: перший рядок — N зірочок,
# останній — 1.
# N = 5
#
# for i in range(1, N - 1):
#     print("*" * i)

# 52. Довжина рядка
# Введіть рядок.
# Порахуйте і виведіть кількість символів у ньому без використання len().
# Підказка: Використайте лічильник і цикл for.
# letter = input("Enter a phrase: ")
#
# count = 0
#
# for char in letter:
#     count += 1
#
# print(count)


# 53. Кількість голосних
# Введіть рядок. Порахуйте кількість голосних літер (a, e, i, o, u та їх українські
# відповідники).
# Підказка: Перевіряйте ch.lower() in "аеиіоуяюєїaeiou".
# text = input("Enter a phrase: ")
#
# count = 0
#
# for ch in text:
#     if ch.lower() in "аеиіоуяюєїaeiou":
#         count += 1
#
# print(count)


# 61. Список із 10 чисел
# Попросіть користувача ввести 10 чисел і збережіть їх у список.
# Виведіть список.
# Підказка: Використайте цикл і метод .append() або list comprehension.
# new_list = []
#
# for i in range(10):
#     ask = input("Please enter a number: ")
#     new_list.append(ask)
# print(new_list)


# 62. Сума елементів списку
# Маючи список чисел,
# обчисліть і виведіть суму всіх його елементів без використання
# sum().
# Підказка: Ітеруйте по списку і накопичуйте суму у змінній total.
# total = 0
#
# num_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
#
# for num in num_list:
#     total += int(num)
# print(total)

# 71. Довгі слова
# Маючи список слів, виведіть лише ті, довжина яких перевищує 5 символів.
# Підказка: Умова фільтрації: len(word) > 5.
# fruits = ["apple", "banana", "cherry"]
#
# for fruit in fruits:
#     if len(fruit) > 5:
#         print(fruit)


# 81. Квадрат числа
# Напишіть функцію square(n),
# яка приймає число і повертає його квадрат. Викличте і
# виведіть результат.
# Підказка: return n ** 2
# def square(n):
#     return n ** 2
#
# square(2)
# print(square(2))

# 82. Куб числа
# Напишіть функцію cube(n),
# яка приймає число і повертає його куб. Викличте і виведіть
# результат.
# Підказка: return n ** 3
# def cube(n):
#     return n ** 3
#
# cube(4)
# print(cube(4))

# 91. Словник учня
# Створіть словник з даними учня: ключі "ім'я", "вік", "клас". Виведіть кожне поле
# окремим рядком.
# Підказка: Зверніться до значень через student["ім'я"] тощо.
# student = {"name": "Ivan",
#            "age": "23",
#            "class": "M"}
# print(student ["name"])
# print(student ["age"])
# print(student ["class"])

# 92. Всі ключі
# Маючи довільний словник, виведіть усі його ключі.
# Підказка: Використайте dict.keys() або ітеруйте: for key in d
# student = {"name": "Ivan",
#            "age": "23",
#            "class": "M",
#            "friend": "Ostap"}
# for key in student:
#     print(key)

# Клас BankAccount — банківський рахунок
# Атрибути: номер рахунку (str), власник (str), баланс (float, за замовчуванням 0).
# Метод deposit(amount): поповнює баланс. Сума має бути більшою за 0.
# Метод withdraw(amount): знімає кошти. Забороняйте зняття більше, ніж є на
# рахунку.
# Метод get_balance(): виводить поточний баланс


class BankAccount:
    def __init__(self, account_number, owner, balance=0):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            print("Сума має бути більшою за 0")

    def withdraw(self, amount):
        if amount <= 0:
            print("Сума має бути більшою за 0")
        elif amount > self.balance:
            print("Недостатньо коштів")
        else:
            self.balance -= amount

    def get_balance(self):
        return self.balance
