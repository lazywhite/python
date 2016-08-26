def dedup(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)

a= [1,2,2,3,3,4,5]
b = dedup(a)
# type(b) --> generator
print(list(b))
print(list(dedup(a)))


def dedupe(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield val
            seen.add(val)

a = [ {'x':1, 'y':2}, {'x':1, 'y':3}, {'x':1, 'y':2}, {'x':2, 'y':4}]
b = list(dedupe(a, key=lambda d: (d['x'],d['y'])))
c = list(dedupe(a, key=lambda d: d['x']))
print(b,c)
