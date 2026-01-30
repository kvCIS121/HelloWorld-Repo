import math

pi = math.pi
human_age = int(input('Enter your age: '))
humanAge_n_horseAge =  3 * (((human_age **2 -47) / 7)+12) # Human age in horse years = 77.5714

years = humanAge_n_horseAge - int(humanAge_n_horseAge) # Takes 77.5714 - 77.0 = 0.5714 
months = years * 12 # Takes 0.5714 * 12 months = 6.8571 months 
b = months - int(months) # Takes 6.8571 - 6.0 = 0.8571 
days = b * 30 # Takes 0.8571 * 30 days = 25.7142 days
c = days - int(days) # Takes 25.7142 - 0.7142

years_final = humanAge_n_horseAge - years # Takes 77.5714 - 0.5714 = 77.0 YEARS
months_final = months - b # Takes 6.8571 - 0.8571 = 6.0 MONTHS
days_final = days - c # Takes 25.7142 - 0.7142 = 25.0 DAYS

print(f'Your age in horse years is {years_final} years, {months_final} months, and {days_final} days.')
