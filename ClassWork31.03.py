# Створіть клас Проект з атрибутами:
#  назва
#  виділений кошторис
#  загальні витрати
#  чи завершений(за замовчуванням False)
#  час виконання(за замовчуванням 0 місяців)
#  список необхідних задач
# Додайте методи:
#  вивід інформації: назва, час виконання, необхідні
# задачі
#  добавити нову задачу
#  розбити задачу на під-задачі: передається назва задачі
# та список під-задач
#  виконати задачу, передається назва, час та ціна
# виконання
#  поповнення кошторису


class Project:
    def __init__(self, name: str, budget: int):
        self.name = name
        self.budget = budget

        self.expenses: int = 0
        self.is_finished: bool = False
        self.time_of_processed: int = 0
        self.tasks: list[str] = []

    def show_info(self):
        print(f"Name: {self.name}")
        print(f"Budget: {self.budget}")
        print(f"Expenses: {self.expenses}")
        print(f"Remaining budget: {self.budget - self.expenses}")
        print(f"Time of processed: {self.time_of_processed}")
        print(f"Is finished: {self.is_finished}")
        print(f"Tasks: {self.tasks}")

    def add_task(self, task: str):
        self.tasks.append(task)

    def decompose(self, task: str, sub_tasks: list[str]):
        self.tasks.remove(task)
        self.tasks.extend(sub_tasks)

    def do_task(self, task: str, budget: int, time: int):
        self.tasks.remove(task)
        self.expenses += budget
        self.time_of_processed += time

    def add_budget(self, budget: int):
        self.budget += budget


project1 = Project("test", 5000)
project1.add_task("write TCs")
project1.add_task("order Pizza")
project1.decompose(task="write TCs", sub_tasks=["idea", "Pizza"])
project1.do_task(task="idea", budget=100, time=1)
project1.add_budget(budget=200)
project1.show_info()
