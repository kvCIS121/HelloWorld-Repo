human_age = int(input('Enter your age: '))
humanAge_n_horseAge = 3 * (((human_age **2 -47)/7)+12)
print(f'You are {human_age} yrs old, but in horse years, you are {round(humanAge_n_horseAge, 1)} yrs old')

ageMonths = humanAge_n_horseAge
ageMonths -= int(humanAge_n_horseAge)
ageMonthsFinal = ageMonths * 12
print(ageMonthsFinal)