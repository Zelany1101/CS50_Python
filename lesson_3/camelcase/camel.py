# implement a program that prompts the user for the name of a variable in camel case
# and outputs the corresponding name in snake case
# assume input will be camel case
# camel case ('mixed case) -- first letter is lowercase, but each subsequent word is uppercase
# snake case -- words are seperated by underscores

def main():
    variable = input('camelCase: ')

    print(convert(variable))

def convert(variable):
    snake_case = ''

    for i in variable:
        if i.isupper() == True:
            snake_case += '_' + i.lower()
        else:
            snake_case += i

    return snake_case


main()
