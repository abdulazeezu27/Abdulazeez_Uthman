#Day 10
# function with output

# def format_name(f_name,l_name):

#     formated_f_name=f_name.title()
#     formated_l_name=l_name.title()

#     return f"{formated_f_name} {formated_l_name}"

# formated_string=format_name("victor","VICTOR")
# print(formated_string)

# function with output

def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs"
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()

    return f"{formated_f_name} {formated_l_name}"


print(format_name(input("What is your first name? "), input("What is your last name?"))

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
days= days_in_month(year,month)
print(days)
