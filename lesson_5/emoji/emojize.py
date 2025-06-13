"""
carpedm20.github.io/emoji/all.html?enableList=enable_list_alias --- list of codes with aliases

implement a program that prompts the user for a str in English and then outputs the emojized version
of that str, coverting any codes or aliases into their corresponding emoji

***note: emoji module comes with two functions:
        emojize -- takes an optional, named parameter
"""

from emoji import emojize


def main():
    alias = input('Input: ')

    if ':thumbsup:' in alias:
        alias = alias.replace(':thumbsup:', ':thumbs_up:')
    if ':earth_asia' in alias:
        alias = alias.replace(':earth_asia:', ':globe_showing_Asia-Australia:')

    print(f'{emojize(alias)}')



if __name__ == '__main__':
    main()
