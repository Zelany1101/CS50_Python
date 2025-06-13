"""
implement a program that enables a user to place an order, protmpitng them
for items, one per line, until the user inputs control-d
after each inputted item, display the total cost of all items inputted
    prefixe them with a dollar sign
    format to two decimal places
treat the user's input case insensitively

ignore any input that isn't an item

assume that every item on the menu will be titlecased
    - string where words start with an uppercase and remaining characters are lower

dictionary:
{
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

catch control-d with EOFError
    inputting control-d does not require inputting enter as well

avoid any KeyError -- raised when mapping (disctionary) key is not found in the
set of existing keys
    'raised when input() function hits an EOF without reading any data. (the io.IOBase.read() and
    io.IOBase.readline() methods return an empty string when they hit EOF)'
    'EOF us a condition in a computer operating system where no more data can be read from a data
    source'

"""

menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00,
}


def main():
    total = 0
    while True:
        try:
            item = input("Item: ").title()
        except EOFError:
            print("\n")
            break
        else:
            try:
                print(f"Total: ${(total + menu[item]):.2f}")
            except KeyError:
                continue
            total += menu[item]


main()
