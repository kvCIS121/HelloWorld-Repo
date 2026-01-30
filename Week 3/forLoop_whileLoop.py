
#add up all the odd numbers between 1 and 6 (exclusively: means do NOT include the endpoints, which are 1 and 6)

num = 2
total = 0

while num < 7: #in order to not include the endpoints, we have to set it to "less than < 7" and not "less than or equal to <= 7"
    if num % 2 == 1:
        total += num
    num += 1

print(f'total = {total}')


#use a For Loop to print all the numbers between 5 and 100 (inclusively)
#Built-in functions: 'range' => in Python, range(start, stop) this includes start, but not stop.
    #therefore, range(4,23) includes start of 4, but not integer 23
    #how to ask for HELP in python -> help(range)

#help(range)

for number in range(5,100+1): #reminder to add the +1 to include the endpoint b/c range doesn't include the stop(endpoint), only start
    if number % 2 == 0:
        print(number)

#notice we didn't declare the variable 'number' ahead of time. The For Loop declares it for us. It also controls the iteration


#---------------------
#print all even numbers between 5 to 100 (exclusively)
#number = 5 # instead of starting at 5, just start at 6, and add 2 since it's gona be each even number increment only

number = (5+1)
while number <= 100:
    print(number)
    number += 2

#--------------------

for number in range(6, 100+1, 2):
    print(number)
#   6 → starting value
#   100+1 → becomes 101, and since Python stops before the second number, it goes up to 100
#   2 → step size, so it jumps by 2 each time


#--------------------
total = 0
for number in range(2,7):
    if number % 2 == 1:
        total += number
print(f'total = {total}')
#--------------------

#let's ask a user for a number until they stop. once they do
#report the sum of the numbers they entered
#For Loops are not necessarily too good at Indeterminate operations

total = 0
for amount_of_time in range(0,10**100): #this asks the user for an input 10 times no matter if they just want to add 2 integers or all 10 in the range
user_input = input('enter a number: ')
if user_input != 'stop':    #if the user input is not equal to the word stop. basically as long as user doesn't type the word stop
    user_number = int(user_input)
    total += user_number 

#--------------------
#While Loop for Indeterminate operations: go on forever till commanded to stop
total = 0
done = False #creating a variable named done to 
#boolean operators = AND, OR, NOT

while not done:
    user_input = input('enter a number: ')
    if user_input == 'stop':
        done = True
    else:
        user_number = int(user_input) #notice we have to type cast, meaning identify USER_INPUT as an INT in order to ensure it's an integer to operate correctly
        total += user_number
print(f'total = {total}')

#--------------------

x=3
y=5

if x==3 and y==5:   #this is called Short Circuit Logic
    #definition:if python can evaluate the value of a boolean expression 
    #using AND, python will automatically evaluate the code but stop when it's found the first true or false search
    #i.e., if x == 3, it will no longer 