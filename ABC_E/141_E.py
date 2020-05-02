import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# AC
# O(N^2)
# 20min

N = int(input())
S = list(input())

ans = 0

for l2 in range(1, N):
    same_len = 0
    for i in range(N):
        if N - 1 < l2 + i:
            continue

        if S[i] == S[l2 + i]:
            same_len += 1
        else:
            same_len = min(l2, same_len)
            ans = max(ans, same_len)
            same_len = 0
    same_len = min(l2, same_len)
    ans = max(same_len, ans)

print(ans)
