"""
10816 숫자 카드2

숫자 카드 n개 중에 정수 m개를 각각 몇개씩 가지고 있는지 출력

알고리즘: binary search

1. n개를 sort
2. 숫자를 하나씩 찾는데 찾으면 그 위아래로 같은 숫자가 있는지 확인
"""

import sys
read = sys.stdin.readline

n = int(read())
a = list(map(int, read().split()))
m = int(read())

a.sort()


def binary_search(target):
    start, end = 0, n-1

    while start <= end:
        mid = (start+end) // 2
        if target == a[mid]:
            break
        elif target < a[mid]:
            end = mid-1
        else:
            start = mid+1

    return mid, target == a[mid]


def binary_search_(start, end, target):
    if start > end:
        return -1
    mid = (start+end) // 2
    if target == a[mid]:
        return mid
    elif target < a[mid]:
        return binary_search_(start, mid-1, target)
    else:
        return binary_search_(mid+1, end, target)


result = []
for q in map(int, read().split()):
    idx = binary_search_(0, n-1, q)
    if idx != -1:
        cnt, now_idx = 1, idx-1
        while 0 <= now_idx < n and q == a[now_idx]:
            cnt += 1
            now_idx -= 1

        now_idx = idx+1
        while 0 <= now_idx < n and q == a[now_idx]:
            cnt += 1
            now_idx += 1

        result.append(str(cnt))
    else:
        result.append('0')
print(" ".join(result))
