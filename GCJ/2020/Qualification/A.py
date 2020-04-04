import sys
sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

T = int(input())


def solve(N):
    M = []
    for _ in range(N):
        r = list(map(int, input().split()))
        M.append(r)

    trace = 0
    for i in range(N):
        trace += M[i][i]

    rpt_row = 0
    for i in range(N):
        row = M[i]
        cnt = len(list(set(row)))
        if cnt != N:
            rpt_row += 1

    rpt_col = 0
    for i in range(N):
        col = []
        for j in range(N):
            col.append(M[j][i])

        cnt = len(list(set(col)))
        if cnt != N:
            rpt_col += 1

    return trace, rpt_row, rpt_col


ans = []
for i in range(T):
    N = int(input())
    a, b, c = solve(N)
    txt = "Case #{}: {} {} {}".format(i + 1, a, b, c)
    ans.append(txt)

print('\n'.join(ans))
