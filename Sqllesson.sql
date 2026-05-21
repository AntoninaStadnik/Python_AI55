-- ПІБ студента;
-- ■ місто;
-- ■ країна;
-- ■ дата народження;
-- ■ електронна адреса;
-- ■ контактний телефон;
-- ■ назва групи;
-- ■ середня оцінка за рік з усіх предметів;
-- ■ назва предмета з мінімальною, середньою оцінкою;
-- ■ назва предмета з максимальною, середньою
-- оцінкою.
-- Наповніть цю базу даних трьома студентами.

-- CREATE TABLE STUDENT(
-- 	ID SERIAL,
-- 	NAME VARCHAR(100),
-- 	CITY VARCHAR(30),
-- 	COUNTRY VARCHAR(40),
-- 	DOB INT,
-- 	EMAIL VARCHAR(50),
-- 	PHONE VARCHAR(11),
-- 	GROUP_NAME VARCHAR(20),
-- 	AVARAGE_MARK INT,
-- 	MAX_MARK INT,
-- 	MIN_MARK INT,
-- 	SUBJECT_MIN VARCHAR(50),
-- 	SUBJECT_MAX VARCHAR(50)
-- )

--DROP TABLE STUDENT;

-- INSERT INTO STUDENT
-- (NAME, CITY, COUNTRY, DOB, EMAIL, PHONE, GROUP_NAME, AVARAGE_MARK, MAX_MARK, MIN_MARK, SUBJECT_MIN, SUBJECT_MAX)
-- VALUES
-- ('Ivan Petrenko', 'Kyiv', 'Ukraine', 2001, 'ivan.petrenko@gmail.com', '0501112233', 'CS-101', 85, 98, 65, 'Physics', 'Math'),
-- ('Olena Kovalenko', 'Lviv', 'Ukraine', 2000, 'olena.k@gmail.com', '0501112234', 'CS-102', 90, 100, 70, 'Chemistry', 'English'),
-- ('John Smith', 'London', 'UK', 1999, 'john.smith@gmail.com', '0501112235', 'ENG-201', 76, 89, 55, 'History', 'Physics'),
-- ('Maria Garcia', 'Madrid', 'Spain', 2002, 'maria.g@gmail.com', '0501112236', 'MED-110', 88, 97, 68, 'Math', 'Biology'),
-- ('Ali Hassan', 'Cairo', 'Egypt', 2001, 'ali.h@gmail.com', '0501112237', 'CS-101', 81, 95, 60, 'English', 'Programming'),
-- ('Anna Melnyk', 'Kyiv', 'Ukraine', 2003, 'anna.m@gmail.com', '0501112238', 'CS-103', 93, 100, 75, 'Physics', 'Math'),
-- ('Petro Bondar', 'Odesa', 'Ukraine', 2000, 'petro.b@gmail.com', '0501112239', 'ENG-201', 69, 82, 50, 'Biology', 'History'),
-- ('Sophia Brown', 'New York', 'USA', 1998, 'sophia.b@gmail.com', '0501112240', 'MED-110', 84, 96, 66, 'Chemistry', 'Biology'),
-- ('Max Müller', 'Berlin', 'Germany', 2001, 'max.m@gmail.com', '0501112241', 'CS-102', 79, 90, 58, 'English', 'Programming'),
-- ('Emma Wilson', 'Toronto', 'Canada', 2002, 'emma.w@gmail.com', '0501112242', 'CS-103', 91, 99, 72, 'History', 'Math'),

-- ('Artem Shevchenko', 'Dnipro', 'Ukraine', 1999, 'artem.s@gmail.com', '0501112243', 'CS-101', 74, 88, 54, 'Chemistry', 'Programming'),
-- ('Kate Johnson', 'Chicago', 'USA', 2000, 'kate.j@gmail.com', '0501112244', 'ENG-202', 86, 97, 67, 'Physics', 'English'),
-- ('Lucas Martin', 'Paris', 'France', 2001, 'lucas.m@gmail.com', '0501112245', 'MED-120', 83, 91, 61, 'Math', 'Biology'),
-- ('Nazar Koval', 'Kyiv', 'Ukraine', 2002, 'nazar.k@gmail.com', '0501112246', 'CS-103', 95, 100, 78, 'History', 'Programming'),
-- ('Yulia Romanova', 'Kharkiv', 'Ukraine', 2003, 'yulia.r@gmail.com', '0501112247', 'CS-101', 80, 92, 59, 'Physics', 'Math'),
-- ('David Lee', 'Seoul', 'South Korea', 2000, 'david.l@gmail.com', '0501112248', 'ENG-202', 87, 98, 69, 'Chemistry', 'English'),
-- ('Sara Ahmed', 'Dubai', 'UAE', 1999, 'sara.a@gmail.com', '0501112249', 'MED-120', 82, 94, 63, 'Biology', 'Chemistry'),
-- ('Denys Tkachenko', 'Lviv', 'Ukraine', 2001, 'denys.t@gmail.com', '0501112250', 'CS-102', 77, 89, 57, 'English', 'Programming'),
-- ('Mila Novak', 'Prague', 'Czech Republic', 2002, 'mila.n@gmail.com', '0501112251', 'ENG-201', 89, 99, 71, 'History', 'English'),
-- ('Chris Evans', 'Boston', 'USA', 1998, 'chris.e@gmail.com', '0501112252', 'MED-110', 73, 85, 52, 'Math', 'Biology');

-- SELECT *
-- FROM STUDENT

-- SELECT NAME
-- FROM STUDENT;

-- SELECT NAME, AVARAGE_MARK
-- FROM STUDENT;

-- SELECT ID, NAME
-- FROM STUDENT
-- WHERE MIN_MARK > 60;

-- DISTINCT USE WHEN NEED TO SELECT UNIQUE NAME 
-- SELECT DISTINCT COUNTRY
-- FROM STUDENT

-- SELECT DISTINCT SUBJECT_MIN, MIN_MARK
-- FROM STUDENT

-- SELECT *
-- FROM STUDENT
-- WHERE CITY = 'LONDON' OR CITY ='BERLIN' OR  CITY = 'LVIV'

-- СТУДЕНТИ З СЕРЕДНІМ БАЛОМ В ДІАПАЗОНІ МІЖ 60 І 100
-- SELECT *
-- FROM STUDENT
-- WHERE AVARAGE_MARK BETWEEN 70 AND 80

-- ВИВЕСТИ ІМ'Я, МАКСИМАЛЬНУ ТА МІН ОЦІНКУ ТА РІЗНИЦЮ МІЖ НИМИ
-- SELECT NAME, MIN_MARK, MAX_MARK - MIN_MARK AS DIFF
-- FROM STUDENT

-- SELECT COUNTRY, AVARAGE_MARK
-- FROM STUDENT
-- WHERE COUNTRY = 'POLAND' OR AVARAGE_MARK > 85

-- SELECT NAME, MAX_MARK, MIN_MARK
-- FROM STUDENT
-- WHERE MAX_MARK > MIN_MARK

-- SELECT NAME, MAX_MARK, MIN_MARK
-- FROM STUDENT
-- WHERE MAX_MARK - MIN_MARK > 20

-- SELECT CITY, LOWER(CITY)
-- FROM STUDENT

-- SELECT CITY, NAME
-- FROM STUDENT
-- WHERE LOWER (CITY) = 'london'

-- SELECT NAME, ID
-- FROM STUDENT
-- WHERE LENGTH(NAME) > 15