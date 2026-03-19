import random

#Є кортеж з назвами міст. Виведіть ті міста, які зустрічаються в кортежі більше одного разу.
def cities_count():
    cities = ("Kyiv", "Lviv", "Poltava", "Madrid", "Kyiv")

    new_cities = []

    for city in cities:
        if cities.count(city) > 1 and city not in new_cities:
            print(city)
        new_cities.append(city)

cities_count()

#Є два кортежі з випадковими числами. Виведіть на екран ті числа, які є в першому кортежі, але немає в другому.
nums = [random.randint(1, 100) for _ in range(5)]
nums2 = [random.randint(1, 100) for _ in range(5)]

for num in nums:
    if num not in nums2:
     print(num)

# Напишіть функцію, яка отримує 2 кортежі. Поверніть
# список з елементами, які є в обох кортежах і мають однакові
# індекси. Підказка: використайте zip()

def get_words():
    words1 = ('dog', 'cat', 'kitty', 'doggy', 'deduction', 'addresses')
    words2 = ('dog', 'spring', 'kitty', 'winter', 'call', 'python')

    for i, (w1, w2) in enumerate(zip(words1, words2)):
        if w1 == w2:
            print(i)


get_words()


