file1 = open('PagesRead.csv', 'r')

lines = file1.readlines()

# dictionary: key = name, value = total pages read
pages_dict = {}

# skip the header row
for line in lines[1:]:
    line = line.strip()
    if line == "":
        continue

    parts = line.split(',')      # ["alice", "30", "23"]
    name = parts[0]
    pages1 = int(parts[1])
    pages2 = int(parts[2])

    total_pages = pages1 + pages2

    # accumulator pattern for dictionary
    if name in pages_dict:
        pages_dict[name] = pages_dict[name] + total_pages
    else:
        pages_dict[name] = total_pages

file1.close()

# print results
for name in pages_dict:
    print(name, "read", pages_dict[name], "pages")
