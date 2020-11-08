import sys
from collections import Counter

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N = list(map(int, list(input())))
L = len(N)

MD3 = [n % 3 for n in N]
C = Counter(MD3)

s = sum(MD3)

# 既に3の倍数
if s % 3 == 0:
    print(0)
    exit()

ans = -1
if s % 3 == 1:
    # 1を1つ消すか、2を2つ消す
    if C[1] >= 1 and L >= 2:
        ans = 1
    elif C[2] >= 2 and L >= 3:
        ans = 2
elif s % 3 == 2:
    # 2を1つ消すか、1を2つ消す
    if C[2] >= 1 and L >= 2:
        ans = 1
    elif C[1] >= 2 and L >= 3:
        ans = 2

print(ans)

