"""
2446 별찍기 9
"""

n = int(input())

for i in range(0, n):
    space = i
    star = (n-i)*2-1
    print("{}{}".format(" "*space, "*"*star))

for i in range(n-2, -1, -1):
    space = i
    star = (n - i) * 2 - 1
    print("{}{}".format(" " * space, "*" * star))
