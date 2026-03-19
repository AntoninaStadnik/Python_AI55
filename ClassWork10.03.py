# Користувач вводить імена людей, поки не введе порожній
# рядок. Збережіть усі імена в множині. Якщо ім’я вводиться
# повторно, то вивести повідомлення про це.
# Виведіть кількість людей
user_name = set()

while True:
    data = input("Введіть ім'я: ")

    if data == "":
        print("Програму завершено")
        break
    if data in user_name:
        print("Таке ім'я вже є")
    else:
        user_name.add(data)

count = len(user_name)
print("Множина користувача:", user_name, count)


# Студентів розбили на 2 групи, кожна з яких навчається у
# свій день. Перевірте чи не виникло помилки, а саме
#  Чи немає студентів які є в двох групах одночасно(якщо є, то вивести їх імена)
#  Чи немає студентів, про яких забули(якщо є, то вивести імена)
# Напишіть відповідну функцію, яка отримує два списки з
# іменами студентів кожної групи, та список усіх студентів
group1 = ["Mike", "John", "Joe", "Jack"]
group2 = ["Mary", "Alise", "Roy", "Jack"]
all_students = ["Mike", "John", "Joe", "Jack", "Mary", "Alise", "Roy", "Tom"]

def students_group(group1, group2, all_students):
    group1 = set(group1)
    group2 = set(group2)
    all_students = set(all_students)

    duplicate_students = group1 & group2
    missing_students = all_students - (group1 | group2)

    print("Студенти в двох групах:", duplicate_students)
    print("Забуті студенти:", missing_students)

students_group(group1, group2, all_students)

# Є словник з цінами продуктів, де ключ – назва продукту, а
# значення – ціна за кг. Організуйте просту роботу магазину:
# користувач вводить назву продукту та вагу, потрібно вивести загальну ціну.

goods = {
    "Хліб": 30,
    "Яблука": 40,
    "Сир": 46,
    "Маслини": 89
}
def product_shop(goods):
    name = input("Введіть назву продукту: ")
    amount = float(input("Введіть скільки потрібно кілограм: "))

    if name in goods:
        price = goods[name]
        total = price * amount
        print("Загальна ціна:", total)
    else:
        print("Такого продукту немає в магазині")

product_shop(goods)





