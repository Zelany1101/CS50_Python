# write a program that enables users to do math, even without knowing python
# prompt the user for an arithmetic expression and then calculate and output the result as a float
# valye formmated to one decimal
# assume formatted as x y z with one space between x and y and one space between y and z
# x is an integer
# y is + - * or /
# z is an integer

def main():
    expression = input('Expression: ')

    value = format(expression)
    print(value)

def format(d):
    d = d.split(' ')
    x = float(d[0])
    y = d[1]
    z = float(d[2])
    value = equation(x, y, z)

    return value

def equation(x, y, z):
    if y == '+':
        return float(x + z)
    elif y == '-':
        return float(x - z)
    elif y == '*':
        return float(x * z)
    elif y == '/':
        return float(x / z)
    else:
        print('Invalid operation')

main()
