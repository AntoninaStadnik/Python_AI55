# Є словник з логінами(ключ) та паролями(значення)
# користувачів. Реалізуйте програму яка дозволяє:
#  завантажити дані з файлу
#  зберегти дані у файл
#  додати нового користувача
#  видалити користувача
#  зміна паролю
#  вхід у систему(якщо логін і пароль правильні)
# Реалізуйте все через функції.
import json
from typing import Any

# def load_data(filename: str = "password.json") -> dict[str, str]:
#     with open(filename, 'r', encoding= "utf-8") as file:
#          data = json.load(file)
#          return data
#
# def save_data(data: dict[str, str], filename: str = "password.json") -> None:
#     with open(filename, 'w', encoding= "utf-8") as file:
#         json.dump(data, file, indent=4, ensure_ascii=False)
#
# def add_user(data: dict[str, str]) -> None:
#     login = input("Please enter your login name: ")
#
#     if login not in data:
#        print("Such user exist")
#        return
#
#     password = input("Please enter your password: ")
#     data[login] = password
#
#     if password not in data[login]:
#         print("Such user exist")
#         return
#
# def delete_user(data: dict[str, str]) -> None:
#     login = input("Please enter your login name: ")
#
#     if login not in data:
#         print("Such user does not exist")
#         return
#
#     del data[login]
#     print("User deleted")
#
# def change_password(data: dict[str, str]) -> None:
#     login = input("Please enter your login name: ")
#
#     if login not in data:
#         print("Such user does not exist")
#         return
#
#     password_new = input("Please enter your new password: ")
#     data[login] = password_new
#     print("Password changed")
#
# def login_user(data: dict[str, str]) -> None:
#     login = input("Please enter your login name: ")
#     password = input("Please enter your password: ")
#
#     if login in data:
#         if password == data[login]:
#             print("Login successful")
#         else:
#             print("Login failed")


# Створіть клас Cart
# Атрибути:
#  user – ім’я користувача
#  items – список товарів
#  total – загальна ціна
# Методи:
#  add(item, price) – добавити товар у кошик
#  delete(item, price) – видалити товар з кошика
#  info() – вивести інформацію про кошик
# Практичне завдання
#  save(filename) – зберегти дані у файл(за
# замовчуванням cart.json)
#  load(filename) – завантажити дані з файла(за
# замовчуванням cart.json)


class Cart:
    def __init__(self, user: str):
        self._user = user

        self._total = 0
        self._items: list[str] = []

    def add(self, item: str, price: int):
        self._items.append(item)
        self._total += price

    def delete(self, item: str, price: int):
        if item not in self._items:
            print("Item not exist")
            return

        self._items.remove(item)
        self._total -= price

    def info(self):
        print(f"{self._user}'s, total price:  {self._total}")
        print(f"items: {self._items}")

    def save(self, filename: str = "cart.json"):
        data = {
            "user": self._user,
            "total": self._total,
            "items": self._items,
        }

        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    def load(self, filename: str = "cart.json"):
        with open(filename, encoding="utf-8") as file:
            data = json.load(file)

        self._user = data["user"]
        self._total = data["total"]
        self._items = data["items"]


cart = Cart("John")
cart.add("milk", 100)
cart.add("bread", 200)
cart.save("cart.json")
cart.info()


# Створіть файл settings.json з базовими налаштуваннями
# програми, наприклад графічного інтерфейсу:
#  розмір зображення – 500х600
#  колір фону – сірий
#  колір кнопок – світлосірий
#  розміщення кнопок – [100, 50]
#  інструкція користувачу
# Напишіть код, де завантажується налаштування і
# створюються відповідні змінні size, background_color, …

with open("setting.json", "w", encoding="utf-8") as file:
    data = {
        "size": [500, 600],
        "color": "grey",
        "button_color": "bright grey",
        "placement_buttons": [100, 50],
        "user_instruction": "be a good person",
    }
    json.dump(data, file, indent=4, ensure_ascii=False)


def load_setting() -> dict[str, Any]:
    with open("setting.json", encoding="utf-8") as file:
        data = json.load(file)
        return dict(data)


def save_settings(data: dict[str, Any]) -> None:
    with open("setting.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def change_size(new_size: list[int]) -> None:
    data = load_setting()
    data["size"] = new_size
    save_settings(data)


def change_color(new_color: str) -> None:
    data = load_setting()
    data["color"] = new_color
    save_settings(data)


def show_info() -> None:
    data = load_setting()
    new = json.dumps(data, indent=4, ensure_ascii=False)
    print(new)


# change_size("400x900")
# change_color("blue")
# show_info()
