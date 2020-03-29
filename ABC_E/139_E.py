import sys
sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# TLE
# O(N^3)の解法

N = int(input())
A = [[int(x) for x in input().split()] for _ in range(N)]

A = [[]] + A

cnt = 0
ok = True

for _ in range(N * (N - 1) // 2):
    can_match_today = [False] * (N+1)
    fin = True
    match = False
    for i in range(1, N + 1):
        if can_match_today[i] or not A[i]:
            continue

        fin = False
        l = A[i][-1]

        if can_match_today[l]:
            continue
        r = A[l][-1]

        if r == i:
            match = True
            can_match_today[l] = True
            can_match_today[i] = True
            A[l].pop()
            A[i].pop()

    if fin:
        break

    if not match:
        ok = False
        break

    cnt += 1


if ok:
    print(cnt)
else:
    print(-1)
