# Напишіть гру Правда або Дія.
# Опис:
# 1. Спочатку, введіть імена гравців.
# 2. Кожен гравець по черзі обирає "Правда" або "Дія".
# 3. Якщо гравець обрав "Правда", йому задається
# запитання, на яке він повинен відповісти правдиво.
# 4. Якщо "Дія", гравець повинен виконати вказане
# завдання.
# 5. Після завершення кожного раунду, виведіть
# результати.
# Функції:
#  get_player_names(): Запитайте імена гравців і поверніть
# їх у вигляді списку.
#  ask_truth_or_dare(player): Функція, яка приймає ім'я
# гравця та запитує його, чи обирати "Правда" чи "Дія".
#  ask_truth_question(player): Функція, яка приймає ім'я
# гравця, виберє одне запитання випадковим чином та
# просить гравця дати відповідь.
#  perform_dare(player): Функція, яка приймає ім'я гравця
# та вибирає одне завдання випадковим чином та
# просить гравця виконаи його.
# Домашнє завдання
#  play_game(players): Функція, яка керує ходом гри.
# Послідовно запитайте кожного гравця, чи обирати
# "Правда" чи "Дія", а потім відповідно викликайте
# функцію ask_truth_question або perform_dare.
# Константи:
#  questions – список питань
#  dares – список завдань
from random import choice

QUESTION = ['Як довго вчиш Python?', 'Чи є у тебе кіт?', 'Який жанр кіно подобається?']
DARES = ['Присісти 10 разів', 'Кукурікай як півень', 'Стій у планці 30 сек']

def get_player_names() -> list[str]:
    names_input = input("Введіть імена гравців через кому: ")
    name_list = names_input.split(",")

    name_list = [name.strip() for name in name_list]

    return name_list


def ask_truth_or_dare(player: str):
    while True:
        choice_truth_or_dare = input(f"{player}, обери 'правда' або 'дія': ").lower()

        if choice_truth_or_dare == "правда":
            return "правда"
        elif choice_truth_or_dare == "дія":
            return "дія"
        else:
            print("Неправильний вибір. Спробуй ще раз.")

def ask_truth_question(player):
    question = choice(QUESTION)
    print(f"{player}, твоє питання:")
    print(question)

def perform_dare(player):
    dare = choice(DARES)
    print(f"{player}, твоє завдання")
    print(dare)


def play_game(players, question=None):
    for player in players:

        choice = ask_truth_or_dare(player)

        if choice == "правда":
            ask_truth_question(player)
        else:
            perform_dare(player)

players = get_player_names()
play_game(players)