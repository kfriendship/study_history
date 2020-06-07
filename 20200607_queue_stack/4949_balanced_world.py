"""
4949 균형잡힌 세상

문자열의 괄호가 잘 짝지어졌는지 알아보는 문제

알고리즘: 스택
"""

import sys
read = sys.stdin.readline

s = read()

while s != '.\n':
    ps = filter(lambda x: x in ['(', ')', '[', ']'], list(s))

    stack, result = [], 'yes'
    for c in ps:
        if c in ['(', '[']:
            stack.append(c)
        elif c in [')', ']']:
            if not stack:
                result = 'no'
                break
            v = stack.pop()
            if (v == '(' and c == ')') or (v == '[' and c ==']'):
                pass
            else:
                result = 'no'
                break
    if stack:
        result = 'no'
    print(result)

    s = read()
