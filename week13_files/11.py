file1 = open('SongPlays.txt', 'r')

lines = file1.readlines()

songs_dict = {}

# skip the header row
for line in lines[1:]:
    line = line.strip()
    if line == "":
        continue

    parts = line.split()      # ["alice", "5"]
    name = parts[0]
    plays = int(parts[1])

    # accumulator pattern for dictionary
    if name in songs_dict:
        songs_dict[name] = songs_dict[name] + plays
    else:
        songs_dict[name] = plays

file1.close()

# print results
for name in songs_dict:
    print(name, "played", songs_dict[name], "times")
