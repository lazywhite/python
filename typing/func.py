from typing import Callable


def addOne(v: int) -> int:
    return v + 1

def f(a: int, b: Callable[[int], int]):
    return b(a)


b = f(10, addOne)
print(b)

