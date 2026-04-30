# Користувач вводить з клавіатури значення у список.
# Після чого запускаються два потоки.
# Перший потік знаходить максимум у списку.
# Другий потік знаходить мінімум
# у списку. Результати обчислень виведіть на екран.

import json
import threading
import time
from audioop import avg


def find_max(nums, result):
    result["max"] = max(nums)
    # print(f"Maximum: {maximum}")


def find_min(nums, result):
    result["min"] = min(nums)
    # print(f"Minimum: {minimum}")


nums = list(map(int, input("Enter numbers: ").split(", ")))
print(f"You entered nums list {nums}")

result: dict[str, int] = {}

thread_max = threading.Thread(target=find_max, args=(nums, result))
thread_min = threading.Thread(target=find_min, args=(nums, result))

thread_max.start()
thread_min.start()

thread_max.join()
thread_min.join()

print(result)

# Користувач вводить з клавіатури значення у список.
# Після чого запускаються два потоки.
# Перший потік знаходить суму елементів у списку.
# Другий потік знаходить
# середнє арифметичне у списку. Результати обчислень
# виведіть на екран


def find_sum(numbers, result):
    print("Start finding sum")
    time.sleep(2)
    result["sum"] = sum(numbers)


def find_average(numbers, result):
    print("Start finding average")
    time.sleep(2)
    result["average"] = avg(numbers)


numbers = []
result_avg: dict[str, int] = {}

n = int(input("Enter a number: "))

for _ in range(n):
    num = int(input("Enter a number: "))
    numbers.append(num)

thread_sum = threading.Thread(
    target=find_sum,
    args=(
        numbers,
        result,
    ),
)
thread_average = threading.Thread(
    target=find_average,
    args=(
        numbers,
        result,
    ),
)
thread_sum.start()
thread_average.start()

thread_sum.join()
thread_average.join()

print(result)


# Користувач вводить з клавіатури шлях до файлу, що
# містить набір чисел.
# Після чого запускаються два потоки.
# Перший потік створює новий файл, в який запише лише
# парні елементи списку. Другий потік створює новий файл,
# в який запише лише непарні елементи списку. Кількість
# парних і непарних елементів виводиться на екран.


def func1(listik: list[int]):
    with open("file_path.json", "w") as file:
        for x in listik:
            if x % 2 == 0:
                file.write(f"{x}\n")


def func2(listik: list[int]):
    with open("file_path1.json", "w") as file:
        for x in listik:
            if x % 2 != 0:
                file.write(f"{x}\n")


file_path = input("Enter file path: ")

with open(file_path) as file:
    count = int(file.readline())
    nums = list(map(int, file.readline().split(", ")))

print(nums)


thread_parne = threading.Thread(target=func1, args=(nums,))
thread_neparne = threading.Thread(target=func2, args=(nums,))
thread_parne.start()
thread_neparne.start()

thread_parne.join()
thread_neparne.join()

# Користувач вводить з клавіатури шлях до файлу та
# слово для пошуку. Після чого запускається потік для
# пошуку цього слова у файлі. Результат пошуку виведіть
# на екран.

filename = "search.json"
word = input("Enter a word: ")


def search(word: str, result: dict[str, int]) -> None:
    with open("search.json") as file:
        items = json.load(file)

    counter = 0

    for item in items:
        if item == word:
            counter += 1

    result[word] = counter


result = {}

thread1 = threading.Thread(target=search, args=("kiwi", result))
thread2 = threading.Thread(target=search, args=("apple", result))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print(result)
