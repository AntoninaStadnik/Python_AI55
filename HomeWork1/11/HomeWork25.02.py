# Напишіть lambda-функції, які:
#  Перевіряє чи рядок непорожній
from numpy.matlib import empty
#  Множить число на -1
def multiplication(num):
    return num * -1

res = lambda num: num * -1
print(res(5))

#  Перевіряє чи рядок непорожній
def check_line(line):
    if line != "":
        return True
    else:
        return False

result = lambda line: line != ""
print(result("test"))
print(result(""))

# Напишіть функцію, яка використовуючи filter:
#  Отримує список чисел, рахує середнє арифметичне та повертає список з числами, які більші за середнє
nums = [1, 4, 2, 2, 5, 6, 3, 5]

avg = sum(nums) / len(nums)

new_nums = list(filter(lambda num: num > avg, nums))

print(f"Середнє: {avg}")
print(f"Числа більші за середнє: {new_nums}")

#  Отримує список слів та повертає список слів, в яких рівно 4 літери
words = ['apple', 'cat', 'apricot', 'watermelon', 'kitty', 'jump', 'ball']
letter_words = filter(lambda word: len(word) == 4, words)
print(list(letter_words))

# Напишіть функцію, яка отримує літеру та список слів і
# знаходить слово зі списку, в якому найбільша кількість даної літери.
words = ['dog', 'cat', 'kitty', 'doggy', 'deduction', 'addresses'] #а чому тут " одинарні кавички не пройшли, считує тільки так, як у списку?
letter = 'd'
def count_d(word):
    return word.lower().count(letter)

res = max(words, key=count_d)
print(res)


