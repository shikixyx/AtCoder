import sys
sys.setrecursionlimit(10 ** 7)

N, M, k = map(int, input().split())

load = 4 * n * m - 2 * n - 2 * m

if k > load:
    print("NO")
    exit()

print("YES")
step = 0
go = True
res = []

n = N
m = M
while k > 0:
    # GO
    if go:
        if k <= n:
            res.append("{} D".format(k))
            step += 1
            break
        else:
            res.append("{} D".format(n))
            step += 1
            k -= n

        if k <= m:
            res.append("{} R".format(k))
            step += 1
            break
        else:
            res.append("{} R".format(m))
            step += 1
            k -= m

        if k <= n:
            res.append("{} U".format(k))
            step += 1
            break
        else:
            res.append("{} U".format(n))
            step += 1
            k -= n

        if k <= m:
            res.append("{} L".format(k))
            step += 1
            break
        else:
            res.append("{} L".format(m))
            step += 1
            k -= m

    # BACK
    else:
        if k <= m:
            res.append("{} R".format(k))
            step += 1
            break
        else:
            res.append("{} R".format(m))
            step += 1
            k -= m

        if k <= n:
            res.append("{} D".format(k))
            step += 1
            break
        else:
            res.append("{} D".format(n))
            step += 1
            k -= n

        if k <= m:
            res.append("{} L".format(k))
            step += 1
            break
        else:
            res.append("{} L".format(m))
            step += 1
            k -= m

        if k <= n:
            res.append("{} D".format(k))
            step += 1
            break
        else:
            res.append("{} D".format(n))
            step += 1
            k -= n

