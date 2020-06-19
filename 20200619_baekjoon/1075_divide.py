"""
1075 나누기

주어진 숫자 N의 뒤 두자리수를 F로 나누어 떨어지게 적절히 바꿔보자.

알고리즘: 수학
"""

import sys
read = sys.stdin.readline

n, f = int(read()), int(read())
minimum = n//100*100
a = n//f
result = a*f
while minimum <= result:
    a -= 1
    result = a*f
result = str((a+1)*f)[-2:]
if len(result) == 1:
    result = "0" + result
print(result)
