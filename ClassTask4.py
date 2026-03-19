#Користувач вводить свій вік, якщо він працездатного
#віку(18-65) то виведіть фразу «Працездатний/на», інакше
#«Непрацездатний/на»

# age = int(input("Введіть свій вік: "))
#
# if age > 18 and age < 65:
#     print("Працездатний/на")
#
# else:
#     print("Непрацездатний/на")

#Оформіть чек покупки. Користувач вводить ціну за
#одиницю товару, кількість товару та свій вік.
#Якщо користувач неповнолітній або старший за 65 років,
#то застосуйте знижку 15%

# DISCOUNT = 0.15

# price_for_item = float(input("Введіть ціну товару: "))
# quantity = int(input("Ввудіть кількість товару: "))
# age = int(input("Введіть свій вік: "))
#
# total_price = price_for_item * quantity
#
# if age < 18 or age > 65:
#     use_discount = DISCOUNT * price_for_item
#     print(f"Ваша знижка за віком: {use_discount:.2f}")
#
# else:
#     print("Знижка не застосовується")


#Користувач вводить ціле число.
#Якщо воно ділиться на 3, виведіть Fizz
#Якщо воно ділиться на 5, виведіть Buzz
#Якщо ділиться на 3 і 5, виведіть FizzBuzz

num = int(input("Введіть ціле число: "))

if num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")

elif num % 5 == 0:
    print("Buzz")

    if num % 3 == 0:
        print("Fizz")



#Завдання з уроку
# правильний промокод
TRUE_PROMOCODE = 'FREEBUY27'

# отримати дані від користувача
price_per_unit = float(input("Введіть ціну за одиницю товару: "))
quantity = int(input("Введіть кількість товару: "))

is_promo_code = input("чи є у вас промокод: так/ні ")

# ціна за товар
total = price_per_unit * quantity

# # перевірка
# print(f"{total = }")

# ціна за доставку
if total > 1000:
    delivery_price = 0
else:
    delivery_price = 100

#  Якщо є промокод, то користувач його повинен ввести.
# Якщо промокод вірний(FREEBUY27) то
# застосовується знижка 12%

if is_promo_code == 'так':
    user_promo_code = input("Введіть промокод: ")

    # первірка промокоду
    if user_promo_code == TRUE_PROMOCODE:
        discount = 0.12 * total
        print(f"Застосовується знижка {discount:.2f} грн")

        total -= discount
    else:
        print("Неправильний промокод")
else:
    print("Виввели ні")

# остаточна ціна
total += delivery_price

print(f"З вас {total:.2f} грн")

#Допишіть до завдання 3.
#Користувач вводить свій бюджет.
#Якщо грошей достатньо, то треба вивести «Замовлення
#оплачене» а також скільки грошей залишилось
#Якщо грошей не достатньо, то треба вивести
#Недостатньо коштів для оплати» та скільки не
#вистачає

budget = float(input("Введіть свій бюджет: "))

if budget > total:
    print("Замовлення оплачене")

elif budget < total:
    print("Недостатньо коштів для оплати")

else:
    print("Помилка")

budget -= total
print(f"Не вистачає {budget:.2f}")







