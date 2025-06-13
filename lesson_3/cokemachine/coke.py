# a machine sells bottles of cocacola for 50 ccents and only accepts quarters, dimes, and nickles
# implement a program that prompts the user to insert a coin, one at a time, each time informing
# the user of the amount due
# once 50 cents is inputted, output how many cents in change the user is owned

import math

def main():
    prompt()

def prompt():
    coin = 0
    total = 0
    due = 50

    while total < 50:
        print(f'Amount Due: {due}')
        coin = int(input('Insert Coin: '))
        if coin == 5 or coin == 10 or coin == 25:
            total += coin
            due -= coin
        else:
            coin = 0

    if total == 50:
        print('Change Owed: 0')
    else:
        print(f'Change Owed: {abs(total - 50)}')

main()
