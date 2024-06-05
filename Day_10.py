#Day 10
# function with output

# def format_name(f_name,l_name):

#     formatted_f_name=f_name.title()
#     formatted_l_name=l_name.title()

#     return f"{formatted_f_name} {formatted_l_name}"

# formatted_string=format_name("victor","VICTOR")
# print(formatted_string)

# function with output

def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs"
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()

    return f"{formated_f_name} {formated_l_name}"


print(format_name(input("What is your last name?"), input("What is your first name? "))

def is_leap(year):

    if year% 4 ==0:
        if year% 100 ==0:
            if year% 400 == 0:
                print("Leap year")
            else:print("Not a leap year")

        else:
            print("Leap year")
    else:
        print("Not a leap year")

def days_in_month():
    month_days=[31, 28, 31,30, 31, 30,31,31,30,31,30,31]

year= int(input("Enter a year: "))
month=int(input("Enter a month: "))
days_in_month(year, month)
print(days)
