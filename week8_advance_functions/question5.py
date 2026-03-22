# 5. Luke Skywalker has friends and family, but he is getting older and having trouble remembering them
# all. Write a function that will return the relation defined in the table below. The arguments to
# the function will be name (name of the person related to Luke), if no argument is provided then the
# default should be nothing. That is, the empty word ” ”.

# Person Relation
# Darth Vader Father
# Leia Sister
# Han Brother in law
# R2D2 Droid

# *If he types any other name, return ”unknown”.

# Examples:
# find_relation( ”Darth Vader”) → ”Father”,
# find_relation( ”R2D2”) → ”Droid”,
# find_relation( ”Jabba the Hutt”) → ”Unknown”
# find_relation( ) → ”Unknown”

def find_relation(name = ''):

    if name == '':
        return 'unknown'
    
    if name == 'darth vader':
        relation = relationship['darth vader']
    elif name == 'leia':
        relation = relationship['leia']
    elif name == 'han':
        relation = relationship['han']           
    elif name == 'r2d2':
        relation = relationship['r2d2']
    else:
        relation = 'unknown'
    return relation  

name = input('enter a name: ')

relationship = ({'darth vader': 'father', 'leia': 'sister', 'han': 'bro n law', 'r2d2': 'droid'})
print(find_relation(name))