import weakref

class Expensive:
    def __del__(self):
        print('deleting {!r}'.format(self))

obj = Expensive()

r = weakref.ref(obj)

print('obj:', obj)
print('ref:', r)
print('r():',r())
print(r() is obj)
print(obj.__weakref__)
print(obj.__weakref__())

a = weakref.proxy(obj)
print(a)
print(a is obj)

del obj

