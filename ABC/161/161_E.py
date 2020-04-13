from collections import Counter
import sys
sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# WA

# N日中 K日間 C日おき
N, K, C = map(int, input().split())
S = list(input())

C += 1

forward = [0] * N
backward = [0] * N

prev = 0
for i in range(N - 1, -1, -1):
    s = S[i]

    # K日あとのがある
    if i + C <= N - 1:
        prev = max(prev, backward[i + C])

    if s != 'o':
        continue

    backward[i] += 1 + prev


prev = 0
for i in range(N):
    s = S[i]

    # K日前のがある
    if 0 <= i - C:
        prev = max(prev, forward[i - C])

    if s != 'o':
        continue

    forward[i] += 1 + prev

print(forward)
print(backward)


backward = [K-x+1 if x != 0 else 0 for x in backward]

m = max(forward)

if K < m:
    exit()

print(forward)
print(backward)

ans = []
for i in range(N):
    if forward[i] == 0:
        continue
    if forward[i] == backward[i]:
        ans.append(i+1)


if not ans:
    exit()

print('\n'.join(map(str, ans)))
exit()

b_k = [[] for _ in range(K + 1)]
f_k = [[] for _ in range(K + 1)]

for x, x_k in [(backward, b_k), (forward, f_k)]:
    for i in range(N):
        n = x[i]

        if n == 0:
            continue

        x_k[n].append(i + 1)

ans = []

print(b_k)
print(f_k)

for x_k in [b_k, f_k]:
    for i in range(1, K + 1):
        i_s = x_k[i]
        if len(i_s) != 1:
            continue

        ans.append(i_s[0])

ans = list(set(ans))
ans.sort()
print('\n'.join(map(str, ans)))
