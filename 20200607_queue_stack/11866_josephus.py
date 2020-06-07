"""
11866 요세푸스 문제 0

1부터 n까지 사람이 원으로 앉아있고
k번째 사람을 제거한다.
그후 그 다음사람을 기준으로 다시 k번째 사람을 제거한다.
모두 제거된 순서를 출력

알고리즘: 큐

1. 큐에서 하나씩 꺼내며 k번째라면 제거한다.
"""

from collections import deque
import sys
read = sys.stdin.readline

n, k = map(int, read().split())
q = deque(range(1, n+1))
cnt, result = 1, []
while q:
    v = q.popleft()
    if cnt == k:
        result.append(v)
        cnt = 0
    else:
        q.append(v)
    cnt += 1

print("<{}>".format(", ".join(map(str, result))))
