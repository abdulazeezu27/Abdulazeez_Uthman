#Day 9
#NEsting
capital={
    "France":"Paris",
    "Germany": "berlin",
}

#nesting a list in a dictionary

travel_log={
    "France":["paris","Lille","Dijon" ],
    "Germany":["Berlin", "Hamburg","Stuttgart"],
}

#Nesting dictionary in a dictionary
travel_log={
    "France":{"cities_visted":["paris","Lille","Dijion" ],"total_visted":12} ,
    "Germany":{"cities_visted":["Berlin", "Hamburg","Stuttgart"],"total_vists":5},
}

#nesting a dictionary in a list
travel_log=[
   {
        "country": "France",
        "cities_visted":["paris","Lille","Dijion" ],
        "total_visted":12
    } ,
    {
        "country":"Germany" ,
        "cities_visted":["Berlin", "Hamburg","Stuttgart"],
        "total_vists":5
        },

logo = ''' 

                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

import os

os.system('cls||clear')

from art import logo

print(logo_new)

bids = {}
bidding_finished = False


def find_highest_bidder(bidding_record):
    highest_bid = 0
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


while not bidding_finished:
    name = input("What is your name?")
    price = int(input("What is your bid: $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes or 'no'.")
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue == "yes":
        os.system('cls||clear')

        programming_dictionary = {
            "Bug": "An error in a program that prevents the program from running as expected.",
            "Function": "A piece of code that you can easily call over and over again."
        }

        # Retrieving items from the dictionary

        # print(programming_dictionary["Bug"])

        # adding new items to dictionary
        programming_dictionary["loop"] = "The action of doing something over and over again"

        # print(programming_dictionary)

        # create an empty dictionary
        empty_dictionary = {}

        # wipe an existing dictionary
        # programming_dictionary={}
        # print(programming_dictionary)

        # edit an item in the dictionary
        # programming_dictionary["Bug"]= "A moth in your computer"
        # print(programming_dictionary)

        # loop thrrough dictionary
        for key in programming_dictionary:
            print(key)
            print(programming_dictionary[key])

            student_scores = {
                "Harry": 81,
                "Ron": 78,
                "Hermione": 99,
                "Draco": 74,
                "Neville": 62,
            }

            student_grades = {}
            for student in student_scores:
                score = student_scores[student]
                if score > 90:
                    student_grades[student] = "outstanding"
                elif score > 80:
                    student_grades[student] = "Exceeds Expectation"
                elif score > 70:
                    student_grades[student] = "Acceptable"
                elif score < 70:
                    student_grades[student] = "Fail"

            print(student_grades)