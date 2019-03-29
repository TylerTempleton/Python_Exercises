# The purpose of this program is to use user entered date of birth to see if its currently, upcoming or a passed birthday and display the difference if present to days from the current system date.
# This program uses date time to determine birthdate data
#import datetime 
import datetime

# Title bar string

def print_title():
    title = """
---------------------
Birthday App
---------------------
"""



def get_birthday():
    print("When were you born? ")
    year = int(input("Year [YYYY]: "))
    month = int(input("Month [MM]: "))
    day = int(input("Day [DD]: "))

    birthday = datetime.date(year, month, day)
    return birthday


def compute_dates(original_date, target_date):
    this_year = datetime.date(target_date.year, original_date.month, original_date.day)

    dt = this_year - target_date
    return dt.days


def print_birthday_information(days):
    if days < 0:
        print("You had your birthday {} days ago this year.".format(-days))
    elif days > 0:
        print("Your birthday is in {} days!".format(days))
    else:
        print("Happy birthday")









def main():
    print_title()
    bday = get_birthday()
    today = datetime.date.today()
    number_of_days = compute_dates(bday, today)
    print_birthday_information(number_of_days)


main()