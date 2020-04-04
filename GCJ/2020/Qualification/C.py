import sys
sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

T = int(input())


def solve():
    N = int(input())
    SE = [[int(x) for x in input().split()] for _ in range(N)]

    SES = [(se, i) for i, se in enumerate(SE)]
    SES.sort()

    ans = [None] * N

    J = -1
    C = -1

    for se, i in SES:
        start = se[0]
        end = se[1]

        if J <= start:
            J = end
            ans[i] = 'J'
        elif C <= start:
            C = end
            ans[i] = 'C'
        else:
            ans = 'IMPOSSIBLE'
            return ans

    return "".join(ans)


ans = []
for i in range(1, T + 1):
    r = solve()
    txt = "Case #{}: {}".format(i, r)
    ans.append(txt)

print("\n".join(ans))
