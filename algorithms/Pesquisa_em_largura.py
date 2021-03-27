from collections import deque


variavel = deque()
variavel.appendleft(5)
variavel.appendleft(6)
variavel.popleft()
print(variavel[0])