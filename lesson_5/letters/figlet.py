"""

FIGlet, named after Frank, Ian, and Glen's letters, is a program from early 1990s for making large
letters out of ordinary text, a form of ASCII art.

http://www.figlet.org/examples.html
https://en.wikipedia.org/wiki/FIGlet
https://github.com/cmatsuoka/figlet


FIGlet has since been ported to Python as a module called pyfiglet

implement a program that expects zero or two command-line arguments:
    zero if the user would liek to output text in a random font
    two if the user would liek to output text in a specific font, in which the first of the two
        should be -f or --font, and the second of the two should be the name of the font
    prompts the user for a str of text once the program runs
    outputs the text in the desired font

"""
from pyfiglet import Figlet
import sys
import random

#set up
figlet = Figlet()
fonts = figlet.getFonts()
chosen_font = ''

def check_arguments():
    if sys.argv[1] not in ['-f', '--font']:
        sys.exit('Invalid usage')

    if sys.argv[2] not in fonts:
        sys.exit('Invalid usage')

    return sys.argv[2]

def convert(text_input, chosen_font):
    figlet.setFont(font=chosen_font if chosen_font else random.choice(fonts))
    print('Output: ')
    print(figlet.renderText(text_input))

def main():
    if len(sys.argv) not in [1, 3]:
        sys.exit('Invalid usage')

    chosen_font = check_arguments() if len(sys.argv) == 3 else ''

    text_input = input('Input: ')
    convert(text_input, chosen_font)

if __name__ == '__main__':
    main()
