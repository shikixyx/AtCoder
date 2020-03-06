import sys
import bisect
sys.setrecursionlimit(10 ** 7)

# TLE

N, Q = map(int, input().split())
STX = []
for _ in range(N):
    s, t, x = map(int, input().split())
    STX.append((s, t, x))

PEOPLE = []
for i in range(Q):
    d = int(input())
    PEOPLE.append((d, i))

ans = [-1] * Q

STX.sort(key=lambda x: x[2])

for s, t, x in STX:
    if len(PEOPLE) == 0:
        break

    i = bisect.bisect_left(PEOPLE, (s - x, -1))
    j = bisect.bisect_left(PEOPLE, (t - x, -1))

    if i == j:
        continue

    use = [PEOPLE[x][1] for x in range(i, j)]

    for k in use:
        ans[k] = x

    del PEOPLE[i:j]


print("\n".join(map(str, ans)))
