# 13. Write a function that takes a list of fruits and returns the total caloric value of the fruits consumed.
# You may use the following dictionary named calories:
#   - calories = { ”apple” : 95, ”banana” : 105, ”orange” : 62, ”grape” 3, ”pear” : 102}
# 
# Hint: You can calculate the total calories by summing up the caloric values of all valid fruits in the
# list. You may assume the calories dictionary is defined in your code. You don’t need to rewrite it.
    # Examples:
        # total_calories([ ”apple”, ”banana”, ”orange”]) → 262 (since 95 + 105 + 62 = 262)
        # total_calories([ ”grape”, ”grape”, ”grape”, ”grape”, ”grape”]) → 15
        # total_calories([ ”banana”, ”pear”, ”apple”]) → 302

def total_calories(lysts):
  result = 0

  for fruit in lysts:
    if fruit in calories_dictionary:
       result = result + calories_dictionary[fruit]
  return result
   
calories_dictionary = { 'apple' : 95, 'banana' : 105, 'orange' : 62, 'grape' : 3, 'pear': 102}

lyst_1 = ([ 'apple', 'banana', 'orange'])
lyst_2 = ([ 'grape', 'grape', 'grape', 'grape', 'grape'])
lyst_3 = ([ 'banana', 'pear', 'apple'])

print(total_calories(lyst_1))
print(total_calories(lyst_2))
print(total_calories(lyst_3))
