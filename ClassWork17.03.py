# Є текстовий файл. Виведіть кількість рядків та кількість символів в ньому
# with open("text.txt") as file:
#     text = file.read()
#
# count_chars = len(text)
# print(count_chars)
#
# count_lines = text.count('\n') + 1
# print(count_lines)
import fileinput

# Користувач вводить ім’я та вік. Запишіть їх у файл. Назву
# файлу також вводить користувач(без розширення .txt)
# name = input("Input name: ")
# age = int(input("Input age: "))
# file_name = input("Input file name: ")
#
# with open(file_name + ".txt", "w", encoding="UTF-8") as file:
#     file.write("Hello " + name + "!")
#     file.write("\n")
#     file.write(f"{age}")


# Є текстовий файл. Запишіть його рядки в інший файл.
# with open('text.txt','r') as file:
#     text = file.readlines()
#
#     with open('text1.txt','w') as file:
#         file.writelines(text)

# Користувач вводить літеру та назву файлу. Виведіть усі
# слова з файлу, які починаються на цю літеру.

# letter = input("Enter a letter: ").lower().strip()
#
# file_name = input("Enter a file name: ") + ".txt"
#
# with open(file_name, "r", encoding="utf-8") as file:
#     file_content = file.read()
#
# words = file_content.split()  # розбиваємо на слова, а не на рядки
#
# for word in words:
#     if word.lower().startswith(letter):
#         print(word)

# Є текстовий файл. Замініть у ньому усі символи * на &, та
# навпаки.
with open("text.txt") as file:
    text = file.read()

new_text = ""

for line in text:
    if line == "*":
        new_text += "&"
    elif line == "&":
        new_text += "*"
    else:
        new_text += line

with open("text.txt", "w") as file:
    file.write(new_text)