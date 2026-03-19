import string_utils

text1 = "Hey! Today, is the best day to start! Agree?"
remove_punctuation = string_utils.remove_punctuation(text1)
print(remove_punctuation)

text2 = "Hello Python"
vowels_count = string_utils.is_vowel(text2)
print(f"Голосних у '{text1}': {vowels_count}")


word = "Козак з казок"
if string_utils.is_palindrome(text2):
    print(f"'{text2}' — це паліндром")

