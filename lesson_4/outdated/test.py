
"""
def main():
    while True:
        inputted_date = input('Date: ')

        if len(inputted_date) <7:
            continue

        if inputted_date[1].isalpha() == True:
            date = inputted_date.replace(',' , '').split(' ')

            if len(date) != 3:
                continue

            for month in months.keys():
                if date[0].title() == month:
                    date[0] = months[month]
                    if len(date[1]) == 1 or len(date[1]) == 2:
                        if len(date[2]) == 4 or len(date[2]) == 2:
                            return False
                        else:
                            break
                    else:
                        break
                else:
                    continue

            return date


        else:
            date = inputted_date.split('/')

            if len(date) != 3:
                continue

            if len(date[0]) != 2 and len(date[0]) != 1 and len(date[1]) != 2  and len(date[1]) != 1 and len(date[2]) != 4:
                continue
            else:
                return False, date



main()
"""

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
    "June":5,
    "July":7,
    "August":8,
    "September":9,
    "October":10,
    "November":11,
    "December":12,
}

days = range(32)

months_numerical = range(13)

date = ''

def validate_date(date):
    if len(date) != 3:
        return False
    if not (len(date[0]) in [1, 2] and len(date[1]) in [1, 2] and len(date[2]) == 4):
        return False
    return True

def convert_month(date):
    for month in months.keys():
        if date[0].title() == month:
            date[0] = months[month]
            break
        else:
            return None
    for day in days:
        if date[1] == day:
            break
        else:
            return None
    if len(date[2]) == 4:
        return date
    else:
        return None

def pull_date():
    while True:
        inputted_date = input('Date: ')

        if len(inputted_date) < 7:
            continue

        if inputted_date[1].isalpha():
            if ',' not in inputted_date:
                continue

            date = inputted_date.replace(',', '').split(' ')
            date = convert_month(date)
            if date and validate_date(date):
                return date
        else:
            date = inputted_date.split('/')
            if validate_date(date):
                return date

def main():
    date = pull_date()
    print(f'{int(date[2]):04}-{int(date[0]):02}-{int(date[1]):02}')

main()
