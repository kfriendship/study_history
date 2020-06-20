"""
1076 저항

저항 계산법에 따라 저항 값을 출력하는 문제

알고리즘: 구현
"""

import sys
read = sys.stdin.readline

color = {'black': 0, 'brown': 1, 'red': 2, 'orange': 3, 'yellow': 4, 'green': 5, 'blue': 6, 'violet': 7, 'grey': 8, 'white': 9}
result = color[read().strip()]*10
result += color[read().strip()]
result *= 10**color[read().strip()]
print(result)
