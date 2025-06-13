"""
reimplement 'Setting up my twttr' from problem set 2, restructuring
code as per below, where shorten expects a str as input and returns
that same str but with all vowels (AEIOU) omitted, whether inputted
in as uppercase or lowercase

"""

def main():
    word = input('Input: ')

    print(shorten(word))

def shorten(word):
    output = ''
    for letter in word:
        if letter == 'a' or letter == 'A':
            continue
        elif letter == 'i' or letter == 'I':
            continue
        elif letter == 'e' or letter == 'E':
            continue
        elif letter == 'u' or letter == 'U':
            continue
        elif letter == 'o' or letter == 'O':
            continue
        else:
            output += letter

    return output

if __name__ == '__main__':
    main()
