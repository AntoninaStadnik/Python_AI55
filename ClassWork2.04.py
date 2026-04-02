# Створіть наступні класи:
#  Rectangle – атрибути width, height
#  Circle – атрибути radius
#  Triangle – атрибути a, b, c
# Методи:
#  get_perimeter()
#  display_info()
# Напишіть функцію create_figure() яка запитує у користувача
# тип фігури та потрібні атрибути і повертає об’єкт.
# Створіть декілька фігур, добавте їх у список та для кожної
# викличте відповідні методи.
import math


class Rectangle:
    def __init__(self, width: int, height: int):
        self._width = width
        self._height = height

    def get_area(self) -> float:
        return 2 * (self._width + self._height)

    def display_info(self):
        print(f"The area of rectangle is width: {self._width} height: {self._height}")


class Circle:
    def __init__(self, radius: float):
        self.radius = radius

    def get_area(self) -> float:
        return 2 * math.pi * self.radius

    def display_info(self):
        print(f"The area of circle is {self.radius}")


class Triangle:
    def __init__(self, a: float, b: float, c: float):
        self.a = a
        self.b = b
        self.c = c

    def get_area(self) -> float:
        return self.a + self.b + self.c

    def display_info(self):
        print(f"The area of triangle is {self.a} x {self.b} x {self.c}")


def create_figure() -> Rectangle | Circle | Triangle | None:
    figure_type = input("Please enter figure type Rectangle, Circle, Triangle: ")
    if figure_type == "Rectangle":
        width = int(input("Please enter width of rectangle: "))
        height = int(input("Please enter height of rectangle: "))
        return Rectangle(width, height)

    elif figure_type == "Circle":
        radius = float(input("Please enter radius of circle: "))
        return Circle(radius)

    elif figure_type == "Triangle":
        a = float(input("Please enter number for a side: "))
        b = float(input("Please enter number for b side: "))
        c = float(input("Please enter number for c side: "))
        return Triangle(a, b, c)

    else:
        print("Invalid input")
        return None


figures = []
figures.append(create_figure())
figures.append(create_figure())
figures.append(create_figure())

for figure in figures:
    if figure is not None:
        figure.display_info()
        print("Invalid input")


# Створіть наступні класи:
#  Manager – атрибути name, base_salary
#  Developer – атрибути name, base_salary, work_experience
#  Inter – атрибути name, base_salary
# Методи:
#  get_salary() – менеджер отримує базову ставку,
# Практичне завдання
# розробник отримує на 20% більше якщо стаж більше 4
# років, інтерн отримує половину базової ставки
# Напишіть функцію create_worker() яка запитує у
# користувача тип працівника та потрібні атрибути і повертає об’єкт.
# Створіть декілька співробітників,
# добавте їх у список та для кожного викличте відповідні методи.


class Manager:
    def __init__(self, name: str, base_salary: float):
        self._name = name
        self._base_salary = base_salary

    def get_salary(self) -> float:
        return self._base_salary


class Developer:
    def __init__(self, name: str, base_salary: float, work_experience: float):
        self._name = name
        self._base_salary = base_salary
        self._work_experience = work_experience

    def get_salary(self) -> float:
        if self._work_experience >= 4:
            return self._base_salary * 1.2
        return self._base_salary


class Inter:
    def __init__(self, name: str, base_salary: float):
        self._name = name
        self._base_salary = base_salary

    def get_salary(self) -> float:
        return self._base_salary / 2


def create_worker() -> Manager | Developer | Inter | None:
    worker = input("Please enter your worker type: ")
    if worker == "Manager":
        name = input("Please enter your worker name: ")
        base_salary = float(input("Please enter your worker salary: "))
        return Manager(name, base_salary)

    elif worker == "Developer":
        name = input("Please enter your worker name: ")
        base_salary = float(input("Please enter your worker salary: "))
        work_experience = float(input("Please enter your worker experience: "))
        return Developer(name, base_salary, work_experience)

    elif worker == "Inter":
        name = input("Please enter your worker name: ")
        base_salary = float(input("Please enter your worker salary: "))
        return Inter(name, base_salary)

    else:
        print("No such worker")
        return None


employees = []

for _ in range(3):
    worker = create_worker()

    if worker:
        employees.append(worker)

for employee in employees:
    print(f"{employee._name} -> {employee.get_salary()}")


# Створіть наступні класи:
#  Car – атрибути speed
#  Bicycle – атрибути speed
#  Boat – атрибути speed
# Методи:
#  move() – виводить повідомлення про рух
# o Car – їде по шосе зі швидкістю
# o Bicycle – їде по дорозі зі швидкістю
# o Boat – пливе по воді зі швидкістю
#  check_speed(speed) – перевіряє чи правильна швидкість,
# якщо ні то в __init__ треба викикати ValueError з
# відповідним повідомленням
# o Car – від 20 до 200
# o Bicycle – від 10 до 30
# o Boat – від 0 до 50
# Напишіть функцію create_vehicle() яка запитує у
# користувача тип транспорту та потрібні атрибути і повертає об’єкт.


class Car:
    def __init__(self, speed: int):
        self._speed = speed

    def move(self):
        print(f"Moving on a road {self._speed} km/h")

    def check_speed(self) -> None:
        if not (20 <= self._speed <= 200):
            raise ValueError("Speed must be between 20 and 200")


class Bicycle:
    def __init__(self, speed: int):
        self._speed = speed

    def move(self):
        print(f"Moving on a road {self._speed} km/h")

    def check_speed(speed) -> int:
        if speed == 10 or speed == 30:
            return True
        else:
            raise ValueError("Speed must be between 10 and 30")


class Boat:
    def __init__(self, speed: int):
        self._speed = speed

    def move(self):
        print(f"Moving on water {self._speed} km/h")

    def check_speed(speed) -> int:
        if speed == 0 or speed == 100:
            return True
        else:
            raise ValueError("Speed must be between 0 and 100")


def create_vehicle() -> Car | Bicycle | Boat | None:
    vehicle = input("Please enter your vehicle type: ")
    if vehicle == "Car":
        speed = int(input("Please enter your vehicle speed: "))
        return Car(speed)
    elif vehicle == "Bicycle":
        speed = int(input("Please enter your vehicle speed: "))
        return Bicycle(speed)
    elif vehicle == "Boat":
        speed = int(input("Please enter your vehicle speed: "))
        return Boat(speed)
    else:
        print("No such vehicle")
        return None


vehicles: list[Car | Bicycle | Boat] = []

for _ in range(3):
    v = create_vehicle()

    if v is not None:
        vehicles.append(v)

for v in vehicles:
    v.move()
