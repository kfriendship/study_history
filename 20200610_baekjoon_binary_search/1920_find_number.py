"""
1920 수 찾기

N개의 정수에서 X가 존재하는지 찾자.

알고리즘: binary search

1. 정렬한 후 이분탐색하기

1. 그냥 찾기? X
"""

import sys
read = sys.stdin.readline

n = int(read())
a = list(map(int, read().split()))
m = int(read())
question = list(map(int, read().split()))

a.sort()


def binary_search(target):
    start, end = 0, n-1

    while start <= end:
        mid = (end + start) // 2
        if target < a[mid]:
            end = mid - 1
        elif target > a[mid]:
            start = mid + 1
        else:
            break
    return int(target == a[mid])


for q in question:
    print(binary_search(q))
