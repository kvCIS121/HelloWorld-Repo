def greeting(name, age):
    print(f'hello {name} it is cool being {age} years old')

greeting('ashley', 35)

# if they don't put in their age, and only their name, do this:

def greeting(name):
    print(f'hello {name}, how old are you?')

greeting('ashley')

# but this is not correct

# let's say we pass this argument


# the reason this doesn't work is b/c the first greeting got overwritten by the 
# second one b/c they have same defined function names, therefore,
# compiler takes the 2nd one that has the same name, but with only one argument 
# since the parameter in the function only has one formal parameter as well

# To give a parameter a DEFAULT value if it's unk and we just want 'something':
# then let it equal 0, 'unk', etc as follows:

def greeting(name, age = 'unk'):
    print(f'hello {name}, it is cool being {age} yrs old')

greeting('dexter')

# just note that if you DO give it an argument, the argument will 
# notice this prints the default parameter = 'unk', so age is 'unk'
# We MUST still pass a 'name' though

def greeting(name = input('enter your name: '), age = input('enter your age: ')):
    print(f'hello {name}, it is cool being {age} yrs old')

greeting()

# go research ARGS* (arguments) and KWARGS* (key word arguments), this will help you understand
# how to return the arguments as a LIST, and not as a parameter if we decided to do this:
