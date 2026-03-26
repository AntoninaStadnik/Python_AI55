import math

# Створіть клас Student з атрибутами name та age. Додайте
# метод для виводу інформації у форматі «Ім’я: {name}, вік:
# {age}»
# Створіть список з 3-ма студентами, дані вводить
# користувач. Після чого для кожного студента виведіть
# інформацію про нього за допомогою метода.


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print(f"Name {self.name}, age {self.age}")


student1 = Student("John", 22)
student2 = Student("Mike", 23)
student3 = Student("Sam", 26)

students = []
students.append(student1)
students.append(student2)
students.append(student3)

for student in students:
    student.show_info()

print(students)

student1.show_info()
student2.show_info()
student3.show_info()

# Створіть клас Circle з атрибутом radius. Додайте метод для
# отримання площі кола


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius**2


circle = Circle(5)
circle2 = Circle(10)
print("Площа кола:", circle.get_area())
print("Площа кола:", circle.get_area())


# Створіть клас BankAccount з атрибутами owner та balance.
# Додайте метод deposit для поповнення рахунку
# Додайте метод withdraw для зняття грошей з рахунку
# Додайте метод info для виведення інформації про баланс
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            print(f"{self.owner}: сума для поповнення має бути більше 0")

    def withdraw(self, amount):
        if amount <= 0:
            print(f"{self.owner}: сума має бути більше 0")
        elif amount <= self.balance:
            self.balance -= amount
        else:
            print(f"{self.owner}: недостатньо коштів")

    def info(self):
        print(f"{self.owner} balance: {self.balance}")


client1 = BankAccount("John", 220)
client2 = BankAccount("Mike", 723)
client3 = BankAccount("Sam", 926)

client1.deposit(100)
client1.info()
client1.withdraw(100)


# Створіть клас Car з атрибутами brand(марка), year(рік
# випуску), is_ready(чи готовий до поїздки, за замовчування
# False).
# Додайте метод start_engine який заводить двигун, і змінює
# атрибут is_ready
# Додайте метод move який виводить повідомлення, що
# автомобіль їде, або ж ще не готовий в залежності від is_ready.


class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
        self.is_ready = False

    def start_engine(self):
        self.is_ready = True
        print(f"Автомобіль {self.brand} двигун заводиться")

    def move_car(self):
        if not self.is_ready:
            print(f"Автомобіль {self.brand} не їде")
        else:
            print(f"Автомобіль {self.brand} їде")


car1 = Car("BMW", 1900)
car2 = Car("Audi", 2025)

car1.start_engine()
car2.move_car()
