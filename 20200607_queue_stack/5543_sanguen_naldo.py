"""
5543 상근날도

123번째는 버거
45번째는 음료

버거하나 음료하나 싼거 고르고 -50하자.
"""

import sys
read = sys.stdin.readline

min_burger = min([int(read()), int(read()), int(read())])
min_beverage = min(int(read()), int(read()))
print(min_burger+min_beverage-50)
