# vanity plate requirements
#      start with at least two lettesr
#      max of 6 characters and min of 2
#      numbers cannot be used in the middle of a plate (must come at the end)
#               first number cannot be a 0
#      no periods, spaces, or punctuation marks are allowed

# implement a program that asks the user for a vanity plate and then ouputs valid or invalid if
# it meets the requirements
# assume any letters inputted will be uppercase

# structure program wherein is_valid() returns True if s meets all requirements and False if not
# assume s will br a str

special_charc = ['.', ' ', '?', '!']

def main():
    plate = input("Plate: ")
    if is_valid(plate) == True:
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if length(s):
        if punctuation(s):
            return False
        else:
            if letters(s):
                return True
            else:
                if check_first_two(s):
                    if check_zero(s):
                        if check_num(s):
                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    return False


def length(s):
    if 1 < len(s) < 7:
        return True


def punctuation(s):
    for i in s:
        for c in special_charc:
            if i == c:
                return True

def letters(s):
    if s.isalpha() == True:
        return True
    else:
        return False

def check_first_two(s):
    if s[0:2].isalpha() == True:
        return True
    else:
        return False

def check_zero(s):
    index = 0
    for i in s:
        if i.isnumeric() == True:
            index = s.find(i)
            break
    if s[index] != '0':
        return True

def check_num(s):
    index1 = 0
    index2 = len(s) -1
    for i in s:
        if i.isnumeric() == True:
            index1 = s.find(i)
            break
        
    while index1 < len(s):
        if s[index1].isalpha() == True:
            return False
        else:
            index1 += 1
    return True
main()
