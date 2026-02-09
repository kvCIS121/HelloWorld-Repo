larger = float(input('enter a number: '))
smaller = float(input('enter a number: '))
count = 0

while larger >= smaller:
    print(f'larger number is {round(larger, 1)}, smaller number is {round(smaller, 1)}')

    larger = larger / 2
    count += 1
    
    print('')
    print(f'the number of times larger can be divided by smaller is: {count}')


#+++++-----<>

#+++++-----<>   Original Program 

larger = float(input('enter a number: '))   #note: use "1e9" for 10 x 10^9 = 1,000,000,000 b/c (10**)
smaller = float(input('enter a number: '))
count = 0   #count is just a variable to help keep track of how many times program iterates

  #number initially is 100
while larger >= smaller:    #while larger is greater than or equal to smaller

    print(f'value of larger is {larger}, and smaller is {smaller}')   #print initial value of larger, 1000
    larger /= 2     #divide larger by 2 => read as, "larger = larger divide by 2"
    count += 1      #this is 'counter' => adds 1 to count everytime the iteration is run thru. keeps track how many times larger is getting halved
    print(f'this is how many times larger can be halved when still >= smaller: {count}')   





#+++++-----<>   Alternate Program to simply round the {larger} and {smaller} values to 1 decimal for cleaner print 

larger = float(input('enter a number: '))   #note: use "1e9" for 10 x 10^9 = 1,000,000,000 b/c (10**)
smaller = float(input('enter a number: '))
count = 0   #count is just a variable to help keep track of how many times program iterates

  #number initially is 100
while larger >= smaller:    #while larger is greater than or equal to smaller

    print(f'value of larger is {round(larger, 1)}, and smaller is {round(smaller, 1)}')   #print initial value of larger, 1000
    larger /= 2     #divide larger by 2 => read as, "larger = larger divide by 2"
    count += 1      #this is 'counter' => adds 1 to count everytime the iteration is run thru. keeps track how many times larger is getting halved
    print(f'this is how many times larger can be halved when still >= smaller: {count}')   


#another way to round the intial input of an integer:
#   larger = round(float(input('enter a number: ')), 1) notice how round was set at start of variable
