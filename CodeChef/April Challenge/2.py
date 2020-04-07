import sys
sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

T = int(readline())


def solve(N, A):
    ones = [i for i, a in enumerate(A) if a == 1]
    L = len(ones)

    if L <= 1:
        return 'YES'

    ok = True
    for i in range(1, L):
        d = ones[i] - ones[i - 1]
        if d < 6:
            ok = False
            break

    if ok:
        ret = 'YES'
    else:
        ret = 'NO'

    return ret


ans = []
for _ in range(T):
    N = int(readline())
    A = list(map(int, readline().split()))
    r = solve(N, A)
    ans.append(r)

print('\n'.join(map(str, ans)))
