# a)
# if boolean_A:
#    block x
# if boolean_B:
#    blocky y

# This one is just performing the program/code in sequence, line by line. It doesn't care if the first condition
# was true or not. It proceeds either way.

# b)
# if boolean_A:
#    block x
# elif boolean_b:
#    block yield

# This one is first performing the first line of code, boolean_A, but if it's
# not true, then it will resort to/ execute the ELIF line