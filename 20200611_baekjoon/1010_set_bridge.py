"""
1010 다리 놓기

다리는 놓아야하는데 m개 중에 n개를 고르면 된다.
즉 조합이다.
조합 식은 nCr = n!/((n-r)!*r!

알고리즘: 수학
"""
from math import factorial
import sys
read = sys.stdin.readline

for _ in range(int(read())):
    n, m = map(int, read().split())
    if n == m:
        print(1)
    else:
        print(factorial(m)//(factorial(m-n)*factorial(n)))
