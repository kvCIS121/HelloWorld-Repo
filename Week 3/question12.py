knuts = int(input('enter amount of knuts: '))
k = 29  # constant, number of knuts ratio: 29 knuts per 1 sickle
s = 17  # constant, number of sicles ratio: 17 sickles per 1 galleon

    #sickles calculations
knuts_to_sickles = (knuts/k)    #product; the formula to convert to sickles given knuts => x_sickles = (knuts/29)
output_knuts = round(((knuts_to_sickles) - int(knuts_to_sickles)) * k)    # (float product - int product) * 29 = formula to print the remaining Knuts. rounds the value to nearest whole number
outpt_sickles = int(knuts_to_sickles - (output_knuts/k)) #takes the product - fractional value = whole integer for the number of sickles for each 29 given knuts (1.103 - 0.103 = 1 sickle...) I had to divide by k (29) to cancel it from the output_knuts formula
  
    #galleons calculations
knuts_to_galleon_formula = (knuts)*(1/29)*(1/17)  # => [knuts * (1 sickle/29 knuts) (1 galleon/17 sickles)] = x_galleons
decimal_of_galleons = (knuts_to_galleon_formula) - int(knuts_to_galleon_formula)  #=> float(1.103) - int(1.103) = 0.103
number_of_galleons = int(knuts_to_galleon_formula - decimal_of_galleons)   # 1.103 - 0.103 = 1 galleon (whole integer)

galleons_to_sickles_formula = round((decimal_of_galleons) * (s/1)) #galleons -> sickles formula = galleons (17 sickles/1 galleon)
decimal_of_sickles = galleons_to_sickles_formula - int(galleons_to_sickles_formula) # float(1.758 sickles) - int(1) = 0.758 sickles 
number_of_sickles = int(galleons_to_sickles_formula - decimal_of_galleons)  # 1.758 sickles - 0.758 sickles = 1 sickles
sickles_to_knuts_formula = round(number_of_sickles * (k/1))    # x_sickles * (29 knuts/1 sickles) = x_number_of_knuts

if knuts <= 32:
    print(f'given {knuts} knuts, output {outpt_sickles} sickles, {output_knuts} knuts')
elif knuts >= 33 and knuts <= 544:
    print(f'given {knuts} knuts, output {number_of_sickles} sickles, {galleons_to_sickles_formula} galleons and {sickles_to_knuts_formula} knuts')
else:
    print(f'given {knuts} knuts, output {number_of_sickles} sickles, {number_of_galleons} galleons and {galleons_to_sickles_formula} knuts')