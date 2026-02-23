# To train for an upcoming marathon, Samuel goes on one long-distance run each Saturday. He wants
# to track how often the number of miles he runs fall short of the previous Saturday. This is called a
# lag day. Write a function that takes in a list of miles run every Saturday and returns Samuel’s total
# number of lag days

# Examples:
    # lag days([5, 3, 2, 1]) → 3, (3 lag days, day2 since (3<5), day3 since (2<3), and day4 since (1<2))
    # lag days([10, 11, 12, 9, 10]) → 1,
    # lag days([6, 5, 4, 3, 2, 9]) → 4,
    # lag days([9, 9]) → 0


def lag_days(runs):
    lag_days = 0

    for i in range(len(runs)-1):
       if runs[i] > runs[i+1]:
        lag_days = lag_days + 1
    return lag_days
    
run_record_1 = [5, 3, 2, 1]
run_record_2 = [10, 11, 12, 9, 10]
run_record_3 = [6, 5, 4, 3, 2, 9]
run_record_4 = [9, 9]

print(lag_days(run_record_1))
print(lag_days(run_record_2))
print(lag_days(run_record_3))
print(lag_days(run_record_4))
