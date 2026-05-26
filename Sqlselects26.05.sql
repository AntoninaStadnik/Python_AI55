-- Створіть наступні запити для бази даних з оцінками
-- студентів із попереднього практичного завдання:
-- SELECT *
-- FROM STUDENT
-- ■ Показати ПІБ усіх студентів з мінімальною оцінкою у вказаному діапазоні.
-- SELECT NAME
-- FROM STUDENT
-- WHERE MIN_MARK BETWEEN 70 AND 80

-- ■ Показати інформацію про студентів, яким виповнилося 20 років.
-- SELECT NAME, AGE(DOB)
-- FROM STUDENT
-- WHERE AGE(DOB) > INTERVAL '20 years'

-- ALTER TABLE STUDENT
-- DROP COLUMN DOB

-- ALTER TABLE STUDENT
-- ADD COLUMN DOB DATE 

-- UPDATE STUDENT 
-- SET DOB = '1991-05-09'

-- ■ Показати інформацію про студентів із конкретним ім’ям. Наприклад, показати студентів з ім’ям Борис.
-- SELECT NAME
-- FROM STUDENT
-- WHERE NAME ILIKE '%ANNA%'

-- ■ Показати інформацію про студентів, в номері яких є три сімки.
-- SELECT NAME, PHONE
-- FROM STUDENT
-- WHERE PHONE ILIKE '%2%2%2%'

-- ■ Показати електронні адреси студентів, що починаються з конкретної літери.
-- SELECT NAME, EMAIL
-- FROM STUDENT
-- WHERE EMAIL ILIKE 'l%'


-- ■ Показати максимальну середню оцінку по всіх студентах.
-- SELECT  MIN_MARK
-- FROM STUDENT

-- SELECT  MAX_MARK
-- FROM STUDENT
-- ■ Показати статистику міст. Має відображатися назва міста та кількість студентів з цього міста.
-- SELECT CITY, COUNT(*)
-- FROM STUDENT
-- GROUP BY CITY

-- ■ Показати статистику студентів. Має відображатися назва країни та кількість студентів з цієї країни.
-- SELECT COUNTRY, COUNT(*)
-- FROM STUDENT
-- GROUP BY COUNTRY

-- ■ Показати кількість студентів з мінімальною середньою оцінкою з математики.
-- SELECT COUNT(*)
-- FROM STUDENT
-- WHERE SUBJECT_MIN = 'Math'

-- ■ Показати кількість студентів з максимальною середньою оцінкою з математики.
-- SELECT COUNT(*)
-- FROM STUDENT
-- WHERE SUBJECT_MAX = 'English'

-- ■ Показати кількість студентів у кожній групі.
-- SELECT GROUP_NAME, COUNT(*), AVG(AVARAGE_MARK)
-- FROM STUDENT
-- GROUP BY GROUP_NAME

-- SELECT MAX(AVARAGE_MARK)
-- FROM STUDENT

-- SELECT * 
-- FROM STUDENT
-- WHERE AVARAGE_MARK = (

-- 	SELECT MAX(AVARAGE_MARK)
-- 	FROM STUDENT
-- ) 

-- ВИВЕСТИ МІСТА І КІЛЬКІСТЬ СТУДЕНТІВ
-- SELECT CITY, COUNT(*)
-- FROM STUDENT
-- GROUP BY CITY

--ВИВЕСТИ НАЙБІЛЬШУ  КІЛЬКІСТЬ СТУДЕНТІВ СЕРЕД МІСТ
-- WITH CITY_NAME AS(
-- 	SELECT CITY, COUNT(*)
-- 	FROM STUDENT
-- 	GROUP BY CITY
-- )
-- SELECT MAX(COUNT)
-- FROM CITY_NAME

--ВИВЕСТИ ГРУПИ І СЕРЕДНІ ОЦІНКИ
-- WITH GROUP_INFO AS (
-- 	SELECT GROUP_NAME, AVG(AVARAGE_MARK) AS GROUP_GRADE
-- 	FROM STUDENT
-- 	GROUP BY GROUP_NAME
-- )
-- SELECT GROUP_NAME, GROUP_GRADE 
-- FROM GROUP_INFO
-- WHERE GROUP_GRADE = (
-- 	SELECT MAX(GROUP_GRADE)
-- 	FROM GROUP_INFO
-- )

