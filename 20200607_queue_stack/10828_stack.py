"""
10828 스택

스택을 구현
push X: X를 push
pop: stack pop 없으면 -1
size: len
empty: 비어있으면 1 아니면 0
top: 젤 위 출력 없으면 -1
"""

import sys
read = sys.stdin.readline

stack = []
for _ in range(int(read())):
    op = read().split()
    if 'pu' in op[0]:
        stack.append(op[1])
    elif 'po' in op[0]:
        if len(stack):
            print(stack.pop())
        else:
            print(-1)
    elif 'si' in op[0]:
        print(len(stack))
    elif 'em' in op[0]:
        print(int(len(stack) == 0))
    elif 'to' in op[0]:
        if len(stack):
            print(stack[-1])
        else:
            print(-1)
