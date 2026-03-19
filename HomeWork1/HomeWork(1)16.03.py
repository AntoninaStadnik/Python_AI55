# Є словник з курсами валют, де ключ – назва валюти,
# значення – курс до гривні. Користувач вводить назву валюти,
# суму та назву нової валюти, в яку треба перевести суму.
# Підказка 1: для того щоб перевести, скажімо, 10 доларів у
# євро, спочатку треба перевести 10 доларів у гривні, після чого
# гривні переводити у євро.
# Підказка 2: щоб можна було переводити долари у
# гривні(або гривні у долари), потрібно щоб у словнику була
# інформація скільки гривень в 1 гривні
#from contourpy.util import data

rates = {
    "USD": 40,
    "EUR": 50,
    "PLN": 10,
    "UAH": 1
}

ask_currency = input("Введіть валюту з якої перевести: ").upper()
ask_amount = float(input("Введіть суму: "))
get_new_currency = input("Введіть валюту, в яку бажаєте перевести: ").upper()

if ask_currency not in rates:
    raise ValueError("Такої валюти немає")

if get_new_currency not in rates:
    raise ValueError("Такої валюти немає")

rate_from = rates[ask_currency]
rate_to = rates[get_new_currency]

amount_uah = ask_amount * rate_from
result = amount_uah / rate_to

print(f"{ask_amount} {ask_currency} = {result} {get_new_currency}")


# Напишіть функцію, яка отримує 2 множини з іменами
# працівників, які працюють в офісі та віддалено. Виведіть на
# екран:
#  Імена усіх працівників
#  Імена працівників, які працюють і в офісі, і віддалено
#  Відсоток працівників, які працюють і в офісі, і віддалено
emp_in_office = ["John", "Mike", "Odry", "Sara"]
emp_remote = ["Jack", "Wesley", "Abby", "Chad"]

def get_employees(emp_in_office, emp_remote):
    emp_in_office = set(emp_in_office)
    emp_remote = set(emp_remote)

    all_employees = emp_in_office | emp_remote
    office_and_remote = all_employees & emp_in_office
    if len(all_employees) > 0:
        percentage = len(office_and_remote) / len(all_employees) * 100
    else:
        percentage = 0

    print(f"Імена всіх працівників: {all_employees}")
    print(f"Імена працівників, які працюють і в офісі, і віддалено {office_and_remote}")
    print(f"Відсоток працівників, які працюють і в офісі, і віддалено {percentage:.2f}%")

get_employees(emp_in_office, emp_remote)



