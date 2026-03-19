# Є список з товарами. Користувач вводить індекс товару,
# який треба вивести. Обробіть виняток
product = ["orange", "apple", "bread", "cherry"]

try:
    index = int(input("Введіть номер товару (0-3): "))
    print(f"Ви обрали: {product[index]}")

except ValueError:
    print("Помилка: будь ласка, введіть ціле число.")

# Напишіть функцію, яка запитує користувача вік та
# повертає його. Якщо вік неправильний(<0 або >130)
# викликати виняток ValueError.
# Написати код try … except який використовує дану функцію.
def ask_age():
    age = int(input("Enter age: "))

    if age < 0:
        raise ValueError("Invalid age, can't be less than 0")

    if age > 130:
        raise ValueError("Invalid age, can't be greater than 130")

    return age


try:
    age = ask_age()
    print(f"{age = }")

except ValueError as err:
    print(f"Error, {err}")

# Напишіть функцію, яка запитує користувача номер
# телефону та повертає його. Якщо номер не вірний, тобто не
# починається з +038 або в ньому не 11 символів то викликати
# виняток ValueError.
# Написати код try … except який використовує дану функцію.
def ask_number():
    number = int(input("Enter phone number: "))

    if number[:4] != '+380':
        raise ValueError("Not Ukraine number")

    if len(number) != 11:
        raise ValueError("Incorrect number")

    return number

try:
    number = ask_number()
    print(f"Your number is {number}")

except ValueError as err:
    print("Error:", err)


