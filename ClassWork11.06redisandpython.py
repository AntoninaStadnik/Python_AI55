# Створіть додаток «Музей літератури». Додаток має зберігати
# інформацію про експонати та людей, які мають відношення
# до експонатів. Можливості додатку:
# ■ додати експонат;
# ■ видалити експонат;
# ■ редагування інформації про експонат;
# ■ перегляд повної інформації про експонат;
# ■ виведення інформації про всі експонати;
# ■ перегляд інформації про людей, які мають відношення
# до певного експонату;
# ■ перегляд інформації про експонати, що мають відношення
# до певної людини;
# ■ перегляд набору експонатів на основі певного критерію.
# Наприклад, показати всі книжкові експонати.
# Зберігайте дані у базі даних NoSQL. Можете використовувати Redis в якості платформи

# save password: user 123444
# save exponat: name description
# save people_info: description
# save exponat: name: people
# save exponat: name: people name

from redis import Redis

class SocialApp():
    def __init__(self):
        self.server = Redis(
            host="localhost",
            port=6379,
            db=0,  # індекс бази даних
            decode_responses=True,
        )

        self.current_user = None

        self.islogged_in = False


    def get_cred_key(self, username):
        return f"password:{username}"

    def get_exponat_key(self, exponat):
        return f"exponat:{exponat}"

    def get_people_key(self, person_name):
        return f"people:{person_name}"

    def get_exp_related_name(self, exp_name):
        return f"exponat:{exp_name}: people"

    # ■ вхід за логіном і паролем;
    def login(self, username, password):
        key = self.get_cred_key(username)

        if not self.server.exists(key):
            print("such user doesn't exist")
            return

        true_password = self.server.get(key)

        if true_password != password:
            print("wrong password")
            return

        self.current_user = username
        print("you''re logged in")
        self.islogged_in = True

    def signup(self, username, password):
        key = self.get_cred_key(username)

        if self.server.exists(key):
            print("such user already exist")
            return

        self.server.set(key, password)
        print("signup successful")



    # ■ додати експонат;
    def add_exp_info(self, exp_info, desc):
        if not self.islogged_in:
            print("not logged in")
            return

        key = self.get_exponat_key(exp_info)
        self.server.set(key, desc)
        print("exponat added")



app = SocialApp()


#app.login("username", "12345")




