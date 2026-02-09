#    What type of code this is
# - Beginner Python programming
# - Nested loop logic
# - Pattern‑printing / shape‑generation
# - Console‑based output formatting
# - input handling, loops, and pattern construction



width = int(input('enter a width: '))
length = int(input('enter a length: '))
pattern = input('enter a pattern: ')

for rows in range(1, width + 1):
    for columns in range(1, length + 1):    
        print(pattern, end = "")# "end = " "  lets the cursor stays on the same line, letting the next print continue right beside it
    print() #   a separate print() (with nothing inside) moves to the next line when you want to start a new row.


    
