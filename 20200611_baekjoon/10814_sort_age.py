"""
10814 나이순 정렬

나이순으로 정렬하고 나이가 같으면 입력순으로 정렬한다.

알고리즘: 정렬
"""

import sys
read = sys.stdin.readline

n = int(read())
people = []
for i in range(n):
    age, name = read().split()
    people.append((int(age), i, name))
people.sort()
for age, _, name in people:
    print("{} {}".format(age, name))
