# if greeting == hello --> output $0
# if greeting == h.... --> output $20
# if greeting == '' --> output $100

def main():
    greeting = input('Greeting: ')

    greeting = lower(greeting)

    if 'Hello' in greeting:
        print('$0')
    elif greeting[0] == 'H':
        print('$20')
    else:
        print('$100')

def lower(d):
    d = d.strip().lower().capitalize()
    return d

main()
