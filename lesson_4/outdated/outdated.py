"""
dates are formatted MM/DD/YYYY in the USA

computers use ISO 8601, an international standard that prescribes that dates
should be formatted in YYYY-MM-DD order no matter the country

in this file, implement a program that prompts the user for a date,
anno Domini, in MM-DD-YYYY format (9/8/2020 or September 8, 2020), wherein
the month in the latter might be any of hte vaues in the list below:
    [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]

Then output the same date in YYYY-MM-DD format. If the inpute is not valid
in either format, prompt the user again. Assume that every month has no more than
31 days, no need to validate whether a month has 28, 29, 30, or 31 days.

note:
you can format an 'int' with leading zeroes with code like
    print(f'{n:02}')
where if n is a single digit, it will be prefixed with a 0
"""
months = {
    "January":1,
    "February":2,
    "March":3,
    "April":4,
    "May":5,
    "June":6,
    "July":7,
    "August":8,
    "September":9,
    "October":10,
    "November":11,
    "December":12,
}

days = range(32)

date = ''

def convert_signs(inputted_date):
    if inputted_date[0].isalpha():
        if ',' not in inputted_date:
            return True
        else:
            date_string = inputted_date.replace(',', '').replace(' ', '/')
            return date_string
    else:
        return inputted_date


def validate_date(date_raw):
    date = date_raw.split('/')

    if len(date) != 3:
        return True

    date = convert_month(date)

    if date == True:
        return True

    for day in days:
        if int(date[1]) == day:
            date[1] = day
            return date
        else:
            continue

    return True


def convert_month(list_date):

    for month, value in months.items():
        if list_date[0].isalpha():
            if list_date[0].title() == month:
                list_date[0] = value
                return list_date
        elif list_date[0].isnumeric():
            if int(list_date[0]) == value:
                list_date[0] = value
                return list_date
        else:
            continue

    return True


def pull_date():
    while True:
        inputted_date = input('Date: ').strip()

        if len(inputted_date) < 7:
            continue

        date = convert_signs(inputted_date)

        if date == True:
            continue

        date = validate_date(date)

        if date == True:
            continue

        return date


def main():
    date = pull_date()
    print(f'{int(date[2]):04}-{int(date[0]):02}-{int(date[1]):02}')

main()
