"""队列和栈"""

from collections import deque

deq = deque('abcdefg')
print([item.upper() for item in deq])  # ['A', 'B', 'C', 'D', 'E', 'F', 'G']
deq.append('h')
print([item.upper() for item in deq])  # ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
deq.appendleft('x')
print([item.upper() for item in deq])  # ['X', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
print(deq.pop())
print(deq.popleft())
deq.clear()
