# 3. Write a function that returns the number of copies of the same number. 
# The arguments for the function will be num_1 (first number), num_2 (second number), and num_3 (third number), 
# if no argument is provided then the default for all 3 values should be 0.
    # 
    # Examples:
        # count_duplicates(2, 3, 2) → ”There are 2 of the same number”,
        # count_duplicates(4, 4, 4) → ”There are 3 of the same number”,
        # count_duplicates(1, 2, 3) → ”Each number is unique”
        # count_duplicates(1) → ”There are 2 of the same number”
        # count_duplicates(0) → ”There are 3 of the same number”

def count_duplicates(num1 = 0 , num2 = 0, num3 = 0):
    count = {}
    numbers = [num1, num2, num3]

    for n in numbers: 
        if n in count:
            count[n] += 1
        else:
            count[n] = 1
    
    max_count = 0
    for key in count:
        if count[key] > max_count:
            max_count = count[key]
    
    if max_count == 1:
        return 'each number is unique'
    else:
        return f'there are {max_count} of the same number'


numbers_lyst = (2, 3, 2)
print(count_duplicates(numbers_lyst[0], numbers_lyst[1], numbers_lyst[2]))