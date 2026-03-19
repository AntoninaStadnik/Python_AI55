# Видалення знаків пунктуації з рядка: ,.?!;:
#  Підрахунок кількості голосних у рядку
#  Перевірка чи є рядок паліндромом(читається однаково
# задом наперед)
# Імпортуйте цей модуль в іншому файлі та використайте
# всі 3 функції.
# Додатково у файлі string_utils.py напишіть код перевірки
# роботи функцій: користувач вводить назву функції та рядок,
# потрібно вивести результат.
# Ця перевірка не повинна запускатись при імпорті в
# іншому файлі.

# Видалення знаків пунктуації з рядка: ,.?!;:
def remove_punctuation(string: str):
    punctuation = [",",".", "'","?", "!", ";", ":"]
    for char in string:
        if char in punctuation:
            string = string.replace(char, "")
    return string

text1 = input("Введіть будь-яку фразу англійською: ")

result = remove_punctuation(text1)

print(f"{result}")

#Підрахунок кількості голосних у рядку
VOWELS = {'a', 'e', 'i', 'o', 'u'}

def is_vowel(text: str):
    count = 0

    for letter in text:
        if letter in VOWELS:
            count += 1
    return count

text2 = input("Введіть будь-яку фразу англійською: ")

result = is_vowel(text2)

print(f"Кількість голосних {result}")

#Перевірка чи є рядок паліндромом(читається однаково задом наперед)
def is_palindrome(phrase: str):

    phrase = phrase.strip().lower()

    if phrase == phrase[::-1]:
        return True
    else:
        return False

word = input("Введіть фразу: ")

if is_palindrome(word):
    print("Так, це паліндром")
else:
    print(f"Ні, {word} не палідром")