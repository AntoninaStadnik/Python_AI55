# Користувач вводить з клавіатури число. Перевірте його на парність або
# непарність. Якщо число парне, виведіть на екран число з написом «Even
# number». Якщо непарне, виведіть на екран число з написом «Odd number».

num = int(input("Input number: "))

if num % 2 == 0:

    print("Even number: ", num)

else:
    print("Odd number: ", num)

#Користувач вводить з клавіатури число. Перевірте, чи введене число кратне 7.
#Якщо так, виведіть на екран число з написом «Number is multiple 7». Якщо ні, виведіть на екран число з написом «Number is not multiple 7».

number = int(input("Input number: "))

if number % 7 == 0:
    print("Number is multiple 7")

else:
    print("Number is not multiple of 7")

# Користувач вводить з клавіатури два числа. Знайдіть максимум із двох чисел
# і виведіть його на екран.

value = int(input("Input number1: "))
value1 = int(input("Input number2: "))

if value > value1:
    print("Maximum number: ", value)

else:
    print("Minimum number: ", value1)


#Користувач вводить з клавіатури два числа. Знайдіть мінімум із двох чисел і виведіть його на екран.
value = int(input("Input number1: "))
value1 = int(input("Input number2: "))

if value < value1:
    print("Minimum number: ", value)

else:
    print("Maximus number: ", value1)

#Користувач вводить з клавіатури два числа. Залежно від вибору користувача,покажіть суму двох чисел, різницю двох чисел, середнє арифметичне або
#добуток двох чисел.

value = int(input("Input number1: "))
value1 = int(input("Input number2: "))

user_select = input("Select operation: (+, -, *, /) " )

if user_select == "+":
    result = value + value1
    print(result)

elif user_select == "-":
    result = value - value1
    print(result)

elif user_select == "*":
    result = value * value1
    print(result)

elif user_select == "/":
    result = value / value1
    print(result)

else:
    print("Invalid input")


# Additional tasks
#Користувач вводить з клавіатури час у секундах, який минув з початку дня.Залежно від вибору користувача, підрахуйте, скільки годин, хвилин та секундзалишилося до півночі.

time = int(input("Input time in seconds: "))

user_select = input("Select options: hours before midnight, minutes before midnight, seconds before midnight: " )

if user_select == "hours":
     result = (84000 - time) / 3600
     print(result)

elif user_select == "minutes":
     result = (84000 -time )/ 60
     print(result)

elif user_select == "seconds":
     result = (84000 -time )/ 84000
     print(result)

else:
    print("Invalid input")





