"""
Implement a function called convert that expects a str in any of the 12 hour formats below:
    9:00 AM to 5:00 PM
    9 AM to 5 PM
    9:00 AM to 5 PM
    9 AM to 5:00 PM
And returns the corresponding str in 24-hour format (i.e. 9:00 to 17:00).

Expect that AM and PM will be capitalized with no periods therein and that there will be a space before each.
Assume times are representative of actual times, not 9:00 AM to 5:00 PM specifically.

Raise a ValueError isntead if the input to convert is not in either of those formats or if either time is invalid (e.g
12:60 AM, 13:00 PM, etc). But do not assume that someone's hours will start ante meridiem and end post meridiem.

Note that you can format an int with leading zeroes with code like print(f"{n:02}") wherein, if n is a single digit,
it will be prefixed with one 0
"""
import re
import sys

def main():
    print(convert(input("Hours: ")))


def convert(s):
    pattern = r"^([1-9]|[1][0-2])(:[0-5][0-9])?\s(AM|PM)\s(to)\s([1-9]|[1][0-2])(:[0-5][0-9])?\s(AM|PM)$"
    if not re.match(pattern, s):
        raise ValueError()



    time_list = s.split(" to ")

    pm_time_list = PM_convert(time_list)

    return pm_time_list

def PM_convert(a):
    pattern = r"^(?P<Hour>[1-9]|[1][0-2]):?(?P<Minute>[0-5][0-9])?\s(?P<Meridiem>(?:PM|AM))$"
    list_time = []
    meridiem = ''
    minute = ''
    hour = ''

    for item in a:
        if match := re.match(pattern, item):
            meridiem = match.group('Meridiem')
            minute = match.group('Minute')
            hour = int(match.group('Hour'))
            if meridiem == 'PM' and hour != 12:
                hour = int(match.group('Hour')) + 12
            elif meridiem == 'PM' and hour == 12:
                pass
            elif meridiem == 'AM' and hour == 12:
                hour = 0
            if minute == None:
                minute = '00'
            time = f"{hour:02d}:{minute}"

            list_time.append(time)

    string_time = list_time[0] + ' to ' + list_time[1]

    return string_time

if __name__ == "__main__":
    main()
