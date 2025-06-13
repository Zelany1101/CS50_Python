# Implement a function called convert that accepts a str as input and returns the same input with
# any :) converted to smile emoticon and :( into a frowning face

# Also implement a function called main that prompts the user for input, calls convert on that input,
# and prints the results

def main():
    sentence = input('Give a smilely face: ')
    print(convert(sentence))


def convert(smile):
    smile = smile.replace(':)', '🙂')
    smile = smile.replace(':(', '🙁')
    return smile

main()


