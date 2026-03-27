def hamming_distance(str1, str2):
	if len(str1) != len(str2):
		return "Strings must be of equal length."
	
	returned_letters = ''	
	for i in range(len(str1)):	
		if str1[i] != str2[i]: 
			returned_letters += str1[i] # returning the letter difference from str1 = "c"
			returned_letters += str2[i] # returning the letter difference from str2 = "h"
	return returned_letters


print(hamming_distance("cat", "hat")) # These were my arguments to test for letter matches/differences
