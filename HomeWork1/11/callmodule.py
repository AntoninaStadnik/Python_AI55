from datetime import date
import date_utils

today = date.today()

ask_deadline = input("Введіть дату дедлайну (YYYY-MM-DD): ")
deadline = date.fromisoformat(ask_deadline)

days_left = date_utils.get_deadline_date(today, deadline)

print("До дедлайну залишилося:", days_left, "днів")
