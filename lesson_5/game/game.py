"""
Implement a program that...
    - prompts user for a level, n, if user does not input a positive integer, the program should prompt again
    - randomly generate an integer between 1 and n, using random module
    - prompts user to guess that integer
            - if guess is not positive integer, program should prompt user again for another guess
            - if guess is larger than integer, program should output 'Too large!' and prompt user again
            - if guess is smaller than integer, program should output 'Too small!' and prompt user again
            - if guess is the same as the integer, program should output 'Just right!' and exit

"""

import random

def level_check():
    while True:
        try:
            level = int(input('Level: '))
            if level > 0:
                return level
        except ValueError:
            continue


def guess(n):
    random_int = random.randint(1, n)
    while True:
        try:
            guess = int(input('Guess: '))
        except ValueError:
            continue
        else:
            if guess > 1:
                if guess == random_int:
                    print('Just right!')
                    break
                elif guess > random_int:
                    print('Too large!')
                else:
                    print('Too small!')

def main():
    n = level_check()

    guess(n)

if __name__ == '__main__':
    main()
