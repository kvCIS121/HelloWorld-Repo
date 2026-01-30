# 2nd Pass session, we learned the following:
#   "//": Floor Division = divides two integers and returns the lowest whole integer 
#   "%" : Modulus => divides two integers and returns only the REMAINDER value
#   print(int('55') + 2)) = will change the datatype of the STRING 55 to INT and add 55 + 2 = 57

print(5 % 2)
print(5 // 2)
print(int('55') + 2) #putting INT in front of the string 55 changes the data type to INTEGER, hence why 55 +2 = 57

x = -11
y = 2
print(x // y) # -11 floor divide by 2 = 12 because 11 / 2 = 5.5, but it will round DOWN to lowest value, 
#                   and, -6 is lower than -5.5, cus -5.0 is higher, so -6 is the answer 
#                   Think about the number line=>  -6, -5, -4, -3... 0 ... 3, 4, 5, 6

