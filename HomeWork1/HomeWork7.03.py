# Реалізуйте роботу банку. Усі дані зберігаються у
# словнику, де ключ – ім’я клієнта, значення – баланс на
# рахунку.
# Напишіть функцію, яка отримує словник з даними та
# зараховує гроші на баланс. Для цього вона запитує ім’я та
# суму у користувача, якщо користувача немає, то вносить його
# дані у словник, інакше додає суму до балансу.
# Напишіть іншу функцію, яка отримує словник з даними та
# знімає гроші з рахунку. Для цього вона запитує ім’я та суму у
# користувача, якщо користувача немає, то вивести відповідне
# повідомлення. Якщо на балансі не достатньо грошей, теж
# вивести повідомлення.
# Напишіть функцію main, яка організує роботу всієї
# програми, а саме матиме такий функціонал: поповнити
# рахунок, зняти кошти, завершити роботу

bank_customers = {
    "Mary": 1000,
    "John": 2000,
    "Joe": 3000,
    "Mike": 500
}

def add_to_balance(bank_customers):
    name = input("Enter customer name: ")
    amount = float(input("Enter amount to add: "))

    if name in bank_customers:
        bank_customers[name] += amount
    else:
        bank_customers[name] = amount

    print("Balance:", bank_customers[name])


def get_from_balance(bank_customers):
    name = input("Enter customer name: ")

    if name not in bank_customers:
        print("Customer not found")
        return

    amount = float(input("Enter amount to withdraw: "))

    if amount > bank_customers[name]:
        print("Money not enough")
    else:
        bank_customers[name] -= amount
        print("Balance:", bank_customers[name])


def main():

    while True:

        print("1 - Add money")
        print("2 - Withdraw money")
        print("3 - Exit")

        choice = input("Choose operation: ")

        if choice == "1":
            add_to_balance(bank_customers)

        elif choice == "2":
            get_from_balance(bank_customers)

        elif choice == "3":
            print("Program finished")
            break

        else:
            print("Invalid choice")


main()





