# Користувач вводить рядок англійською мовою. Порахуйте
# скільки в ньому голосних літер(aeuio)
VOWELS = {'a', 'e', 'i', 'o', 'u'}

text = input("Введіть будь-яку фразу англійською: ")

count = 0

for letter in text:
    if letter in VOWELS:
        count += 1

print(f"{count} кількість голосних у фразі")


# Користувач вводить текст.
# Після чого запускається цикл і користувач вводить певне
# слово. Треба це слово в тексті замінити на верхній регістр.
# Цикл закінчується коли введено EXIT
# Приклад:
# Текст – a big red fox is eating red apple
# Слово red – a big RED fox is eating RED apple
# Слово fox – a big RED FOX is eating RED apple
# Слово EXIT – кінець програми, показати результат

text = input("Введіть будь-яку фразу англійською: ")


while True:
    word = input("Введіть слово, яке треба замінити: ")
    if word == "EXIT":
        break
    elif word in text:
        text = text.replace(word, word.upper())
        print(text)

# Користувач вводить текст. Порахуйте скільки в ньому речень

text = input("Введіть текст: ")
count = 0

for char in text:
    if char in '!?':
        count += 1

print(f"В цьому тексті {count}  речення")


