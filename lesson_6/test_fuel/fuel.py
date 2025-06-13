"""
Reimplement Fuel Gauge from Problem Set 3, restructuring code per the below wherein:

    - 'convert' expects a str in X/Y format as input
        - each of X and Y is an integer
        - return that fraction as a percentage rounded to the nearest int between 0 and 100
        - if X and/or Y is not an integer, or if X is greater than Y, then convert should
          raise a ValueError.
        - if Y is 0, then convert should raise a ZeroDivisionError

    - 'gauge' expects an int and returns a str that is:
        - 'E' if that int is less than or equal to 1
        - 'F' if that int is greater than or equal to 99
        - and 'Z%' otherwise, wherein Z is the same as int
"""


def main():
    while True:
        fraction = input('Fraction: ')
        try:
            percentage = convert(fraction)
            break
        except (ValueError, ZeroDivisionError):
            continue

    print(gauge(percentage))


def convert(fraction):
    fraction_list = fraction.split('/')

    try:
        x = int(fraction_list[0])
        y = int(fraction_list[-1])
    except ValueError:
        raise ValueError()

    if y == 0:
        raise ZeroDivisionError()
    elif x > y:
        raise ValueError()
    else:
        z = round((x / y * 100))
        return z

def gauge(percentage):
    if percentage <= 1:
        return 'E'
    elif percentage >= 99:
        return 'F'
    else:
        return f'{percentage}%'


if __name__ == "__main__":
    main()
