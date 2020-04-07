import sys
sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

T = int(readline())
MOD = 10 ** 9 + 7


def solve(N, P):
    P.sort(reverse=True)
    ret = 0

    for i in range(N):
        p = P[i] - i
        if p < 0:
            break
        ret += p
        ret %= MOD

    return ret


ans = []
for _ in range(T):
    N = int(readline())
    P = list(map(int, readline().split()))
    r = solve(N, P)
    r %= MOD
    ans.append(r)

print('\n'.join(map(str, ans)))
exit(0)
