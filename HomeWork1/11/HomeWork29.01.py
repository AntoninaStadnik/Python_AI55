# Створіть 2 списки чисел.
# Створіть на їх основі списки з


nums = [1, 2, 3, 4, 5]
all_nums = [6, 7, 8, 9, 5, 4, 3]

# Усіма числами з обох списків
print(nums + all_nums)

#  Усіма числами з обох списків, але без повторень
not_repeated = []
for num in nums + all_nums:
    if num not in not_repeated:
        not_repeated.append(num)
print(not_repeated)

#  Спільними числами для двох списків
common_nums = []
for num in nums:
    if num in all_nums and num not in common_nums:
        common_nums.append(num)
print(common_nums)

#  Числа які є в першому, але немає в другому
common_nums = []
for num in nums:
    if num not in all_nums:
        common_nums.append(num)
print(common_nums)