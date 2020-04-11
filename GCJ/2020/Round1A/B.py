import sys
sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

T = int(readline())


def solve():
    N = int(readline())
    ans = []

    if N != 501:
        for i in range(1, N+1):
            ans.append("{} 1".format(i))
    else:
        ans.append("1 1")
        ans.append("2 1")
        ans.append("3 2")
        ans.append("3 1")
        for i in range(4, 500):
            ans.append("{} 1".format(i))

    return ans


ans = []
for i in range(1, T+1):
    t = solve()
    txt = "Case #{}:".format(i)
    ans.append(txt)
    for p in t:
        ans.append(p)

print('\n'.join(ans))
