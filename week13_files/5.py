file = open('aMorePerfectUnion.txt', 'r')

speech = file.readlines()

def countRepititions(elements):
    dictionary = {}

    for line in elements:
        words = line.split()      # split line into words
        for w in words:           # loop through actual words
            if w in dictionary:
                dictionary[w] += 1
            else:
                dictionary[w] = 1

    return dictionary

result = countRepititions(speech)
print(result)

file.close()
