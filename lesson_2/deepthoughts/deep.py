# implement a program that asks the user for the answer to the Great Question of Life,
# the Universe and Everything, outputting yes if the user inputs 42, forty-two, or forty two
# otherwise output no


def main():
    check_answer()

def check_answer():
    answer = input('What is the Answer to the Great Question of Life, the Universe,
                   and Everything? ').lower().strip()
    #lower(answer)
    if answer == '42' or answer == 'forty two' or answer == 'forty-two':
        print('Yes')
    else:
        print('No')



main()
