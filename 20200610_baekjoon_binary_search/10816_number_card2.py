"""
10816 숫자 카드2

숫자 카드 n개 중에 정수 m개를 각각 몇개씩 가지고 있는지 출력

알고리즘: binary search

1. n개를 sort
2. 숫자를 하나씩 찾는데 찾으면 그 위아래로 같은 숫자가 있는지 확인
"""

from collections import Counter
import sys
read = sys.stdin.readline

n = int(read())
a = Counter(read().split())
m = int(read())

result = []
for q in read().split():
    if q in a:
        result.append(str(a[q]))
    else:
        result.append('0')

print(' '.join(result))
