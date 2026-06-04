from sqlalchemy import create_engine, text, MetaData
from sqlalchemy.orm import sessionmaker

import os

import dotenv

# host = "localhost"
# port = 5432
# user = "postgres"
# password = ""
# db = "hospital"


dotenv.load_dotenv()

host = os.getenv("HOST")
port = os.getenv("PORT")
user = os.getenv("DB_USER")
password = os.getenv("PASSWORD")
db = os.getenv("DB")


#print(db)

db_uri = f"postgresql+pg8000://{user}:{password}@{host}:{port}/{db}"

engine = create_engine(db_uri)

Session = sessionmaker(bind=engine)
session = Session()

# metadata = MetaData()
# metadata.reflect(bind=engine)
#
# tables = metadata.tables
# print(list(tables.keys()))

#launch sql
# query = """
#     SELECT *
#     FROM DEPARTMENT
#
# """
#
# #text edit
# query = text(query)
#
# # launch
# result = session.execute(query)
#
# # show table data
# for row in result:
#     print(row)

#Вивести прізвища лікарів та їх спеціалізації;
# def show_doctors_and_specializations(session):
#     query = f"""
#         SELECT *
#         FROM doctorsspecializations ds
#         JOIN doctors d ON ds.doctor_id = d.id
#         JOIN specializations s ON ds.specialization_id = s.id
#     """
#
#     query = text(query)
#     result = session.execute(query)
#
#     for row in result:
#         print(row)
#
# show_doctors_and_specializations(session)

#Вивести прізвища та зарплати (сума ставки та надбавки) лікарів, які перебувають у відпустці;
# def doctor_vacation(session):
#     query = f"""
#     SELECT D.SURNAME, D.SALARY + D.PREMIUM
#     FROM DOCTORS D JOIN VACATIONS V ON D.ID = V.DOCTORS_ID
#     WHERE V.ENDDATE > CURRENT_DATE AND STARTDATE < CURRENT_DATE
#
# """
#     query = text(query)
#
#     result = session.execute(query)
#
#     for row in result:
#         print(row)
#
# doctor_vacation(session)

# Вивести назви палат, які знаходяться у певному відділенні;
# def show_dep(session):
#     query = f"""
#     SELECT *
#     FROM DEPARTMENT
# """
#     query = text(query)
#
#     result = session.execute(query)
#
#     for row in result:
#         print(row)
#
#
# def show_ward_department(session):
#     show_dep(session)
#     dep_name = input("Enter dep name: ")
#     query = f"""
#     SELECT *
#     FROM WARS W
#     JOIN DEPARTMENT D ON D.ID = W.DEPARTMENT_ID
#     WHERE D.NAME = '{dep_name}'
# """
#     query = text(query)
#
#     result = session.execute(query)
#
#     for row in result:
#         print(row)
#
# show_ward_department(session)
# show_dep(session)

# Вивести усі пожертвування за вказаний місяць у
# вигляді: відділення, спонсор, сума пожертвування, дата
# пожертвування;
def show_donations(session):
    ask_month = input("Enter the month of donation integer: ")
    ask_year = input("Enter the year of donation: ")
    query = f"""
        SELECT *
        FROM donations D 
            JOIN DEPARTMENT DEP ON DEP.DEPARTMENT_ID = DEP.ID
            JOIN SPONSORS S ON S.ID = DEP.SPONSOR_ID
            WHERE EXTRACT(MONTH FROM D.DATE_DONATION) = '{ask_month}' 
                AND EXTRACT (YEAR FROM D.DATE_DONATION) = '{ask_year}'
    """

    query = text(query)

    result = session.execute(query)

    for row in result:
        print(row)

show_donations(session)
