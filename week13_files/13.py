file1 = open('FamilyAges.csv', 'w')

# write the header row
file1.write("Name,Age\n")

# write family members (you can change these)
file1.write("Kong,20\n")
file1.write("Alice,45\n")
file1.write("Bob,50\n")
file1.write("Charlie,17\n")
file1.write("Daisy,13\n")

file1.close()

print("FamilyAges.csv has been created.")
