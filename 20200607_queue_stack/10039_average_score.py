"""
10039 평균점수
"""

import sys
read = sys.stdin.readline

student = [int(read()) for _ in range(5)]
student = list(map(lambda x: x if x >= 40 else 40, student))
print(sum(student)//5)
