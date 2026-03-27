def design_rug(width, length, pattern):
	result = "Your rug is:\n"
	for i in range(length):
		result += pattern * width
		if i < length - 1: #originaly, this was: if i < length only. I had to add the -1. to make it 5 rows, w/ no space at bottom
			result += "\n"
	return result

#print(design_rug(3, 5, '$')) # Expected output: "Your rug is:\n$$$\n$$$\n$$$\n$$$\n$$$"
print(design_rug(16, 5, "@")) # Expected output: "Your rug is:\n@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@"
# need to add in a 3rd argument in the print(16, 5, "@")