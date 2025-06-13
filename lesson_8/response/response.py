"""
Either using validator collection or validitors from PyPI, implement a program that prompts the
user for an email address via input and then prints Valid or Invalid respectively, based on if
the input is a syntactically valid email address.
    - May not use re
    - Do not validate whether the email address's domain name actually exists.
"""
import validators

def main():
    email = input("email: ")
    if validators.email(email):
        print('Valid')
    else:
        print('Invalid')

if __name__ == "__main__":
    main()
