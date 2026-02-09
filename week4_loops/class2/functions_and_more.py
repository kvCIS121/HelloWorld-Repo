def even_printer(lower_bound, upper_bound):
    for number in range(lower_bound, upper_bound+1):    #use the different ranges here (2,10), (3,15), and (7, 20)
        if number % 2 == 0:
            print(number)

even_printer(2,10)
even_printer(3,15)
even_printer(7,20)

#Functions are abstract tools

#f(x) = 3x+1
#we want this function to be repeated over and over, using For Loop

#keyword => def: definintion 


#      TEMPLATE FOR FUNCTION
# def function_name(parameters):
#     what you want your function to do

#exampl_1


def letter_count_in_word():
    count = 0

    for letter in word:
        if letter == "l":
            count += 1
    print(f'the number of {test_letter}s in a {word} is {count}')

    
#----<>
# 
     
for number in range(5, 100+1):
    if number % 2 == 0:
        number +=1

#++++


while number <= 100:
    if number % 2 == 0:
        print(number)
    number = number + 1

