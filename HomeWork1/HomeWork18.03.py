# Є текстовий файл. Запишіть в інший файл таку
# статистику:
#  Кількість символів
#  Кількість рядків
#  Кількість цифр
#  Кількість голосних літер(aeuio)

filename = "text.txt"

with open(filename, "r", encoding="utf-8") as file:
    text = file.readlines()

total_len = 0
for line in text:
    total_len += len(line)

line_count = len(text)

digit_count = 0
for line in text:
    for char in line:
        if char.isdigit():
            digit_count += 1

vowels = "aeiou"
count_aeuio = 0
for line in text:
    for char in line.lower():
        if char in vowels:
            count_aeuio += 1

new_filename = "new_text.txt"

with open(new_filename, "w", encoding="utf-8") as file:
    file.write(f"Кількість символів: {total_len}\n")
    file.write(f"Кількість рядків: {line_count}\n")
    file.write(f"Кількість цифр: {digit_count}\n")
    file.write(f"Кількість голосних: {count_aeuio}\n")

print("Статистика записана у файл!")

# Користувач вводить слово та назву файлу. Виведіть
# кількість цього слова у файлі.
with open('text.txt', "r", encoding="utf-8") as file:
        text = file.read().lower()

    words = text.split()
    count = words.count(words)

    print(f"Слово '{words}' з'явилося {count} разів.")

#Є текстовий файл. Видаліть з нього останній рядок.
    with open('text.txt', "r", encoding="utf-8") as file:
        lines = file.readlines()

    if lines:
        lines = lines[:-1]

    with open('text.txt', "w", encoding="utf-8") as file:
        file.writelines(lines)

    print("Останій рядок видалено")

