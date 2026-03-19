# Напишіть функцію, яка запитує користувача пароль та
# повертає його. Якщо пароль поганий, тобто менше 8 символів
# чи містить однакові символи то викликати виняток ValueError.
# Написати код try … except який використовує дану функцію
def ask_password():
    password_name = input("Enter your password, 8 symbols: ")

    if len(password_name) < 8:
        raise ValueError("Incorrect password")

    if len(password_name) != len(set(password_name)):
        raise ValueError("Such symbol already exist")

    return password_name

try:
    password_name = ask_password()
    print(f"{password_name = }")

except ValueError as err:
    print(f"Error, {err}")

# Є словник де ключ – логін, а значення – пароль. Напишіть
# функцію, яка запитує користувача логін та пароль. Якщо
# логіна немає в словнику, або невірний пароль, то викликати
# ValueError.
# Написати код try … except який використовує дану функцію.

user_creds = {
    "Mary": 3498,
    "John": 2290,
    "Jack": 3234,
    "Jan": 4221,
}

def get_login_password():
    login = input("Enter login:")
    password = int(input("Enter password:"))

    if login not in user_creds:
        raise ValueError("Invalid login, try again")

    if password != user_creds[login]:
        raise ValueError("Invalid password, try again")

    return login, password

try:
    login, password = get_login_password()
    print(f"Login success {login}")

except ValueError as err:
    print(f"Error: {err}")
