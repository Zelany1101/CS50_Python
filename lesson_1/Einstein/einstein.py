# E = mc^2
# E = Energy (Joules) | m = Mass (Kg) | c = Speed of light (300000000 m/s)
# Equation means mass and energy are equivalent

# Implement a program that prompts the user for mass as an interner in kg and then outputs
# the equivalent number of joules as an integer

# assume the user will input an integer

import math

def main():
    mass = int(input('Give mass: '))
    print(einstein(mass))

def einstein(mass):
    c = 300000000
    energy = int(mass * (c**2))
    return energy
main()
