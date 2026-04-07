# Створіть клас Message з атрибутами
#  user – ім’я автора повідомлення
#  text – текст повідомлення
#  time – час повідомлення(використайте модуль datetime)
# приклад datetime.strptime('10:23', '%H:%M')
# методи:
#  __str__(self) – повертає текст повідомлення та час
#  __len__(self) – повертає довжину повідомлення
#  __gt__(self, other) – перевіряє чи є повідомлення self
# старішим за other
# Створіть список з декількома повідомленнями та виведіть
# його. Відсортуйте список і знову виведіть
# import datetime
#
# class Message:
#     def __init__(self, user:str, text:str, time:str):
#         self.user = user
#         self.text = text
#         self.time = datetime.datetime.strptime(time, '%H:%M')
#
#     def __str__(self):
#         return f'user: {self.user}, text: {self.text}, time: {self.time}'
#
#     def __len__(self):
#         return len(self.text)
#
#     def __gt__(self, other):
#         return self.time > other.time
#
# mes = Message("John", "Hello there", "11:23")
# mes2 = Message("John", "Hello there", "11:30")
# print(mes)
# print(len(mes))
# print(mes2 > mes)
#
# messages = []
# messages.append(Message("John", "Hello there", "11:23"))
# messages.append(Message("John", "What's up", "13:30"))
# messages.append(Message("John", "Good day", "15:23"))
# #
# # for message in messages:
# #     print(message)
#
# messages.sort()
#
# for message in messages:
#     print(message)

# Створіть клас Song з атрибутами
#  name – назва пісні
#  author – ім’я автора
# Практичне завдання методи:
#  __eq__(self, other) – перевіряє чи дві пісні однакові
#  __str__(self, other) – повертає рядок з назвою та автором
# Створіть клас Playlist з атрибутами
#  songs – список пісень(об’єкти класу Song)
# методи:
#  __len__(self) – повертає кількість пісень
#  __contains__(self, item) – перевіряє чи є пісня в плейлисті
#  __iter__(self) – повертає літератор для циклу for
#  add_song(self, song) – додає пісню в плейлист
#  remove_song(self, song) – видаляє пісню з плейлиста
# Створіть порожній плейлист
# Створіть 3 пісні:
# "Imagine", "John Lennon"
# "Bohemian Rhapsody", "Queen"
# "Shape of You", "Ed Sheeran"
# Добавте їх в плейлист
# Пройдіться циклом for по плейлисту та виведіть кожну пісню на екран

# class Songs:
#     def __init__(self, name:str, author:str):
#         self._name = name
#         self._author = author
#
#     def __eq__(self, other):
#         if isinstance(other, Songs):
#             return self._name == other._name and self._author == other._author
#         return False
#
#     def __str__(self):
#         return f'{self._name} by {self._author}'
#
#
# class Playlist:
#     def __init__(self, songs:list[Songs]):
#         self._songs = songs
#
#     def __len__(self):
#         return len(self._songs)
#
#     def __contains__(self, item):
#         return item in self._songs
#
#     def __iter__(self):
#         return iter(self._songs)
#
#     def add_song(self, song:Songs):
#         self._songs.append(song)
#
#     def remove_song(self, song:Songs):
#         if song in self._songs:
#             self._songs.remove(song)
#         else:
#             print("Song not found")
#
# song = Songs("Imagine", "John Lennon")
# song2 = Songs("Bohemian Rhapsody", "Queen")
# song3 = Songs("Shape of You", "Ed Sheeran")
# song4 = Songs("Umbrella", "Rihana")
#
#
# playlist = Playlist([song, song2, song3])
# print(song == [1,2,4])
# print(song)
#
# playlist.add_song(song4)
# playlist.remove_song(song2)
#
# for song in playlist:
#     print(song)
#
# print(song3 in playlist)

# Створіть клас Cart з атрибутами
#  items – список товарів
#  total – загальна ціна товарів
# методи:
#  __str__(self) – повертає рядок зі списком товарів
#  __len__(self) – повертає кількість товарів
#  __add__(self, other) – об’єднує 2 кошики та повертає
# новий кошик
# Створіть два кошики. Виведіть кількість товарів в кожному
# з них. Виведіть самі кошики. Об’єднайте їх та виведіть
# кількість товарів в новому кошику та товари в ньому


class Cart:
    def __init__(self, items: list, total: float):
        self._items = items
        self._total = total

    def __str__(self):
        return f"Goods: {self._items}, Price: {self._total}"

    def __len__(self):
        return len(self._items)

    def __add__(self, other):
        new_items = self._items + other._items
        new_total = self._total + other._total
        return Cart(new_items, new_total)

    def __iter__(self):
        return iter(self._items)

    def __contains__(self, item):
        return item in self._items


cart1 = Cart(["bread", "butter", "cherry"], 100)
cart2 = Cart(["strawberry", "banana"], 200)
print(cart1)
print(cart2)
print(len(cart1))

cart_all = cart1 + cart2
print(cart_all)
