"""
Implement a function called validate that expects an IPv4 address as input as a str and then returns
true or false, respectively, if that input is valid or not.

Structure numb3rs.py as follows, wherein you're welcome to modify main() and/or implement other
functions as seen fit, but may not import other libraries. Not required to use re or sys
"""
import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    ip_list = ip.split('.')

    if len(ip_list) != 4:
        return False

    for value in ip_list:
        try:
            if int(value) >= 0 and int(value) <=255:
                continue
            else:
                return False
        except ValueError:
            return False

    one, two, three, four = ip_list

    pattern = r"^((25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)\.){3}" \
              r'(25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)$'
    if re.match(pattern, ip):
        return True

    return False

if __name__ == "__main__":
    main()
