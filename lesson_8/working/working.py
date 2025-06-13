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
"""
import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    pattern = r"^(?:[1-9]|[1][0-2])(?::[1-5][0-9])?\s(AM|PM)\sto\s(?:[1-9]|[1][0-2])(?::[1-5][0-9])?\s(AM|PM)$"
    if not re.match(pattern, s):
        raise ValueError()

    start, end = s.split(" to ")

    start_24 = convert_to_24(standardize(start))
    end_24 = convert_to_24(standardize(end))

    return f"{start_24} to {end_24}"
def standardize(time_str):
    pattern = r"^(?:[1-9]|[1][0-2])\s(AM|PM)$"
    if re.match(pattern, time_str):
        index = time_str.find(" ")
        time_str = time_str[:index] + ":00" + time_str[index:]
    return time_str

def convert_to_24(standardized_time_str):
    match = re.match(r"^(\d{1,2}):(\d{2})\s(AM|PM)$", standardized_time_str)

    hour = int(match.group(1))
    minute = match.group(2)
    meridiem = match.group(3)

    if meridiem == "PM":
        hour += 12

    return f"{hour:02d}:{minute}"

if __name__ == "__main__":
    main()
"""
import re
import sys

def main():
    print(convert(input("Hours: ")))


def convert(s):
    pattern = r"^([1-9]|[1][0-2])(:[0-5][0-9])?\s(AM|PM)\s(to)\s([1-9]|[1][0-2])(:[0-5][0-9])?\s(AM|PM)$"
    if not re.match(pattern, s):
        raise ValueError()



    list_time = s.split(" to ")

    pm_time_list = PM_convert(list_time)

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
