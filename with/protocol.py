# -*- coding: utf-8 -*-
#!/usr/bin/python



class Context(object):
    def __init__(self,name):
        self.name = name

    def __enter__(self):
        print('entering the zone')
        return self

    def __exit__(self,exception_type,exception_value,exception_traceback):
        if exception_type is None:
            print('leaving with no error')
        else:
            print("leaving with %s" % exception_value)

with Context('bob') as f:
    print(f.name)
    raise StopIteration('what')
