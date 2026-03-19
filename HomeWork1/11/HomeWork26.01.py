# Користувач вводить слово та індекс. Замініть символ під
# цим індексом на *. Скористайтесь зрізами
# Приклади:
# hello 1 – h*llo
# hello 2 – he*lo

# word = input("Введіть слово: ")
# index = int(input("Введіть індекс: "))
#
# if 0 <= index < len(word):
#     result = word[:index] + "*" + word[index + 1:]
#     print(result)
# else:
#     print("Некоректний індекс")


# Користувач вводить слово. Зробіть першу та останню літеру великою.

text = input("Введіть слово: ")

sym = text[0].upper()
sym2 = text [-1].upper()
text1 = text[1:-2]
result = sym +  text1 + sym2
print(result)


# Користувач вводить слова, поки не введе END. Виведіть в
# кінці ті слова, які починаються і закінчуються на одну і ту саму літеру.
# Приклади: око, дід, Ротор, Ангора
count = 0

while True:
    word = input("Введіть слово: ")
    if word == "END":
        break
    elif word == word[::-1]:
        count += 1
        print(f"Паліндром, {word[::-1]}, {count} ")
    else:
        print(f"Не паліндром, {word}")




