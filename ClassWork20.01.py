# Користувач вводить рядок та символ. Порахуйте скільки
# разів цей символ зустрічається у рядку.
# Зробіть двома способами: з методом count та з циклом for
# Приклад: в “it is amazing” символ “і” зустрічається 3 рази

text = input("Введіть будь-яку фразу: ")
user_symbol = input("Введіть будь-яку літеур, яку хочете порахувати: ")

result = text.count(user_symbol)
print(f"{result}")
count = 0
for symbol in text:
    if symbol == user_symbol:
        count += 1
    print(count)

# Користувач вводить рядок. Виведіть наступну
# інформацію:
# ● кількість символів
# ● чи є там слово python
# ● кількість шиплячих літер – szh

TARGET_LETTER = 's z h'

text = input("Введіть будь-яку фразу: ")

count = len(text)
print(count)

if 'Python' in text:
    print("yes, Python exist")
else:
    print("no, Python doesn't exist")

 count = 0

if TARGET_LETTER in text:
     count += 1
     print(f"{count} target letter exist")
else:
      print("no target letter exist")


# Користувач вводить текст та слово. Порахуйте скільки
# разів це слово зустрічається в тексті.

user_input = input("Введіть фразу: ")
symbols = input("Введіть слово для пошуку: ")

count = user_input.count(symbols)
print(f"У рядку {count} слів/а.")

# Користувач вводить текст. Порахуйте скільки в ньому
# літер та цифр.
int_count = 0
letter_count = 0

user_input = input("Введіть фразу: ")

for sum in user_input:
    if sum.isdigit():
        int_count += 1
        print(count)
    elif sum.isalpha():
        letter_count += 1
        print(letter_count)

print("Кількість цифр: ", int_count)
print("Кількість літер: ", letter_count)