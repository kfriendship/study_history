"""
1654 랜선 자르기

여러 길이의 랜선을 같은 길이로 잘라 가장 길면서 n개의 랜선을 만들자.

알고리즘: binary search

1. start는 0 end는 가장 작은 랜선 길이
2. 바이너리 서치로 랜선길이를 찾자.
"""

import sys
read = sys.stdin.readline

k, n = map(int, read().split())
lans = [int(read()) for _ in range(k)]


def binary_search(target):
    start, end = 1, max(lans)

    while start <= end:
        mid = (start+end)//2
        cnt = 0
        for lan in lans:
            cnt += lan // mid

        if cnt >= target:
            start = mid+1
        else:
            end = mid-1

    return end


print(binary_search(n))
