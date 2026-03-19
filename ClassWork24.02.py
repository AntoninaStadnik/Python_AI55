# Напишіть lambda-функції, які:
#  Підносить число до квадрату
def square(num):
    return num ** 2

res = lambda num: num ** 2
print(res(5))

#  Отримує довжини трикутника і повертає периметр
def triangle(side1, side2, side3):
    return side1 + side2 + side3

res = lambda side1, side2, side3: side1 + side2 + side3
print(res(5, 5, 6))
#
# #  Отримує прізвище та ім’я і повертає рядок у форматі «Прізвище, ім’я»
def names(name, secondname):
    return f"{name} {secondname}"

result = lambda name, secondname: names(name, secondname)
print(result("Ivan", "Petrov"))
#
# #  Перевіряє чи є число парним
def even_number(nums: list) -> list:
    return list(filter(lambda num: num % 2 == 0, nums))

print(even_number([1, 2, 3]))


# Напишіть функцію, яка використовуючи filter:
#  Отримує список чисел та повертає список з лише додатніми числами
nums = [-1, 1, 4, 2, -2, 5, 6, -3, -5]
positive_nums = filter(lambda num: num > 0, nums)
positive_nums = list(positive_nums)
print(positive_nums)

#  Отримує список слів та повертає список слів, в яких більше ніж 3 літери
words = ['apple', 'cat', 'apricot', 'watermelon']
long_words = filter(lambda word: len(word) > 3, words)
print(list(long_words))

#  Отримує список слів та літеру і повертає список тих слів, які починаються на цю літеру(регістр неважливий)
words = ['dog', 'cat', 'kitty', 'doggy']
letter = 'd'
search = lambda words, l: list(filter(lambda w: w.lower().startswith(l.lower()), words))
print(search(words, letter))

# Напишіть функцію, яка отримує іншу функцію та параметри. Поверніть час роботи функції у секундах
import time

def measure_time(func, params_list):
    start = time.perf_counter()

    func(*params_list)

    end = time.perf_counter()
    return end - start

def greet(name, delay):
    time.sleep(delay)
    print(f"Привіт, {name}!")

duration = measure_time(greet, ["Геннадій", 1.2])

print(f"Час виконання: {duration} сек.")


