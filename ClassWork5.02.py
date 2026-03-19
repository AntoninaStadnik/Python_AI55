# Напишіть функцію, яка відображає наступний текст
# “Don't let the noise of others' opinions
# drown out your own inner voice.”
# Steve Jobs

# def show_text():
#     print("""
#     “Don't let the noise of others' opinions
#     drown out your own inner voice.”
#                                               Steve Jobs
#     """)
#
# show_text()

# Напишіть функцію, яка приймає два числа як параметри та
# відображає всі парні числа між ними

# def even_nums(start, end):
#     for num in range(start, end+1):
#         if num % 2 == 0:
#             print(num)
#
# start = int(input("Start number: "))
# end = int(input("End number: "))
#
# even_nums(start, end)

# Напишіть функцію, яка відображає горизонтальну або
# вертикальну лінію. Функція має приймати 3 параметри:
# довжину лінії, символ для заповнення та логічну змінну:
#  Якщо вона рівна True, то лінія горизонтальна
#  Якщо False, то лінія вертикальна

def show_lines(len_line, symbol, is_horizontal):
    if is_horizontal:
        print(symbol * len_line)
    else:
        for _ in range(len_line):
            print(symbol)


show_lines(5, "*", True)
show_lines(5, "*", False)

# Напишіть функцію, яка повертає найбільше серед
# чотирьох чисел. Числа передаються як параметри.

# def max_num(num1, num2, num3, num4):
#     maximum = num1
#     if num2 > maximum:
#         maximum = num2
#     if num3 > maximum:
#         maximum = num3
#     if num4 > maximum:
#         maximum = num4
#     return maximum
#
# new_max_num = max_num(2, 3, 4, 5)
# print(new_max_num)

# Напишіть функцію, яка повертає суму чисел в певному
# діапазоні. Межі діапазону передаються як параметри. Якщо,межі неправильні(наприклад числа від 10 до 5), то поміняйте
# їх місцями.

# def sum(start, end):
#     if start > end:
#         start, end = end, start
#
#     total = 0
#     for i in range(start, end):
#         total += i
#
#     return total
#
# print(sum(1, 4))





