"""
10773 제로

숫자가 나오면 스택에 넣고
0이 나오면 스택에서 팝한다.

알고리즘: 스택
"""

import sys
read = sys.stdin.readline

stack = []
for _ in range(int(read())):
    v = int(read())
    if v != 0:
        stack.append(v)
    else:
        stack.pop()
print(sum(stack))
