"""
2108 통계학

1. 평균
2. 중앙값
3. 가장 먆이 등장하는 값, 여러개면 두번째로 작은 값
4. 최대값-최소값

알고리즘: 정렬?
"""

from collections import Counter
import sys
read = sys.stdin.readline

n = int(read())
nums = [int(read()) for _ in range(n)]
nums.sort()

print(round(sum(nums)/n))
print(nums[n//2])

cnter = Counter(nums)
max_count = max(cnter.values())
nums_count = list(filter(lambda x: x[1] == max_count, cnter.items()))
if len(nums_count) == 1:
    print(nums_count[0][0])
else:
    print(nums_count[1][0])

print(nums[-1]-nums[0])
