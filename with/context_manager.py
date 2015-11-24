import contextlib

@contextlib.contextmanager
def f():
    print('entered context')
    yield
    print('left context')

with f():
    print('doing something')


# nesting context
# not in PY3

#@contextlib.contextmanager
#def make_context(name):
#    print('entering {}'.format(name))
#    yield name
#    print('leaving {}'.format(name))


#with contextlib.nested(make_context('A'),make_context('B')) as (A, B):
#    print('inside A>B context')
