file = open('MyName.txt', 'r')

name = file.readline()

for letters in name:
    print(letters)

file.close()