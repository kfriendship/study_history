"""
10989 수 정렬하기 3

중복되는 작은 수들을 정렬하라.

알고리즘: sorting
"""
import sys
read = sys.stdin.readline

n = int(read())
nums = {}
for _ in range(n):
    v = int(read())
    if v in nums:
        nums[v] += 1
    else:
        nums[v] = 1

for key in sorted(nums.keys()):
    print('\n'.join([str(key)]*nums[key]))
