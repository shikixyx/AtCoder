import sys
sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

T = int(input())


# [[素因数,数]]を出力
def fctr1(n):
    f = []
    c = 0
    r = int(n**0.5)
    for i in range(2, r+2):
        while n % i == 0:
            c += 1
            n = n//i
        if c != 0:
            f.append([i, c])
            c = 0
    if n != 1:
        f.append([n, 1])
    return f


def solve(x, k):
    f = fctr1(x)
    cnt = sum([x for _, x in f])
    if k <= cnt:
        ret = 1
    else:
        ret = 0
    return ret


ans = []
for _ in range(T):
    X, K = map(int, input().split())
    t = solve(X, K)
    ans.append(t)

print("\n".join(map(str, ans)))
exit(0)
