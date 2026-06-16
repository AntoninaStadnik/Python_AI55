# Напишіть програму, яка приймає два цілих числа від
# користувача і виводить суму діапазону чисел між ними.

# num1 = int(input("Type num1: "))
# num2 = int(input("Type num2: "))
#
# start = min(num1, num2)
# end = max(num1, num2)
#
# total = 0
#
# for i in range(start, end + 1):
#     total += i
#
# print(total)

# Напишіть програму, для знаходження суми всіх парних
# чисел від 1 до 100.

# total = 0
#
# for i in range(1, 101):
#      if i % 2 == 0:
#         total += i
# print(total)

# Напишіть програму, яка приймає рядок від користувача і
# виводить кожну літеру рядка на окремому рядку.

# phrase = input("Type some text: ")
#
# for letter in phrase:
#     print(letter)

# Напишіть програму, яка створює список цілих чисел та
# виводить новий список, який містить лише парні числа з
# вихідного списку.

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# even_nums = []
#
# for num in nums:
#     if num % 2 == 0:
#         even_nums.append(num)
# print(even_nums)

# Напишіть функцію, яка приймає список рядків від
# користувача і повертає новий список, що містить лише
# рядки, що починаються з великої літери.

# some_text = ['Banana', 'cat', 'apple', 'Vacation', 'Italy']
#
# big_letter = []
#
# for letter in some_text:
#     if letter[0].isupper():
#         big_letter.append(letter)
#
# print(big_letter)

# Напишіть функцію, яка приймає список рядків від
# користувача і повертає новий список, що містить лише
# рядки, які містять слово "Python".

# some_text = ['Banana', 'cat', 'apple', 'Vacation', 'Italy', 'Python', 'Opythons', 'MyPython']
#
# python_list = []
#
# for item in some_text:
#     if 'python' in item.lower():
#         python_list.append(item)
#
# print(python_list)

# Симулятор роботи сайту
# WebSite: Основний клас, який представляє вебсайт.
# Атрибути: назва сайту, URL, список сторінок.
# Методи: додавання/видалення сторінок, відображення
# інформації про сайт.
# WebPage: Клас, який представляє окрему сторінку на сайті.
# Атрибути: заголовок сторінки, вміст, дата публікації.
# Методи: відображення деталей сторінки.
# Реалізація функціональності:
# Дозвольте користувачеві створювати новий сайт з
# певною назвою та URL. Додайте можливість створювати нові
# сторінки для сайту, вводячи заголовок та вміст. Реалізуйте
# функцію для видалення сторінок з сайту. Включіть функцію
# для відображення всієї інформації про сайт, включаючи
# список усіх сторінок.
# Розробіть простий текстовий інтерфейс для взаємодії з
# користувачем. Користувач повинен мати змогу вибирати дії,
# такі як створення сайту, додавання/видалення сторінок,
# перегляд інформації про сайт.
#MENU:
CREATE_WEBSITE = 1
ADD_PAGE = 2
REMOVE_PAGE = 3
SHOW_WEBSITE_INFO = 4


class WebPage:
    def __init__(self, page_header, content, publication_date):
        self.page_header = page_header
        self.content = content
        self.publication_date = publication_date

    def show_information(self):
        print(self.page_header)
        print(self.content)
        print(self.publication_date)
        print()


class WebSite:
    def __init__(self, name, url):
        self.name = name
        self.url = url
        self.page_list = []

    def add_page(self):
        header = input("Enter page header: ")
        content = input("Enter page content: ")
        date = input("Enter publication date: ")

        page = WebPage(header, content, date)
        self.page_list.append(page)

        print("Page added!")

    def remove_page(self):
        header = input("Enter page header to remove: ")

        for page in self.page_list:
            if page.page_header == header:
                self.page_list.remove(page)
                print("Page removed!")
                return

        print("Page not found!")

    def show_information_about_site(self):
        print("SITE INFO")
        print("Name:", self.name)
        print("URL:", self.url)
        print("PAGES:")

        if not self.page_list:
            print("No pages yet")
        else:
            for page in self.page_list:
                page.show_information()




website = None

while True:
    print("MENU:")
    print("1 - Create website")
    print("2 - Add page")
    print("3 - Remove page")
    print("4 - Show website info")
    print("0 - Exit")

    user_choice = input("Choose option: ")

    if user_choice == "1":
        name = input("Enter website name: ")
        url = input("Enter website url: ")
        website = WebSite(name, url)

    elif user_choice == "2":
        if website:
            website.add_page()
        else:
            print("Create website first!")

    elif user_choice == "3":
        if website:
            website.remove_page()
        else:
            print("Create website first!")

    elif user_choice == "4":
        if website:
            website.show_information_about_site()
        else:
            print("Create website first!")

    elif user_choice == "0":
        break

    else:
        print("Invalid option")


