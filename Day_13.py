
#   Debugging-Day_13

# # Describe the problem
def my_function():
    for i in range(1, 21):
        if i == 20:
            print("You got it")


my_function()
#   Reproduce the bug
from random import randint

dice_imgs = ["@", "@", "@", "@", "@", "@"]
dice_num = randint(0, 5)
print(dice_imgs[dice_num])

# # play computer
year = int(input("What is your year of birth?"))
if 1980 < year and year < 1994:
    print("Your are a millenial>")
elif year >= 1994:
    print("You are a Gen.Z")
# # Fix the Errors
age = int(input("How old are you ?"))
if age > 18:
    print(f"You can drive at age {age}")

# # print is your friend
pages = 0
word_per_page = 0
pages = int(input("Number of pages:"))
word_per_page = int(input("Number of words per page:"))
total_words = pages * word_per_page
print(total_words)


#   use a debugger


def mutate(a_list):
    b_list = []
    for items in a_list:
        new_item = items * 2
        b_list.append(new_item)
    print(b_list)


mutate([1, 2, 3, 4, 5, 6])

#   Debug odd or even exercise
number = int(input("Which number do you want to check?"))
if number % 2 == 0:
    print("This is an even number")
else:
    print("This is an odd number")

#   leap year exercise
year = int(input("Which year do you want to check?"))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year")
        else:
            print("Not a leap year")
    else:
        print("Leap year.")
else:
    print("Not leap year")

# Debug Fizz Buzz Exercise

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("fizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print([number])
