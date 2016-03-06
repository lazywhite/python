import contextlib

# phrase before yield is like enter
# after 'yield' is like exit
@contextlib.contextmanager
def f():
    print('entered context')
    yield
    print('left context')

with f():
    print('doing something')

