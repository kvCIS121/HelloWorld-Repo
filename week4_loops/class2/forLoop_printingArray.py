a = "a"
b = "b"

word = "abcde"
#different ways to print the variable [word]
for letter in word:
    print(letter, end = " ")    # end=" " means “after printing, put a space instead of a newline.” 
                                #   this prints "a b c d e" horizontally, instead of each letter vertically and separately


    print(letter, end = "\n")   # this prints two columns with 5 rows of each letter twice, like an array
                                # a a
                                # b b
                                # c c
                                # d d
                                # e e

    