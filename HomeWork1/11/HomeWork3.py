#Користувач вводить з клавіатури три числа. Залежно від вибору користувача, програма виводить на екран суму трьох чисел або
#добуток трьох чисел.

value1 = int(input("Введіть число1: "))
value2 = int(input("Ввдіть число2: "))
value3 = int(input("Введіть число3: "))

user_select = input("Виберіть дію: (+, *,) " )


if user_select == "+":
    result = value1 + value2 + value3
    print("Сума: ", result)

elif user_select == "*":
    result = value1 * value2 * value3
    print("Добуток: ", result)

else:
    print("Дія не підтримується")


#Користувач вводить з клавіатури три числа. Залежно від вибору користувача, програма виводить на екран максимум із трьох,
#мінімум із трьох або середньоарифметичне трьох чисел.

value1 = int(input("Введіть число1: "))
value2 = int(input("Ввдіть число2: "))
value3 = int(input("Введіть число3: "))

user_select = input("Оберіть дію: ( < , >, /) " )

if user_select == "<":
    minimum = min(value1, value2, value3)
    print("Мінімальне: ", minimum)


elif user_select == ">":
    maximum = max(value1, value2, value3)
    print("Максимальне: ", maximum)


elif user_select == "/":
    result = (value1 + value2 + value3) / 3
    print("Середнє арифметичне: ", result)

else:
    print("Невірна дія")




#Користувач вводить з клавіатури якусь кількість метрів.
#Залежно від вибору користувача, програма конвертує метри в
#милі, дюйми або ярди.

meters = float(input("Введіть кількість метрів: "))
user_select = input("Оберіть: (милі, дюйми, ярди)")

if user_select == "милі":
    result = meters / 1609.344
    print(f"Милі: {result:.3f}")

elif user_select == "дюйми":
    result = meters * 39.3701
    print(f"Дюйми: {result:.3f}")

elif user_select == "ярди":
    result = meters * 1.09361
    print(f"Ярди: {result:.3f}")

else:
    print("Немає такої величини")