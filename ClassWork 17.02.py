# Хрестики Нулики

# глобальні змінні
# хрестик
# нулик

# функції(підзадачі)
# створення сітки -- list[list[str]]

# добавити новий елемент на сітку(отримує координати та символ)

# спитати користувача куди добавити новий символ(отримує ім'я користувача)
# уточнює якщо клітинка занята

# перевірка(хто виграв)
# варіанти результату
#   * хрестик
#   * нулик
#   * None -- нічия

# перевірка чи гра все ще триває(чи є вільне місце)

# main -- головна функція, організовує вся роботуґзапускає програму


from typing import Literal, Optional

# Тип для символів на сітці
CROSS = "X"
ZERO = "O"
EMPTY_SYMBOL = " "
Symbol = Literal["X", "O"]
Cell = Literal["X", "O", " "]  # " " — порожня клітинка


def create_grid(size: int = 3) -> list[list[Cell]]:
    """
    Створює і повертає порожню сітку для гри «Хрестики-нулики».

    :param size: int - Розмір квадратної сітки (типово 3x3)
    :return: list[list[Cell]] - Двовимірний список, що представляє ігрове поле.
             Кожна клітинка містить "X", "O" або " " (пробіл для порожньої).
    """
    grid = []

    for _ in range(size):
        row = []
        for empty_row in range(size):
            row.append(EMPTY_SYMBOL)
        grid.append(row)

    return grid


def print_grid(grid: list[list[Cell]]) -> None:
    """
    Виводить поточний стан сітки на екран у зручному для читання вигляді.

    :param grid: list[list[Cell]] - Поточна сітка гри.
    :return: None
    """
    for row in grid:
        print(" | " + " | ".join(row) + " | " )

#if __name__ == "__main__":
    #grid = create_grid()
    #print_grid(grid)

def add_symbol_to_grid(
    grid: list[list[Cell]],
    row: int,
    col: int,
    symbol: Symbol
) -> bool:
    """
    Додає новий символ на сітку за вказаними координатами.

    :param grid: list[list[Cell]] - Поточна сітка гри.
    :param row: int - Індекс рядка (0-based).
    :param col: int - Індекс стовпчика (0-based).
    :param symbol: Symbol - Символ гравця ("X" або "O").
    :return: bool - True, якщо хід успішний (клітинка була вільна),
                    False, якщо клітинка вже зайнята або координати некоректні.
    """
    size = len(grid)

    if not (0 <= row < size and 0 <= col < size):
        print("Помилка: Координати поза межами поля!")
        return False

    if grid[row][col] != EMPTY_SYMBOL:
        print("Помилка: Ця клітинка вже зайнята!")
        return False

    grid[row][col] = symbol
    return True

def ask_user_move(player_name: str, grid: list[list[Cell]]) -> tuple[int, int] | None:
    """
    Запитує у користувача, куди поставити новий символ.

    Повинна:
    - запитати координати (рядок і стовпчик),
    - перевірити, що клітинка вільна,
    - у разі помилки (зайнята/некоректна) — попросити ввести ще раз.

    :param player_name: str - Ім'я поточного гравця (наприклад, "Гравець X").
    :param grid: list[list[Cell]] - Поточна сітка гри.
    :return: tuple[int, int] - Пара (row, col) з коректними координатами для ходу.
    """
    # TODO:
    # 1. В циклі питати в користувача рядок та стовпчик (через input()).
    # 2. Перевіряти:
    #    - чи це числа;
    #    - чи знаходяться в межах сітки;
    #    - чи клітинка вільна.
    # 3. Якщо все добре — повернути (row, col).
    # 4. Якщо ні — вивести повідомлення про помилку і повторити.
    size = len(grid)

    while True:
        row = input(f"Введіть номер рядка (0-{size - 1}): ")
        col = input(f"Введіть номер стовпчика (0-{size - 1}): ")

        if not row.isdigit() or not col.isdigit():
            print("Помилка: потрібно ввести число.")
            continue

        row = int(row)
        col = int(col)

        if row < 0 or row >= size or col < 0 or col >= size:
            print("Помилка: координати поза межами поля.")
            continue

        if grid[row][col] != " ":
            print("Помилка: клітинка вже зайнята.")
            continue

        return row, col

def check_winner(grid: list[list[Cell]]) -> Literal["X", "O", " "] | None:
    """
    Перевіряє, чи є переможець на поточній сітці.

    Перевіряються:
    - усі рядки,
    - усі стовпці,
    - дві діагоналі (головна і побічна).

    :param grid: list[list[Cell]] - Поточна сітка гри.
    :return: Optional[Symbol] - "X", якщо виграв хрестик,
                                "O", якщо виграв нулик,
                                None, якщо переможця ще немає.
    """
    # TODO:
    # 1. Перевірити кожний рядок: всі елементи однакові та не " ".
    # 2. Перевірити кожний стовпець.
    # 3. Перевірити дві діагоналі.
    # 4. Якщо знайдено три однакові символи ("X" або "O") — повернути їх.
    # 5. Якщо переможця немає — повернути None.
    size = len(grid)
        for row in grid:
            if row[0] != EMPTY_SYMBOL:
                win = True
                for cell in row:
                    if cell != row[0]:
                        win = False
                        break
                if win:
                    return row[0]

        for col in range(size):
            if grid[0][col] != EMPTY_SYMBOL:
                win = True
                for row_idx in range(size):
                    if grid[row_idx][col] != grid[0][col]:
                        win = False
                        break
                if win:
                    return grid[0][col]

       # if grid[0][0] != EMPTY_SYMBOL:
            win = True
            #for i in range(size):
               # if grid[i][i] != grid[0][0]:
                   # win = False
                   # break



def has_empty_cells(grid: list[list[Cell]]) -> bool:
    """
    Перевіряє, чи є на сітці ще вільні (порожні) клітинки.

    :param grid: list[list[Cell]] - Поточна сітка гри.
    :return: bool - True, якщо є хоч одна порожня клітинка,
                    False, якщо поле повністю заповнене.
    """
    # TODO: пройти по всіх клітинках і перевірити, чи є хоча б одна " ".
    pass


def is_game_over(grid: list[list[Cell]]) -> bool:
    """
    Перевіряє, чи гра завершена.

    Гра завершується, якщо:
    - є переможець, або
    - немає вільних клітинок (нічия).

    :param grid: list[list[Cell]] - Поточна сітка гри.
    :return: bool - True, якщо гра завершена, False інакше.
    """
    # TODO:
    # 1. Використати check_winner().
    # 2. Використати has_empty_cells().
    # 3. Повернути True, якщо є переможець або немає порожніх клітинок.
    pass


def switch_player(player: Symbol) -> Symbol:
    """
    Змінює поточного гравця.

    :param player: Symbol - Поточний символ гравця ("X" або "O").
    :return: Symbol - Інший символ ("O" якщо був "X", і навпаки).
    """
    # TODO: повернути "O" якщо player == "X", і "X" якщо player == "O".
    pass


def main() -> None:
    """
    Головна функція. Організовує всю роботу гри та запускає програму.

    Алгоритм:
    1. Створити порожню сітку.
    2. Встановити стартового гравця (наприклад, "X").
    3. У циклі:
       - вивести сітку;
       - запитати хід у поточного гравця;
       - додати символ до сітки;
       - перевірити, чи є переможець;
       - перевірити, чи ще є вільні клітинки;
       - при завершенні гри вивести результат (хто виграв або нічия);
       - переключити гравця.
    """
    # TODO: реалізувати основний ігровий цикл за описаним алгоритмом.
    pass
