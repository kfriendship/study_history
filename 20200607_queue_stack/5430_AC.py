"""
5430 AC

R은 뒤집고 D는 맨앞을 버린다.

알고리즘: 큐
"""

from collections import deque
import sys
read = sys.stdin.readline

for _ in range(int(read())):
    p = read().strip()
    n = int(read())
    x = read().strip()[1:-1].split(',')
    if x == ['']: x = []
    q = deque(x)
    direction = True

    error = False
    for op in p:
        if op == 'R':
            direction = not direction
        else:
            if len(q):
                if direction:
                    q.popleft()
                else:
                    q.pop()
            else:
                print("error")
                error = True
                break

    if not error:
        if not direction:
            q.reverse()
        print("[{}]".format(",".join(q)))