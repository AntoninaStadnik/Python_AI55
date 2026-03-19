# Напишіть власний модуль date_utils.py з функцією яка
# отримує дату дедлайну у форматі YYYY-MM-DD. Поверніть
# кількість днів яка залишилаь до дедлайна.
# Імпортуйте цей модуль в іншому файлі та використайте
# функцію, дедлайн вводить користувач. Якщо залишилось
# менше тижня до кінця дедлайна, виведіть відповідне
# повідомлення.
# Див datetime.date.fromisoformat()
#  datetime.date.today()
#  datetime.timedelta.days

from datetime import date, datetime

def get_deadline_date(today: date, deadline: date) -> int:
    days_left = (deadline - today).days

    if days_left <= 7:
        print(f"До дедлайну залишилося менше 7 днів")

    return days_left

today = date.today()
ask_deadline = input("Введіть скільки залишилося до дедлайну(у форматі YYYY-MM-DD): ")
deadline = date.fromisoformat(ask_deadline)

days_left = get_deadline_date(today, deadline)

print("До дедлайну залишилося:", days_left, "днів")




