# Напишіть функцію, яка відображає наступний текст
# “Don't compare yourself with anyone in this world…
# if you do so, you are insulting yourself.”
# Bill Gates

def show_text():
    print("""
    “Don't compare yourself with anyone in this world…
        if you do so, you are insulting yourself.”
                                              Bill Gates
    """)
show_text()

# Напишіть функцію, яка приймає два числа як параметри та відображає всі непарні числа між ними.
def odd_nums(start, end):
    for num in range(start, end+1):
        if num % 2 != 0:
            print(num)

start = int(input("Start number: "))
end = int(input("End number: "))

odd_nums(start, end)

# Напишіть функцію, яка відображає пустий(лише межі) або
# заповнений квадрат. Функція має приймати 3 параметри:
# довжину сторони, символ для заповнення та логічну змінну:
#  Якщо вона рівна True, то квадрат заповнений
#  Якщо False, то квадрат пустий

def square(len_side, symbol, is_full):
    if is_full:
        for _ in range(len_side):
            print(symbol * len_side)
    else:
        print(symbol * len_side)
        for _ in range(len_side - 2):
            print(symbol + " " * (len_side - 2) + symbol)
        if len_side > 1:
            print(symbol * len_side)

square(4, "*", True)
square(4, "*", False)

# Напишіть функцію, яка повертає найменше серед п’яти чисел. Числа передаються як параметри.
def min_num(num1, num2, num3, num4, num5):
     min = num1
     if num2 < min:
        min = num2
     if num3 < min:
        min = num3
     if num4 < min:
        min = num4
     if num5 < min:
        min = num5
     return min

new_min_num = min_num(2, 3, 4, 5, 6)
print(new_min_num)

# Напишіть функцію, яка повертає добуток чисел в певному діапазоні. Межі діапазону передаються як параметри. Якщо
# межі неправильні(наприклад числа від 10 до 5), то поміняйте їх місцями.

def product(start, end):
    if start > end:
        start, end = end, start

    for i in range(start, end+1):
        result = start * end

    return result

print(product(5, 4))

# Напишіть функцію, яка повертає кількість цифр у числі.
# Число передається як параметр. Наприклад, якщо передали
# число 3875, то функція повертає 4.

def amount(num):
    count = 0
    for _ in str(num):
        count += 1

    return count

print(amount(54763))


    