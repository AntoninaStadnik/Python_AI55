# Користувач вводить через кому список товарів. Виведіть
# цей список на екран, але без повторень назв товарів
data = input("Введіть товари через кому: ")

if data.strip():
    user_goods = set((x.strip()) for x in data.split(","))
    print(f"Ви обрали наступні товари: {user_goods}")

# У магазині є два списки клієнтів: ті хто отримав знижкові купони, і ті хто ними скористався.
# Напишіть функцію, яка отримує 2 списки та виводить
# інформацію:
#  Імена тих, хто отримав купон, але не скористався, також вивести їх кількість
#  Імена шахраїв, які скористались знижкою, але магазин не давав їм купони
customers_with_discount = ["Олена", "Галина", "Орися", "Петро", "Іван"]
customers_used_discount = ["Марина", "Оксана", "Григорій"]

def shop_customers(customers_with_discount, customers_used_discount):
    unused_discount = set(customers_with_discount)
    scammers_user = set(customers_used_discount)

    scam_res = unused_discount - scammers_user
    print(f"Хто отримав купон, але не використав: {scam_res}")
    print(f"Кількість: {len(scam_res)}")

    used_res = scammers_user - unused_discount
    print(f"Шахраї {used_res}")


shop_customers(customers_with_discount, customers_used_discount)



