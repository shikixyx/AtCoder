import sys
from collections import defaultdict
sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N = int(input())
A = list(map(int, input().split()))

NUM = defaultdict(int)

for a in A:
    NUM[a] += 1

s = 0
for v in NUM.values():
    s += v * (v - 1) // 2

#print(s)

ans = []
for a in A:
    r = NUM[a]
    t = s - (r - 1)
    ans.append(t)

print("\n".join(map(str, ans)))
