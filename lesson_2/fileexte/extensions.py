# implement a program that prompts the user for the name of a file and then outputs
# that file's media type if the file's name ends, case insensitively, in...
# .gif | .jpg | .jpeg | .png | .pdf | .txt | .zip

def main():
    file = input('File name: ')

    type = extension(file)

    if type == 'gif' or type == 'jpg' or type == 'jpeg' or type == 'png':
        print(f'image/{type}')
    elif type == 'pdf' or type == 'zip':
        print(f'application/{type}')
    elif type == 'txt':
        print(f'text/plain')
    else:
        print(f'application/octet-stream')


def extension(file):
    index = file.strip().lower().split('.')
    extension = index[-1]
    if extension == 'jpg':
        extension = 'jpeg'

    return extension

main()
