# implement a program that prompts the user for a str of text and then outputs that same text
# but with all vowels omitted, whether inputted as uppercase or lowercase

def main():
    prompt = input('Input: ')

    print(output(prompt))

def output(prompt):
    output = ''
    for letter in prompt:
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


main()
