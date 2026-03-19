# Напишіть функцію, яка повертає суму чисел з списку. Список передається як параметр.
def get_numbers(nums):
    total = 0
    for num in nums:
        total += num

    return total

nums = [1, 2, 3, 4, 5]

nums = get_numbers(nums)

print(nums)

# Напишіть функцію, яка повертає найбільше число з списку. Список передається як параметр.
def biggest_num(nums):
    max_num = nums[0]
    for num in nums:
        if num > max_num:
            max_num = num

    return max_num

nums = [1, 2, 3, 4, 5]

print(biggest_num(nums))

# Напишіть функцію, яка видаляє всі від’ємні числа зі списку. Список передається як параметр. Функція має
# повернути кількість видалених чисел.
def remove_nums(nums):
    counter = 0
    for num in nums:
        if num <= 0:
            counter += 1
            nums.remove(num)

    new_nums = nums.copy()
    for num in nums:
        if num <= 0:
            new_nums.remove(num)

    return new_nums

nums = [-1, 0, -2, 3, 8, 2, -5]

nums = remove_nums(nums)

print(nums)

# Напишіть функцію, яка шукає певне число в списку.
# Функція повинна повертати список усіх індексів цього числа в списку. Якщо числа немає в списку, то потрібно
# повернути порожній список. Список та число передаються як два параметри.

def find_number(num_list, numbers_list):
    result_indices = []

    for i in range(len(num_list)):
        if num_list[i] == numbers_list:
            result_indices.append(i)

    return result_indices

numbers = [1, 3, 5, 7, 2, 9, 2]

target = 2

res = find_number(numbers, target)

print(res)

# Напишіть функцію, рахує факторіал кожного
# елемента списку. Результатом має бути список з
# факторіалами.
# Факторіалом числа n (позначають n!) називаю
# добуток усіх чисел від 1 до n. Наприклад 6! =
# 1*2*3*4*5*6. Якщо число від’ємне, то вважайте що
# його факторіал рівний Nonе. Факторіал число 0 вважають
# рівним 1.

def factorial(numbers):
    result = []

    for n in numbers:
        if n < 0:
            result.append(None)
        elif n == 0:
            result.append(1)
        else:
            fact = 1
            for i in range(1, n + 1):
                fact *= i
            result.append(fact)

    return result

nums = [1, 3, 7, 9, 0]
print(factorial(nums))









