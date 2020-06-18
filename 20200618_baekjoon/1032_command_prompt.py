"""
1032 명령 프롬프트

문자열들을 받아 정규식처럼 표현하는 문제

알고리즘: 문자열
"""

import sys
read = sys.stdin.readline

n = int(read())
files = [read().strip() for _ in range(n)]
result = list(files[0])
for filename in files[1:]:
    for i, (c1, c2) in enumerate(zip(result, filename)):
        if c1 != c2:
            result[i] = '?'
print(''.join(result))
