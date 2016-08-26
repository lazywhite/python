#!/usr/bin/env python
# unpacking a sequnce into seperate variables
a, b, c = (1, 2, [1,2,3])
a, b, *c = range(10)
a, *b, c = range(10)

# variable function parameters
def f(a, *args): # type(args) --> list
    pass

def f(a, **kwargs): # type(kwargs) --> dict
    pass

