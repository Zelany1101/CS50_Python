"""
implement a program that ...
    - prompts the user for a level, n, if the user does not input 1, 2, or 3, the program should prompt again
    - randomly generate ten math problems formatted as X + Y =, wherein each of X and Y is a non-negative interger with n digits.
            - no need to support operations other than addition (+)
    - prompt user to solve each of those problems
            - if answer is not correct, program should output EEE and prompt user again
            - user gets three tries in total for that problem
            - if user does not answer correctly after three tries, program outputs the correct answer
    - program should ultimately output the user's score
            - the number of correct answers out of ten

structure program as follow, wherein 'get_level' prompts (and if need to be, re-prompts) the user for a level and returns
1, 2, or 3, and 'generate_integer' returns a randomly generated non-negative itneger with 'level' digits or raises a ValueError
if 'level' is not 1, 2, or 3
"""
import random


def main():
    level = get_level()

    count = 0
    correct = 0

    while count < 10:
        x = generate_integer(level)
        y = generate_integer(level)

        tries = 0
        while tries < 3:
            guess = input(f'{x} + {y} = ')
            try:
                int(guess)
            except ValueError:
                print('EEE')
                tries += 1
            else:
                if int(guess) == x + y:
                    correct += 1
                    break
                else:
                    print('EEE')
                    tries += 1

        if tries == 3:
            print(f'{x} + {y} = {x + y}')

        count += 1

    wins = correct
    print(f'Score: {wins}')

def get_level():
    while True:
        try:
            level = int(input('Level: '))
        except ValueError:
            pass
        else:
            if level in [1, 2, 3]:
                return level

# returns a randomly generated non-negative interger with level digots
def generate_integer(level):
    max_value = (10**level)-1
    min_value = 10**(level - 1) if level > 1 else 0

    number = random.randint(min_value, max_value)

    return number

if __name__ == "__main__":
    main()


