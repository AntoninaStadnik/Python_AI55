# # Створіть список чисел [1, 8, -5, 9]
# #  Виведіть на екран елементи цього списку
# numbers = [1, 8, -5, 9]
# print(numbers)
#
# # Збільшіть кожне число в 3 рази та виведіть результат
# new_list = []
#
# for item in numbers:
#     new_list.append(item * 3)
#
# print(new_list)
#
# # Замініть усі числа більші 10 на 0 та виведіть результат
# for i in range(len(numbers)):
#     if numbers[i] > 10:
#     numbers[i] = 0
#     print(numbers)
#
# # Користувач вводить числа, поки не введе -1. Збережіть усі
# # ці числа в список. Виведіть їхню кількість, суму, мінімальне,
# # максимальне та середнє.
# # numbers = []
# #
# total = 0
# count = 0
#
# while True:
#     num = int(input("Введіть число: "))
#     if num == -1:
#         break
#     numbers.append(num)
#     if len(numbers) > 0:
#         count = len(numbers)
#         total = sum(numbers)
#         minimum = min(numbers)
#         maximum = max(numbers)
#         average = total / count
#
#         print("Кількість:", count)
#         print("Сума:", total)
#         print("Мінімальне:", minimum)
#         print("Максимальне:", maximum)
#         print("Середнє:", average)
#     else:
#         print("Список порожній")
#
#
# # Користувач вводить числа, поки не введе 0. Створіть два
# # нових списки: з додатніми та від’ємними числами.
# # Виведіть елементи обох списків на екран.
#
# values = []
# values2 = []
#
# total = 0
#
# while True:
#     num = int(input("Введіть число: "))
#     if num == 0:
#         break
#     if num < 0:
#         total += num
#         values.append(num)
#     print(f"Від’ємні числа {values}")
#     if num > 0:
#         total += num
#         values2.append(num)
#     print(f"Додатні числа {values2}")
#
# # Допоможіть користувачу створити набір з унікальних чисел.
# # Спочатку користувач вводить кількість чисел, після чого
# # самі числа. Якщо число нове, то добавте його в список. Якщо число уже є в списку, виведіть повідомлення про це.
# # Практичне завдання
# # Продовжуйте, поки не на збираєте потрібну кількість чисел
#
# data = []
#
# amount = int(input("Введіть кількість чисел: "))
#
# while True:
#     item = int(input("Введіть число: "))
#
#     if item == amount:
#         break
#
#     if item in data:
#         print("Таке число вже є в списку")
#     else:
#         data.append(item)
#         print("Додано:", data)
#
# print("Готовий список:", data)
#
#
# # Користувач вводить зарплати співробітників, поки не
# # введе -1. Після чого вводить відсоток на який треба збільшити усім зарплату.
# # Виведіть нові зарплати
#
# salaries = []
#
# while True:
#     salary = int(input("Введіть зарплату: "))
#     if salary == -1:
#         break
#     salaries.append(salary)
#
#     percent = int(input("Введіть відсоток: "))
#     multiplier = 1 + percent / 100
#
#     new_salaries = []
#
#     for salary in salaries:
#         new_salaries.append(salary * multiplier)
#
#     print("Нові зарплати:", new_salaries)
#

nums = [1, 2, 3]
print(nums[3])
