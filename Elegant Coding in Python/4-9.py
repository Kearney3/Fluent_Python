"""使用__slot__提高性能"""
from timeit import timeit


class WithSlots:
    __slots__ = "foo"

class WithoutSlots:
    pass

with_slots = WithSlots()
without_slots = WithoutSlots()

print((timeit("with_slots.foo = 1", globals=globals())))
print((timeit("without_slots.foo = 1", globals=globals())))

