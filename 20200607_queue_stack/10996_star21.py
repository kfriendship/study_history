"""
10996 별찍기21
"""

n = int(input())

for _ in range(n):
    l1 = "* "*((n+1)//2)
    l1 = l1[:n]
    l2 = " *"*(n//2)
    print(l1)
    print(l2)
