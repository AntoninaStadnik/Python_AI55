# Напишіть функцію, яка отримує 2 словника та об’єднує їх
# в один. Якщо ключі співпадають то потрібно додати відповідні їм значення.
def unite_dict(data, data2):
    result = data.copy()

    for key, value in data2.items():
        if key in result:
            result[key] = result[key] + value
        else:
            result[key] = value

    return result

data_list = {
        "Oksana": 50,
        "Petro": 60,
        "Oleksiy": 70,
    }

data2_list = {
        "Ofelia": 50,
        "Peter": 60,
        "Oleksiy": 70,
    }

united = unite_dict(data_list, data2_list)
print(united)

# Напишіть функцію, яка отримує словник та інвертує його,
# тобто повертає новий словник, де ключі та значення змінені місцями.
def invert(data):
    result = {}

    for key, value in data.items():
         result[value] = key

    return result

vocabulary = {
        "Ivan": 25,
        "Oksana": 30,
        "Petro": 40
    }

print(invert(vocabulary))

# Користувач вводить назви товарів та їх ціни поки не введе
# порожній рядок. Збережіть дані у словник. Якщо користувач
# вводить товар повторно та треба додати стару та нову ціни.
# В кінці виведіть таблицею товар – ціна. Також виведіть загальну ціну.

goods = {}

while True:
    name = input("Введіть товар: ").strip()

    if name == "":
        break

    price = float(input("Введіть ціну: "))

    if name in goods:
        goods[name] += price
    else:
        goods[name] = price


total = 0

for key, value in goods.items():
    print(f"Товар {key}, ціна {value}")
    total += value

print(f"Загальна ціна {total}")

print("Загальна сума:", sum(goods.values()))