# Користувач вводить свій вік. Виведіть рік, коли він народився
age = input("Введіть Ваш вік: ")
age = int(age)

current_year = 2025 - age

print("Ви народилися: ", current_year)

#Користувач вводить довжину ребра куба. Виведіть його об’єм.
cube_edge = input("Введіть довжину ребра куба: ")
cube_edge = int(cube_edge)

result = cube_edge ** 3
print("Об'єм куба: ",  result)

# Користувач вводить число та відсоток. Збільшіть дане число на цей відсоток.
# Наприклад, якщо введено 100 та 15, то потрібно збільшити
# 100 на 15%, тобто 115

num = input("Введіть число: ")
num = int(num)

percent = input ("Введіть відсоток: ")
percent = int(percent)

result = num + percent
print(result)

#Користувач вводить два числа: ціле(int) та дробове(float).
#Обчисліть суму, добуток та частку

userNumber = int(input("Ввудіть ціле число: "))

userNumber2 = float(input("Введіть дробове число: "))

result = userNumber * userNumber2
result1 = userNumber / userNumber2
result2 = userNumber + userNumber2

print(f"Ваша сума {result2}", f"Ваша частка {result1}", f"Ваш добуток {result}")

# Користувач вводить радіус кола. Виведіть його площу.
# Вважайте що =3.1415
# Округліть результат до двох знаків після коми.
r = float(input("Введіть радіус: "))

result = 3.14 * r **2
print(f"Площа кола {result:.2f}")


# Користувач вводить ціну однієї кружки та загальний бюджет. Обчисліть скільки кружок можна купити. Скільки грошей залишиться.

cup_price = float(input("Введіть ціну чашки: "))

budget = float(input("Введіть загальний бюджет: "))

cup_amount = budget / cup_price
rest_balance = budget % cup_price

print(f"Ви можете купити {cup_amount:.2f} чашок")
print(f"У Вас залишиться {rest_balance} грошей")

# Користувач вводить суму вкладу в банк та відсоток ставки.
# Обчисліть скільки користувач отримує через 5 років, якщо кожного року сума вкладу збільшується на даний відсоток
# Виведіть суму вкладу кожного року окремо - пройдемо на наступному заданні

bank_deposit = float(input("Введіть суму вкладу: "))

interest_rate = float(input("Введіть відсоток від вкладу: ")) / 100

year1 = bank_deposit * (1 + interest_rate)
year2 = year1 * (1 + interest_rate)
year3 = year2 * (1 + interest_rate)
year4 = year3 * (1 + interest_rate)
year5 = year4 * (1 + interest_rate)

print("Через 1 рік:  ", year1)
print("Через 2 роки:  ", year2)
print("Через 3 роки:  ", year3)
print("Через 4 роки:  ", year4)
print("Через 5 роки:  ", year5)



# Користувач вводить довжину в метрах. Виведіть цю
# довжину в футах та ярдах.
# 1 метр = 3.2808399 фута
# 1 метр = 1.0936133 ярда

poundy = float(input ("Введіть кількість метрів: "))

yards = float(input ("Введіть кількість метрів: "))

value_poundy = poundy * 3.2808399
value_yards = yards * 1.0936133

print("Результат в фунтах", value_poundy)
print("Результат в ярдах", value_yards)

#Щоб спекти пиріг потрібно 4 яблука та 1.2 літра молока.
#Користувач вводить кількість яблук та молока(у літрах).
#Виведіть скільки він може спекти пирогів.
#Виведіть скільки яблук та молока залишиться
apples_per_pie = 4
milk_per_pie = 1.2

apples = int(input("Введіть кількість яблук: "))
milk = float(input("Введіть кількість молока (в літрах): "))

pies_by_apples = apples // apples_per_pie
pies_by_milk = milk // milk_per_pie


pies = int(min(pies_by_apples, pies_by_milk))


apples_left = apples - pies * apples_per_pie
milk_left = round(milk - pies * milk_per_pie, 2)

print("Можна спекти пирогів:", pies)
print("Залишилося яблук:", apples_left)
print("Залишилося молока:", milk_left, "літр(ів)")

#Користувач вводить кількість днів. Виведіть скільки це років, тижнів та днів.
#Наприклад, 398 днів – 1рік 4 тижні 5 днів
total_days = int(input("Введіть кількість днів: "))

years = total_days // 365
remaining_days = total_days % 365
weeks = remaining_days // 7
days = remaining_days % 7

print(f"{total_days} днів — це {years} рік(років), {weeks} тиждень(тижнів), {days} день(днів)")









