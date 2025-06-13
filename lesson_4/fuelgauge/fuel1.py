# fuel gauges indicate with fractions how much fuel is left in a tank

# implement a program that prompts the user for a fraction, formmated as x/y, wherein each of
# x and y is an integer and then outputs, as a percentage rounded to the nearest integer,
# how much fuel is in the tank

# if 1% or less remains, output E instead to indicate that the tank is emoty
# if 99% or more, output F to indicate the tank is full

# if x or y is not an integer, x is greater than y, or y is 0, prompt the user again

# catch any exceptions like ValueError or ZeroDivisionError

def main():
    values = convert(values_inputted())
    if values <= 1:
        print('E')
    elif values >= 99:
        print('F')
    else:
        print(f'{values}%')

def values_inputted():
    while True:
        fraction = input('Fraction: ').split('/')
        try:
            x = int(fraction[0])
            y = int(fraction[-1])
        except ValueError:
            continue
        else:
            if x > y:
                continue
            else:
                try:
                    z = x / y
                except ZeroDivisionError:
                    continue
                else:
                    return z

def convert(values_inputted_returned):
    result = round(values_inputted_returned * 100)
    return result

main()
