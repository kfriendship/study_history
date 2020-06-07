"""
큐 2

큐에 관련된 여러가지 연산들을 구현한다.
push X: X를 큐에 push
pop: 가장 앞에 있는 정수 pop하고 출력. 없으면 -1
size: 큐 길이 출력
empty: 비어있으면 1 아니면 0
front: 맨앞 출력 없으면 -1
back: 맨뒤 출력 없으면 -1

알고리즘: 큐
"""
from collections import deque
import sys
read = sys.stdin.readline

q = deque()
for _ in range(int(read())):
    op = read().strip()
    if "push" in op:
        op, x = op.split()
        q.append(x)
    elif op == "pop":
        if len(q):
            print(q.popleft())
        else:
            print(-1)
    elif op == 'size':
        print(len(q))
    elif op == 'empty':
        print(int(len(q) == 0))
    elif op == 'front':
        if len(q):
            print(q[0])
        else:
            print(-1)
    elif op == 'back':
        if len(q):
            print(q[-1])
        else:
            print(-1)
