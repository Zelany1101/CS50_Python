"""
Implement a program that ...
    * Expects the user to provide two command-line arguments:
        - The name of an existing CSV file to read as input, whose columns are assumed to be in
        order, name and house
        - Convert that input to that output, splitting each name into a first name and last name.
            * Assume that each student will have both a first name and last name.
    * If user does not provide exactly two command line arguments, or the first cannot be read,
    the program should exit via sys.exit with an error message
"""
import csv
import sys

def file_type_check(checkers):
    if len(checkers) < 2:
        sys.exit('Too few command-line arguments')
    if len(checkers) > 2:
        sys.exit('Too many command-line arguments')

    for item in checkers:
        file = str(item)
        if not file.endswith('.csv'):
            sys.exit('Not a CSV file')

def main():
    file_type_check(sys.argv[1:])

    before_file = sys.argv[1]
    after_file = sys.argv[2]

    names_list = []
    house_list = []
    try:
        with open(before_file, 'r') as before, open(after_file, 'w', newline='') as after:
            reader = csv.reader(before)
            for row in reader:
                names_list.append(row[0])
                house_list.append(row[1])
    except FileNotFoundError:
        sys.exit('File does not exist')

    first_last_name_list = []
    n = 1
    for name in names_list[1:]:
        first_last_name_list.append(name.split(","))
    for row in first_last_name_list:
        row.append(house_list[n])
        n += 1
    headers = ['first', 'last', 'house']
    first_last_name_list.insert(0, headers)

    with open(after_file, 'w') as after:
        writer = csv.DictWriter(after, fieldnames=first_last_name_list[0])
        writer.writeheader()

        for row in first_last_name_list[1:]:
            writer.writerow(
                {
                    "first": row[1].strip(),
                    "last": row[0],
                    "house": row[2]
                }
            )

if __name__ == '__main__':
    main()

