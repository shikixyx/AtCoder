import sys
sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

T = int(readline())


def solve():
    N = int(readline())
    ans = []

    if N == 1:
        ans.append([1, 1])
    elif N == 2:
        ans.append([1, 1])
        ans.append([2, 1])
    elif N <= 998:
        for i in range(1, N // 2 + 1):
            ans.append([i, 1])

        m = N // 2
        if N % 2 == 1:
            ans.append([m + 1, 1])

        ans.append([m+1, 2])
    elif N <= 1000:
        ans.append([1, 1])

        for i in range(2, 46):
            ans.append([i, i - 1])

        rest = N - 991

        for i in range(45, 45 + rest):
            ans.append([i, i])
    else:
        ans.append([1, 1])

    return [' '.join(map(str, x)) for x in ans]


ans = []
for i in range(1, T+1):
    t = solve()
    txt = "Case #{}:".format(i)
    ans.append(txt)
    for p in t:
        ans.append(p)

print('\n'.join(ans))
