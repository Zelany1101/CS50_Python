def is_valid(fraction):
    #print(fraction.count('/'))
    if fraction.count('/') != 1:
        return False

    fraction_split = fraction.split('/')
    #print(fraction_split)
    numerator = fraction_split[0]
    #print(f"numerator: {numerator}")
    denominator = fraction_split[1]
    #print(f"denominator: {denominator}")

    special_chars = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-",
                     "+", "?", "_", "=", ",", "<", ">", "/", ".", " "]

    if (numerator in special_chars) or (denominator in special_chars):
        #print("Not a number (S Chars)")
        return False

    if (numerator.isnumeric() == False) or (denominator.isnumeric() == False):
        #print("Not a number (Letters)")
        return False

    if denominator == '0':
        #print("undefined")
        return False

    #rint(f"numerator: {numerator}")
    #print(f"denominator: {denominator}")
    if int(numerator) > int(denominator):
        #print("Over 100%")
        return False

    calculate_gas(numerator, denominator)

def calculate_gas(numerator, denominator):
    percent = int(round(int(numerator) / int(denominator), 2)*100)
    #print(round(int(numerator) / int(denominator), 2))
    #print(int(numerator) / int(denominator))
    if percent >= 99:
        print("F")
    elif percent <= 1:
        print("E")
    else:
        print(f"{percent}%")

def main():
    #fraction = input("Fraction: ")
    #fraction = '100/100'
    #is_valid(fraction)

    while(is_valid(input("Fraction: "))) == False:
        pass


if __name__ == "__main__":
    main()
