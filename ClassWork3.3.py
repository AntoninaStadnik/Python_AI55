# Користувач вводить числа через кому. Збережіть їх у
# множину. Також створіть власну множину з випадковими
# числами(12 шт). Виведіть наступну інформацію:
import random

data = input("Введіть числа через кому: ")

if data.strip():
    user_numbers = {int(x.strip()) for x in data.split(",")}
else:
    user_numbers = set()

count = len(user_numbers)
random_numbers = set(random.sample(range(1, 101), 12))
user_numbers = set(user_numbers) - set(random_numbers)
both = user_numbers & random_numbers
diff = user_numbers - random_numbers

print("Множина користувача:", user_numbers)
print("Випадкова множина:", random_numbers)
print(f"Максимальне число: {max(user_numbers)}")
print(f"Мінімальне число: {min(user_numbers)}")
print(f"Всього введенно чисел {count}")
print(f"Унікальні числа, яких немає серед випадкових: {list(user_numbers)}")
print(f"Кількість таких чисел: {len(user_numbers)}")
print(f"Спільні числа у двох списках: {both}")
print(f"Усі числа, які є або в одній або в іншій множині: {diff}")

# Напишіть функцію, яка отримує список гостей(гості можуть повторюватись) та назву події. Потрібно вивести
# запрошення для кожного гостя і лише один раз.

guests = ["Ivan", "John", "Kevin", "Vasya", "Ivan", "John"]
holiday = "Birthday"

def celebrate(guests, holiday):
    unique_guests = set(guests)

    for guest in unique_guests:
        print(f"{guest}, Вас запрошують на {holiday}")

celebrate(guests, holiday)
