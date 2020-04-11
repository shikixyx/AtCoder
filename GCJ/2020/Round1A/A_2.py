import sys
sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

T = int(readline())


def solve():
    N = int(readline())
    SS = [str(readline().rstrip().decode('utf-8')) for _ in range(N)]

    PART = [S.split('*') for S in SS]

    PART1 = [(-len(P[0]), P[0]) for P in PART]
    PART2 = [(-len(P[1]), P[1]) for P in PART]

    PART1.sort()
    PART2.sort()

    longest1 = PART1[0][1]
    longest2 = PART2[0][1]

    ok = True
    for i in range(1, N):
        l, s = PART1[i]

        if l == 0:
            continue

        l = -l
        if s != longest1[:l]:
            ok = False
            break

    if not ok:
        return '*'

    for i in range(1, N):
        l, s = PART2[i]

        if l == 0:
            continue
        if s != longest2[l:]:
            ok = False
            break

    ans = None
    if not ok:
        ans = '*'
    else:
        ans = longest1 + longest2

    return ''.join(ans)


ans = []
for i in range(1, T+1):
    t = solve()
    txt = "Case #{}: {}".format(i, t)
    ans.append(txt)

print('\n'.join(ans))
exit(0)
