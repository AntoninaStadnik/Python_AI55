# # Напишіть програму для заповнення списку товарів.
# # Назви товарів вводить користувач. Реалізуйте функціонал:
# #  додати новий товар
# #  вивести список товарів
# #  зберегти дані через json
# #  зберегти дані через pickle
# #  завантажити дані через json
# #  завантажити дані через pickle
import json
import pickle


def add_product(items: list[str]) -> None:
    product = input("Add new product: ")
    items.append(product)
    print(f"{product} added.")


def show_products(items: list[str]) -> None:
    print("Products:")
    for item in items:
        print(item)


def save_products_json(items: list[str], filename: str = "products.json") -> None:
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(items, file, indent=4, ensure_ascii=False)
        print(f"{filename} saved.")


def save_products_pickle(items: list[str], filename: str = "products.pickle") -> None:
    with open(filename, "wb") as file:
        pickle.dump(items, file)
        print(f"{filename} saved.")


def load_products_pickle(filename: str = "products.pickle") -> list[str]:
    with open(filename, "rb") as file:
        return list(pickle.load(file))


def load_products_json(filename: str = "products.json") -> list[str]:
    with open(filename, encoding="utf-8") as file:
        return list(json.load(file))


products: list[str] = []

add_product(products)
add_product(products)
add_product(products)


save_products_pickle(products)
save_products_json(products)


items_pkl = load_products_pickle(filename="products.pickle")
items_json = load_products_json(filename="products.json")

show_products(items_json)
show_products(items_pkl)

#
# Напишіть клас Student
# Атрибути:
#  name – ім’я
#  specialization – спеціалізація
#  grades – список оцінок
# Методи:
#  add_grade(grade) – додати нову оцінку
#  show_info() – вивести ім’я, спеціалізацію та середню
# оцінку
# Практичне завдання
# Створіть список з трьох студентів. Збережіть цей список
# використовуючи pickle та json.
# Завантажте дані за допомогою pickle та json.


class Student:
    def __init__(self, name: str, specialization: str, grades: list[int]):
        self._name = name
        self._specialization = specialization
        self._grades = grades

    def add_grade(self, grade: int):
        self._grades.append(grade)
        print(f"{grade} added")

    def get_average_grades(self) -> float:
        if len(self._grades) == 0:
            return 0

        average = sum(self._grades) / len(self._grades)
        return average

    def show_info(self):
        print(f"Name: {self._name}")
        print(f"Specialization: {self._specialization}")
        print(f"Average grades: {self.get_average_grades()}")

    def get_state_dict(self) -> dict[str, object]:
        return {
            "name": self._name,
            "specialization": self._specialization,
            "grades": self._grades,
        }


def save_students_json(
    students: list[Student],
    filename: str = "students.json",
):
    data = []

    for student in students:
        data.append(student.get_state_dict())

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def load_students_json(filename: str = "students.json") -> list[Student]:
    with open(filename, encoding="utf-8") as file:
        data = json.load(file)

    students = [student1, student2, student3]

    for student_data in data:
        student = Student(
            student_data["name"],
            student_data["specialization"],
            student_data["grades"],
        )
        students.append(student)

    return list(students)


def save_students_pickle(
    students: list[Student],
    filename: str = "students.pkl",
):
    with open(filename, "wb") as file:
        pickle.dump(students, file)


def load_students_pickle(filename: str = "students.pkl") -> list[Student]:
    with open(filename, "rb") as file:
        students: list[Student] = pickle.load(file)

        return students


student1 = Student("Anna", "QA", [90, 95, 100])
student2 = Student("Oleh", "Python", [70, 80, 85])
student3 = Student("Ira", "Design", [100, 100, 95])

students = [student1, student2, student3]


save_students_pickle(students)
save_students_json(students)


students_pkl = load_students_pickle(filename="students.pkl")
students_json = load_students_json(filename="students.json")


students_pkl[0].show_info()
students_pkl[1].show_info()
students_pkl[2].show_info()

students_json[0].show_info()
students_json[1].show_info()
students_json[2].show_info()


# Additional task
def add_friends(friends: dict[str, list[str]]):
    friend1 = input("Input friend name 1:")
    friend2 = input("Input friend name 2:")

    if friend1 not in friends:
        friends[friend1] = []

    if friend2 not in friends:
        friends[friend2] = []

    friends[friend1].append(friend2)
    friends[friend2].append(friend1)


def save_json(
    friends: dict[str, list[str]], filename: str = "friends_name.json"
) -> None:
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(friends, file, indent=4, ensure_ascii=False)


def load_json(filename: str = "friends_name.json") -> dict[str, list[str]]:
    with open(filename, encoding="utf-8") as file:
        return dict(json.load(file))


def save_pickle(friends: dict[str, list[str]], filename: str = "friends_name.pickle"):
    with open(filename, "wb") as file:
        pickle.dump(friends, file)


def load_pickle(filename: str = "friends_name.pickle") -> dict[str, list[str]]:
    with open(filename, "rb") as file:
        return dict(pickle.load(file))


friends: dict[str, list[str]] = {}

add_friends(friends)
add_friends(friends)

save_pickle(friends)
save_json(friends)

print(friends)

load1 = load_json()
load2 = load_pickle()

print(load1)
print(load2)
