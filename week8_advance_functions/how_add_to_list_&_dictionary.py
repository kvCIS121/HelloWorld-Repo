#   How to add to a  LIST -> []
#   use .append
#   Example:

lyst = [1,2,3]
lyst.append(4)
print(lyst)

#   If you want to add MULTIPLE items to the List and update it same time, then add
#   to the list by using a list of the values to be added, i.e., however, this includes the
#   square brackets, which is why the new list is: [1, 2, 3, 4, [4, 5, 6, 7, 8, 9, 10]] UNLESS we use
# .extend -> lyst.extend (but we don't want to use this buitl-in function)

lyst.append([4,5,6,7,8,9,10])
print(lyst)



#   How to add to a Dictionary

def shoes(types):
    brand = {'nike':65}    # initial dictionary
    brand['new balance']=80 # adding to the dictionary
    return brand

print(shoes('brand'))