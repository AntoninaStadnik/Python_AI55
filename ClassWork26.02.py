# Користувач вводить числа через кому. Збережіть їх у кортеж. Виведіть на екран:
from itertools import count
import random

data = input("Введіть числа через кому: ")

# # Додатково, якщо користувач введе порожній рядок, то створіть власний кортеж з випадковими числами(12 шт).
if data.strip() == "":
    nums = tuple(random.randint(1, 100) for _ in range(12))
    print("Створено випадковий кортеж:", nums)
else:
    nums = tuple(int(x.strip()) for x in data.split(','))

# #  Суму чисел
total = sum(nums)
print(total)

# #  Найбільше та найменше число
max_num = max(nums)
min_num = min(nums)
print(max_num)
print(min_num)

# #  Перші та останні 3 числа
print(nums[-3:])
print(nums[:3])

# #  Кількість чисел 7
print(nums.count(7))

#  Пари індекс – число
nums = tuple(int(x.strip()) for x in data.split(','))
print("Пари індекс – число:")
for index, value in enumerate(nums):
    print(f"Індекс {index}: число {value}")


# Напишіть наступну програму: є кортеж з іменами зареєстрованих студентів. Користувач вводить ім’я студента
# після чого отримує повідомлення, чи студент зареєстрований.
# Програма закінчує роботу коли користувач введе порожній рядок
def stud_func():
    student_name = ('Іван', 'Петро', 'Василь', 'Марина', 'Олена')

    while True:
        ask_name = input("Введіть ім'я зареєстрованого студента: ")

        if ask_name.strip() == "":
            break

        if ask_name in student_name:
            print(f"Студент {ask_name} зареєстрований")
        else:
            print(f"Студента {ask_name} немає в списку")

stud_func()

# Напишіть наступну програму: є кортеж з назвами фільмів.
# Користувач вводить назву фільму.
#  Якщо фільм знаходиться в першій половині кортежу, треба вивести ретро-фільм
#  Якщо в другій половині – сучасний фільм
#  Якщо один з останніх п'яти – новий фільм
def select_movie():
    movies = ('Фільм1', 'Фільм2', 'Фільм3', 'Фільм4', 'Фільм5', 'Фільм6', 'Фільм7', 'Фільм8', 'Фільм9', 'Фільм10')

    while True:
        ask_movie = input("Введіть назву фільму, 'exit' для виходу: ")

        if ask_movie.lower() == 'exit':
            print("Вихід з програми.")
            break

        if ask_movie in movies:
            index = movies.index(ask_movie)

            if index >= len(movies) - 5:
                print("Це новий фільм")

            elif index < len(movies) / 2:
                print("Це ретро-фільм")

            else:
                print("Це сучасний фільм")

        else:
            print("Такого фільму немає в списку.")

select_movie()

