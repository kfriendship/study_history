"""
1427 소트인사이드

숫자가 주어지면 그 숫자를 내림차순으로 솔팅하자.

알고리즘: 정렬

1. 숫자를 받아서 문자열로 바꾸자.
2. 솔팅하자.
"""

import sys
read = sys.stdin.readline

print("".join(sorted(read().strip(), reverse=True)))
