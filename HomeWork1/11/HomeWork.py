# Користувач вводить з клавіатури три числа. Необхідно знайти суму чисел, добуток чисел. Результат обчислень вивести на екран.
num1 = input("Введіть перше число: ")
num1 = int(num1)

num2 = input("Введіть друге число: ")
num2 = int(num2)

num3 = input("Введіть третє число: ")
num3 = int(num3)

result = num1 * num2 * num3
result2 = num1 + num2 + num3
print("Добуток чисел", result)
print("Сума чисел", result2)

# Напишіть програму, що обчислює площу ромба. Користувач з клавіатури вводить довжину двох його діагоналей.
length = input("Введіть довжину ромба : ")
length = float(length)

width = input("Введіть ширину ромба : ")
width = float(width)

result = (length * width) / 2
print("Площа ромба: ", result)

# Користувач вводить з клавіатури три числа. Перше число - зарплата за місяць, друге число — сума місячного платежу за кредитом у банку, третє число — заборгованість за комунальні послуги. Необхідно вивести на екран суму, яка залишиться у користувача після всіх виплат.
salary = input("Введіть місячну зарплату: ")
salary = float(salary)

bank_credit = input("Введіть суму кредиту на місяць: ")
bank_credit = float(bank_credit)

utility_debt = input("Введіть суму заборгованості комунальних: ")
utility_debt = float(utility_debt)

result = salary - bank_credit - utility_debt
print("Залишок по грошам: ", result)

# Напишіть програму, яка обчислює вартість поїздки на автомобілі. Користувач вводить відстань у кілометрах, витрату палива на 100 кілометрів і ціну за літр бензину. Програма повинна вивести підсумкову вартість поїздки.
distance = input("Введіть відстань у км: ")
distance = float(distance)

use_of_gas = input("Введіть використання бензину на 100км: ")
use_of_gas = float(use_of_gas)

gas_cost = input("Введіть вартість бензину 1л/грн: ")
gas_cost = float(gas_cost)

fuel_needed = (distance / 100) * use_of_gas
result = fuel_needed * gas_cost

print("Вартість поїздки: ", result)