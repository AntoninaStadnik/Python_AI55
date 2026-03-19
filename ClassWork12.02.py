# Напишіть функцію, яка отримує назву мови
# програмування та виводить повідомлення:
# «You are learning [мова програмування]»
# За замовчуванням, має бути Python.
def show_word(word: str = "Python"):
    print(f'You are learning {word}')

show_word()

# Напишіть функцію, яка отримує текст як параметр та
# виводить його на екран. Також має бути параметр
# lowercase:
#  Якщо він True, то текст потрібно перевести в
# нижній регістр
#  Якщо False, то текст не змінюється
# За замовчуванням False.
def print_text(text: str, lowercase=False):
    if lowercase:
        print(text.lower())
    else:
        print(text)

print_text(text="Apple", lowercase=True)
print_text(text="Apple", lowercase=False)

# Напишіть функцію, яка отримує температуру та
# переводить її в градуси Цельсія або в Фаренгейта. Для цього є додатковий параметр unit_mapping:
#  Якщо він C_to_F, то функція повинна повернути
# градуси Фаренгейта
#  Якщо він F_to_C, то функція повинна повернути градуси Цельсія
#  Якщо він щось інше, то функція виводить
# повідомлення про помилку, та повертає число без змін
# За замовчуванням, C_to_F
def show_temperature(input_temp, unit_mapping='C_to_F' ):
    if unit_mapping == 'C_to_F':
        return input_temp * 9 / 5 + 32

    elif unit_mapping == 'F_to_C':
        return (input_temp - 32)  * 5 / 9

    else:
        print("No such value")
        return input_temp

print(show_temperature(45))
print(show_temperature(45, 'F_to_C'))
print(show_temperature(25, 'C_to_F'))

# Напишіть функцію, яка отримує список чисел як
# параметр та повертає кількість парних або непарних
# чисел в ньому, в залежності від параметра odd:
#  Якщо він True, то кількість непарних
#  Якщо False, то кількість парних
# За замовчуванням False.
def num_count(nums, odd=False):
    count = 0

    for num in nums:
        if odd:
            if num % 2 != 0:
                count += 1
        else:
            if num % 2 == 0:
                count += 1

    return count

print(num_count([1, 2, 3, 4, 5]))

print(num_count([1, 2, 3, 4, 5], odd=True))
print(num_count([1, 2, 3, 4, 5], odd=False))

# Напишіть функцію, яка отримує декілька чисел як параметрів.
#  Якщо числа 2, то повернути найбільше
#  Якщо числа 3, то повернути суму
#  Якщо чисел більше 3, то повернути їхній добуток

def process_numbers(*args):
    count = len(args)

    if count == 2:
        return max(args)

    elif count == 3:
        return sum(args)

    elif count > 3:
        result = 1
        for num in args:
            result *= num
        return result

    else:
        return "Введено менше ніж 2 числа"

print(f"2 числа (max): {process_numbers(10, 25)}")
print(f"3 числа (сума): {process_numbers(5, 10, 15)}")
print(f"4 числа (добуток): {process_numbers(2, 3, 4, 5)}")









