

def main():
    greeting = input('Greeting: ').strip()

    money = value(greeting)

    print(f'${money}')


def value(greeting):
    greeting = greeting.lower()

    if 'hello' in greeting:
        x = 0
    elif greeting[0] == 'h':
        x = 20
    else:
        x = 100

    return x

#"""
if __name__ == '__main___':
    main()
#"""
#main()
