# fizzBuzz_exercise.py
total = 0

for number in range(1, 101):

    if number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    elif number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    else:
        print(number)

# Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91


# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P


password_list = []
for char in range(1, nr_letters + 1):
    password_list.append(random.choice(letters))
# print(password)


for sym in range(1, nr_symbols + 1):
    password_list += random.choice(symbols)
# print(password2)

for num in range(1, nr_numbers + 1):
    password_list += random.choice(numbers)
# print(password3)

random.shuffle(password_list)

password = ""
for char in password_list:
    password += char

print(f"your password is: {password}")

# For_loop.py
fruits = ["apple", "peach", "pear"]

for fruit in fruits:
    print(fruit)
    print(fruit + "pie")

# average_height_exercise.py
student_heights = input("Input a list of student height").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

total_height = 0

for height in student_heights:
    total_height += height
# print(total_height)

number_of_students = 0
for student in student_heights:
    number_of_students += 1

average = round(total_height / number_of_students)
print(average)

# highest score exercise.py
student_scores = input("Input a list of student scores").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

max_score = 0
for score in student_scores:
    if score > max_score:
        max_score = score
print(f"The highest score in the class is: {max_score}")

# more for loop examples
# for number in range(1,11, 3):
#     print(number)
total = 0

for number in range(1,101):
    total += number
print(total)
# adding even numbers
total = 0

for number in range(2,101,2):

    total += number
print(total)

