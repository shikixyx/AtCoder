import sys
sys.setrecursionlimit(10 ** 7)

N = int(input())
X = list(map(int, input().split()))

cnt = 10 ** 10
for i in range(101):
    p = 0
    for x in X:
        p += (i - x) ** 2

    cnt = min(cnt, p)

print(cnt)
