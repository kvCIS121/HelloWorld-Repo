# 14. Write a function that takes a list of ingredients and returns the total cost of making a recipe. You
# may use the following dictionary named prices:

    # prices = { ”flour” : 2.50, ”sugar” : 1.80, ”eggs” : 3.00, ”milk” : 2.00, ”butter” : 2.75, ”vanilla” :
    # 4.50, ”chocolate” : 5.00 }
# 
# Hint: You can calculate the total cost by summing up the prices of all valid ingredients in the list. You
# may assume the prices dictionary is defined in your code. You don’t need to rewrite it.
    # Examples:
        # total_cost([ ”flour”, ”sugar”, ”eggs”, ”butter”]) → 10.05
        # total_cost([ ”milk”, ”vanilla”, ”chocolate”]) → 11.50
        # total_cost([ ”eggs”, ”eggs”, ”flour”, ”sugar”]) → 10.30

def total_cost(recipes):
    total = 0

    for ingredients in recipes:
        if ingredients in ingredients_dictionary:
            total = total + ingredients_dictionary[ingredients]
    return total

ingredients_dictionary = {'flour':2.50, 'sugar':1.80, 'eggs':3.00, 
                          'milk':2.00, 'butter':2.75, 'vanilla':4.50, 'chocolate':5.00}

recipe_lyst_1 = (['flour', 'sugar', 'eggs', 'butter'])
recipe_lyst_2 = (['milk', 'vanilla', 'chocolate'])
recipe_lyst_3 = (['eggs', 'eggs', 'flour', 'sugar'])

print(total_cost(recipe_lyst_1))
print(total_cost(recipe_lyst_2))
print(total_cost(recipe_lyst_3))