# 15.
# In BlackJack, cards are counted with -1, 0, 1 values:
    # 2, 3, 4, 5, 6 are counted as +1
    # 7, 8, 9 are counted as 0
    # 10, j, q, k, a are counted as -1

# Write a function that takes a list called cards, counts the number, and returns it from the list of
# cards provided.
  
  # Examples:
        # count([5, 9, 10, 3, ”j”, ”a”, 4, 8, 5]) → 1,
        # count([ ”a”, ”a”, ”k”, ”q”, ”q”, ”j”]) → -6,
        # count([ ”a”, 5, 5, 2, 6, 2, 3, 8, 9, 7]) → 5

def count(cards):
    
    counter = 0

    for number in cards:
        if number in range(2, 6+1):
            counter = counter + 1
        elif number in range(7, 9+1):
            counter = counter + 0
        elif number == 10:
            counter = counter - 1
        else:
            counter = counter - 1
    result = counter    
    return result

cards1 = [5,9,10,3,'j','a',4,8,5]
cards2 = ['a','a','k','q','q','j']
cards3 = ['a',5,5,2,6,2,3,8,9,7]

print(count(cards1))
print(count(cards2))
print(count(cards3))
