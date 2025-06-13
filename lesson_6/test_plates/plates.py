def main():
    if (is_valid(input("Enter Plate: ").upper())) == False:
        print("Invalid")
    else:
        print("Valid")

def is_valid(s):
    if not 2 <= len(s) <=6:
        return False
    if s[0:2].isalpha() == False:
         return False

    numbers = []
    for char in s:
        if char in ['.', ' ', '?', '!']:
            return False
        if len(numbers) != 0 and char.isalpha():
            return False
        if char.isnumeric() and (len(numbers) == 0 and char == '0'):
            return False
        elif char.isnumeric():
            numbers.append(char)

    return True


if __name__ == "__main__":
    main()
