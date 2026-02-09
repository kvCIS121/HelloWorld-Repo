#   Using a loop, write a program that prints every even number between 37 and 1050 (inclusively)
#   I used 38, because the first integer of the range will always be included and printed, so, 37 
#   is not an even number, so I went on ahead and started at 38, to 1050+1 to stop with inclusive 1050, 
#   and then STEP by 2 steps, which is why every even number prints

for number in range(38, 1050+1, 2): # RANGE(START, STOP, STEP)
    print(number)