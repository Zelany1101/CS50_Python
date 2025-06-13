'''
# vanity plate requirements
#      start with at least two letters
#      max of 6 characters and min of 2
#      numbers cannot be used in the middle of a plate (must come at the end)
#               first number cannot be a 0
#      no periods, spaces, or punctuation marks are allowed

# implement a program that asks the user for a vanity plate and then ouputs valid or invalid if
# it meets the requirements
# assume any letters inputted will be uppercase

# structure program wherein is_valid() returns True if s meets all requirements and False if not
# assume s will br a str
'''

def is_valid(vanity_plate):
    if not 2 <= len(vanity_plate) <=6:
        #print("Wrong Length")
        return False
    if vanity_plate[0].isalpha() != True or vanity_plate[1].isalpha() != True:
         #print("First 2 Chars need to be letters")
         return False

    numbers = []
    for char in vanity_plate:
       if char in ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "+", "?", "_", "=", ",", "<", ">", "/", ".", " "]:
           #print("No Special Chars Allowed")
           return False
       if len(numbers) != 0 and char.isalpha():
           #print("Can't have letters after numbers")
           return False
       if char.isnumeric() and (len(numbers) == 0 and char == '0'):
           #print("First number cannot be zero")
           return False
       elif char.isnumeric():
           numbers.append(char)

    #print(f"'{vanity_plate}' is a valid vanity plate")
    return True

def main():
    '''
    while is_valid(input("Enter Plate: ").upper()) == False:
        pass
    '''
    if (is_valid(input("Enter Plate: ").upper())) == False:
        print("Invalid")
    else:
        print("Valid")


if __name__ == "__main__":
    main()
