human_age_in_dogAge = 7 * float(input("Enter your age: "))
ha_n_dogAge = human_age_in_dogAge

human_age_in_dogMonths = ((ha_n_dogAge) - (int(ha_n_dogAge))) * 12
ha_n_dogMonths = human_age_in_dogMonths

human_age_in_dogDays = ((ha_n_dogMonths) - int(ha_n_dogMonths)) * 30
ha_n_dogDays = human_age_in_dogDays

a = ha_n_dogAge - int(ha_n_dogAge)
b = ha_n_dogMonths - int(ha_n_dogMonths)
c = ha_n_dogDays - int(ha_n_dogDays)

print(f"Your age in dog years is: {float(ha_n_dogAge - a )} years, {float(ha_n_dogMonths - b )} months, and {float(ha_n_dogDays - c )} days.")