import sys
sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

T = int(input())

# AC


def solve(N):
    if N == 1:
        return ["1", "1 1"]

    m = N // 2

    RET = []
    RET.append(m)

    l = [1]
    for i in range(2, N + 1, 2):
        l.append(i)
        if i + 1 <= N:
            l.append(i + 1)
        LN = len(l)
        tmp = [LN] + l
        RET.append(" ".join(map(str, tmp)))
        l = []

    return RET


ans = []
for _ in range(T):
    N = int(input())
    t = solve(N)
    ans.append("\n".join(map(str, t)))

print("\n".join(map(str, ans)))
exit(0)
