# 17.
# To train for an upcoming marathon, Johnny goes on one long-distance run each Saturday. He wants to
# track how often the number of miles he runs exceeds the previous Saturday. This is called a progress
# day. 

# Write a function that takes in a list of miles run every Saturday and returns Johnny’s total
# number of progress days.

# Examples:
    # progress_days([3, 4, 1, 2]) → 2, (Two progress days, day 2 since (4 > 3) and day 4 since (2 > 1))
    # progress_days([10, 11, 12, 9, 10]) → 3,
    # progress_days([6, 5, 4, 3, 2, 9]) → 1,
    # progress_days([9, 9]) → 0

def progress_days(runs):
    total_progress_days = 0
    
    for i in range(len(runs)-1):
        if runs[i] < runs[i+1]:
            total_progress_days = total_progress_days + 1
    
    return total_progress_days
    
miles_run_1 = [3, 4, 1, 2]
miles_run_2 = [10, 11, 12, 9, 10]
miles_run_3 = [6, 5, 4, 3, 2, 9]
miles_run_4 = [9, 9]

print(progress_days(miles_run_1))
print(progress_days(miles_run_2))
print(progress_days(miles_run_3))
print(progress_days(miles_run_4))