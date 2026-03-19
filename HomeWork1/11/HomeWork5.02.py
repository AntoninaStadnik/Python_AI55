# Напишіть гру «Wordy». Є загадане комп’ютером
# слово з 5-ти літер, здача користувача вгадати його.
# Користувач по черзі вводить свої варіанти
# відповіді після чого показується статистика:
#  скільки літер правильні і стоять в правильному
# місці
#  скільки літер правильні, але стоять в
# неправильному місці
# Гра продовжується поки користувач не вгадає
# слово, або не введе END(в цьому випадку показати
# загадане слово

SECRET_WORD = "apple"

trial_counter = 7
right_place_counter = 0
exist_wrong_place = 0
used_letters = []

print("Вітаємо у Wordly, почнемо! Комп'ютер загадав слово. Ваша задача, вдгадати слово.")

while True:
    letter = input("Введіть слово: ").lower().strip()
    # зупиняємо гру, якщо юзер ввід слово енд
    if letter == "end":
        print(f"Гра завершена, загадане слово {SECRET_WORD}")
        break
    #перевірка чи літера
    if not letter.isalpha():
        print("Допустимі тільки літери")
        continue
    #перевіряємо чи в слові дійсно 5 літер
    if len(letter) != 5:
        print("Слово має складатися з 5 літер")
        continue
    #якщо словов вже використовувалося
    if letter in used_letters:
        print("Ви вже вводили це слово")
        continue
    else:
        used_letters.append(used_letters)

    #якщо в слові є буква і вона на правильному місці (наче правильно)
    for i in range(len(SECRET_WORD)):
        if SECRET_WORD[i] == letter[i]:
            right_place_counter += 1

    for i in range(len(SECRET_WORD)):
        if SECRET_WORD[i] == user_word[i]:
            right_place_counter += 1

        elif user_word[i] in SECRET_WORD and SECRET_WORD[i] != user_word[i]:
            exist_wrong_place += 1


    trial_counter -= 1

    print(f"Правильні літери на правильному місці: {right_place_counter}")
    print(f"Правильні літери на неправильному місці: {exist_wrong_place}")
    print(f"Залишилось спроб: {trial_counter}")
    #перемога
    if right_place_counter == len(SECRET_WORD):
        print("ВІТАЮ! Ви вгадали слово!")
        break
    #програш
    if trial_counter == 0:
        print(f"Ви програли. Загадане слово було: {SECRET_WORD}")
        break









