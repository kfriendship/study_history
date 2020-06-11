"""
11651 좌표 정렬하기2

좌표들이 주어지면 정렬하자. 반대로 y증가 x증

알고리즘: 정렬
"""

import sys
read = sys.stdin.readline

n = int(read())
pos = []
for _ in range(n):
    x, y = map(int, read().split())
    pos.append((y, x))
pos.sort()
for x, y in pos:
    print("{} {}".format(y, x))
