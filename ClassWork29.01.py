# Створіть список кольорів [“black”, “yellow”, “blue”]

colors_list = ['black', 'yellow', 'blue']

#  Виведіть усі кольори
print(color_list)

#  Виведіть кольори які починаються на b
for color in colors_list:
    if color.startswith('b'):
        print(color)

#  Виведіть кольори де більше 5-ти літер
for color in colors_list:
    if len(color) > 5:
        print(color)

#  Добавте кольори red, green, purple
colors_list.extend(['red', 'green', 'purple'])
print(colors_list)

#  Зробіть усі слова в списку upper
for color in range(len(colors_list)):
    colors_list[color] = colors_list[color].upper()
print(colors_list)

#  Видаліть blue
colors_list.remove('blue')
print(colors_list)

#  Відсортуйте список в алфавітному порядку
colors_list.sort()
print(colors_list)

#  У списку що вийшов виведіть елементи у форматі:
# 1. колір
# 2. колір
for color in enumerate(colors_list, start = 1):
    print(f"{color}. {colors_list}")

# Користувач вводить слова через пропуск. Потрібно до
# кожного слова добавити ** на початку та в кінці і вивести результат через кому.
# Приклад: **яблуко**, **груша**, **персик**
text = input("Введіть слова через пробіл: ")

words = text.split()

result = []

for word in words:
    result.append(f"**{word}**")
print(",", result)

# Є два списки:
# Користувач вводить назву товару, якщо такого товару
# немає, повідомити про це.
# Якщо товари є, то отримати його індекс та вивести
# відповідну ціну.


goods = [
    "хліб", "молоко", "сир", "яблука", "кава"
]

prices = [
    20.5, 28.0, 120.0, 45.3, 89.9
]

while True:
    product = input("Введіть назву товару: ")
    if product not in goods:
        print("Немає такого товару")
        break


    idx = goods.index(product)
    price = prices[idx]
    print(f"Ви обрали {product} за ціною {price}")
    break

# На основі попереднього завдання створіть консольну
# програму магазину. Функціонал:
#  додати товар до кошика
#  видалити товар з кошика
#  вивести загальну ціну
#  очистити кошик
#  добавити новий товар у магазин
#  вихід
total = 0

print("Функціонал")
print("1. додати товар до кошика")
print("2. видалити товар з кошика")
print("3. вивести загальну ціну")
print("4. очистити кошик")
print("5. добавити новий товар у магазин")
print("6. вихід")

while True:
    user_choice = int(input("Ввеідть номер дії(1-6): "))
    if user_choice == 6:
        print("Кінець програми")
        break

    if user_choice == 1:
        ask = input("Введіть товар, який буде доданий у кошик: ")
        idx = goods.index(product)
        print(f"{goods[idx]} добавлено в кошик")

    elif user_choice == 2:
        print("Товар видалено з кошика")
