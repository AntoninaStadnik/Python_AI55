#Напишіть функцію, яка повертає добуток чисел з списку. Список передається як параметр.
def get_numbers(nums):
    result = 1
    for num in nums:
        result *= num

    return result

nums = [2, 3, 4, 5]

nums = get_numbers(nums)

print(nums)

# Напишіть функцію, яка повертає найменше число з списку. Список передається як параметр.
def lesser_num(nums):
    min_num = nums[0]
    for num in nums:
        if num < min_num:
            min_num = num

    return min_num

nums = [1, 2, 3, 4, 5]

print(lesser_num(nums))

# Напишіть функцію, яка повертає кількість парних
# чисел з списку. Список передається як параметр.
def found_even(nums):
    for num in nums:
        if num % 2 == 0:
            print(num)

nums = [5, 6, 7, 10, 12, 13]

found_even(nums)

print(nums)

# Напишіть функцію, яка видаляє з списку певне число.
# Якщо число повторюється, то треба видалити всі входження.
# Функція повинна повернути кількість видалених елементів.
# Список та число передаються як параметри.
def remove_nums(nums):
    counter = 0
    for num in nums:
        if num == 3:
            counter += 1
            nums.remove(num)

    new_nums = nums.copy()
    for num in nums:
        if num == 3:
            new_nums.remove(num)

    return new_nums

nums = [-1, 0, 3, 3, 8, 2, -5]

nums = remove_nums(nums)

print(nums)

# Напишіть функцію, яка отримує два списи як параметри.
# Функція повинна об’єднати списки та повернути результат.
# Наприклад, якщо функція отримує списки [1, 2, 3] та [3, 4]
# то результатом має бути список [1, 2, 3, 3, 4]

def united_lists(first_list, second_list):
        print(first_list + second_list)

first_list = [1, 2, 3]
second_list = [4, 5, 6]

united_lists(first_list, second_list)

# Напишіть функцію, яка підносить кожен елемент списку
# до степеня. Результатом має бути список з степенями всіх
# чисел. Список та показник степеня передаються як параметри.
def exponent(num_list, power):
    new_list = []
    for num in num_list:
        new_list.append(num ** power)
    return new_list

num_list = [1, 2, 3, 4, 5, 6]
power_value = 2

final_result = exponent(num_list, power_value)

print(final_result)

