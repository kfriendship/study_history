"""
9012 괄호

올바른 괄호인지 아닌지 판단하라.

알고리즘: 스택

1. 왼쪽 괄호면 스택에 넣고 오른쪽 괄호면 스택에 있던 것을 pop한다.
2. 스택에 아무것도 없는데 pop하기를 바라면 no 문자열이 끝나는데 pop을 원하면 no
3. 다 아니면 yes
"""

import sys
read = sys.stdin.readline

for _ in range(int(read())):
    case = read().strip()

    result = 'YES'
    stack = []
    for c in case:
        if c == '(':
            stack.append(c)
        else:
            if stack:
                stack.pop()
            else:
                result = 'NO'
                break
    if stack:
        result = 'NO'
    print(result)
