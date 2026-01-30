# 1 human year = 9 cat years => human age in cat years is (1/9) * human age
# 12 months in 1 yr; 30 days average in a month

human_age_in_catYears = (1/9) * float(input("Enter your age: "))
ha_n_catYears = human_age_in_catYears 

human_age_in_catMonths = (ha_n_catYears - int(ha_n_catYears)) * 12
ha_n_catMonths = human_age_in_catMonths

human_age_in_catDays = (human_age_in_catMonths - int(human_age_in_catMonths)) * 30


a = ha_n_catYears - int(ha_n_catYears)
b = ha_n_catMonths - int(ha_n_catMonths)
c = human_age_in_catDays - int(human_age_in_catDays)

print(f"{float(ha_n_catYears - a)} years, {float(ha_n_catMonths - b)} months, and {float(human_age_in_catDays  - c)} days")
