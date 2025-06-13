"""
Implement a program expecting exactly one command line argument, the name of a csv file in
Pinocchio's format, and outputs a table formatted as ASCII art using tabulate, a package on PyPI
at pypi.org/project/tabulate.
    * Format the table using the library's grid format.
    * If user does not specify exactly one command line argument, or specified file name does not
    end in .csv, or if the specified file does not exist, program should exit via sys.exit
"""

import sys
from tabulate import tabulate #tablefmt = 'grid'
import csv

def main():
    if len(sys.argv) < 2:
        sys.exit('Too few command-line arguments')
    if len(sys.argv) > 2:
        sys.exit('To many command-line arguments')

    argu = str(sys.argv[1])
    argu_index = argu.find('.')
    argu_type = argu[argu_index:]

    if argu_type != '.csv':
        sys.exit('Not a CSV file')

    table = []
    try:
        with open(argu, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                table.append(row)
    except FileNotFoundError:
        sys.exit('File does not exist')

    print(tabulate(table, headers="firstrow", tablefmt="grid"))
if __name__ == '__main__':
    main()
