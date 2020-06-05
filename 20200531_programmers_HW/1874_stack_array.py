"""
1874 스택 수열

1-n까지 수를 stack에 push했다가 pop함으로써 주어진 수열을 만들 수 있는지 출력하라.

알고리즘: 스택

1. 입력받고
2. 1-n을 입력하는데
    1. 주어진 수열과 넣고 아니면 넣었다가 빼기
"""

import sys
read = sys.stdin.readline

n = int(read())
s, op = [], []
cnt = 1
for i in range(n):
    num = int(read())
    while cnt <= num:
        s.append(cnt)
        op.append('+')
        cnt += 1
    if s[-1] == num:
        s.pop()
        op.append('-')
    else:
        print("NO")
        exit()
print("\n".join(op))
