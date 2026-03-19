# Напишіть функцію, яка отримує ім’я студента та
# виводить повідомлення:
# «You are welcome, [студент]»
# За замовчуванням, має бути ваше ім’я
def show_name(name = 'Tonya'):
    print(f"You are welcome, {name}")

show_name()

# Напишіть функцію, яка отримує два числа як
# параметр та тип операції, що з ними можна зробити:
#  Якщо він add, то поверніть суму чисел
#  Якщо diff, то поверніть різницю чисел
#  Якщо mult, то поверніть добуток чисел
#  Якщо щось інше, виведіть інформацію про помилку
# За замовчуванням add.
def get_num(num1: int, num2: int, add=False, diff = True, mult = False):
    if add:
        result = num1 + num2

    if diff:
        result = num1 - num2

    if mult:
        result = num1 * num2

    if not result:
        print("Помилка, немає такого")

    return result

print(get_num(5,3, False))
print(get_num(5,3, diff =True))
print(get_num(5,3, mult=False))

# Напишіть функцію, яка отримує назву свята та імена
# декількох гостей. Виведіть кожному гостю
# повідомлення:
# «[ім’я], you are invited to [назва свята]»
# Якщо гостей немає, потрібно вивести повідомлення:
# «No guests»

def show_guests(guests: list, holiday_name: str = "Birthday"):
    if not guests:
        print("No guests")
        return

    for guest in guests:
        print(f"{guest}, you are invited to {holiday_name} ")

guests = ['John', 'Mike', 'Emily', 'Abby']
show_guests(guests, holiday_name="Birthday")
