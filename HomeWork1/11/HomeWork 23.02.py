# Напишіть функцію для обрахунку температури склянки
# води, яку помістили в холодильник через деякий час
# Параметри:
# T_env – температура в холодильнику
# T0 – початкова температура води
# t – час у секундах проведений в холодильнику
# k – коефіцієнт охолодження, за замовчуванням 0.05
# Див math.exp()
import math

K = 0.05

def glass_temperature(T_env: float, T0: float, t: float):
    return T_env + (T0 - T_env) * math.exp(-K * t)

T_env = float(input("Введіть температуру в холодильнику: "))
T0 = float(input("Введіть початкову температуру води: "))
t = float(input("Введіть час у секундах: "))

result = glass_temperature(T_env, T0, t)

print(f"Температура води через {t} сек: {result:.2f}")

# Напишіть функцію з параметром show_time, яка запитує в
# користувача ім’я та повертає його.
# Якщо show_time = True, то функція повинна вивести на
# екран час своєї роботи у секундах.
# Див time.time()
import time

def ask_user_name(show_time):
    start = time.time()
    name = input("Введіть ім'я: ")

    if show_time:
        end = time.time()
        execution_time = end - start
        print(f"Функція працювала {execution_time}")

    return name

res = ask_user_name(True)

print(f"Введене ім'я {res}")







