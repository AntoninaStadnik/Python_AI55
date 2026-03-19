# Є деякий текст. Виведіть по ньому статистику:
#  кількість слів
#  середня довжина слова
#  найдовше слово
#  найкоротше слово

# text = input("Введіть текст: ")
#
# #  кількість слів
# words = text.split()
# num_words = len(words)
# print("Кількість слів:", num_words)
#
# #  середня довжина слова
# total = 0
#
# for word in words:
#     total += len(word)
#
# avarage_length = total / num_words
#
# print("Середня довжина слова:", avarage_length)
#
# #  найдовше слово
# longest_word = words[0]
#
# for word in words:
#     if len(word) > len(longest_word):
#         longest_word = word
#
# print("Найдовше слово: ", longest_word)
#
# #  найкоротше слово
# shortest_word = words[0]
#
# for word in words:
#     if len(word) < len(shortest_word):
#         shortest_word = word
#
# print("Найкоротше слово: ", shortest_word)


# Є список з іменами. Видаліть лишні пробіли і переведіть
# їх у формат “Прізвище Ім’я”
# Приклад:
# Список:
#  " іванов пЕТРО",
#  "сидорЕНКО марія ",
#  " Коваленко АНДРІЙ",
#  " мИХАЙЛЕНКО оЛЕНА "

names = [" іванов пЕТРО"]

new_names = []

for name in names:
    clean = name.strip()
    new = clean.split()

    for name in new_names:
        new_names.append(new)








