# Створіть абстрактний клас Robot з атрибутами:
#  name – назва робота або id
#  battery_level – рівень заряду(за замовчуванням 100%)
#  status – поточний стан (один з on, off, working)
# Методи:
#  info() – виводить інформацію
#  charge() – відновлює заряд до 100%
#  turn_on() – змінює стан на on
#  turn_off() – змінює стан на off

from abc import ABC
from enum import Enum
from uuid import uuid4


class RobotStatus(Enum):
    off = "off"
    on = "on"


class Robot(ABC):
    def __init__(
        self, name: str, battery_level: int = 100, status: RobotStatus = RobotStatus.off
    ):
        if name is None:
            name = str(uuid4())

        self.name = name
        self.battery_level = battery_level
        self.status = status

    def show_info(self):
        print(f"Robot: {self.name}")
        print(f"Battery Level: {self.battery_level}")
        print(f"Status: {self.status}")

    def charge(self):
        self.battery_level = 100

    def turn_on(self):
        self.status = RobotStatus.on


robot1 = Robot("Wolli", 100)
robot1.show_info()

# Створіть дочірній клас CleaningRobot
# Додаткові атрибути:
#  dust_capacity – ємність контейнеру для пилу(за
# замовчуванням 0%)
#  water_capacity – ємність контейнеру для води(за
# замовчуванням 100%)
#  cleaning_mode – тип прибирання(вологе або сухе)
# Методи:
#  info() – додатково виводить інформацію про робота
# Практичне завдання
#  turn_on() – якщо контейнер для пилу повний або
# контейнер для води порожній то виводить повідомлення,
# інакше запускається turn_on() з класу Robot
#  empty_dustbin() – очищає контейнер для пилу
#  fill_water() – заповнює контейнер для води
#  swap_mode() – змінює тип прибирання на протилежний
#  clean(energy, dust, water=None) – чистить поверхню,
# якщо прибирання сухе, то просто перенести пил у
# контейнер(якщо місця не достатньо вивести помилку),
# якщо прибирання вологе то додатково витратити воду.
# Також зменшує рівень заряду на energy


class CleaningStatus(Enum):
    dry = "dry"
    wet = "wet"


class CleaningRobot(Robot):
    def __init__(
        self,
        name: str,
        cleaning_mode: CleaningStatus,
        battery_level: int = 100,
        status: RobotStatus = RobotStatus.off,
        dust_capacity: int = 0,
        water_capacity: int = 100,
    ):
        super().__init__(name, battery_level)
        self.dust_capacity = dust_capacity
        self.water_capacity = water_capacity
        self.cleaning_mode = cleaning_mode

    def show_info(self):
        super().show_info()
        print(f"Cleaning mode: {self.cleaning_mode}")
        print(f"Dust capacity: {self.dust_capacity}")
        print(f"Water capacity: {self.water_capacity}")

    def turn_on(self):
        if self.dust_capacity == 100:
            print(f"Dust capacity: {self.dust_capacity} full")
            return

        if self.water_capacity == 0 and self.cleaning_mode == CleaningStatus.wet:
            print(f"Water capacity: {self.water_capacity} empty")
            return

        super().turn_on()

    def empty_dustbin(self):
        self.dust_capacity = 0
        print(f"{self.name}Empty dust bin")

    def fill_water(self):
        self.water_capacity = 100
        print(f"{self.name} filling water = Full")

    def swap_mode(self):
        if self.cleaning_mode == CleaningStatus.dry:
            self.cleaning_mode = CleaningStatus.wet
        else:
            self.cleaning_mode = CleaningStatus.dry
        print(f"{self.name}Swapped mode = {self.cleaning_mode}")

    def clean(self, energy: int, dust: int, water=None):
        if self.status == RobotStatus.off:
            print(f"Cleaning mode: {self.cleaning_mode}")
            return

        if water is None and self.cleaning_mode == CleaningStatus.wet:
            print(f"Cleaning mode: {self.cleaning_mode}")
            return

        if self.cleaning_mode == CleaningStatus.wet and self.water_capacity < water:
            print(f"Cleaning mode: {self.cleaning_mode}")
            return

        if self.dust_capacity + dust > 100:
            print(f"Cleaning mode: {self.cleaning_mode}")
            return

        if self.battery_level < energy:
            print(f"Cleaning mode: {self.cleaning_mode}")
            return

        self.dust_capacity += dust

        if self.cleaning_mode == CleaningStatus.wet:
            self.water_capacity -= water
        self.battery_level -= energy


# Створіть дочірній клас SecurityRobot
# Додаткові атрибути:
#  min_speed – мінімальна швидкість руху, щоб помітити
# об’єкт
#  alert_level – рівень небезпеки (low, middle, high)
#  dangerous_items – список небезпечних предметів(gun,
# knife, bat)
# Методи:
#  info() – додатково виводить інформацію про робота
#  turn_off() – перед виключенням змінює рівень небезпеки
# на low
#  add_dangerous_item(item) – додає небезпечний предмет
#  remove_dangerous_item(item) – видаляє небезпечний
# предмет
#  detect(speed, item) – виявляє загрозу
# o якщо швидкість занизька, то ігноруємо
# o якщо швидкість велика, то рівень небезпеки
# middle
# o якщо це небезпечний предмет, то рівень
# небезпеки high
# Рівень небезпеки не може стати нижчим


class RobotAlert(Enum):
    low = "low"
    middle = "middle"
    high = "high"


class SecurityRobot(Robot):
    def __init__(
        self,
        name: str,
        min_speed: int,
        alert_level: RobotAlert,
        battery_level: int = 100,
        status: RobotStatus = RobotStatus.off,
        dangerous_items: list[str] | None = None,
    ):
        super().__init__(name, battery_level, status)
        self.alert_level = alert_level
        self.min_speed = min_speed

        if dangerous_items is None:
            self.dangerous_items = []
        else:
            self.dangerous_items = dangerous_items

    def show_info(self):
        super().show_info()
        print(f"Robot: {self.name}")
        print(f"Alert Level: {self.alert_level}")
        print(f"Mining Speed: {self.min_speed}")
        print(f"Dangerous Items: {self.dangerous_items}")
