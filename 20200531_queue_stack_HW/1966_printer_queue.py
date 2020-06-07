"""
1966 프린터 큐

1. 현재 queue 가장 앞문서의 중요도 확인
2. 나머지 문서들중 현재 문서보다 중요도가 높은 문서가 있으면 이 문서를 queue 맨뒤에 위치
    1. 없으면 인쇄

알고리즘: 큐

1. q를 팝해서 얻은 값이 queue 전체 max와 같거나 크다면 인쇄
    1. 아니면 뒤로 넣기
"""
import sys
from collections import deque

read = sys.stdin.readline
for _ in range(int(read())):
    n, m = map(int, read().split())
    q_list = list(map(int, read().split()))
    q = deque()
    for i, important in enumerate(q_list):
        q.append((important, i == m))

    time = 1
    while q:
        important, target = q.popleft()
        if important >= max(q_list):
            if target:
                print(time)
                break
            q_list.remove(important)
            time += 1
        else:
            q.append((important, target))
