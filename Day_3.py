# example_1.py
print("Welcome to the roller coaster!")
height = int(input("What is your height in cm?"))
if height >= 120:
    print("you can ride the roller coaster!")
    age = int(input("what is your age?"))
    if age < 12:
        print("Please pay $5.")
    elif age <= 18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")

else:
    print("You can't ride the roller coaster!")

# exercise_1.py

# number = int(input("which number do you want to check "))
# if number% 2==1: print("this is an odd number")
# else: print("this is an even number")

# BMI_exercise_2
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
bmi_1 = float(weight) / float(height) ** 2
# print(round(bmi))
bmi = round(bmi_1)

if bmi <= 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")

elif bmi <= 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")

elif bmi <= 30:
    print(f"Your BMI is {bmi}, you are overweight.")
elif bmi <= 35:
    print(f"Your BMI is {bmi}, you are obese.")

else:
    print(f"Your BMI is {bmi}, you are clinically obese")

# Leap year exercise
year = int(input("which year do want to check"))

# if year% 4 ==0 and (year% 100 != 0 or year % 400==0) : print("This is a leap year.")

# else :print("This is not a leap year")

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year")
        else:
            print("Not a leap year")

    else:
        print("Leap year")
else:
    print("Not a leap year")

# pizza_ordering exercise
print("Welcome to Python Pizza Deliveries")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N")

bill = 0
if size == "S":
    bill += 15

elif size == "M":
    bill += 20
elif size == "L":
    bill += 25

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1
print(f"Your final bill is: ${bill}")

# coaster_text_ex_2
print("Welcome to the roller coaster!")
height = int(input("What is your height in cm?"))
if height >= 120:
    print("you can ride the roller coaster!")
    age = int(input("what is your age?"))
    if age < 12:
        bill = 5
        print("Child ticket are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    elif 45 <= age < 55:
        print("Everything is ok. have a free ride on us!")
    else:
        bill = 12
        print("Adult tickers are $12.")

    wants_photo = input("Do you want a photo taken? Y or N.")
    if wants_photo == "Y":
        bill += 3

    print(f"your final bill is {bill}")
else:
    print("sorry, You have to grow taller before you  can ride.")

# love calculator.py
print("Welcome to the Love Calculator!")
name1 = input("What is your name \n")
name2 = input("What is their name \n")
combined_string = (name1 + name2)
lower_case_string = combined_string.lower()

t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")

true = t + r + u + e

l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")

love = l + o + v + e

score = str(true) + str(love)
score1 = int(score)

if (score1 < 10) or (score1 > 90):
    print(f"Your score is {score1}, you go together like coke and menthol")
elif (score1 >= 40) and (score1 <= 50):
    print(f"Your score is {score1}, you are alright together")
else:
    print(f"Your score is {score1}")
# treasure game.py
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
cross_road = input("left or right \n")

lower1 = cross_road.lower()

if cross_road == "left":

    boat = input("what do you at the lake ?swim or wait \n")
    lower2 = boat.lower()

    if boat == "wait":
        doors = input("pick a door. red,blue, yellow\n")
        if doors == "red":
            print("game over")
        elif doors == "blue":
            print("game over")
        elif doors == "yellow":
            print("you win")
    else:
        print("game over")

else:
    print("game over")
