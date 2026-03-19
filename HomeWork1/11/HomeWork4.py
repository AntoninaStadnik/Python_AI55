#Користувач вводить ціну за одиницю товару та кількість
#товару. Якщо загальна сума більша за 500грн або купівля
#оптом(більше 10 шт), застосувати знижку 10%


DISCOUNT = 0.10
COMMON_PRICE = 500
COMMON_QUANTITY = 10

price_per_unit = float(input("Input price: "))
quantity = int(input("Input quantity: "))

goods_result = price_per_unit * quantity

if goods_result > COMMON_PRICE or goods_result > COMMON_QUANTITY:
    use_discount = DISCOUNT * goods_result
    goods_result = goods_result - use_discount
    print(f"Your discount is: {use_discount:.2f}" )

else:
    print("No discount:")

print("Final price:", goods_result)


#Користувач вводить 2 оцінки студента.
# Якщо обидві більші за 60, то вивести «Склав»
# Якщо лише одна більша за 60 – вивести «Перездача»
# Якщо обидві менші за 60 – вивести «Не склав»

student_mark1 = int(input("Input marks1: "))
student_mark2 = int(input("Input marks2: "))

if student_mark1 > 60 and student_mark2 > 60:
    print("Passed")

elif student_mark1 > 60 or student_mark2 > 60:
    print("Need to re-pass")

elif student_mark1 < 60 and student_mark2 < 60:
    print("Failed")

else:
    print("Try again")


# Користувач вводить рік, перевірте чи є він високосним.
# Високосний рік має ділитись на 4 та не ділитись на 100
# Наприклад, 2024 – високосний, 2025 – не високосний(не
# ділиться на 4), 2100 – не високосний(ділиться на 100)

year = int(input("Input year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 4 != 0 and year % 100 == 0):
    print("leap year")
else:
    print("non-leap year")


# Користувач вводить суму кредиту та термін у роках.
# Виберіть відсоткову ставку за такими умовами:
#  Для кредиту до 10 000$ на термін до 3 років – ставка 8%
#  Для кредиту до 10 000$ на термін понад 3 роки – ставка 10%
#  Для кредиту від 10 001$ до 50 000$ на термін до 3 років – ставка 12%
#  Для кредиту від 10 001$ до 50 000$ на термін понад 3роки – ставка 14%
#  Для кредиту від 50 000$ на будь-який термін – ставка 20%
# Виведіть відсоткову ставку, загальну суму кредиту та щомісячний платіж

credit_amount = float(input("Input credit amount: "))
years_credit = int(input("Input duration in years: "))

if credit_amount <= 10000 and years_credit <= 3:
    rate = credit_amount * 0.08 * years_credit
    print(f"Your rate amount is: {rate:.2f}")
    common_amount = credit_amount + rate
    print(f"Your common amount is: {common_amount:.2f}")
    monthly = common_amount / (years_credit * 12)
    print(f"Your monthly amount is: {monthly:.2f}")


#  Для кредиту до 10 000$ на термін понад 3 роки – ставка 10%
elif credit_amount <= 10000 and years_credit > 3:
    rate = credit_amount * 0.10 * years_credit
    print(f"Your rate amount is: {rate:.2f}")
    common_amount = credit_amount + rate
    print(f"Your common amount is: {common_amount:.2f}")
    monthly = common_amount / (years_credit * 12)
    print(f"Your monthly amount is: {monthly:.2f}")


#  Для кредиту від 10 001$ до 50 000$ на термін до 3 років – ставка 12%
elif 10001 <= credit_amount <= 50000 and years_credit <= 3:
    rate = credit_amount * 0.12 * years_credit
    print(f"Your rate amount is: {rate:.2f}")
    common_amount = credit_amount + rate
    print(f"Your common amount is: {common_amount:.2f}")
    monthly = common_amount / (years_credit * 12)
    print(f"Your monthly amount is: {monthly:.2f}")

#  Для кредиту від 10 001$ до 50 000$ на термін понад 3роки – ставка 14%
elif 10001 <= credit_amount <= 50000 and years_credit >= 3:
    rate = credit_amount * 0.14 * years_credit
    print(f"Your rate amount is: {rate:.2f}")
    common_amount = credit_amount + rate
    print(f"Your common amount is: {common_amount:.2f}")
    monthly = common_amount / (years_credit * 12)
    print(f"Your monthly amount is: {monthly:.2f}")

#  Для кредиту від 50 000$ на будь-який термін – ставка 20%
elif credit_amount >= 50000:
    rate = credit_amount * 0.20 * years_credit
    print(f"Your rate amount is: {rate:.2f}")
    common_amount = credit_amount + rate
    print(f"Your common amount is: {common_amount:.2f}")
    monthly = common_amount / (years_credit * 12)
    print(f"Your monthly amount is: {monthly:.2f}")

else:
    print("Credit conditions are not met")