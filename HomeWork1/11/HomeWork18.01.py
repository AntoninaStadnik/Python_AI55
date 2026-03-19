# Напишіть програму для роботи онлайн магазину.
# Товари:
#  подушка – 450 грн
#  ковдра – 1200 грн
#  лампа – 500 грн
#  брилок – 60 грн
# Меню:
#  додати товар
#  видалити товар
#  очистити кошик
#  показати суму покупки
#  вихід
# В залежності від вибору користувача, програма просить
# ввести назву товару та його кількість
total = 0

CUP = 450
BLANKET = 1200
LAMP = 500
KEYCHAIN = 60

print("Меню:")
print("1. додати товар")
print("2. видалити товар")
print("3. очистити кошик")
print("4. вихід")

while True:
    user_choice = int(input("Введіть номе дії (1-4): "))
    if user_choice == 4:
        print("Вихід")
        break

    elif user_choice == 1:
        product = input("Оберіть товар (чашка, ковдра, лампа, брелок): ")
        amount = int(input("Введіть кількість: "))

        if product == "чашка":
            total += amount * CUP
            print(f"Додано чашок на суму {amount * CUP}")
        elif product == "ковдра":
            total += amount * BLANKET
            print(f"Додано ковдр на суму {amount * BLANKET}")
        elif product == "лампа":
            total += amount * LAMP
            print(f"Додано ламп на суму {amount * LAMP}")
        elif product == "брелок":
            total += amount * KEYCHAIN
            print(f"Додано брелків на суму {amount * KEYCHAIN}")
        else:
            print("Немає такого товару")
            break

    if user_choice == 2:
        product = input("Оберіть товар (чашка, ковдра, лампа, брелок): ")
        amount = int(input("Введіть кількість: "))
        if product == "чашка":
            total += amount * CUP
            print(f"Ви видалили чашки з корзини на сумму {amount * CUP}")
        elif product == "ковдра":
            total += amount * BLANKET
            print(f"Ви видалили ковдри з корзини на сумму {amount * BLANKET}")
        elif product == "лампа":
            total += amount * LAMP
            print(f"Ви видалили лампи з корзини на сумму {amount * LAMP}")
        elif product == "брелок":
            total += amount * KEYCHAIN
            print(f"Ви видалили брелки з корзини на сумму {amount * KEYCHAIN}")
        else:
            print("Немає такого товару")
            break

    if user_choice == 3:
            print("Кошик очищенно")
            break

print("Дякуємо, що обрали наш онлайн магазин. До зустрічі!")


