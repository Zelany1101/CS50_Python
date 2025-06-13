"""
Implement a program that expects exactly one command line argument, the name (or path) of a Python file,
and outputs the number of lines of code in that file, excluding comments and blank lines.
    * If user does not specify exactly one command-line argument, or specified file does not end in .py
    or specified file does not exist, program should exit via sys.exit
    * Assume that any line starts with #, optionally preceded by whitespace, is a comment.
        * docstring should not be considered a comment
    * Assume that any line only containing whitespace is blank
"""
import sys

def main():
    if len(sys.argv) < 2:
        sys.exit('Too few command-line arguments')
    if len(sys.argv) > 2:
        sys.exit('To many command-line arguments')

    argu = str(sys.argv[1])
    argu_index = argu.find('.')
    argu_type = argu[argu_index:]

    if argu_type != '.py':
        sys.exit('Not a Python file')

    try:
        with open(argu, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        sys.exit('File does not exist')
    else:
        stripped_lines = [line.strip() for line in lines]

    count = 0
    for line in stripped_lines:
        if line == "":
            continue
        elif line.startswith("#") == True:
            continue
        else:
            count += 1

    print(count)
if __name__ == '__main__':
    main()


    #docstring_flag = False
      #  elif line.startswith('"""') == True:
      #      if docstring_flag == False:
      #          docstring_flag = True
      #          continue
      #      else:
       #         docstring_flag = False
      #          continue
      #  elif docstring_flag == True:
       #     continue

