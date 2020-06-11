"""
1181 단어정렬

단어들이 들어오면 정렬하라.
1. 짧은 순으로
2. 알바펫 순으로

알고리즘: 정렬

1. length기준으로 dictionary 만들기
2. length가 작은순대로 가져와서 문자열 솔팅
"""

import sys
read = sys.stdin.readline

n = int(read())
words = {}
for _ in range(n):
    word = read().strip()
    length = len(word)
    if length not in words:
        words[length] = set()
    words[length].add(word)


result = []
for length in sorted(words.keys()):
    result.extend(sorted(words[length]))
print("\n".join(result))
