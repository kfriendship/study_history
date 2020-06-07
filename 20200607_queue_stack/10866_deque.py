"""
10866 덱

덱을 구현하라.
push_front x: x를 덱의 앞에 넣기
push_back x: x를 덱의 뒤에 넣기
pop_front: 덱 앞의 수 빼는데 없으면 -1
pop_back: 덱 뒤에 수 빼는데 없으면 -1
size: size 출력
empty: 비어있으면 1 아니면 0
front: 덱 앞 수 출력 없으면 -1
back: 덱 뒤 수 출력 없으면 -1

알고리즘: 덱
"""

from collections import deque
import sys
read = sys.stdin.readline

q = deque()
for _ in range(int(read())):
    op = read().split()
    if "h_f" in op[0]:
        q.appendleft(op[1])
    elif "h_b" in op[0]:
        q.append(op[1])
    elif "p_f" in op[0]:
        if len(q):
            print(q.popleft())
        else:
            print(-1)
    elif "p_b" in op[0]:
        if len(q):
            print(q.pop())
        else:
            print(-1)
    elif "si" in op[0]:
        print(len(q))
    elif "em" in op[0]:
        print(int(len(q) == 0))
    elif op[0] == "front":
        if len(q):
            print(q[0])
        else:
            print(-1)
    elif op[0] == 'back':
        if len(q):
            print(q[-1])
        else:
            print(-1)
