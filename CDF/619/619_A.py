import sys
sys.setrecursionlimit(10 ** 7)

T = int(input())

CASE = []
for _ in range(T):
    a = input()
    b = input()
    c = input()
    CASE.append([a, b, c])

res = []
for a, b, c in CASE:
    l = len(c)
    ans = 'YES'
    for i in range(l):
        if c[i] != a[i] and c[i] != b[i]:
            ans = 'NO'
            break

    res.append(ans)

print("\n".join(res))
