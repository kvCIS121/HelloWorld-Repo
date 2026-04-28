fileName = input('enter name of a text file: ')

try:
    file = open(fileName, 'r')
    print(file.read())
    file.close()

except FileNotFoundError:
    print('File not found')

#Note: 'except FileExistsError' does not work. I had to use FileNotFoundError