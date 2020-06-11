"""
11650 좌표 정렬하기

좌표들이 주어지면 정렬하자.

알고리즘: 정렬
"""

import sys
read = sys.stdin.readline

n = int(read())
pos = [tuple(map(int, read().split())) for _ in range(n)]
pos.sort()
for x, y in pos:
    print("{} {}".format(x, y))
