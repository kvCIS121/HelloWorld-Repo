# The hamming distance is the number of characters that differ between two strings.
# To illustrate,
# str1 = "abcbba"
# str2 = "abcbda"
# The hamming distance is 1 since the only difference is the 5th character.
# That is, "b” in str1 vs. "d” in str2.
# Your task: create a function named hamming distance that takes two strings as arguments, and returns
# the hamming distance between the two strings

def hamming_distance(s1, s2):
    count = 0

    for i in range(len(s1)):
        if s1[i] != s2[i]:
            count = count + 1
    return count

str1 = 'abvbba'
str2 = 'abvbda'
print(hamming_distance(str1, str2))