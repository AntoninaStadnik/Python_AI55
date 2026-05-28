-- CREATE TABLE DEPARTMENTS(
-- 	ID SERIAL NOT NULL PRIMARY KEY,
-- 	BUILDING INT NOT NULL CHECK(1 < BUILDING AND BUILDING < 5),
-- 	FINANCING INT NOT NULL CHECK(FINANCING >= 0) DEFAULT 0,
-- 	NAME VARCHAR(100) NOT NULL UNIQUE 
	
-- )


-- INSERT INTO DEPARTMENTS (BUILDING, FINANCING, NAME)
-- VALUES
-- (2, 500000, 'Cardiology'),
-- (3, 450000, 'Neurology'),
-- (4, 600000, 'Surgery'),
-- (2, 300000, 'Pediatrics'),
-- (3, 350000, 'Oncology'),
-- (4, 400000, 'Emergency'),
-- (2, 280000, 'Radiology'),
-- (3, 320000, 'Dermatology'),
-- (4, 370000, 'Orthopedics'),
-- (2, 290000, 'Gynecology');

-- CREATE TABLE DISEASES(
-- 	ID SERIAL NOT NULL PRIMARY KEY,
-- 	NAME VARCHAR(100) NOT NULL UNIQUE,
-- 	SEVERITY INT NOT NULL CHECK(SEVERITY >= 1) DEFAULT 1
-- )

-- INSERT INTO DISEASES (NAME, SEVERITY)
-- VALUES
-- ('Influenza', 2),
-- ('Pneumonia', 4),
-- ('Diabetes', 3),
-- ('Hypertension', 3),
-- ('Asthma', 2),
-- ('Tuberculosis', 5),
-- ('COVID-19', 4),
-- ('Migraine', 1),
-- ('Arthritis', 2),
-- ('Cancer', 5),
-- ('Hepatitis', 4),
-- ('Bronchitis', 2),
-- ('Malaria', 5),
-- ('Anemia', 2),
-- ('Epilepsy', 3),
-- ('Stroke', 5),
-- ('Depression', 3),
-- ('Alzheimer''s Disease', 4),
-- ('Kidney Failure', 5),
-- ('Appendicitis', 3);


-- CREATE TABLE DOCTORS(
-- 	ID SERIAL NOT NULL PRIMARY KEY,
-- 	NAME VARCHAR(255) NOT NULL,
-- 	PHONE CHAR(10),
-- 	SALARY INT NOT NULL CHECK(SALARY >= 0),
-- 	SURNAME VARCHAR(255) NOT NULL
-- )

-- INSERT INTO DOCTORS (NAME, PHONE, SALARY, SURNAME)
-- VALUES
-- ('John', '0501234567', 120000, 'Smith'),
-- ('Emily', '0502345678', 115000, 'Johnson'),
-- ('Michael', '0503456789', 130000, 'Williams'),
-- ('Sarah', '0504567890', 110000, 'Brown'),
-- ('David', '0505678901', 140000, 'Jones'),
-- ('Anna', '0506789012', 125000, 'Garcia'),
-- ('Robert', '0507890123', 118000, 'Miller'),
-- ('Olivia', '0508901234', 132000, 'Davis'),
-- ('James', '0509012345', 145000, 'Rodriguez'),
-- ('Sophia', '0510123456', 121000, 'Martinez'),
-- ('Daniel', '0511234567', 128000, 'Hernandez'),
-- ('Isabella', '0512345678', 119000, 'Lopez'),
-- ('Matthew', '0513456789', 150000, 'Gonzalez'),
-- ('Mia', '0514567890', 117000, 'Wilson'),
-- ('Christopher', '0515678901', 134000, 'Anderson'),
-- ('Charlotte', '0516789012', 126000, 'Thomas'),
-- ('Andrew', '0517890123', 138000, 'Taylor'),
-- ('Amelia', '0518901234', 122000, 'Moore'),
-- ('Joshua', '0519012345', 129000, 'Jackson'),
-- ('Evelyn', '0520123456', 116000, 'Martin');


-- CREATE TABLE EXAMINATIONS(
--     ID SERIAL NOT NULL PRIMARY KEY,
--     DAYOFWEEK INT NOT NULL CHECK (DAYOFWEEK BETWEEN 1 AND 7),
--     NAME VARCHAR(100) NOT NULL UNIQUE,
--     STARTTIME TIME NOT NULL CHECK (STARTTIME BETWEEN TIME '08:00' AND TIME '18:00'),
--     ENDTIME TIME NOT NULL CHECK (ENDTIME > STARTTIME)
-- );

-- INSERT INTO EXAMINATIONS (DAYOFWEEK, NAME, STARTTIME, ENDTIME)
-- VALUES
-- (1, 'General Checkup', '08:00', '09:00'),
-- (1, 'Blood Test', '09:00', '10:00'),
-- (2, 'Cardiology Exam', '10:00', '11:30'),
-- (2, 'Neurology Screening', '11:30', '12:30'),
-- (3, 'X-Ray', '08:30', '09:30'),
-- (3, 'MRI Scan', '09:30', '11:00'),
-- (4, 'Ultrasound', '10:00', '11:00'),
-- (4, 'Dental Check', '11:00', '12:00'),
-- (5, 'Eye Examination', '08:00', '09:00'),
-- (5, 'ENT Consultation', '09:00', '10:00'),
-- (6, 'Pediatrics Visit', '10:00', '11:00'),
-- (6, 'Dermatology Check', '11:00', '12:00'),
-- (7, 'Surgery Prep', '08:00', '09:30'),
-- (7, 'Post-op Review', '09:30', '10:30'),
-- (1, 'Vaccination', '10:00', '11:00'),
-- (2, 'Physiotherapy', '11:00', '12:00'),
-- (3, 'Oncology Screening', '12:00', '13:00'),
-- (4, 'Cardio Stress Test', '13:00', '14:00'),
-- (5, 'ECG', '14:00', '15:00'),
-- (6, 'Lab Analysis Review', '15:00', '16:00');


-- CREATE TABLE WARDS(
-- 	ID SERIAL NOT NULL PRIMARY KEY,
-- 	BUILDING INT NOT NULL CHECK(BUILDING BETWEEN 1 AND 5),
-- 	FLOOR INT NOT NULL CHECK(FLOOR >= 1),
-- 	NAME VARCHAR(20) NOT NULL UNIQUE
-- )

-- INSERT INTO WARDS (BUILDING, FLOOR, NAME)
-- VALUES
-- (1, 1, 'Ward A1'),
-- (1, 2, 'Ward A2'),
-- (1, 3, 'Ward A3'),
-- (2, 1, 'Ward B1'),
-- (2, 2, 'Ward B2'),
-- (2, 3, 'Ward B3'),
-- (3, 1, 'Ward C1'),
-- (3, 2, 'Ward C2'),
-- (3, 3, 'Ward C3'),
-- (4, 1, 'Ward D1'),
-- (4, 2, 'Ward D2'),
-- (4, 3, 'Ward D3'),
-- (5, 1, 'Ward E1'),
-- (5, 2, 'Ward E2'),
-- (5, 3, 'Ward E3'),
-- (3, 4, 'Ward C4'),
-- (4, 4, 'Ward D4'),
-- (5, 4, 'Ward E4'),
-- (2, 4, 'Ward B4'),
-- (1, 4, 'Ward A4');

-- 1. Вивести вміст таблиці палат.
-- SELECT *
-- FROM WARDS
-- 2. Вивести прізвища та телефони усіх лікарів.
-- SELECT SURNAME, PHONE 
-- FROM DOCTORS
-- 3. Вивести усі поверхи без повторень, де розміщуються
-- палати.
-- SELECT DISTINCT FLOOR
-- FROM WARDS
-- 4. Вивести назви захворювань під назвою « Name of
-- Disease» та ступінь їхньої тяжкості під назвою «Severity of Disease».
-- SELECT DISTINCT NAME AS NAME_OF_DISEASE, SEVERITY AS "SEVERITY OF DISEASE"
-- FROM DISEASES
-- 5. Вивести назви відділень, які знаходяться у корпусі 5 з фондом фінансування меншим, ніж 30000.
-- SELECT NAME 
-- FROM DEPARTMENTS
-- WHERE BUILDING = 4 AND FINANCING < 400000
-- 6. Вивести назви відділень, які знаходяться у корпусі 3 з фондом фінансування у діапазоні від 12000 до 15000.
-- SELECT NAME 
-- FROM DEPARTMENTS
-- WHERE BUILDING = 2 AND FINANCING < 400000 AND FINANCING > 2000000
-- 8. Вивести назви палат, які знаходяться у корпусах 4 та 5 на 1-му поверсі.
-- SELECT NAME, BUILDING, FLOOR
-- FROM WARDS
-- WHERE (BUILDING = 2 OR BUILDING =1) AND FLOOR = 1
-- 9. Вивести назви, корпуси та фонди фінансування відділень, які знаходяться у корпусах 3 або 6 та мають
-- фонд фінансування менший, ніж 11000 або більший за 25000.
-- SELECT NAME, BUILDING, FINANCING
-- FROM DEPARTMENTS
-- WHERE (FINANCING < 110000 OR FINANCING > 250000) AND (BUILDING = 3 OR BUILDING = 4 )
-- SELECT *
-- FROM DEPARTMENTS
-- 10. Вивести прізвища лікарів, зарплата (сума ставки та надбавки 120) яких перевищує 1500.
-- SELECT SURNAME, SALARY
-- FROM DOCTORS
-- WHERE SALARY + 120 > 150000
-- SELECT *
-- FROM DOCTORS
-- 11. Вивести прізвища лікарів, у яких половина зарплати перевищує триразову надбавку у вигляді 500.
-- SELECT SURNAME
-- FROM DOCTORS
-- WHERE SALARY > 500 * 3
-- 12. Вивести назви обстежень без повторень, які проводяться у перші три дні тижня з 12:00 до 15:00.
-- SELECT DISTINCT NAME, STARTTIME, ENDTIME
-- FROM EXAMINATIONS
-- WHERE (DAYOFWEEK BETWEEN 1 AND 3) AND (STARTTIME >= '10:00' AND ENDTIME <= '12:00')

-- SELECT *
-- fROM EXAMINATIONS

-- 13. Вивести назви та номери корпусів відділень, які знаходяться у корпусах 1, 3, 8 або 10.
-- SELECT *
-- FROM DEPARTMENTS

-- SELECT NAME, BUILDING
-- FROM DEPARTMENTS
-- WHERE BUILDING IN (1,3,8,10)

-- 14. Вивести назви захворювань усіх ступенів тяжкості, крім 1-го та 2-го.
-- SELECT *
-- FROM DISEASES

-- SELECT NAME, SEVERITY
-- FROM DISEASES
-- WHERE SEVERITY NOT IN (1,2)

-- 15. Вивести назви відділень, які не знаходяться у першому або третьому корпусі.
-- SELECT NAME, BUILDING
-- FROM DEPARTMENTS
-- WHERE BUILDING NOT IN (1, 3)

-- 16. Вивести назви відділень, які знаходяться у першому або третьому корпусі.
-- SELECT NAME, BUILDING
-- FROM DEPARTMENTS
-- WHERE BUILDING IN (1, 3)

-- 17. Вивести прізвища лікарів, що починаються з літери «N»
-- SELECT *
-- fROM DOCTORS

-- SELECT SURNAME
-- FROM DOCTORS
-- WHERE SURNAME ILIKE 'M%'

-- Вивести кількість палат у кожному корпусі.
-- SELECT BUILDING, COUNT(*)
-- FROM WARDS
-- GROUP BY BUILDING

-- Вивести кількість палат на кожному поверсі.
-- SELECT FLOOR, COUNT(*)
-- FROM WARDS
-- GROUP BY FLOOR
-- ORDER BY FLOOR

-- Вивести максимальний фонд фінансування серед відділень у кожному корпусі.
-- SELECT BUILDING, AVG(FINANCING)
-- FROM DEPARTMENTS
-- GROUP BY BUILDING

-- Вивести максимальний фонд фінансування серед відділень у кожному корпусі.
-- SELECT BUILDING, MAX(FINANCING)
-- FROM DEPARTMENTS
-- GROUP BY BUILDING

-- Вивести мінімальний фонд фінансування серед відділень у кожному корпусі.
-- SELECT BUILDING, MIN(FINANCING)
-- FROM DEPARTMENTS
-- GROUP BY BUILDING

-- Вивести загальну суму фінансування для кожного корпусу.
-- SELECT BUILDING, SUM(FINANCING)
-- FROM DEPARTMENTS
-- GROUP BY BUILDING

-- Вивести кількість відділень у кожному корпусі.
-- SELECT BUILDING, COUNT(*)
-- FROM DEPARTMENTS
-- GROUP BY BUILDING

-- Вивести кількість захворювань для кожного ступеня тяжкості.
-- SELECT SEVERITY, COUNT(*)
-- FROM DISEASES
-- GROUP BY SEVERITY

-- Вивести середню зарплату лікарів залежно від наявності телефону.
-- INSERT INTO DOCTORS (NAME, PHONE, SALARY, SURNAME)
-- VALUES
-- ('Ivan', NULL, 125000, 'Petrenko'),
-- ('Olena', NULL, 118000, 'Koval'),
-- ('Andrii', NULL, 132000, 'Shevchenko'),
-- ('Iryna', NULL, 121000, 'Bondar'),
-- ('Dmytro', NULL, 129000, 'Tkachenko');
-- SELECT AVG(SALARY)
-- FROM DOCTORS
-- GROUP BY PHONE = 'NULL'

-- Вивести кількість обстежень для кожного дня тижня.
-- SELECT DAYOFWEEK, COUNT(*)
-- FROM EXAMINATIONS
-- GROUP BY DAYOFWEEK
-- ORDER BY DAYOFWEEK

-- Вивести найраніший час початку обстежень для кожного дня тижня.
-- SELECT MIN(STARTTIME), DAYOFWEEK
-- FROM EXAMINATIONS
-- GROUP BY DAYOFWEEK
-- ORDER BY DAYOFWEEK

-- Вивести найпізніший час завершення обстежень для кожного дня тижня.
-- SELECT MAX(ENDTIME), DAYOFWEEK
-- FROM EXAMINATIONS
-- GROUP BY DAYOFWEEK
-- ORDER BY DAYOFWEEK

-- SELECT SURNAME, SALARY
-- FROM DOCTORS
-- WHERE SALARY = (SELECT MAX(SALARY)
-- FROM DOCTORS)

-- SELECT SURNAME, SALARY
-- FROM DOCTORS
-- WHERE SALARY = (
-- 	SELECT MIN(SALARY)
-- 	FROM DOCTORS
-- 	)

-- SELECT SURNAME, SALARY
-- FROM DOCTORS
-- WHERE SALARY > (
-- 	SELECT AVG(SALARY)
-- 	FROM DOCTORS
-- 	)

-- SELECT MIN(STARTTIME)
-- FROM EXAMINATIONS

-- SELECT *
-- FROM EXAMINATIONS
-- WHERE STARTTIME = (
-- 	SELECT MIN(STARTTIME)
-- 	FROM EXAMINATIONS
-- )

-- SELECT *
-- FROM EXAMINATIONS
-- WHERE ENDTIME = (
-- 	SELECT MAX(ENDTIME)
-- 	FROM EXAMINATIONS
-- )